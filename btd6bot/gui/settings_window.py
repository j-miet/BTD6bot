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

        self.version = tk.StringVar(value=self.read_value("version"))
        self.record_time = tk.StringVar(value='Off')
        self.gamesettings = tk.StringVar(value='Off')
        self.time_limit = tk.StringVar(value=self.read_value("checking_time_limit"))
        self.update_variables()

        tk.Label(self.settings_window, 
                 text='Settings are saved in/loaded from a file and carry over sessions\n'
                    '# Text in boxes can be scrolled if there\'s more available #\n'
                ).grid(column=1, row=0, columnspan=3)
        basic_text = tk.Label(self.settings_window, 
                              text='o-------o\n'
                                   '|  Basic  |\n'
                                   'o-------o')
        basic_text.grid(column=0, columnspan=2, row=1, sticky='w', padx=5)

        version_label = tk.Label(self.settings_window, text='Game version')
        version_label.grid(column=0, row=2, sticky='se', padx=(1,21), pady=(5,1))
        version_current_value = tk.Label(self.settings_window, relief='ridge', textvariable=self.version)
        version_current_value.grid(column=1, row=2, sticky='sw', padx=1, pady=(5,1))

        self.version_entry = tk.Entry(self.settings_window, width=10)
        self.version_entry.grid(column=0, row=3, sticky='e', pady=(1,10), padx=(21,31))

        version_button = tk.Button(self.settings_window, text="Update version", anchor='w', padx=5,
                                           command=self.set_version_value)
        version_button.grid(column=1, row=3, sticky='w', pady=(1,10))

        checksettings_toggle = tk.Checkbutton(self.settings_window, 
                                                text="Update esc menu settings automatically", anchor='nw', 
                                                onvalue='On', offvalue='Off', pady=5, padx=18, 
                                                variable=self.gamesettings,
                                                command=self.change_checksettings_status)
        checksettings_toggle.grid(column=0, row=5, columnspan=2, sticky='nw')
        checksettings_text = tk.Text(self.settings_window, wrap=tk.WORD, width=62, height=3)
        checksettings_text.grid(column=0, row=6, columnspan=5, pady=5)
        checksettings_text.insert('end', "Checks if following are enabled and if not, enables them automatically: "
                                        "drag & drop, disable nudge mode, auto start. Checking is done only once in"
                                        "a session, after entering a map first time.")
        checksettings_text['state'] = 'disabled'

        record_toggle = tk.Checkbutton(self.settings_window, text="Record round times and update plan version", 
                                       anchor='nw', onvalue='On', 
                                       offvalue='Off', pady=5, padx=18, variable=self.record_time,
                                       command=self.change_record_status)
        record_toggle.grid(column=0, row=7, columnspan=2, sticky='nw')
        record_text = tk.Text(self.settings_window, wrap=tk.WORD, width=62, height=3)
        record_text.grid(column=0, row=8, columnspan=5, pady=5)
        record_text.insert('end', "Records all round times during a plan and updates them under "
                            "\'Show Plot\'. Bot must finish all rounds without restarts and return to menu "
                            "screen, otherwise no data is stored. Current version is also stored for each plan which "
                            "is then displayed in info panel. Overwrites existing data, making updating values easy." 
                            )        
        record_text['state'] = 'disabled'
        
        
        debug_text = tk.Label(self.settings_window, 
                              text='o--------------------------------------o\n'
                                   '|  Advanced (for debugging/testing)  |\n'
                                   'o--------------------------------------o')
        debug_text.grid(column=0, columnspan=2, row=9, sticky='w', padx=5, pady=(15, 1))
        
        time_limit_label = tk.Label(self.settings_window, text='Ocr time limit')
        time_limit_label.grid(column=0, row=10, sticky='se', padx=(1,21), pady=(5,1))
        time_limit_current_value = tk.Label(self.settings_window, relief='ridge', textvariable=self.time_limit)
        time_limit_current_value.grid(column=1, row=10, sticky='sw', padx=1, pady=(5,1))

        self.time_limit_entry = tk.Entry(self.settings_window, width=10)
        self.time_limit_entry.grid(column=0, row=11, sticky='e', pady=(1,10), padx=(21,31))

        time_limit_button = tk.Button(self.settings_window, text="Update time limit", anchor='w', padx=5,
                                           command=self.set_time_limit_value)
        time_limit_button.grid(column=1, row=11, sticky='w', pady=(1,10))

        time_limit_text = tk.Text(self.settings_window, wrap=tk.WORD, width=62, height=4)
        time_limit_text.grid(column=0, row=12, columnspan=5)
        time_limit_text.insert('end', "Time limit, in seconds, until bot stops trying to place/upgrade a monkey/search "
                                "for the next round, and returns to menu. Only needed if ocr gets stuck; high value "
                                "(300 or greater) is recommended.")
        time_limit_text['state'] = 'disabled'

    def update_variables(self) -> None:
        """Updates toggle button values with matching gui_vars.json values."""
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, Any] = json.load(f)
            if gui_vars_dict["check_gamesettings"]:
                self.gamesettings.set('On')
            if gui_vars_dict["time_recording_status"]:
                self.record_time.set('On')

    def change_checksettings_status(self) -> None:
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, Any] = json.load(f)
        if self.gamesettings.get() == 'On':
            gui_vars_dict["check_gamesettings"] = True
        elif self.gamesettings.get() == 'Off':
            gui_vars_dict["check_gamesettings"] = False
        with open(gui_paths.FILES_PATH/'gui_vars.json', 'w') as f:
            json.dump(gui_vars_dict, f, indent=4)

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

    def set_version_value(self) -> None:
        """Saves current version value to gui_vars.json.
        
        Accepted time values are integer from 1 to 999.
        """
        try:
            val = int(self.version_entry.get())
            if 0 < val <= 999:
                with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
                    gui_vars_dict: dict[str, Any] = json.load(f)
                gui_vars_dict["version"] = val
                self.version.set(str(gui_vars_dict["version"]))
                with open(gui_paths.FILES_PATH/'gui_vars.json', 'w') as f:
                    json.dump(gui_vars_dict, f, indent=4)
        except ValueError:
            ...

    def read_value(self, id_str: str) -> str:
        """Sets previously stored value in labels as initial value."""
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, int | bool | str] = json.load(f)
        return str(gui_vars_dict[id_str])

    def get_settingswindow(self) -> tk.Toplevel:
        """Get current settings window.
        
        Returns:
            Current Toplevel window object of SettingsWindow.
        """
        return self.settings_window