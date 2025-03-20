"""Contains MainWindow class responsible for operating entire GUI."""

from __future__ import annotations
from typing import TYPE_CHECKING

import os
import signal
import sys
import threading
import time
import tkinter as tk
from tkinter import ttk

import pynput

import gui.gui_tools as gui_tools
from gui.help_window import HelpWindow
from gui.hotkey_window import HotkeyWindow
from gui.monitoring_window import MonitoringWindow
from gui.queue_window import QueueModeWindow
import gui.roundplot.roundplot as roundplot
from gui.settings_window import SettingsWindow
import gui.gui_paths as gui_paths
from utils import plan_data

if TYPE_CHECKING:
    from typing import Any, TextIO
    from pynput.keyboard import Key, KeyCode

class MainWindow:
    """GUI main window.

    Places main window frame inside root. All GUI windows need the main thread which is tied to this root:
    if this thread is terminated, all other windows and their respective threads will also close.

    Static Methods:
    --
    exit ((Key | KeyCode | str) -> None): Terminates program when EXIT_HOTKEY press is detected. Is 
        targeted by 'kb_listener' thread object.

    Attributes:
        MAP_IMAGES (list[str], class attribute): List of all map image names.
        EXIT_HOTKEY (pynput.Key, class attribute): Hotkey for stopping the entire program at any moment. Current: F11.
        kb_listener (pynput.keyboard.Listener, class attribute): Pynput keyboard listener to track key presses for 
            'exit'. Listener is a thread object so it can track inputs at all times and is terminated only after entire 
            program is closed.

        root (tk.Tk): A tkinter.root object for placing the main window.
        reader_init (bool): Tracks ocr reader initialization status. Starts as False, and after   
            initialization, remains True for the rest of program runtime.
        init_button_first_time (bool): Tracks if initialization button has been pressed or not. This is important as 
            otherwise opening and closing windows/toggling button On then Off, could enable button access prematurely.
        replay (tk.StringVar): StringVar to set On/Off value for a replay mode button.
        queue (tk.StringVar): StringVar to set On/Off value for a queue mode button.
        collection (tk.StringVar): StringVar to set On/Off value for collection event mode button.
        current_map (str): Currently selected map.
        maps_box (ttk.Combobox): Dropdown menu of all maps.
        info_window (tk.Text): Displays plan information based on current map and strategy. Info is read from current 
            plan file located in 'plans' folder using current current_map and current_strat values.
        current_strat (str): Currently selected strategy based on current_map.
        strat_box (ttk.Combobox): Dropdown menu of all strategies for currently selected map.
        mapscreen_text_str (str): Default string text to display in place of mapscreen.
        mapscreen (tk.Label): Label used for displaying current map image. Images are stored and loaded from 
            'map images' folder. If no image is found, insert mapscreen_text_str into label instead.
        help_button (tk.Button): Opens a separate help window.
        hotkey_button (tk.Button): Opens a separate hotkey settings window.
        queueoptions_button (tk.Button): Opens a separate options window for queue mode settings.
        settings_button (tk.Button): Opens a separate settings window.
        collection_toggle (tk.Checkbutton): Enable/disable collection event mode.
        queue_toggle (tk.Checkbutton): Enable/disable queue mode.
        replay_toggle (tk.Checkbutton): Enable/disable replay mode.
        monitor_plot_button (tk.Button): Button to open a matplotlib screen which lists all rounds and their respective 
            commands. Useful for users that want to see how commands are written and want to see how the current plan 
            progresses.
             >Plots are quite resource-intensive and can be lagging if you drag their contents around.
        start_button (tk.Button): Button object which opens a separate MonitoringWindow for running the bot.
    """
    try:
        MAP_IMAGES = os.listdir(gui_paths.MAP_IMAGES_PATH)
    except FileNotFoundError:
        ...
    EXIT_HOTKEY = pynput.keyboard.Key.f11

    @staticmethod
    def exit(key: Key | KeyCode | None) -> None:
        """Program termination via hotkey.

        It's important to not put any pausing functions inside this (time.sleep() or similar) as it will cause all 
        keyboard inputs to lag during program runtime.

        Args:
            key: Latest keyboard key the user has pressed.       
        """
        if key == MainWindow.EXIT_HOTKEY: 
            os.kill(os.getpid(), signal.SIGTERM)

    # listener thread object sends keyboard inputs to exit function
    kb_listener = pynput.keyboard.Listener(on_press = exit)
    kb_listener.daemon = True
    kb_listener.start()

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

        self.reader_init = False
        self.init_button_first_time = True

        # variables to check if replay/queue/collection mode is enabled
        self.replay = tk.StringVar(value='Off')
        self.queue = tk.StringVar(value='Off')
        self.collection = tk.StringVar(value='Off')

        mainframe = tk.Frame(root, borderwidth=5, relief='groove', padx=15, pady=15)
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        mainframe.grid(sticky='nwes')
        mainframe.bind("<ButtonRelease-1>", lambda _: self.root.focus())
        
        self.current_map = 'dark castle'
        self.maps_box = ttk.Combobox(mainframe, state='readonly', values=self.get_maps())
        self.maps_box.grid(column=0, row=5, sticky='sw', pady=10)
        self.maps_box.bind("<<ComboboxSelected>>", lambda _: self.update_mapconfig())
        self.maps_box.bind("<<ComboboxSelected>>", lambda _: self.root.focus(), add='+')
        self.maps_box.set(self.current_map)     # initialize with default value

        info_window_scroll = ttk.Scrollbar(mainframe, orient='vertical')
        info_window_scroll.grid(column=2, row=3, rowspan=2, sticky="nsw")

        self.info_window = tk.Text(mainframe, height=9, yscrollcommand=info_window_scroll.set, 
                                   font=("Times New Roman", 11),
                                wrap=tk.WORD, relief='sunken')
        self.info_window.grid(column=0, columnspan=2, row=3, rowspan=2)
        info_window_scroll.configure(command=self.info_window.yview)

        self.current_strat = 'Easy-Standard'
        self.strat_box = ttk.Combobox(mainframe, state='readonly', values=self.get_strats())
        self.strat_box.grid(column=1, row=5, sticky='sw', pady=10)
        self.strat_box.bind("<<ComboboxSelected>>", lambda _: self.update_stratconfig())
        self.strat_box.bind("<<ComboboxSelected>>", lambda _: self.root.focus(), add='+')
        self.strat_box.set(self.current_strat)
        self.show_mapinfo() # initialize info_window with default value 

        self.mapscreen_text_str = (r" ___  _____  ___    __  _          _    "+"\n"
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
            map_image = tk.PhotoImage(file=gui_paths.MAP_IMAGES_PATH+'\\dark castle.png')
            self.mapscreen = ttk.Label(mainframe, image=map_image, compound='top', anchor='nw', relief='sunken', 
                                      justify='left', style='Style.TButton')
            # Save image reference; otherwise Python garbage collection destroys it.
            # For some reason, image is not recognized as an attribute of Label. Thus type ignore to avoid mypy errors.
            self.mapscreen.image = map_image # type: ignore
            self.mapscreen.grid(column=0, row=0, columnspan=3, rowspan=3, sticky='nw')
        except (FileNotFoundError, tk.TclError):
            self.mapscreen = ttk.Label(mainframe, relief='sunken', style='Style.TButton', justify='left')
            self.mapscreen.grid(column=0, row=0, columnspan=2, rowspan=3)
            # Text generated with 'Graceful' font on https://patorjk.com/software/taag
            # Picture is self-made.
            self.mapscreen['text'] = self.mapscreen_text_str

        self.help_button= tk.Button(mainframe, text="Help", height=2, width=5, command=self.help_window, padx=20,
                                    pady=5)
        self.help_button.grid(column=3, row=0, pady=10, sticky='nwe')

        self.hotkey_button = tk.Button(mainframe, text="Set\nhotkeys", height=2, width=5, command=self.hotkey_window,
                                       padx=20, pady=5)
        self.hotkey_button.grid(column=3, row=1, pady=10, sticky='we')

        self.queueoptions_button = tk.Button(mainframe, text="Queue mode\nmaplist", height=2, width=5, 
                                             command=self.queue_mode_window, padx=20, pady=5)
        self.queueoptions_button.grid(column=3, row=2, pady=10, sticky='wes') 

        self.settings_button= tk.Button(mainframe, text="Settings", height=2, width=5,
                                        command=self.settings_window, padx=20, pady=5)
        self.settings_button.grid(column=2, row=0, padx=30, pady=10, sticky='nwe')

        # TODO add editing of plan files inside gui
        #self.edit_plans_button= tk.Button(mainframe, text="Edit Plans", height=2, width=5, command='', padx=20, pady=5)
        #self.edit_plans_button.grid(column=2, row=1, padx=30, pady=10, sticky='nwe')

        self.collection_toggle = tk.Checkbutton(mainframe, text='Collection Event', anchor='e', 
                                                variable=self.collection, offvalue='Off', onvalue='On', pady=10,
                                                state='disabled')
        self.collection_toggle.grid(column=3, row=4, sticky='ne')

        self.queue_toggle = tk.Checkbutton(mainframe, text='Queue mode', anchor='e', variable=self.queue,
                                           command=self.queue_mode_check, offvalue='Off', onvalue='On', pady=10,
                                           state='disabled')
        self.queue_toggle.grid(column=3, row=4, sticky='e')

        self.replay_toggle = tk.Checkbutton(mainframe, text='Replay mode', anchor='e', variable=self.replay, 
                                            command=self.replay_mode_check , offvalue='Off', onvalue='On', pady=10,
                                            state='disabled')
        self.replay_toggle.grid(column=3, row=4, sticky='se')

        # lambda is required to pass a function call with args under 'command'.
        self.monitor_plot_button = tk.Button(mainframe, text='Show plot', height=1, state='normal',
                                             command=lambda: roundplot.plot_plan(self.get_original()))
        self.monitor_plot_button.grid(column=2, row=5, sticky='e', padx=55)

        self.start_button = tk.Button(mainframe, text="Initialize bot", height=2, command=self.monitoring_window,
                                      state='active', padx=10, pady=0)
        self.start_button.grid(column=3, row=5, sticky='e')
    
    def get_maps(self) -> list[str]:
        """Get all map names.

        Returns:
            names: List of all map names parsed from files in 'plans' folder.
        """
        names = []
        for m in self.MAP_NAMES_AND_STRATS_DICT.keys():
            names.append(m)
        return names

    def get_strats(self) -> list[str]:
        """Get all strategy names and update current map info window.

        Returns:
            strats: List of all strategy names parsed from files in 'plans' folder.
        """
        strats = []
        for s in self.MAP_NAMES_AND_STRATS_DICT[self.current_map]:
            strats.append(s)
        self.show_mapinfo()
        return strats

    def update_mapconfig(self) -> None:
        """Reads map combobox value, and updates current map, image and strategies.

        Also sets default value for current strategy after map value is read."""
        for map_name in self.MAP_NAMES_AND_STRATS_DICT.keys():
            if self.maps_box.get() == map_name:
                self.current_map = map_name
                try:
                    temp = tk.PhotoImage(file=gui_paths.MAP_IMAGES_PATH+
                                '\\'+MainWindow.MAP_IMAGES[MainWindow.MAP_IMAGES.index(self.current_map+'.png')])
                    self.mapscreen['text'] = ''
                    self.mapscreen.configure(image=temp)
                    self.mapscreen.image = temp # type: ignore 
                except (AttributeError, ValueError):
                    self.mapscreen.configure(image='', compound='center', anchor='center', justify='left')
                    self.mapscreen['text'] = self.mapscreen_text_str
                self.strat_box.set(self.MAP_NAMES_AND_STRATS_DICT[map_name][0])
                strats_for_map = []
                for strats in self.MAP_NAMES_AND_STRATS_DICT[map_name]:
                    strats_for_map.append(strats)
                self.strat_box.configure(values=strats_for_map)
                self.current_strat = self.MAP_NAMES_AND_STRATS_DICT[map_name][0]
                self.info_window.insert('end', '')
                self.update_stratconfig()
                return
    
    def update_stratconfig(self) -> None:
        """Updates current strat value and possible map info screen if available."""
        for maps in self.MAP_NAMES_AND_STRATS_DICT.keys():
            if self.maps_box.get() == maps:
                strats_for_map = []
                for strats in self.MAP_NAMES_AND_STRATS_DICT[maps]:
                    strats_for_map.append(strats)
                    self.strat_box.configure(values=strats_for_map)
        self.current_strat = self.strat_box.get()
        self.show_mapinfo()

    def show_mapinfo(self) -> None:
        """Displays optional info screen.
        
        Info texts are defined at the beginning of each plan file in 'plans' folder.
        If no valid info string is found, displays a blank screen.
        """
        original = self.get_original()
        with open(gui_paths.PLANS_PATH+'\\'+original+'.py') as file_read:
            infolist = file_read.readlines()
        try:
            if infolist[0] == '\"\"\"\n':
                info_comment_end = infolist[1:].index('\"\"\"\n')
                readtext = ''.join(infolist[1:info_comment_end+1])
                self.current_info = readtext
                self.info_window['state'] = 'normal'
                self.info_window.delete(1.0, tk.END)
                self.info_window.insert('end', self.current_info)
                self.info_window['state'] = 'disabled'
            else:
                self.current_info = ''
                self.info_window['state'] = 'normal'
                self.info_window.delete(1.0, tk.END)
                self.info_window.insert('end', '')
                self.info_window['state'] = 'disabled'
        except IndexError:    
            self.current_info = ''
            self.info_window['state'] = 'normal'
            self.info_window.delete(1.0, tk.END)
            self.info_window.insert('end', '')
            self.info_window['state'] = 'disabled'

    def get_original(self) -> str:
        """Reconstruct the original plan name from a .py file using name and strat components.

        Returns:
            Original strategy file name as a string without .py.
        """
        namesplit = self.current_map.split()
        stratsplit = self.current_strat.split('-')
        return '_'.join(namesplit) + stratsplit[0] + stratsplit[1]
    
    def choose_mode(self) -> list[str]:
        """Returns either a single plan or list of plans from queue list.

        Returns:
            String list of plans based on queue mode settings.
        """
        if self.queue.get() == 'Off':
            return [self.get_original()]
        else:
            with open(gui_paths.QUEUE_LIST_PATH) as file_read:
                return plan_data.list_format(file_read.readlines())

    def ocr_init(self, init_win: tk.Toplevel) -> None:
        """Imports ocr Reader object from bot.ocr.ocr_reader, which also initializes it for use.
        
        This method is called through root.after method to allow mainloop to create a init label and only after start 
        the importing, as otherwise everything would happen at once and init label would quickly flash after then 
        disappear.

        Initialization process takes several seconds as the ocr model is loaded into memory: afterwards, all initially 
        disabled buttons are enabled and free to use. Current init label window is destroyed at the end.
        """
        from bot.ocr.ocr_reader import OCR_READER
        init_win.destroy()
        self.start_button['state'] = 'active'
        self.start_button['text'] = "Open\nbot window"
        self.collection_toggle['state'] = 'active'
        self.queue_toggle['state'] = 'active'
        self.replay_toggle['state'] = 'active'
        self.reader_init = True

    def monitoring_window(self) -> None:
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
            threading.Thread(target=lambda: self.ocr_init(ocr_init_window), daemon=True).start()
            self.start_button.configure(state='disabled')
            return
        self.start_button.configure(state='disabled')
        monitoringwindow = MonitoringWindow(self.choose_mode(), self.replay.get(), self.queue.get(),
                                            self.collection.get())
        monitoringthread = threading.Thread(target=self.is_monitoringwindow, 
                                            args=[monitoringwindow.get_monitoringwindow(),
                                                  monitoringwindow.get_old_output()],
                                            daemon=True)
        monitoringthread.start()

    def is_monitoringwindow(self, current_monitoringwin: tk.Toplevel, old_stdout: TextIO | Any) -> None:
        """MainWindow method that tracks existence of a MonitoringWindow.

        If current MonitoringWindow object no longer exists, enables start button for main screen again and also 
        terminates existing thread allocated to bot program; see gui_vars.py docstring for info. Manual termination 
        is important because if monitoring window was closed during bot runtime, the thread its allocated to would
        still keep executing code. This in turn would prevent you from stopping the current bot execution until it
        finishes, eating up CPU and memory. 

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
            while not current_monitoringwin.winfo_exists():
                gui_tools.terminate_thread(MonitoringWindow.current_bot_thread)
                sys.stdout =  old_stdout # return to original output stream
                if self.queue.get() == 'On':
                    with open(gui_paths.QUEUE_LIST_PATH) as f:
                        if len(f.readlines()) != 0:
                            self.start_button.configure(state='active')
                            return
                    self.start_button.configure(state='disabled')
                    return
                if self.reader_init:
                    self.start_button.configure(state='active')
                return
            self.start_button.configure(state='disabled')
            time.sleep(0.01) # tracking frequency; don't set this to too low as it will strain your CPU for nothing.

    def queue_mode_window(self) -> None:
        """Open queue mode window which operates on its own thread."""
        self.queueoptions_button.configure(state='disabled')
        self.start_button.configure(state='disabled')
        optionwindow = QueueModeWindow()
        optionwindowthread = threading.Thread(target=self.is_queue_mode_screen, args=[optionwindow.get_optionwindow()])
        optionwindowthread.daemon = True
        optionwindowthread.start()

    def is_queue_mode_screen(self, current_options: tk.Toplevel) -> None:
        """Checks if queue mode window exists and handles button access based on this.
        
        Args:
            current_options: Current QueueModeWindow object.
        """
        while True:
            while not current_options.winfo_exists():
                self.queueoptions_button.configure(state='active')
                if self.queue.get() == 'On':
                    self.start_button.configure(state='disabled')
                    with open(gui_paths.QUEUE_LIST_PATH) as f:
                        if len(f.readlines()) != 0:
                            self.start_button.configure(state='active')
                    return
                elif self.init_button_first_time:
                    self.start_button.configure(state='active')
                elif self.reader_init:
                    self.start_button.configure(state='active')
                return
            self.start_button.configure(state='disabled')
            time.sleep(0.01)

    def replay_mode_check(self) -> None:
        """Disables and enabled initialization button based on replay mode toggle.
        
        If replay mode is off and reader has been initialized, enabled start button.
        """
        if self.replay.get() == 'Off' and self.reader_init:
            self.start_button.configure(state='active') 

    def queue_mode_check(self) -> None:
        """Disables and enabled initialization button based on queue mode toggle.
         
        If queue mode is off and reader has been initialized, enabled start button.
        If queue mode is On, but queue has no plans, also disables start button.
        """
        if self.queue.get() == 'Off' and self.reader_init:
            self.start_button.configure(state='active') 
        else:
            with open(gui_paths.QUEUE_LIST_PATH) as file_read:             
                if len(file_read.readlines()) == 0:
                    self.start_button.configure(state='disabled')

    def hotkey_window(self) -> None:
        """Open hotkey window which operates on its own thread."""
        self.hotkey_button.configure(state='disabled')
        self.start_button.configure(state='disabled')
        hotkeywindow = HotkeyWindow()
        hotkeywindowthread = threading.Thread(target=self.is_hotkeywindow, args=[hotkeywindow.get_hotkeywindow()])
        hotkeywindowthread.daemon = True
        hotkeywindowthread.start()

    def is_hotkeywindow(self, current_hotkey: tk.Toplevel) -> None:
        """Checks if hotkey window exists and handles button access based on this.
        
        Args:
            current_hotket: Current HotkeyWindow object.
        """
        while True:
            while not current_hotkey.winfo_exists():
                if HotkeyWindow.input_key_listener.is_alive():
                    HotkeyWindow.input_key_listener.stop()
                self.hotkey_button.configure(state='active')
                if self.queue.get() == 'On':
                    self.start_button.configure(state='disabled')
                elif self.init_button_first_time:
                    self.start_button.configure(state='active')
                elif self.reader_init:
                    self.start_button.configure(state='active')
                return
            self.start_button.configure(state='disabled')
            time.sleep(0.01)

    def help_window(self) -> None:
        """Open help window which operates on its own thread."""
        self.help_button.configure(state='disabled')
        self.start_button.configure(state='disabled')
        helpwindow = HelpWindow()
        helpwindowthread = threading.Thread(target=self.is_helpwindow, args=[helpwindow.get_helpwindow()])
        helpwindowthread.daemon = True
        helpwindowthread.start()

    def is_helpwindow(self, current_help: tk.Toplevel) -> None:
        """Checks if help window exists and handles button access based on this.
        
        Args:
            current_help: Current HelpWindow object.
        """
        while True:
            while not current_help.winfo_exists():
                self.help_button.configure(state='active')
                if self.queue.get() == 'On':
                    self.start_button.configure(state='disabled')
                elif self.init_button_first_time:
                    self.start_button.configure(state='active')
                elif self.reader_init:
                    self.start_button.configure(state='active')
                return
            self.start_button.configure(state='disabled')
            time.sleep(0.01)
     
    def settings_window(self) -> None:
        """Open settings window which operates on its own thread."""
        self.settings_button.configure(state='disabled')
        self.start_button.configure(state='disabled')
        settingswindow = SettingsWindow()
        settingsthread = threading.Thread(target=self.is_settingswindow, args=[settingswindow.get_settingswindow()])
        settingsthread.daemon = True
        settingsthread.start()

    def is_settingswindow(self, current_settings: tk.Toplevel) -> None:
        """Checks if settings window exists and handles button access based on this.
        
        Args:
            current_settings: Current SettingsWindow object.
        """
        while True:
            while not current_settings.winfo_exists():
                self.settings_button.configure(state='active')
                if self.queue.get() == 'On' and self.reader_init:
                    self.start_button.configure(state='disabled')
                elif self.init_button_first_time:
                    self.start_button.configure(state='active')
                elif self.reader_init:
                    self.start_button.configure(state='active')
                return
            self.start_button.configure(state='disabled')
            time.sleep(0.01)