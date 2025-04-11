"""Contains SettingsWindow class."""

from __future__ import annotations
from typing import TYPE_CHECKING
import json
import tkinter as tk

import gui.gui_paths as gui_paths

if TYPE_CHECKING:
    from typing import Any

class SettingsWindow:
    """Creates a settings window. All settings in stored and read from gui_vars.json.
    
    Attributes:
        settings_window (Tk.Toplevel): Toplevel window.
        record_time (tk.StringVar): Stores current status of record_toggle button.
        time_limit_entry (tk.Entry): Entry box to type new time recording limit value. This value is saved into 
            gui_vars.json file.
    """
    def __init__(self) -> None:
        """Initialize settings window."""
        self.settings_window = tk.Toplevel()
        self.settings_window.title("Settings")
        self.settings_window.geometry('580x750+100+250')
        self.settings_window.minsize(580,750)
        self.settings_window.maxsize(580,750)

        self.settings_window.grid_columnconfigure((0,1,2,3,4), weight=1, uniform='1')

        self.record_time = tk.StringVar(value='Off')
        self.roundtime = tk.StringVar(value='Off')
        self.update_current_status()
        self.update_roundtime_status()

        tk.Label(self.settings_window, 
                 text='These control bot behaviour (more stuff is added later).\n'
                    'Settings carry over sessions: remember to adjust them if necessary.\n'
                    '# Text can be scrolled down if there\'s more available #\n'
                 ).grid(column=1, row=0, columnspan=3)
        

        basic_text = tk.Label(self.settings_window, 
                              text='o-------o\n'
                                   '|  Basic  |\n'
                                   'o-------o')
        basic_text.grid(column=0, columnspan=2, row=1, sticky='w', padx=5)

        roundtime_toggle = tk.Checkbutton(self.settings_window, text="Display round timer", anchor='nw', onvalue='On', 
                                            offvalue='Off', pady=5, padx=18, variable=self.roundtime,
                                            command=self.change_roundtime_status)
        roundtime_toggle.grid(column=0, row=2, columnspan=2, sticky='nw')
        roundtime_text = tk.Text(self.settings_window, wrap=tk.WORD, width=62, height=1)
        roundtime_text.grid(column=0, row=3, columnspan=5, pady=5)
        roundtime_text.insert('end', "Display current round timer inside monitoring window.")
        roundtime_text['state'] = 'disabled'


        record_toggle = tk.Checkbutton(self.settings_window, text="Record round times", anchor='nw', onvalue='On', 
                                       offvalue='Off', pady=5, padx=18, variable=self.record_time,
                                       command=self.change_record_status)
        record_toggle.grid(column=0, row=4, columnspan=2, sticky='nw')
        record_text = tk.Text(self.settings_window, wrap=tk.WORD, width=62, height=4)
        record_text.grid(column=0, row=5, columnspan=5, pady=5)
        record_text.insert('end', "Records all round times during a plan and updates them under "
                            "\'Show Plot\'. Plan must be completed with all rounds finished in one go "
                            "and bot returned to menu screen. Overwrites existing data so updating times is easy.")
        record_text['state'] = 'disabled'
        
        
        debug_text = tk.Label(self.settings_window, 
                              text='o-------------------------------------o\n'
                                   '| Advanced (mostly for debugging) |\n'
                                   'o-------------------------------------o')
        debug_text.grid(column=0, columnspan=2, row=6, sticky='w', padx=5, pady=(15, 1))

        self.time_limit = tk.StringVar(value=self.read_checking_time_limit())
        
        time_limit_label = tk.Label(self.settings_window, text='Ocr time limit: ')
        time_limit_label.grid(column=0, row=7, sticky='se', padx=15, pady=(5,1))
        time_limit_current_value = tk.Label(self.settings_window, relief='ridge', textvariable=self.time_limit)
        time_limit_current_value.grid(column=1, row=7, sticky='sw', padx=1, pady=(5,1))

        self.time_limit_entry = tk.Entry(self.settings_window, width=10)
        self.time_limit_entry.grid(column=0, row=8, sticky='sw', pady=(1,10), padx=21)

        time_limit_button = tk.Button(self.settings_window, text="Set time limit", anchor='w', padx=5,
                                           command=self.set_time_limit_value)
        time_limit_button.grid(column=1, row=8, sticky='w', pady=(1,10))

        time_limit_text = tk.Text(self.settings_window, wrap=tk.WORD, width=62, height=3)
        time_limit_text.grid(column=0, row=9, columnspan=5)
        time_limit_text.insert('end', "Time limit, in seconds, until bot stops trying to place/upgrade a monkey/search "
                                "for the next round, and returns to menu. Only needed if ocr gets stuck; high value "
                                "(300 or greater) is recommended.")
        time_limit_text['state'] = 'disabled'

    def update_roundtime_status(self) -> None:
        """After re-opening this window, updates toggle button value to actual round time status value."""
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, Any] = json.load(f)
        if gui_vars_dict["get_botdata"] == True:
            self.roundtime.set('On')

    def change_roundtime_status(self) -> None:
        """Changes round time display status value based on toggle button value."""
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, Any] = json.load(f)
        if self.roundtime.get() == 'On':
            gui_vars_dict["get_botdata"] = True
        elif self.roundtime.get() == 'Off':
            gui_vars_dict["get_botdata"] = False
        with open(gui_paths.FILES_PATH/'gui_vars.json', 'w') as f:
            json.dump(gui_vars_dict, f, indent=4)

    def update_current_status(self) -> None:
        """After re-opening this window, updates toggle button value to actual record status value."""
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, Any] = json.load(f)
        if gui_vars_dict["time_recording_status"] == True:
            self.record_time.set('On')

    def change_record_status(self) -> None:
        """Changes time recording status value based on toggle button value."""
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, Any] = json.load(f)
        if self.record_time.get() == 'On':
            gui_vars_dict["time_recording_status"] = True
        elif self.record_time.get() == 'Off':
            gui_vars_dict["time_recording_status"] = False
        with open(gui_paths.FILES_PATH/'gui_vars.json', 'w') as f:
            json.dump(gui_vars_dict, f, indent=4)

    def read_checking_time_limit(self) -> str:
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, int | bool | str] = json.load(f)
        return str(gui_vars_dict["checking_time_limit"])

    def set_time_limit_value(self) -> None:
        """Saves current time limit value to gui_vars.json.
        
        Accepted time values are integer from 1 (a second) to 3600 (an hour).
        """
        try:
            val = int(self.time_limit_entry.get())
            if 0 < val <= 3600:
                with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
                    gui_vars_dict: dict[str, Any] = json.load(f)
                gui_vars_dict["checking_time_limit"] = val
                self.time_limit.set(str(gui_vars_dict["checking_time_limit"]))
                with open(gui_paths.FILES_PATH/'gui_vars.json', 'w') as f:
                    json.dump(gui_vars_dict, f, indent=4)
        except ValueError:
            ...

    def get_settingswindow(self) -> tk.Toplevel:
        """Get current settings window.
        
        Returns:
            Current Toplevel window object of SettingsWindow.
        """
        return self.settings_window