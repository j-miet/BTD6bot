"""Implements HotkeyWindow class."""

from __future__ import annotations
from typing import TYPE_CHECKING
import sys
import tkinter as tk
from tkinter import simpledialog

import pynput

from bot.hotkeys import PYNPUT_KEYS
from gui.guihotkeys import GuiHotkeys
import gui.gui_paths as gui_paths
from gui.gui_tools import os_font
from utils import plan_data

if TYPE_CHECKING:
    from pynput.keyboard import Key, KeyCode

class HotkeyWindow:
    """Handles reading and updating of hotkey settings.

    Text is both read and written to a text file ./text files/help.txt.
    A separate Toplevel object is created so that other tkinter widgets can be placed inside it.

    Attributes:
        input_key_listener (pynput.keyboard.Listener, class attribute): 
            Only used for handling a hotkey-related bug: if user presses 'set hotkey' button in hotkey window, program 
            waits for an input. But if no input is given and window gets closed, then input tracking should also stop. 
            But it doesn't unless MainWindow stops the listener after HotkeyWindow no longer exists. By giving 
            MainWindow access by class attribute, this gets solved easily.
    """
    input_key_listener: pynput.keyboard.Listener = pynput.keyboard.Listener()

    def __init__(self) -> None:  
        """Initialize hotkey window."""   
        self.hotkeywindow = tk.Toplevel()
        self.hotkeywindow.title("Hotkeys")
        self.hotkeywindow.iconbitmap(gui_paths.FILES_PATH/'btd6bot.ico')
        self.hotkeywindow.columnconfigure(0, minsize=190, weight=1)
        self.hotkeywindow.rowconfigure(0, weight=1)
        self.hotkeywindow.geometry('800x600+900+350')
        self.hotkeywindow.minsize(800,600)
        self.hotkeywindow.maxsize(800,600)

        self.input_key: pynput.keyboard.Listener

        with open(gui_paths.HOTKEYS_PATH) as hotkey_read:
            self.hotkey_list: list[str] = plan_data.list_format(hotkey_read.readlines())
        with open(gui_paths.GUIHOTKEYS_PATH) as guihotkey_read:
            self.guihotkey_list: list[str] = plan_data.list_format(guihotkey_read.readlines())

        hotkeylabel = tk.Label(
            self.hotkeywindow, 
            text='Hotkeys', 
            height=1, 
            relief="groove", 
            font=os_font
        )
        hotkeylabel.grid(column=0, row=0, sticky="nsew", padx=20, pady=5)
        self.hotkeyoptionlist = tk.Listbox(
            self.hotkeywindow, 
            width=30, 
            font=os_font
        )
        self.hotkeyoptionlist.grid(column=0, row=1, padx=20, sticky="nsew")

        self.guihotkeyoptionlist = tk.Listbox(
            self.hotkeywindow, 
            width=30, 
            height=3, 
            font=os_font
        )
        self.guihotkeyoptionlist.grid(column=0, row=2, padx=20, sticky="nsew")

        self.sethotkeybutton = tk.Button(
            self.hotkeywindow, 
            text='Set hotkey', 
            width=15, 
            height=1, 
            font=os_font,
            command=self._set_hotkey
        )
        self.sethotkeybutton.grid(column=0, row=3, sticky="s")

        hotkeyhelplabel = tk.Label(
            self.hotkeywindow, 
            text='Instructions', 
            height=1, 
            relief="groove", 
            font=os_font
        )
        hotkeyhelplabel.grid(column=1, row=0, sticky="nsew", padx=20, pady=5)
        
        self.info = tk.Label(
            self.hotkeywindow, 
            justify='left', 
            relief='sunken', 
            text=self._showhotkeyhelp(), 
            font=os_font
        )
        self.info.grid(column=1, row=1, padx=20, sticky="nsew")

        self._read_hotkeys()
        if sys.platform != 'darwin':
            self._read_guihotkeys()
        else:
            self.sethotkeybutton = tk.Button(
                self.hotkeywindow, 
                text='Edit selected entry', 
                width=15, 
                height=1, 
                font=os_font,
                command=self._save_hotkeys
            )
            self.sethotkeybutton.grid(column=0, row=3, sticky="s")
            self.guihotkeyoptionlist.insert(0, "Gui hotkeys are disabled")
            self.guihotkeyoptionlist.insert(1, "for MacOS platforms")
            self.guihotkeyoptionlist.insert(2, "")
            self.guihotkeyoptionlist['state'] = 'disabled'

    def _save_hotkeys(self) -> None:
        """Set a hotkey value for currently highlighted row without pynput.Listener.
        
        Similar to set_hotkey, but requires user to manually type in hotkeys. 
        
        Used with Mac operating systems as pynput Listener/Controller thread objects cause critical error when used
        alongside tkinter gui.
        """
        self.sethotkeybutton.configure(state='disabled')
        new_input = self.hotkeyoptionlist.curselection()
        new_input2 = self.guihotkeyoptionlist.curselection()
        if new_input == () and new_input2 == ():
            self.sethotkeybutton.configure(state='active')
            return
        elif new_input != ():
            selected = self.hotkeyoptionlist.curselection()[0]
            selected_text = self.hotkey_list[selected].split(' = ')[0]
            user_input = simpledialog.askstring(title="Hotkey", prompt="Insert a new key value for: "+selected_text)
            if user_input is not None:
                if len(user_input) != 0:
                    self.hotkey_list[selected] = selected_text + ' = ' + user_input.lower()
                    with open(gui_paths.HOTKEYS_PATH, 'w') as file_write:
                        for line in self.hotkey_list:
                            file_write.write(line+'\n')
                    self.hotkeyoptionlist.delete(0, 'end')
                    self._read_hotkeys()
            self.sethotkeybutton.configure(state='active')
        elif new_input2 != ():
            selected = self.guihotkeyoptionlist.curselection()[0]
            selected_text = self.guihotkey_list[selected].split(' = ')[0]
            user_input = simpledialog.askstring(title="Hotkey", prompt="Insert a new key value for: "+selected_text)
            if user_input is not None:
                if len(user_input) != 0:
                    self.guihotkey_list[selected] = selected_text + ' = ' + user_input.lower()
                    with open(gui_paths.GUIHOTKEYS_PATH, 'w') as file_write:
                        for line in self.guihotkey_list:
                            file_write.write(line+'\n')
                    self.guihotkeyoptionlist.delete(0, 'end')
                    self._read_guihotkeys()
            self.sethotkeybutton.configure(state='active')

    def _showhotkeyhelp(self) -> str:
        """Return hotkey help text for info label.

        Returns:
            Help text string.
        """
        with open(gui_paths.HOTKEY_HELP_PATH) as file_read:
            return ''.join(file_read.readlines())
            
    def _set_hotkey(self) -> None:
        """Set a hotkey value for currently highlighted row.
        
        Listener objects can be passed values by using lambda functions and giving the key as first argument to target 
        function.
        """
        self.sethotkeybutton.configure(state='disabled')
        new_input = self.hotkeyoptionlist.curselection()
        new_input2 = self.guihotkeyoptionlist.curselection()
        if new_input == () and new_input2 == ():
            self.sethotkeybutton.configure(state='active')
            return
        elif new_input != ():
            selected = self.hotkeyoptionlist.curselection()[0]
            self.input_key = pynput.keyboard.Listener(on_press=lambda event: 
                                                    self._press_hotkey(key=event, selected_row=selected))
        elif new_input2 != ():
            selected = self.guihotkeyoptionlist.curselection()[0]
            self.input_key = pynput.keyboard.Listener(on_press=lambda event: 
                                                    self._press_guihotkey(key=event, selected_row=selected))
        HotkeyWindow.input_key_listener = self.input_key
        self.input_key.daemon = True
        self.input_key.start()

    def _press_hotkey(self, key: Key | KeyCode | None, selected_row: int) -> None:
        """Update pressed hotkey to text file, then call read_hotkeys to update current Listbox.

        Args:
            key: Latest keyboard key the user has pressed.
            selected_row: Number of currently selected row: top row is 0, increases downwards.
        """
        previous_key_begin: str = self.hotkey_list[selected_row].split(' = ')[0]
        key_pressed: str = str(key)
        if 'Key.' in key_pressed:
            key_pressed = key_pressed.replace("Key.", "")
            if key_pressed not in PYNPUT_KEYS.keys():
                self.input_key.stop()
                self.sethotkeybutton.configure(state='active')
                return
        self.hotkey_list[selected_row] = previous_key_begin + ' = ' + key_pressed.replace('\'', '')
        with open(gui_paths.HOTKEYS_PATH, 'w') as file_write:
            for line in self.hotkey_list:
                file_write.write(line+'\n')
        self.hotkeyoptionlist.delete(0, 'end')
        self._read_hotkeys()
        self.input_key.stop()
        self.sethotkeybutton.configure(state='active')

    def _read_hotkeys(self) -> None:
        """Read all hotkeys from hotkey_list and insert them to Listbox object."""
        for index in range(0, len(self.hotkey_list)):
            self.hotkeyoptionlist.insert(index, self.hotkey_list[index])
    
    def _press_guihotkey(self, key: Key | KeyCode | None, selected_row: int) -> None:
        """Update pressed gui hotkey to hotkey text file, then call read_guihotkeys to update current Listbox.
        
         Args:
            key: Latest keyboard key the user has pressed.
            selected_row: Number of currently selected row: top row is 0, increases downwards.
        """
        previous_key_begin = self.guihotkey_list[selected_row].split(' = ')[0]
        key_pressed: str = str(key)
        if 'Key.' in key_pressed:
            key_pressed = key_pressed.replace("Key.", "")
            if key_pressed not in PYNPUT_KEYS.keys():
                self.input_key.stop()
                self.sethotkeybutton.configure(state='active')
                return
        self.guihotkey_list[selected_row] = previous_key_begin + ' = ' + key_pressed.replace('\'', '')
        with open(gui_paths.GUIHOTKEYS_PATH, 'w') as file_write:
            for line in self.guihotkey_list:
                file_write.write(line+'\n')
        self.guihotkeyoptionlist.delete(0, 'end')
        self._read_guihotkeys()
        self.input_key.stop()
        GuiHotkeys.update_guihotkeys()
        self.sethotkeybutton.configure(state='active')

    def _read_guihotkeys(self) -> None:
        """Read all gui hotkeys from guihotkey_list and insert them to Listbox object."""
        for index in range(0, len(self.guihotkey_list)):
            self.guihotkeyoptionlist.insert(index, self.guihotkey_list[index])

    def get_hotkeywindow(self) -> tk.Toplevel:
        """Get current hotkey window.
        
        Returns:
            Current Toplevel window object of HotkeyWindow.
        """
        return self.hotkeywindow