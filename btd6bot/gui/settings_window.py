"""Contains SettingsWindow class."""

from __future__ import annotations
from typing import TYPE_CHECKING
import json
import tkinter as tk

import pyautogui

import gui.gui_paths as gui_paths

if TYPE_CHECKING:
    from typing import Any

class SettingsWindow:
    """Creates a settings window. All settings in stored and read from gui_vars.json.
    
    Attributes:
        settings_window (Tk.Toplevel): Toplevel window.
        resolution (tk.StringVar): Enable/disable Custom display resolution.
        resolution_value (tk.StringVar): Custom display resolution value.
        version (tk.StringVar): Game version.
        record_time (tk.StringVar): Time recording status.
        gamesettings (tk.StringVar): Enable/disable saving game values for monitoring window.
        time_limit (tk.StringVar): Ocr time limit until bot gives up.
        delta_ocrtext (tk.StringVar): Delta text print enabled/disabled.
        substring_ocrtext (tk.StringVar): Substring text print enabled/disabled. 
        windowed (tk.StringVar): Windowed mode enabled/disabled.
        ocrtext (tk.StringVar): Enable/disable print of ocr text values.
        resolution_width_entry (tk.Entry): Width value for display resolution.
        resolution_height_entry (tk.Entry): Height value for display resolution.
        windowed_toggle (tk.Checkbutton): Toggle windowed mode on/off.
        version_entry (tk.Entry): Entry box for game version.
        time_limit_entry (tk.Entry): Entry box for ocr time limit value.
    """

    def __init__(self) -> None:
        """Initialize settings window."""
        self.settings_window = tk.Toplevel()
        self.settings_window.title("Settings")
        self.settings_window.geometry('580x750+100+250')
        self.settings_window.minsize(580,750)
        self.settings_window.maxsize(580,750)

        self.settings_window.grid_columnconfigure((0,1,2,3,4), weight=1, uniform='1')

        self.resolution = tk.StringVar(value='Off')
        self.resolution_value = tk.StringVar(value=self.read_value("custom_resolution"))
        self.version = tk.StringVar(value=self.read_value("version"))
        self.record_time = tk.StringVar(value='Off')
        self.gamesettings = tk.StringVar(value='Off')
        self.time_limit = tk.StringVar(value=self.read_value("checking_time_limit"))
        self.delta_ocrtext = tk.StringVar(value='Off')
        self.substring_ocrtext = tk.StringVar(value='Off')
        self.windowed = tk.StringVar(value='Off')

        tk.Label(self.settings_window, 
                 text='Settings are saved in/loaded from a file and carry over sessions\n'
                    '# Text in boxes can be scrolled if there\'s more available #\n'
                ).grid(column=1, row=0, columnspan=3)
        basic_text = tk.Label(self.settings_window, 
                              text='o-------o\n'
                                   '|  Basic  |\n'
                                   'o-------o')
        basic_text.grid(column=0, columnspan=2, row=1, sticky='w', padx=5)

        resolution_toggle = tk.Checkbutton(self.settings_window, 
                                            text="Enable custom resolution", anchor='nw', 
                                            onvalue='On', offvalue='Off', pady=5, padx=18, 
                                            variable=self.resolution,
                                            command=self.change_resolution_status)
        resolution_toggle.grid(column=0, row=2, columnspan=3, sticky='nw')

        resolution_label = tk.Label(self.settings_window, text='Current resolution')
        resolution_label.grid(column=2, row=2, sticky='sw', padx=1, pady=(1,10))
        resolution_current_value = tk.Label(self.settings_window, relief='ridge', textvariable=self.resolution_value)
        resolution_current_value.grid(column=3, row=2, sticky='sw', padx=(1,35), pady=(1,10))

        self.resolution_width_entry = tk.Entry(self.settings_window, width=10)
        self.resolution_width_entry.grid(column=0, row=3, sticky='e', pady=(1,10), padx=(5,31))
        self.resolution_width_entry.insert(0, "width")
        self.resolution_width_entry.bind('<FocusIn>', lambda _: self._clear_entry())
        self.resolution_width_entry.config(fg='grey')
        self.resolution_height_entry = tk.Entry(self.settings_window, width=10)
        self.resolution_height_entry.grid(column=1, row=3, sticky='w', pady=(1,10), padx=(1,1))
        self.resolution_height_entry.insert(0, "height")
        self.resolution_height_entry.bind('<FocusIn>', lambda _: self._clear_entry())
        self.resolution_height_entry.config(fg='grey')
        resolution_button = tk.Button(self.settings_window, text="Update resolution", anchor='w', padx=5,
                                        command=self.set_resolution_value)
        resolution_button.grid(column=2, row=3, sticky='w', pady=(1,10))

        self.windowed_toggle = tk.Checkbutton(self.settings_window, 
                                            text="Windowed mode (BTD6 must be opened with -popupwindow "
                                                "launch option)", 
                                            anchor='nw', 
                                            onvalue='On', offvalue='Off', pady=5, padx=18, 
                                            variable=self.windowed,
                                            command=self.change_windowed_status)
        self.windowed_toggle.grid(column=0, row=4, columnspan=5, sticky='nw')

        version_label = tk.Label(self.settings_window, text='Game version')
        version_label.grid(column=0, row=5, sticky='se', padx=(1,21), pady=(5,1))
        version_current_value = tk.Label(self.settings_window, relief='ridge', textvariable=self.version)
        version_current_value.grid(column=1, row=5, sticky='sw', padx=1, pady=(5,1))

        self.version_entry = tk.Entry(self.settings_window, width=10)
        self.version_entry.grid(column=0, row=6, sticky='e', pady=(1,10), padx=(21,31))
        version_button = tk.Button(self.settings_window, text="Update version", anchor='w', padx=5,
                                           command=self.set_version_value)
        version_button.grid(column=1, row=6, sticky='w', pady=(1,10))

        checksettings_toggle = tk.Checkbutton(self.settings_window, 
                                                text="Update esc menu settings automatically", anchor='nw', 
                                                onvalue='On', offvalue='Off', pady=5, padx=18, 
                                                variable=self.gamesettings,
                                                command=self.change_checksettings_status)
        checksettings_toggle.grid(column=0, row=7, columnspan=3, sticky='nw')

        checksettings_text = tk.Text(self.settings_window, wrap=tk.WORD, width=62, height=3)
        checksettings_text.grid(column=0, row=8, columnspan=5, pady=5)
        checksettings_text.insert('end', "Checks if following are enabled and if not, enables them automatically: "
                                        "drag & drop, disable nudge mode, auto start. Checking is done only once in "
                                        "a session, after entering a map first time: thus, check status resets only if "
                                        "you restart the entire program.")
        checksettings_text['state'] = 'disabled'

        record_toggle = tk.Checkbutton(self.settings_window, text="Record round times and update plan version", 
                                       anchor='nw', onvalue='On', 
                                       offvalue='Off', pady=5, padx=18, variable=self.record_time,
                                       command=self.change_record_status)
        record_toggle.grid(column=0, row=9, columnspan=3, sticky='nw')

        record_text = tk.Text(self.settings_window, wrap=tk.WORD, width=62, height=3)
        record_text.grid(column=0, row=10, columnspan=5, pady=5)
        record_text.insert('end', "Records all round times during plan execution and saves them time_data.json. "
                            "Current version value is also stored. Used in:\n"
                            "- to display a 2d time plot under \'Show Plot\',\n"
                            "- to update version in info panel which confirms the plan \n"
                            "  can be finished on current game version.\n"
                            "Bot must finish all rounds without a single defeat and return to menu "
                            "screen, otherwise no data is stored. Previous version & time data for "
                            "current plan gets overwritten each time, making updating values easy." 
                            )        
        record_text['state'] = 'disabled'
        
        debug_text = tk.Label(self.settings_window, 
                              text='o--------------------------------------o\n'
                                   '|  Advanced (for debugging/testing)  |\n'
                                   'o--------------------------------------o')
        debug_text.grid(column=0, columnspan=2, row=11, sticky='w', padx=5, pady=(15, 1))
        
        time_limit_label = tk.Label(self.settings_window, text='Ocr time limit')
        time_limit_label.grid(column=0, row=12, sticky='se', padx=(1,21), pady=(5,1))
        time_limit_current_value = tk.Label(self.settings_window, relief='ridge', textvariable=self.time_limit)
        time_limit_current_value.grid(column=1, row=12, sticky='sw', padx=1, pady=(5,1))

        self.time_limit_entry = tk.Entry(self.settings_window, width=10)
        self.time_limit_entry.grid(column=0, row=13, sticky='e', pady=(1,10), padx=(21,31))
        time_limit_button = tk.Button(self.settings_window, text="Update time limit", anchor='w', padx=5,
                                           command=self.set_time_limit_value)
        time_limit_button.grid(column=1, row=13, sticky='w', pady=(1,10))

        time_limit_text = tk.Text(self.settings_window, wrap=tk.WORD, width=62, height=3)
        time_limit_text.grid(column=0, row=14, columnspan=5)
        time_limit_text.insert('end', "Time limit, in seconds, until bot gives up on trying to place/upgrade a monkey "
                                "or search for the next round and returns to menu, halting current plan. Only needed "
                                "if bot ocr gets stuck; a high value of 300 or greater is recommended for normal use.")
        time_limit_text['state'] = 'disabled'

        delta_ocrtext_toggle = tk.Checkbutton(self.settings_window, 
                                                text="Print ocr delta text values in monitoring window", anchor='nw', 
                                                onvalue='On', offvalue='Off', pady=5, padx=18, 
                                                variable=self.delta_ocrtext,
                                                command=self.change_deltaocr_status)
        delta_ocrtext_toggle.grid(column=0, row=15, columnspan=3, sticky='nw')

        substring_ocrtext_toggle = tk.Checkbutton(self.settings_window, 
                                                text="Print ocr substring text values in monitoring window", 
                                                anchor='nw', 
                                                onvalue='On', offvalue='Off', pady=5, padx=18, 
                                                variable=self.substring_ocrtext,
                                                command=self.change_substringocr_status)
        substring_ocrtext_toggle.grid(column=0, row=16, columnspan=3, sticky='nw')

        self.update_variables()

    def _clear_entry(self) -> None:
        if self.resolution_width_entry.get() == 'width':
            self.resolution_width_entry.delete(0, "end")
            self.resolution_width_entry.config(fg='black')
        elif self.resolution_height_entry.get() == 'height':
            self.resolution_height_entry.delete(0, "end")
            self.resolution_height_entry.config(fg='black')

    def update_variables(self) -> None:
        """Updates toggle button values with matching gui_vars.json values."""
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, Any] = json.load(f)
            if gui_vars_dict["check_resolution"]:
                self.resolution.set('On')
                self.windowed_toggle['state'] = 'normal'
                self.resolution_value.set(self.read_value("custom_resolution"))
                self.resolution_width_entry['state'] = 'normal'
                self.resolution_height_entry['state'] = 'normal'
            else:
                self.windowed_toggle['state'] = 'disabled'
                res = pyautogui.size()
                self.resolution_value.set(' '+str(res[0])+' x '+str(res[1])+' ')
                self.resolution_width_entry['state'] = 'disabled'
                self.resolution_height_entry['state'] = 'disabled'
            if gui_vars_dict["windowed"]:
                self.windowed.set('On')
            if gui_vars_dict["check_gamesettings"]:
                self.gamesettings.set('On')
            if gui_vars_dict["time_recording_status"]:
                self.record_time.set('On')
            if gui_vars_dict["delta_ocrtext"]:
                self.delta_ocrtext.set('On')
            if gui_vars_dict["substring_ocrtext"]:
                self.substring_ocrtext.set('On')

    def change_resolution_status(self) -> None:
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, Any] = json.load(f)
        if self.resolution.get() == 'On':
            self.windowed_toggle['state'] = 'normal'
            gui_vars_dict["check_resolution"] = True
            if self.windowed.get() == 'On':
                gui_vars_dict["windowed"] = True
            self.resolution_value.set(self.read_value("custom_resolution"))
            self.resolution_width_entry['state'] = 'normal'
            self.resolution_height_entry['state'] = 'normal'
        elif self.resolution.get() == 'Off':
            self.windowed_toggle['state'] = 'disabled'
            gui_vars_dict["check_resolution"] = False
            gui_vars_dict["windowed"] = False
            res = pyautogui.size()
            self.resolution_value.set(' '+str(res[0])+' x '+str(res[1])+' ')
            self.resolution_width_entry['state'] = 'disabled'
            self.resolution_height_entry['state'] = 'disabled'
        with open(gui_paths.FILES_PATH/'gui_vars.json', 'w') as f:
            json.dump(gui_vars_dict, f, indent=4)

    def change_windowed_status(self) -> None:
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, Any] = json.load(f)
        if self.windowed.get() == 'On':
            gui_vars_dict["windowed"] = True
        elif self.windowed.get() == 'Off':
            gui_vars_dict["windowed"] = False
        with open(gui_paths.FILES_PATH/'gui_vars.json', 'w') as f:
            json.dump(gui_vars_dict, f, indent=4)

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

    def change_deltaocr_status(self) -> None:
        """Changes ocr substring matching text display status based on toggle button value."""
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, Any] = json.load(f)
        if self.delta_ocrtext.get() == 'On':
            gui_vars_dict["delta_ocrtext"] = True
        elif self.delta_ocrtext.get() == 'Off':
            gui_vars_dict["delta_ocrtext"] = False
        with open(gui_paths.FILES_PATH/'gui_vars.json', 'w') as f:
            json.dump(gui_vars_dict, f, indent=4)

    def change_substringocr_status(self) -> None:
        """Changes ocr delta matching text display status based on toggle button value."""
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, Any] = json.load(f)
        if self.substring_ocrtext.get() == 'On':
            gui_vars_dict["substring_ocrtext"] = True
        elif self.substring_ocrtext.get() == 'Off':
            gui_vars_dict["substring_ocrtext"] = False
        with open(gui_paths.FILES_PATH/'gui_vars.json', 'w') as f:
            json.dump(gui_vars_dict, f, indent=4)

    def set_resolution_value(self) -> None:
        try:
            width = self.resolution_width_entry.get()
            height = self.resolution_height_entry.get()
            if int(width) >= 0 and int(height) >= 0:
                val = width+' x '+height
                with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
                    gui_vars_dict: dict[str, Any] = json.load(f)
                gui_vars_dict["custom_resolution"] = val
                self.resolution_value.set(' '+val+' ')
                with open(gui_paths.FILES_PATH/'gui_vars.json', 'w') as f:
                    json.dump(gui_vars_dict, f, indent=4)
        except ValueError:
            ...

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
                self.time_limit.set(' '+str(gui_vars_dict["checking_time_limit"])+' ')
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
                self.version.set(' '+str(gui_vars_dict["version"])+' ')
                with open(gui_paths.FILES_PATH/'gui_vars.json', 'w') as f:
                    json.dump(gui_vars_dict, f, indent=4)
        except ValueError:
            ...

    def read_value(self, id_str: str) -> str:
        """Get current stored value from gui_vars.
        
        Args:
            id_str: Dictionary key.
        Returns:
            Value of dictionary casted as string.
        """
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, int | bool | str] = json.load(f)
        return ' '+str(gui_vars_dict[id_str])+' '

    def get_settingswindow(self) -> tk.Toplevel:
        """Get current settings window.
        
        Returns:
            Current Toplevel window object of SettingsWindow.
        """
        return self.settings_window