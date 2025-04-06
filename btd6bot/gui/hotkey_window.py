"""Contains HotkeyWindow class."""

from __future__ import annotations
from typing import TYPE_CHECKING
import tkinter as tk

import pynput

import gui.gui_paths as gui_paths
from utils import plan_data

if TYPE_CHECKING:
    from pynput.keyboard import Key, KeyCode

class HotkeyWindow:
    """Handles reading and updating of hotkey settings.

    Text is both read and written to a text file ./text files/help.txt.
    A separate Toplevel object is created so that other tkinter widgets can be placed inside it.

    Attributes:
        hotkey_list (list[str], class attribute): Loads current hotkey settings from a file and saves them into a 
            string list.
        input_key_listener (pynput.keyboard.Listener, class attribute): Only used for handling a hotkey-related bug: if 
            user presses 'set hotkey' button in hotkey window, program waits for an input. But if no input is given and 
            window gets closed, then input tracking should also stop - but it doesn't, unless MainWindow stops the 
            listener after HotkeyWindow no longer exists. By giving MainWindow access by class attribute, this gets 
            solved easily.

        hotkeywindow (tk.Toplevel): Toplevel object that creates a new window where other elements can be inserted.
        hotkeyoptionlist (tk.Listbox): Listbox containing all hotkeys as separate rows.
        sethotkeybutton (tk.Button): Button to rebind currently selected hotkey in hotkey list.
        info (tk.Label): Label that displays hotkey help text.
    """
    with open(gui_paths.HOTKEYS_PATH) as file_read:
        hotkey_list: list[str] = plan_data.list_format(file_read.readlines())

    input_key_listener: pynput.keyboard.Listener = pynput.keyboard.Listener()

    def __init__(self) -> None:  
        """Initialize hotkey window."""   
        self.hotkeywindow = tk.Toplevel()
        self.hotkeywindow.title("Hotkeys")
        self.hotkeywindow.columnconfigure(0, weight=1)
        self.hotkeywindow.rowconfigure(0, weight=1)
        self.hotkeywindow.geometry('800x600+900+350')
        self.hotkeywindow.minsize(800,600)
        self.hotkeywindow.maxsize(800,600)

        hotkeylabel = tk.Label(self.hotkeywindow, text='Hotkeys', height=1, relief="groove")
        hotkeylabel.grid(column=0, row=0, sticky="nsew", padx=20, pady=5)
        self.hotkeyoptionlist = tk.Listbox(self.hotkeywindow, width=30)
        self.hotkeyoptionlist.grid(column=0, row=1, padx=20, sticky="nsew")

        self.sethotkeybutton = tk.Button(self.hotkeywindow, text='Set hotkey', width=15, height=1,
                                         command=self.set_hotkey)
        self.sethotkeybutton.grid(column=0, row=2, sticky="s")

        hotkeyhelplabel = tk.Label(self.hotkeywindow, text='Instructions', height=1, relief="groove")
        hotkeyhelplabel.grid(column=1, row=0, sticky="nsew", padx=20, pady=5)
        self.info = tk.Label(self.hotkeywindow, justify='left', relief='sunken',
                             text=self.showhotkeyhelp())
        self.info.grid(column=1, row=1, padx=20, sticky="nsew")

        self.read_hotkeys()

    def showhotkeyhelp(self) -> str:
        """Return hotkey help text for info label.

        Returns:
            Help text string.
        """
        with open(gui_paths.HOTKEY_HELP_PATH) as file_read:
            return ''.join(file_read.readlines())
            
    def set_hotkey(self) -> None:
        """Set a hotkey value for currently highlighted row.
        
        Listener objects can be passed values by using lambda functions and giving the key as first argument to target 
        function.
        """
        self.sethotkeybutton.configure(state='disabled')
        new_input = self.hotkeyoptionlist.curselection() # type: ignore
        if new_input == ():
            self.sethotkeybutton.configure(state='active')
            return
        selected = self.hotkeyoptionlist.curselection()[0] # type: ignore
        self.input_key = pynput.keyboard.Listener(on_press=lambda event: 
                                                  self.press_hotkey(key=event, selected_row=selected))
        HotkeyWindow.input_key_listener = self.input_key
        self.input_key.daemon = True
        self.input_key.start()
    
    def press_hotkey(self, key: Key | KeyCode | None, selected_row: int) -> None:
        """Update pressed hotkey to hotkey text file, then call read_hotkeys to update current Listbox.

        Args:
            key: Latest keyboard key the user has pressed.
            selected_row: Number of currently selected row: top row is 0, increases downwards.
        """
        previous_key_begin = HotkeyWindow.hotkey_list[selected_row].split(' = ')[0]
        HotkeyWindow.hotkey_list[selected_row] = previous_key_begin + ' = ' + str(key).replace('\'', '')
        with open(gui_paths.HOTKEYS_PATH, 'w') as file_write:
            for line in HotkeyWindow.hotkey_list:
                file_write.write(line+'\n')
        self.hotkeyoptionlist.delete(0, 'end')
        self.read_hotkeys()
        self.input_key.stop()
        self.sethotkeybutton.configure(state='active')
        return

    def read_hotkeys(self) -> None:
        """Read all hotkeys from hotkey_list and insert them to Listbox object."""
        index = 0
        for index in range(0, len(HotkeyWindow.hotkey_list)):
            self.hotkeyoptionlist.insert(index, HotkeyWindow.hotkey_list[index])

    def get_hotkeywindow(self) -> tk.Toplevel:
        """Get current hotkey window.
        
        Returns:
            Current Toplevel window object of HotkeyWindow.
        """
        return self.hotkeywindow