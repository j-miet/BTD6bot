"""Implements MainWindow class responsible for operating entire GUI.

Also includes MainWindowCombobox class which requires a MainWindow instance as argument.
For this reason placing it anywhere else would result into circular import.
"""

from __future__ import annotations
from typing import TYPE_CHECKING

import itertools as it
import json
import os
import signal
import sys
import threading
import time
import tkinter as tk
from tkinter import ttk

import pynput
from pynput.keyboard import Key, KeyCode

from gui.guihotkeys import GuiHotkeys
import gui.gui_tools as gui_tools
from gui.help_window import HelpWindow
from gui.hotkey_window import HotkeyWindow
from gui.monitoring_window import MonitoringWindow
import gui.gui_paths as gui_paths
from gui.gui_tools import os_font
from gui.queue_window import QueueModeWindow
import gui.roundplot.roundplot as roundplot
from gui.settings_window import SettingsWindow
from utils import plan_data

if TYPE_CHECKING:
    from typing import Any, TextIO
    from tkinter import Event

class MainWindowCombobox(ttk.Combobox):
    """Custom combobox class specifically made for MainWindow class.

    It adds a letter-based search for faster map selection when using combobox elements which also auto-updates info 
    panel (both text+image) without requiring the user to press enter afterwards like normal combobox does.
    
    Searching algorithm simply selects items i.e. maps or strats by their first letter when combobox is opened and 
    user presses any key.

    Original:
    https://stackoverflow.com/questions/53848622/how-to-bind-keypress-event-for-combobox-drop-out-menu-in-tkinter-python-3-7/53864105#53864105
    """
    def __init__(self, mainwindow: MainWindow, *args, **kwargs): # type: ignore[no-untyped-def]
        super().__init__(*args, **kwargs)
        self.mainwindow = mainwindow

        pd = self.tk.call('ttk::combobox::PopdownWindow', self) # get popdownWindow reference 
        lb = pd + '.f.l' # get popdown listbox
        self._bind(('bind', lb), "<KeyPress>", self._comboboxsearch, None) # type: ignore[attr-defined]

    def _updateselection(self, i: int, event: Event) -> None:
        self.current(i)
        self.icursor(i)
        self.tk.eval(str(event.widget) + ' selection clear 0 end') # clear current selection
        self.tk.eval(str(event.widget) + ' selection set ' + str(i)) # select new element
        self.tk.eval(str(event.widget) + ' see ' + str(i)) # spin combobox popdown for selected element will be

    def _comboboxsearch(self, event: Event) -> str:
        """Implements custom combobox behavior.

        Using keyword string "break" as return value disables current widget's (= this combobox) default behavior.
        Importantly, moving up and down with arrow keys interferes with custom letter-based search and messes up index 
        tracking. Disabling this and making Custom "Up", "Down" and "Return" (= pressing Enter) events fixes this.
        """
        values = self.cget("values")
        match event.keysym:
            case "Return":
                try:
                    self.focus_displayof() # 'Enter' to unfocus combobox. Throws KeyError which must be handled.
                except KeyError:
                    ...
                return ""
            case "Up":
                if self.current() <= 0:
                    return ""
                i: int = self.current()-1
                self._updateselection(i, event)
            case "Down":
                if self.current() >= len(values)-1:
                    return ""
                i = self.current()+1
                self._updateselection(i, event)
            case _:
                for i in it.chain(range(self.current() + 1,len(values)), range(0,self.current())):
                    if event.char.lower() == values[i][0].lower():
                        self._updateselection(i, event)
                        break
        if self._name == 'mapbox': # type: ignore[attr-defined]
            self.mainwindow._update_mapconfig() # auto-update map info panel when for currently selected element
        elif self._name == 'stratbox': # type: ignore[attr-defined]
            self.mainwindow._update_stratconfig()
        return "break"


class MainWindow:
    """GUI main window.

    Places main window frame inside root. Other GUI windows need the main thread which is tied to this root:
    if this thread is terminated, all other windows and their respective threads will also close.
    """
    try:
        _MAP_IMAGES = os.listdir(gui_paths.MAP_IMAGES_PATH)
    except FileNotFoundError:
        ...
    GuiHotkeys.update_guihotkeys()

    @staticmethod
    def _hotkey_tracker(key: Key | KeyCode | None) -> None:
        """Handles gui hotkey states.

        It's important to not put any pausing functions inside this (time.sleep() or similar) as it will cause all 
        keyboard inputs to lag during program runtime.

        Args:
            key: Latest keyboard key the user has pressed.       
        """
        if key == GuiHotkeys.exit_hotkey or (isinstance(key, KeyCode) and key.char == GuiHotkeys.exit_hotkey): 
            os.kill(os.getpid(), signal.SIGTERM)
        elif key == GuiHotkeys.start_stop_hotkey:
            GuiHotkeys.start_stop_status = True
        elif key == GuiHotkeys.pause_hotkey:
            GuiHotkeys.pause_status = True

    # Listener thread object sends keyboard inputs to _hotkey_tracker function. 
    # If user operating system is MacOS, gui hotkeys must be disabled in order to avoid errors with keyboard controller 
    # used in bot\kb_mouse.py
    # Should other Listener objects exist, make sure to disable them on any unsupported OS and implement alternate
    # systems in place.
    if sys.platform != 'darwin':
        _kb_listener = pynput.keyboard.Listener(on_press = _hotkey_tracker)
        _kb_listener.daemon = True
        _kb_listener.start()    

    def __init__(self, root: tk.Tk) -> None:
        """Initialize main window using the passed tkinter root.
        
        Args:
            root: Tkinter root object.
        """
        self.root = root
        self.root.title("BTD6bot")
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.geometry("655x442+700+300")
        self.root.minsize(655,442)
        self.root.maxsize(655,442)
        self.MAP_NAMES_AND_STRATS_DICT = plan_data.return_maps_and_strats(plan_data.read_plans())

        self.reader_init: bool = False
        self.init_button_first_time: bool = True

        mainframe = tk.Frame(
            root, 
            borderwidth=5, 
            relief='groove', 
            padx=15, 
            pady=15
        )
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe.grid(sticky='nwes')
        mainframe.bind("<ButtonRelease-1>", lambda _: self.root.focus())
        
        self.current_map: str = 'dark castle'
        self.maps_box = MainWindowCombobox(
            mainwindow=self,
            master=mainframe, 
            state='readonly', 
            values=self._get_maps(),
            name='mapbox'
        )
        self.maps_box.grid(column=0, row=5, sticky='sw', pady=10)
        self.maps_box.bind("<<ComboboxSelected>>", lambda _: self._update_mapconfig())
        self.maps_box.bind("<<ComboboxSelected>>", lambda _: self.root.focus(), add='+')
        self.maps_box.set(self.current_map) # initialize with default value

        info_window_scroll = ttk.Scrollbar(
            mainframe, 
            orient='vertical'
        )
        info_window_scroll.grid(column=2, row=3, rowspan=2, sticky="nsw")

        self.info_window = tk.Text(
            mainframe,
            height=9, 
            yscrollcommand=info_window_scroll.set, 
            font=("Times New Roman", 11),
            wrap=tk.WORD, relief='sunken'
        )
        self.info_window.grid(column=0, columnspan=2, row=3, rowspan=2)
        info_window_scroll.configure(command=self.info_window.yview)

        self.current_strat: str = 'Easy-Standard'
        self.strat_box = MainWindowCombobox(
            mainwindow=self,
            master=mainframe, 
            state='readonly',
            name='stratbox'
        )
        self.strat_box.grid(column=1, row=5, sticky='sw', pady=10)
        self.strat_box.bind("<<ComboboxSelected>>", lambda _: self._update_stratconfig())
        self.strat_box.bind("<<ComboboxSelected>>", lambda _: self.root.focus(), add='+')
        self._show_mapinfo() # initialize info_window with default value 
 
        self.MAPSCREEN_TEXT_STR = (r" ___  _____  ___    __  _          _    "+"\n"
                                r"| _ )|_   _||   \  / / | |__  ___ | |_  "+"\n"
                                r"| _ \  | |  | |) |/ _ \| '_ \/ _ \|  _| "+"\n"
                                r"|___/  |_|  |___/ \___/|_.__/\___/ \__| "+"\n"
                                r"   _    _____________       ___    _____"+"\n"
                                r"__| \_//   // //     \_____/   \ _/     "+"\n"
                                r" _|__//    || ||      \   |     |       "+"\n"
                                r"(____)(    || ||      ))   \   /      __"+"\n"
                                r"  |  \\    || ||      /     /_\      /  "+"\n"
                                r"  |_/ \\___\\_\\_____/              /   "+"\n"
                                r"___________________________________/    "
                                )
        style = ttk.Style()
        style.configure('Style.TButton', font='TkFixedFont')
        try:
            map_image = tk.PhotoImage(file=gui_paths.MAP_IMAGES_PATH/'dark castle.png')
            self.mapscreen = ttk.Label(
                mainframe, 
                image=map_image, 
                compound='top', 
                anchor='nw', 
                relief='sunken', 
                justify='left', 
                style='Style.TButton'
            )
            # Save image reference; otherwise Python garbage collection destroys it.
            # For some reason, image is not recognized as an attribute of Label. Thus type ignore to avoid mypy errors.
            self.mapscreen.image = map_image # type: ignore[attr-defined]
            self.mapscreen.grid(column=0, row=0, columnspan=3, rowspan=3, sticky='nw')
        except (FileNotFoundError, tk.TclError):
            self.mapscreen = ttk.Label(
                mainframe, 
                relief='sunken', 
                style='Style.TButton', 
                justify='left'
            )
            self.mapscreen.grid(column=0, row=0, columnspan=2, rowspan=3)
            # Text generated with 'Graceful' font on https://patorjk.com/software/taag
            # Picture is self-made.
            self.mapscreen['text'] = self.MAPSCREEN_TEXT_STR

        self.help_button= tk.Button(
            mainframe, 
            text="Help", 
            height=2, 
            width=5, 
            command=self._help_window, 
            padx=20,
            pady=5
        )
        self.help_button.grid(column=2, row=0, padx=30, pady=10, sticky='nwe')

        self.settings_button= tk.Button(
            mainframe, 
            text="Settings", 
            height=2, 
            width=5,
            command=self._settings_window, 
            padx=20, 
            pady=5
        )
        self.settings_button.grid(column=3, row=0, pady=10, sticky='nwe')

        self.hotkey_button = tk.Button(
            mainframe, 
            text="Set\nhotkeys", 
            height=2, 
            width=5, 
            command=self._hotkey_window,
            padx=20, 
            pady=5
        )
        self.hotkey_button.grid(column=3, row=1, pady=10, sticky='we')

        self.queueoptions_button = tk.Button(
            mainframe, 
            text="Queue mode\nmaplist", 
            height=2, 
            width=5, 
            command=self._queue_mode_window, 
            padx=20, 
            pady=5
        )
        self.queueoptions_button.grid(column=3, row=2, pady=10, sticky='wes') 

        self.collection = tk.StringVar(value='Off')
        self.collection_toggle = tk.Checkbutton(
            mainframe, 
            text='Collection Event', 
            anchor='e', 
            variable=self.collection,
            command=self._collection_mode_check,
            offvalue='Off', 
            onvalue='On', 
            state='disabled'
        )
        self.collection_toggle.grid(column=3, row=3, sticky='se', pady=(1,1))

        self.farming = tk.StringVar(value='Off')
        self.collection_farm_toggle = tk.Checkbutton(
            mainframe, 
            text='Farm mode', 
            anchor='e', 
            variable=self.farming,
            command=self._farming_mode_check,
            offvalue='Off', 
            onvalue='On', 
            state='disabled'
        )
        self.collection_farm_toggle.grid(column=3, row=4, sticky='ne', pady=(1,2))

        self.queue = tk.StringVar(value='Off')
        self.queue_toggle = tk.Checkbutton(
            mainframe, 
            text='Queue mode', 
            anchor='e', 
            variable=self.queue,
            command=self._queue_mode_check, 
            offvalue='Off', 
            onvalue='On', 
            state='disabled'
        )
        self.queue_toggle.grid(column=3, row=4, sticky='e', pady=(2,2))

        self.replay = tk.StringVar(value='Off')
        self.replay_toggle = tk.Checkbutton(
            mainframe, 
            text='Replay mode', 
            anchor='e', 
            variable=self.replay,
            offvalue='Off', 
            onvalue='On', 
            state='disabled'
        )
        self.replay_toggle.grid(column=3, row=4, sticky='se', pady=(2,5))

        self.monitor_plot_button = tk.Button(
            mainframe, 
            text='Show plot', 
            height=1, 
            state='normal',
            command=lambda: roundplot.plot_plan(self._get_original())
        )
        self.monitor_plot_button.grid(column=2, row=5, sticky='e', padx=55)

        self.start_button = tk.Button(
            mainframe, 
            text="Initialize bot", 
            height=2, 
            command=self._monitoring_window,
            state='active', 
            padx=10, 
            pady=0
        )
        self.start_button.grid(column=3, row=5, sticky='e')
    
        if sys.platform == "darwin": # adjust gui element placements if macOS
            self.root.geometry("695x442+700+300")
            self.root.minsize(695,442)
            self.root.maxsize(695,442)
            self.maps_box.config(font=os_font)
            self.maps_box.grid(column=0, row=6, sticky='sw', pady=10)
            info_window_scroll.grid(column=2, row=3, rowspan=3, sticky="nsw")
            self.info_window.config(font=os_font)
            self.info_window.grid(column=0, columnspan=2, row=3, rowspan=3)
            self.strat_box.config(font=os_font)
            self.strat_box.grid(column=1, row=6, sticky='sw', pady=10)
            self.collection_toggle.config(font=os_font)
            self.collection_toggle.grid(column=3, row=3, sticky='ne')
            self.queue_toggle.config(font=os_font)
            self.replay_toggle.config(font=os_font)
            self.replay_toggle.grid(column=3, row=5, sticky='se')
            self.monitor_plot_button.grid(column=2, row=6, sticky='e', padx=55)
            self.start_button.grid(column=3, row=6, sticky='e')

        self._delete_readme_html()
        self._update_mapconfig()
        self._update_stratconfig()
        self.strat_box.set(self.current_strat)

    def _delete_readme_html(self) -> None:
        if os.path.exists(gui_paths.FILES_PATH/'helpwindow'/'README.html'):
            os.remove(gui_paths.FILES_PATH/'helpwindow'/'README.html')

    def _reorder_strats(self, strategies: list[str]) -> list[str]:
        filter = {"Easy": 1, "Medium": 2, "Hard": 3} # change plan list order: Easy first then Medium and last Hard
        strats: list[str] = strategies.copy()
        current: str
        for i in range(0, len(strats)-1):
            strat_current: str = strats[i].split('-')[0]
            strat_next: str = strats[i+1].split('-')[0]
            try:
                if filter[strat_current] > filter[strat_next]:
                    current = strats[i]
                    strats[i] = strats[i+1]
                    strats[i+1] = current
            except KeyError:
                ...
        return strats

    def _get_maps(self) -> list[str]:
        """Get all map names.

        Returns:
            names: List of all map names parsed from files in 'plans' folder.
        """
        names: list[str] = []
        for m in self.MAP_NAMES_AND_STRATS_DICT.keys():
            names.append(m)
        return names

    def _get_strats(self) -> list[str]:
        """Get all strategy names and update current map info window.

        Returns:
            strats: List of all strategy names parsed from files in 'plans' folder.
        """
        strats: list[str] = []
        for s in self.MAP_NAMES_AND_STRATS_DICT[self.current_map]:
            strats.append(s)
        self._show_mapinfo()
        return strats

    def _update_mapconfig(self) -> None:
        """Reads map combobox value, and updates current map, image and strategies.

        Also sets default value for current strategy after map value is read."""
        for map_name in self.MAP_NAMES_AND_STRATS_DICT.keys():
            if self.maps_box.get() == map_name:
                self.current_map = map_name
                try:
                    temp = tk.PhotoImage(file=gui_paths.MAP_IMAGES_PATH/
                                        MainWindow._MAP_IMAGES[MainWindow._MAP_IMAGES.index(self.current_map+'.png')])
                    self.mapscreen['text'] = ''
                    self.mapscreen.configure(image=temp)
                    self.mapscreen.image = temp # type: ignore[attr-defined]
                except (AttributeError, ValueError):
                    self.mapscreen.configure(image='', compound='center', anchor='center', justify='left')
                    self.mapscreen['text'] = self.MAPSCREEN_TEXT_STR
                self.strat_box.set(self.MAP_NAMES_AND_STRATS_DICT[map_name][0])
                strats_for_map = []
                for strats in self.MAP_NAMES_AND_STRATS_DICT[map_name]:
                    strats_for_map.append(strats)
                self.strat_box.configure(values=strats_for_map)
                self.current_strat = self.MAP_NAMES_AND_STRATS_DICT[map_name][0]
                self.info_window.insert('end', '')
                self._update_stratconfig()

    def _update_stratconfig(self) -> None:
        """Updates current strat value and possible map info screen if available."""
        for maps in self.MAP_NAMES_AND_STRATS_DICT.keys():
            if self.maps_box.get() == maps:
                strats_for_map = []
                for strats in self.MAP_NAMES_AND_STRATS_DICT[maps]:
                    strats_for_map.append(strats)
                all_strats: list[str] = self._reorder_strats(strats_for_map)
                self.strat_box.configure(values=all_strats)
        self.current_strat = self.strat_box.get()
        self._show_mapinfo()

    def _show_mapinfo(self) -> None:
        """Displays optional info screen.
        
        Info texts are defined at the beginning of each plan file in 'plans' folder.
        If no valid info string is found, displays a blank screen.
        """
        original = self._get_original()
        with open(gui_paths.PLANS_PATH/(original+'.py')) as file_read:
            infolist = file_read.readlines()
        try:
            if infolist[0] == '\"\"\"\n':
                info_comment_end = infolist[1:].index('\"\"\"\n')
                try:
                    with open(gui_paths.FILES_PATH/'time_data.json') as timedata_read:
                        current_version = json.load(timedata_read)[original]["version"]
                except KeyError:
                    current_version = '-'
                core_text = ['[Plan Name] '+original+'\n','[Game Version] '+str(current_version)+'\n']
                core_text.extend(infolist[1:info_comment_end+1])
                readtext = ''.join(core_text)
                self.info_window['state'] = 'normal'
                self.info_window.delete(1.0, tk.END)
                self.info_window.insert('end', readtext)
                self.info_window['state'] = 'disabled'
            else:
                self.info_window['state'] = 'normal'
                self.info_window.delete(1.0, tk.END)
                self.info_window.insert('end', '')
                self.info_window['state'] = 'disabled'
        except IndexError:    
            self.info_window['state'] = 'normal'
            self.info_window.delete(1.0, tk.END)
            self.info_window.insert('end', '')
            self.info_window['state'] = 'disabled'

    def _get_original(self) -> str:
        """Reconstruct the original plan name from a .py file using name and strat components.

        Returns:
            Original strategy file name as a string without .py.
        """
        namesplit = self.current_map.split()
        stratsplit = self.current_strat.split('-')
        return '_'.join(namesplit) + stratsplit[0] + stratsplit[1]
    
    def _choose_mode(self) -> list[str]:
        """Returns either a single plan or list of plans from queue list.

        Returns:
            String list of plans based on queue mode settings.
        """
        if self.queue.get() == 'Off':
            return [self._get_original()]
        else:
            with open(gui_paths.QUEUE_LIST_PATH) as file_read:
                return plan_data.list_format(file_read.readlines()) # type: ignore[no-any-return]

    def _ocr_init(self, init_win: tk.Toplevel) -> None:
        """Imports ocr Reader object from bot.ocr.ocr_reader, which also initializes it for use.
        
        This method is called through root.after method to allow mainloop to create a init label and only after start 
        the importing, as otherwise everything would happen at once and init label would quickly flash after then 
        disappear.

        Initialization process takes several seconds as the ocr model is loaded into memory: afterwards, all initially 
        disabled buttons are enabled and free to use. Current init label window is destroyed at the end.
        """
        from bot.ocr.ocr_reader import OCR_READER # this is required here for reader initialization
        init_win.destroy()
        self.start_button['state'] = 'active'
        self.start_button['text'] = "Open\nbot window"
        self.collection_toggle['state'] = 'active'
        self.queue_toggle['state'] = 'active'
        self.replay_toggle['state'] = 'active'
        self.reader_init = True

    def _monitoring_window(self) -> None:
        """Create monitoring window object and allocate it to its own thread.

        When attempting to open a monitoring window first time in a session, a reader is also loaded. This 
        reader is part of optical character recognition library 'easyocr' which requires a new reader object to be 
        initialized i.e. loaded into memory, but only once per session.

        After initialization, the window gets passed the values of additional modes check (queue/replay). Creates a 
        separate thread to keep checking on monitoring window's existence until it's closed. This process is allocated 
        to a separate function which gets passed following values:

        monitoringwindow.get_monitoringwindow(): Current monitoring window to check if it's still open,
        monitoringwindow.get_old_output(): Original standard output stream to return to after bot no longer needs it.
        
        Already existing window also disables start button access to prevent multiple instances of same window.
        
        ---
        
        Thread has daemon=True to prevent 'RuntimeError: main thread is not in main loop' if MainWindow is closed while
        any top level windows are still open. For user, this nasty error wouldn't really matter as program still closes
        after printing these and they would likely oblivious to them. However, processing them for no reason still 
        wastes resources and more importanly, adds a bit of extra time in closing the program.
        
        General structure of this method is also used in setting up QueueModeWindow, HotkeyWindow and HelpWindow under
        their respective methods queue_mode_window, hotkey_window and help_window.
        """
        if not self.reader_init:
            self.init_button_first_time = False
            ocr_init_window = tk.Toplevel(self.root, borderwidth=5, relief='solid')
            ocr_init_window.overrideredirect(True)

            def adjust_ocr_init_label_to_root() -> None:
                """Adjust initiation label to current root location (650x440+700+300)."""
                step1 = self.root.geometry().split('x')
                step2 = '+'.join(step1)
                geom = step2.split('+')
                adj_geom = [str(val) for val in (int(geom[0])-150, int(geom[1])-400, int(geom[2])+75, int(geom[3])+220)]
                geom_str = adj_geom[0]+'x'+adj_geom[1]+'+'+adj_geom[2]+'+'+adj_geom[3]
                ocr_init_window.geometry(geom_str)

            adjust_ocr_init_label_to_root()
            tk.Label(ocr_init_window, 
                     text='Loading ocr model into memory, please wait.',
                     font=("Times", 16, "bold")).pack()
            ocr_init_window.attributes('-topmost', True)
            threading.Thread(target=lambda: self._ocr_init(ocr_init_window), daemon=True).start()
            self.start_button.configure(state='disabled')
            return
        self.start_button.configure(state='disabled')
        monitoringwindow = MonitoringWindow(
            self._choose_mode(), 
            self.replay.get(), 
            self.queue.get(),
            self.collection.get(),
            self.farming.get()
        )
        monitoringthread = threading.Thread(
            target=self._is_monitoringwindow, 
            args=[monitoringwindow.get_monitoringwindow(), monitoringwindow.get_old_output()],
            daemon=True)
        monitoringthread.start()

    def _is_monitoringwindow(self, current_monitoringwin: tk.Toplevel, old_stdout: TextIO | Any) -> None:
        """MainWindow method that tracks existence of a MonitoringWindow.

        If current MonitoringWindow object no longer exists, enables start button for main screen again and also 
        terminates existing thread allocated to bot program. Manual termination is important because if monitoring 
        window was closed during bot runtime, the thread its allocated to would still keep executing code. This in turn 
        would prevent you from stopping the current bot execution until it finishes, eating up CPU and memory. 

        Another, more serious issue would be that user could repeat this as start button gets enabled after any window,
        not just MonitoringWindow, no longer exists. You could then open another window, run bot, close window
        etc. and keep repeating this. Then eventually the usage of that CPU core this program utilizes gets capped and
        your program pretty much freezes. To prevent any of these unintended behaviours, this method - and other window 
        status tracking methods - keep re-applying the disabled status and won't allow the user to click button, unless 
        they really try it deliberately (time it within the time.sleep window below).

        Finally, despite all efforts, closing current bot thread forcefully while it's running presents a very small 
        memory leak. You'd have to purposefully create a new monitoring window, run bot on it and then close this 
        window while bot is still running - hundreds or even thousands of times, for it to become an issue. From my 
        testing, it allocates about 0.5 MB per cycle.
        
        Args:
            current_monitorwin: Current MonitoringWindow object.
            old_stdout: Original standard output stream.
        """
        while True:
            if not current_monitoringwin.winfo_exists():
                gui_tools.terminate_thread(MonitoringWindow.current_bot_thread)
                sys.stdout = old_stdout # return to original output stream
                if self.queue.get() == 'On':
                    self.start_button.configure(state='disabled')
                    with open(gui_paths.QUEUE_LIST_PATH) as f:
                        if len(f.readlines()) != 0:
                            self.start_button.configure(state='active')
                    return
                if self.reader_init:
                    self.start_button.configure(state='active')
                return
            self.start_button.configure(state='disabled')
            time.sleep(0.01) # tracking frequency; don't set this to too low as it will strain your CPU for nothing.

    def _queue_mode_window(self) -> None:
        """Open queue mode window which operates on its own thread."""
        self.queueoptions_button.configure(state='disabled')
        self.start_button.configure(state='disabled')
        queuewindow = QueueModeWindow()
        queuewindowthread = threading.Thread(
            target=self._is_queue_mode_screen, 
            args=[queuewindow.get_queuewindow()]
        )
        queuewindowthread.daemon = True
        queuewindowthread.start()

    def _is_queue_mode_screen(self, current_options: tk.Toplevel) -> None:
        """Checks if queue mode window exists and handles button access based on this.
        
        Args:
            current_options: Current QueueModeWindow object.
        """
        while True:
            if not current_options.winfo_exists():
                self.queueoptions_button.configure(state='active')
                if self.queue.get() == 'On':
                    self.start_button.configure(state='disabled')
                    with open(gui_paths.QUEUE_LIST_PATH) as f:
                        if len(f.readlines()) != 0:
                            self.start_button.configure(state='active')
                elif self.init_button_first_time:
                    self.start_button.configure(state='active')
                elif self.reader_init:
                    self.start_button.configure(state='active')
                return
            self.start_button.configure(state='disabled')
            time.sleep(0.01)

    def _queue_mode_check(self) -> None:
        """Disables and enabled initialization button based on queue mode toggle.
         
        If queue mode is off and reader has been initialized, enabled start button.
        If queue mode is On, but queue has no plans, also disables start button.
        """
        if self.queue.get() == 'On':
            self.start_button.configure(state='disabled')
            with open(gui_paths.QUEUE_LIST_PATH) as file_read:             
                if len(file_read.readlines()) != 0:
                    self.start_button.configure(state='active')
        else:
            self.start_button.configure(state='active')

    def _hotkey_window(self) -> None:
        """Open hotkey window which operates on its own thread."""
        self.hotkey_button.configure(state='disabled')
        self.start_button.configure(state='disabled')
        hotkeywindow = HotkeyWindow()
        hotkeywindowthread = threading.Thread(
            target=self._is_hotkeywindow, 
            args=[hotkeywindow.get_hotkeywindow()]
        )
        hotkeywindowthread.daemon = True
        hotkeywindowthread.start()

    def _is_hotkeywindow(self, current_hotkey: tk.Toplevel) -> None:
        """Checks if hotkey window exists and handles button access based on this.
        
        Args:
            current_hotket: Current HotkeyWindow object.
        """
        while True:
            if not current_hotkey.winfo_exists():
                if HotkeyWindow.input_key_listener.is_alive():
                    HotkeyWindow.input_key_listener.stop()
                self.hotkey_button.configure(state='active')
                if self.queue.get() == 'On':
                    self.start_button.configure(state='disabled')
                    with open(gui_paths.QUEUE_LIST_PATH) as f:
                        if len(f.readlines()) != 0:
                            self.start_button.configure(state='active')
                elif self.init_button_first_time:
                    self.start_button.configure(state='active')
                elif self.reader_init:
                    self.start_button.configure(state='active')
                return
            self.start_button.configure(state='disabled')
            time.sleep(0.01)

    def _help_window(self) -> None:
        """Open help window which operates on its own thread."""
        self.help_button.configure(state='disabled')
        helpwindow = HelpWindow()
        helpwindowthread = threading.Thread(
            target=self._is_helpwindow, 
            args=[helpwindow.get_helpwindow()]
        )
        helpwindowthread.daemon = True
        helpwindowthread.start()

    def _is_helpwindow(self, current_help: tk.Toplevel) -> None:
        """Checks if help window exists and handles button access based on this.
        
        Args:
            current_help: Current HelpWindow object.
        """
        while True:
            if not current_help.winfo_exists():
                self._delete_readme_html()
                self.help_button.configure(state='active')
                if self.queue.get() == 'On':
                    self.start_button.configure(state='disabled')
                    with open(gui_paths.QUEUE_LIST_PATH) as f:
                        if len(f.readlines()) != 0:
                            self.start_button.configure(state='active')
                elif self.init_button_first_time:
                    self.start_button.configure(state='active')
                elif self.reader_init:
                    self.start_button.configure(state='active')
                return
            time.sleep(0.01)
     
    def _settings_window(self) -> None:
        """Open settings window which operates on its own thread."""
        self.settings_button.configure(state='disabled')
        self.start_button.configure(state='disabled')
        settingswindow = SettingsWindow()
        settingsthread = threading.Thread(
            target=self._is_settingswindow, 
            args=[settingswindow.get_settingswindow()]
        )
        settingsthread.daemon = True
        settingsthread.start()

    def _is_settingswindow(self, current_settings: tk.Toplevel) -> None:
        """Checks if settings window exists and handles button access based on this.
        
        Args:
            current_settings: Current SettingsWindow object.
        """
        while True:
            if not current_settings.winfo_exists():
                self.settings_button.configure(state='active')
                if self.queue.get() == 'On':
                    self.start_button.configure(state='disabled')
                    with open(gui_paths.QUEUE_LIST_PATH) as f:
                        if len(f.readlines()) != 0:
                            self.start_button.configure(state='active')
                elif self.init_button_first_time:
                    self.start_button.configure(state='active')
                elif self.reader_init:
                    self.start_button.configure(state='active')
                return
            self.start_button.configure(state='disabled')
            time.sleep(0.01)

    def _collection_mode_check(self) -> None:
        """Disables and enabled farm mode toggle depending on collection mode toggle."""
        if self.collection.get() == 'On':
            self.collection_farm_toggle.configure(state='active')
        else:
            self._farming_mode_check()
            self.collection_farm_toggle.configure(state='disabled')
            self.collection_farm_toggle.deselect()

    def _farming_mode_check(self) -> None:
        if self.farming.get() == 'On' and self.collection.get() == 'On':
            if self.queue.get() == 'On':
                self.start_button.configure(state='active')
            self.queue.set('Off')
            self.replay.set('Off')
            self.queue_toggle.configure(state='disabled')
            self.replay_toggle.configure(state='disabled')
        else:
            self.queue_toggle.configure(state='active')
            self.replay_toggle.configure(state='active')