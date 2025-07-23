"""Contains SettingsWindow class."""

from __future__ import annotations
from typing import TYPE_CHECKING
import json
import tkinter as tk

import pyautogui
import torch

import gui.gui_paths as gui_paths
from gui.gui_tools import os_font

if TYPE_CHECKING:
    from typing import Any

class SettingsWindow:
    """Creates a settings window. All settings in stored and read from gui_vars.json.
    
    Attributes:
        settings_window (Tk.Toplevel): Toplevel window.
        resolution (tk.StringVar): Enable/disable Custom display resolution.
        resolution_value (tk.StringVar): Custom display resolution value.
        windowed (tk.StringVar): Windowed mode enabled/disabled.
        version (tk.StringVar): Game version.
        retries
        verify_limit (tk.StringVar):
        time_limit (tk.StringVar): Ocr time limit until bot gives up.
        ocr_frequency
        logging (tk.StringVar): Enable/disable printing of ocr text values and saving them into Logs.txt in root.
        delta_ocrtext (tk.StringVar): Delta text print enabled/disabled.
        substring_ocrtext (tk.StringVar): Substring text print enabled/disabled. 
        ocr_adjust (tk.StringVar): Enabled/disable upgrade auto-adjust process
        resolution_width_entry (tk.Entry): Width value for display resolution.
        resolution_height_entry (tk.Entry): Height value for display resolution.
        resolution_button (tk.Button): Apply current width and height entry values.
        windowed_toggle (tk.Checkbutton): Toggle windowed mode on/off.
        version_entry (tk.Entry): Entry box for game version.
        retry_entry: (tk.Entry): Entry box for retries value.
        verify_limit_entry (tk.Entry): Entry for upgrade check verification limit i.e. how many times bot checks for
            upgrade text before path upgrade key is pressed again. Setting this value to higher than 1 helps with 
            preventing missed ocr inputs
        time_limit_entry (tk.Entry): Entry box for ocr time limit value.
        ocr_frequency_entry (tk.Entry): Entry for ocr frequency.
        delta_ocrtext_toggle (tk.Checkbutton) Ocr delta check toggle
        substring_ocrtext_toggle (tk.Checkbutton) Ocr substring check toggle
        ocr_autoadjust_entry (tk.Entry): Entry field for ocr upgrade data adjusting parameters.
        ocr_autoadjust_button (tk.Button): Apply adjusting parameters.
        ocr_autoadjust_reset_button (tk.Button): Reset adjusting parameters entry field without applying the values; 
            use autoadjust button afterwards to do this.
    """

    def __init__(self) -> None:
        """Initialize settings window."""
        self.settings_window = tk.Toplevel()
        self.settings_window.title("Settings")
        self.settings_window.geometry('580x850+100+150')
        self.settings_window.minsize(580,850)
        self.settings_window.maxsize(580,850)

        self.settings_window.grid_columnconfigure((0,1,2,3,4), weight=1, uniform='1')

        self.resolution = tk.StringVar(value='Off')
        self.resolution_value = tk.StringVar(value=self.read_value("custom_resolution"))
        self.windowed = tk.StringVar(value='Off')
        self.version = tk.StringVar(value=self.read_value("version"))
        self.retries = tk.StringVar(value=self.read_value("retries"))
        # self.ingame_res = tk.StringVar(value='Off')
        # self.ingame_res_value = tk.StringVar(value=self.read_value("ingame_resolution"))
        self.verify_limit = tk.StringVar(value=self.read_value("upg_verify_limit"))
        self.gpu = tk.StringVar(value='Off')
        self.time_limit = tk.StringVar(value=self.read_value("checking_time_limit"))
        self.ocr_frequency = tk.StringVar(value=self.read_value("ocr_frequency"))
        self.logging = tk.StringVar(value='Off')
        self.delta_ocrtext = tk.StringVar(value='Off')
        self.substring_ocrtext = tk.StringVar(value='Off')
        self.ocr_adjust = tk.StringVar(value='Off')

        basic_text = tk.Label(self.settings_window, 
                              text='o--------o\n'
                                   '| Basic |\n'
                                   'o--------o', 
                              font=os_font)
        basic_text.grid(column=0, columnspan=2, row=0, sticky='w', padx=5)

        resolution_toggle = tk.Checkbutton(self.settings_window, 
                                            text="Enable custom resolution", anchor='nw', 
                                            onvalue='On', offvalue='Off', pady=5, padx=18, 
                                            variable=self.resolution,
                                            command=self.change_resolution_status,
                                            font=os_font)
        resolution_toggle.grid(column=0, row=1, columnspan=3, sticky='nw')
        resolution_label = tk.Label(self.settings_window, 
                                    text='Current resolution', 
                                    font=os_font)
        resolution_label.grid(column=2, row=1, sticky='sw', padx=1, pady=(1,10))
        resolution_current_value = tk.Label(self.settings_window, 
                                            relief='ridge', 
                                            textvariable=self.resolution_value, 
                                            font=os_font)
        resolution_current_value.grid(column=3, columnspan=2, row=1, sticky='sw', padx=(1,35), pady=(1,10))
        res_reminder = tk.Text(self.settings_window, 
                               wrap=tk.WORD, 
                               width=10, 
                               height=5, 
                               relief='sunken', 
                               font=os_font)
        res_reminder.grid(column=4, row=1, rowspan=3, sticky='nw', padx=1, pady=(1,10))
        res_reminder.insert("end", '[Reminder] Aspect ratio should be 16:9')
        res_reminder['state'] = 'disabled'

        self.resolution_width_entry = tk.Entry(self.settings_window, 
                                               width=10, 
                                               font=os_font)
        self.resolution_width_entry.grid(column=0, row=2, sticky='e', pady=(1,10), padx=(21,31))
        self.resolution_width_entry.insert(0, "width")
        self.resolution_width_entry.bind('<FocusIn>', lambda _: self._clear_entry())
        self.resolution_width_entry.config(fg='grey')
        self.resolution_height_entry = tk.Entry(self.settings_window, 
                                                width=10, 
                                                font=os_font)
        self.resolution_height_entry.grid(column=1, row=2, sticky='w', pady=(1,10), padx=(1,31))
        self.resolution_height_entry.insert(0, "height")
        self.resolution_height_entry.bind('<FocusIn>', lambda _: self._clear_entry())
        self.resolution_height_entry.config(fg='grey')
        self.resolution_button = tk.Button(self.settings_window, 
                                           text="Update resolution", 
                                           anchor='w', 
                                           padx=5,
                                           command=self.set_resolution_value, 
                                           font=os_font)
        self.resolution_button.grid(column=2, columnspan=2, row=2, sticky='w', pady=(1,10))

        self.windowed_toggle = tk.Checkbutton(self.settings_window, 
                                            text="Windowed mode (BTD6 must be opened with -popupwindow "
                                                "launch option)", 
                                            anchor='nw', 
                                            onvalue='On', 
                                            offvalue='Off', 
                                            pady=5, 
                                            padx=18, 
                                            variable=self.windowed,
                                            command=self.change_windowed_status,
                                            font=os_font)
        self.windowed_toggle.grid(column=0, row=3, columnspan=4, sticky='nw')

        version_label = tk.Label(self.settings_window, 
                                 text='Game version', 
                                 font=os_font)
        version_label.grid(column=0, row=4, sticky='se', padx=(1,21), pady=(5,1))
        version_current_value = tk.Label(self.settings_window, 
                                         relief='ridge', 
                                         textvariable=self.version, 
                                         font=os_font)
        version_current_value.grid(column=1, row=4, sticky='sw', padx=1, pady=(5,1))

        self.version_entry = tk.Entry(self.settings_window, 
                                      width=10, 
                                      font=os_font)
        self.version_entry.grid(column=0, row=5, sticky='e', pady=(1,10), padx=(21,31))
        version_button = tk.Button(self.settings_window, 
                                   text="Update version", 
                                   anchor='w', 
                                   padx=5,
                                   command=self.set_version_value, 
                                   font=os_font)
        version_button.grid(column=1, row=5, sticky='w', pady=(1,10))

        retry_label = tk.Label(self.settings_window, 
                               text='Retries', 
                               font=os_font)
        retry_label.grid(column=2, row=4, sticky='w', padx=(17,21), pady=(5,1))
        retry_current_value = tk.Label(self.settings_window, 
                                       relief='ridge', 
                                       textvariable=self.retries, 
                                       font=os_font)
        retry_current_value.grid(column=3, row=4, sticky='sw', padx=1, pady=(5,1))

        self.retry_entry = tk.Entry(self.settings_window, 
                                    width=10, 
                                    font=os_font)
        self.retry_entry.grid(column=2, row=5, sticky='e', pady=(1,10), padx=(21,31))
        retry_button = tk.Button(self.settings_window, 
                                 text="Update retries", 
                                 anchor='w', 
                                 padx=5,
                                 command=self.set_retries_value, 
                                 font=os_font)
        retry_button.grid(column=3, row=5, sticky='w', pady=(1,10))

        advanced_text = tk.Label(self.settings_window, 
                                 text='o--------------o\n'
                                      '| Advanced |\n'
                                      'o--------------o', 
                                 font=os_font)
        advanced_text.grid(column=0, columnspan=2, row=8, sticky='w', padx=5, pady=(1, 1))
            
        time_limit_label = tk.Label(self.settings_window, 
                                    text='Ocr time limit', 
                                    font=os_font)
        time_limit_label.grid(column=0, row=13, sticky='se', padx=(1,21), pady=(5,1))
        time_limit_current_value = tk.Label(self.settings_window, 
                                            relief='ridge', 
                                            textvariable=self.time_limit, 
                                            font=os_font)
        time_limit_current_value.grid(column=1, row=13, sticky='sw', padx=1, pady=(5,1))

        self.time_limit_entry = tk.Entry(self.settings_window, 
                                         width=10, 
                                         font=os_font)
        self.time_limit_entry.grid(column=0, row=14, sticky='e', pady=(1,10), padx=(21,31))
        time_limit_button = tk.Button(self.settings_window, 
                                      text="Update time limit", 
                                      anchor='w', 
                                      padx=5,
                                      command=self.set_time_limit_value, 
                                      font=os_font)
        time_limit_button.grid(column=1, row=14, sticky='w', pady=(1,10))


        ocr_frequency_label = tk.Label(self.settings_window, 
                                       text='Ocr frequency', 
                                       font=os_font)
        ocr_frequency_label.grid(column=2, row=13, sticky='se', padx=(1,21), pady=(5,1))
        ocr_frequency_current_value = tk.Label(self.settings_window, 
                                               relief='ridge', 
                                               textvariable=self.ocr_frequency,
                                               font=os_font)
        ocr_frequency_current_value.grid(column=3, row=13, sticky='sw', padx=1, pady=(5,1))

        self.ocr_frequency_entry = tk.Entry(self.settings_window, 
                                            width=10, 
                                            font=os_font)
        self.ocr_frequency_entry.grid(column=2, row=14, sticky='e', pady=(1,10), padx=(21,31))
        ocr_frequency_button = tk.Button(self.settings_window, 
                                         text="Update frequency value", 
                                         anchor='w',
                                         padx=5,
                                         command=self.set_ocr_frequency_value, 
                                         font=os_font)
        ocr_frequency_button.grid(column=3, columnspan=2, row=14, sticky='w', pady=(1,10))

        verify_limit_label = tk.Label(self.settings_window, 
                                      text='Upgrade checks', 
                                      font=os_font)
        verify_limit_label.grid(column=0, row=15, sticky='se', padx=(18,5), pady=(5,1))
        verify_limit_current_value = tk.Label(self.settings_window, 
                                              relief='ridge',
                                              textvariable=self.verify_limit, ##
                                              font=os_font)
        verify_limit_current_value.grid(column=1, row=15, sticky='sw', padx=1, pady=(5,1))

        self.verify_limit_entry = tk.Entry(self.settings_window, 
                                           width=10, 
                                           font=os_font)
        self.verify_limit_entry.grid(column=0, row=16, sticky='e', pady=(1,10), padx=(21,31))
        verify_limit_button = tk.Button(self.settings_window, 
                                        text="Update check limit", 
                                        anchor='w', 
                                        padx=5,
                                        command=self.set_verify_limit_value,
                                        font=os_font)
        verify_limit_button.grid(column=1, row=16, sticky='w', pady=(1,10))

        self.gpu_toggle = tk.Checkbutton(self.settings_window, 
                                         text="Use gpu in ocr (requires a restart to update value)", 
                                         anchor='nw', 
                                         onvalue='On', 
                                         offvalue='Off', 
                                         pady=5, 
                                         padx=18, 
                                         variable=self.gpu,
                                         command=self.change_gpu_status,
                                         font=os_font)
        self.gpu_toggle.grid(column=0, row=17, columnspan=4, sticky='nw')

        logging_toggle = tk.Checkbutton(self.settings_window,
                                        text="Enable logging", 
                                        anchor='nw', 
                                        onvalue='On', 
                                        offvalue='Off', 
                                        pady=5,
                                        padx=18, 
                                        variable=self.logging,
                                        command=self.change_logging_status,
                                        font=os_font)
        logging_toggle.grid(column=0, row=18, columnspan=3, sticky='nw')

        self.delta_ocrtext_toggle = tk.Checkbutton(self.settings_window, 
                                                   text="Print ocr delta text values in monitoring window", 
                                                   anchor='nw', 
                                                   onvalue='On', 
                                                   offvalue='Off', 
                                                   pady=5, 
                                                   padx=40, 
                                                   variable=self.delta_ocrtext,
                                                   command=self.change_deltaocr_status,
                                                   font=os_font)
        self.delta_ocrtext_toggle.grid(column=0, row=19, columnspan=3, sticky='nw')

        self.substring_ocrtext_toggle = tk.Checkbutton(self.settings_window, 
                                                      text="Print ocr substring text values in monitoring window", 
                                                      anchor='nw', 
                                                      onvalue='On', 
                                                      offvalue='Off', 
                                                      pady=5, 
                                                      padx=40, 
                                                      variable=self.substring_ocrtext,
                                                      command=self.change_substringocr_status,
                                                      font=os_font)
        self.substring_ocrtext_toggle.grid(column=0, row=20, columnspan=3, sticky='nw')

        ocr_autoadjust_toggle = tk.Checkbutton(self.settings_window, 
                                               text="Auto-adjust ocr upgrade data the next time a plan is run", 
                                               anchor='nw', onvalue='On', 
                                               offvalue='Off', 
                                               pady=5, 
                                               padx=18, 
                                               variable=self.ocr_adjust,
                                               command=self.change_ocradjust_status,
                                               font=os_font)
        ocr_autoadjust_toggle.grid(column=0, row=21, columnspan=3, sticky='nw')
        self.ocr_autoadjust_entry = tk.Entry(self.settings_window, 
                                             width=50, 
                                             font=os_font)
        self.ocr_autoadjust_entry.grid(column=0, columnspan=4, row=22, sticky='w', pady=(1,10), padx=(21,31))
        self.ocr_autoadjust_button = tk.Button(self.settings_window, 
                                               text="Set args", 
                                               anchor='w',
                                               padx=5,
                                               command=self.set_ocradjust_value, 
                                               font=os_font)
        self.ocr_autoadjust_button.grid(column=3, columnspan=2, row=22, sticky='w', pady=(1,10))
        self.ocr_autoadjust_reset_button = tk.Button(self.settings_window, 
                                                     text="Reset args", 
                                                     anchor='w', 
                                                     padx=5,
                                                     command=self.reset_ocradjust_value, 
                                                     font=os_font)
        self.ocr_autoadjust_reset_button.grid(column=4, row=22, sticky='w', padx=(1,20), pady=(1,10))

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
            self.resolution_button['state'] = 'normal'
        else:
            self.windowed_toggle['state'] = 'disabled'
            res = pyautogui.size()
            self.resolution_value.set(f' {res[0]} x {res[1]} ')
            self.resolution_width_entry['state'] = 'disabled'
            self.resolution_height_entry['state'] = 'disabled'
            self.resolution_button['state'] = 'disabled'
        if gui_vars_dict["windowed"]:
            self.windowed.set('On')
        if torch.cuda.is_available():
            if gui_vars_dict["use_gpu"]:
                self.gpu.set('On')
        else:
            self.gpu.set('Off')
            self.gpu_toggle['text'] = "Use gpu in ocr (Gpu has no CUDA support, using CPU instead)"
            self.gpu_toggle['state'] = "disabled"
            self.change_gpu_status()
        if gui_vars_dict["logging"]:
            self.logging.set('On')
            self.delta_ocrtext_toggle['state'] = 'normal'
            self.substring_ocrtext_toggle['state'] = 'normal'
        else:
            self.delta_ocrtext_toggle['state'] = 'disabled'
            self.substring_ocrtext_toggle['state'] = 'disabled'
        if gui_vars_dict["delta_ocrtext"]:
            self.delta_ocrtext.set('On')
        if gui_vars_dict["substring_ocrtext"]:
            self.substring_ocrtext.set('On')
        if gui_vars_dict["ocr_adjust_deltas"]:
            self.ocr_adjust.set('On')
            self.ocr_autoadjust_entry['state'] = 'normal'
            self.ocr_autoadjust_button['state'] = 'normal'
            self.ocr_autoadjust_reset_button['state'] = 'normal'
            self.ocr_autoadjust_entry.insert("end", gui_vars_dict["adjust_args"])
        else:
            self.ocr_autoadjust_button['state'] = 'disabled'
            self.ocr_autoadjust_reset_button['state'] = 'disabled'
            self.ocr_autoadjust_entry['state'] = 'normal'
            self.ocr_autoadjust_entry.insert("end", gui_vars_dict["adjust_args"])
            self.ocr_autoadjust_entry['state'] = 'disabled'

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
            self.resolution_button['state'] = 'normal'
        elif self.resolution.get() == 'Off':
            self.windowed_toggle['state'] = 'disabled'
            gui_vars_dict["check_resolution"] = False
            gui_vars_dict["windowed"] = False
            res = pyautogui.size()
            self.resolution_value.set(' '+str(res[0])+' x '+str(res[1])+' ')
            self.resolution_width_entry['state'] = 'disabled'
            self.resolution_height_entry['state'] = 'disabled'
            self.resolution_button['state'] = 'disabled'
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

    def change_gpu_status(self) -> None:
        """Change gpu toggle status based on toggle button value."""
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, Any] = json.load(f)
        if self.gpu.get() == 'On':
            gui_vars_dict["use_gpu"] = True
        else:
            gui_vars_dict["use_gpu"] = False
        with open(gui_paths.FILES_PATH/'gui_vars.json', 'w') as f:
            json.dump(gui_vars_dict, f, indent=4)

    def change_logging_status(self) -> None:
        """Changes logging status based on toggle button value."""
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, Any] = json.load(f)
        if self.logging.get() == 'On':
            gui_vars_dict["logging"] = True
            self.delta_ocrtext_toggle['state'] = 'normal'
            self.substring_ocrtext_toggle['state'] = 'normal'
            if self.delta_ocrtext.get() == 'On':
                gui_vars_dict["delta_ocrtext"] = True
            if self.substring_ocrtext.get() == 'On':
                gui_vars_dict["substring_ocrtext"] = True
        elif self.logging.get() == 'Off':
            gui_vars_dict["logging"] = False
            gui_vars_dict["delta_ocrtext"] = False
            gui_vars_dict["substring_ocrtext"] = False
            self.delta_ocrtext_toggle['state'] = 'disabled'
            self.substring_ocrtext_toggle['state'] = 'disabled'
        with open(gui_paths.FILES_PATH/'gui_vars.json', 'w') as f:
            json.dump(gui_vars_dict, f, indent=4)

    def change_deltaocr_status(self) -> None:
        """Changes ocr delta matching text display status based on toggle button value."""
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, Any] = json.load(f)
        if self.delta_ocrtext.get() == 'On':
            gui_vars_dict["delta_ocrtext"] = True
        elif self.delta_ocrtext.get() == 'Off':
            gui_vars_dict["delta_ocrtext"] = False
        with open(gui_paths.FILES_PATH/'gui_vars.json', 'w') as f:
            json.dump(gui_vars_dict, f, indent=4)

    def change_substringocr_status(self) -> None:
        """Changes ocr substring matching text display status based on toggle button value."""
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, Any] = json.load(f)
        if self.substring_ocrtext.get() == 'On':
            gui_vars_dict["substring_ocrtext"] = True
        elif self.substring_ocrtext.get() == 'Off':
            gui_vars_dict["substring_ocrtext"] = False
        with open(gui_paths.FILES_PATH/'gui_vars.json', 'w') as f:
            json.dump(gui_vars_dict, f, indent=4)

    def change_ocradjust_status(self) -> None:
        """Changes ocr upgrade data adjust status based on toggle button value."""
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, Any] = json.load(f)
        if self.ocr_adjust.get() == 'On':
            self.ocr_autoadjust_entry['state'] = 'normal'
            self.ocr_autoadjust_button['state'] = 'normal'
            self.ocr_autoadjust_reset_button['state'] = 'normal'
            gui_vars_dict["ocr_adjust_deltas"] = True
        elif self.ocr_adjust.get() == 'Off':
            self.ocr_autoadjust_entry['state'] = 'disabled'
            self.ocr_autoadjust_button['state'] = 'disabled'
            self.ocr_autoadjust_reset_button['state'] = 'disabled'
            gui_vars_dict["ocr_adjust_deltas"] = False
        with open(gui_paths.FILES_PATH/'gui_vars.json', 'w') as f:
            json.dump(gui_vars_dict, f, indent=4)

    def set_resolution_value(self) -> None:
        try:
            width = self.resolution_width_entry.get()
            w = int(width)
            height = self.resolution_height_entry.get()
            h = int(height)
            native = pyautogui.size()
            if 1 <= w < native[0] and 1 <= h < native[1]:
                    val = width+' x '+height
                    with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
                        gui_vars_dict: dict[str, Any] = json.load(f)
                    gui_vars_dict["custom_resolution"] = val
                    self.resolution_value.set(' '+val+' ')
                    with open(gui_paths.FILES_PATH/'gui_vars.json', 'w') as f:
                        json.dump(gui_vars_dict, f, indent=4)
        except ValueError:
            ...

    def set_version_value(self) -> None:
        """Saves current version value to gui_vars.json.
        
        Accepted values are integer from 1 to 999.
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

    def set_retries_value(self) -> None:
        """Saves current retries value to gui_vars.json.
        
        Accepted values are integer from 1 to 99.
        """
        try:
            val = int(self.retry_entry.get())
            if 1 <= val <= 99:
                with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
                    gui_vars_dict: dict[str, Any] = json.load(f)
                gui_vars_dict["retries"] = val
                self.retries.set(' '+str(gui_vars_dict["retries"])+' ')
                with open(gui_paths.FILES_PATH/'gui_vars.json', 'w') as f:
                    json.dump(gui_vars_dict, f, indent=4)
        except ValueError:
            ...

    def set_verify_limit_value(self) -> None:
        """Saves current upgrade verification limit value to gui_vars.json.
        
        Accepted values are integer from 1 to 99.
        """
        try:
            val = int(self.verify_limit_entry.get())
            if 1 <= val <= 99:
                with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
                    gui_vars_dict: dict[str, Any] = json.load(f)
                gui_vars_dict["upg_verify_limit"] = val
                self.verify_limit.set(' '+str(gui_vars_dict["upg_verify_limit"])+' ')
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

    def set_ocr_frequency_value(self) -> None:
        """Saves current ocr frequency value to gui_vars.json.
        
        Accepted frequency values are float numbers from 0 (no extra delay) to 5 (five second added delay).
        """
        try:
            val = float(self.ocr_frequency_entry.get())
            if 0 <= val <= 5:
                with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
                    gui_vars_dict: dict[str, Any] = json.load(f)
                gui_vars_dict["ocr_frequency"] = val
                self.ocr_frequency.set(' '+str(gui_vars_dict["ocr_frequency"])+' ')
                with open(gui_paths.FILES_PATH/'gui_vars.json', 'w') as f:
                    json.dump(gui_vars_dict, f, indent=4)
        except ValueError:
            ...

    # TODO when ingame resolution is added, a new check must be added:
    # > when ingame res is enabled, ocr auto-adjust must use this resolution instead of base/custom res
    # so reset_ocradjust_value, monitoring_window and _adjust_deltas.py require some changes
    def set_ocradjust_value(self) -> None:
        """Saves current ocr adjust data to gui_vars.json."""
        val = self.ocr_autoadjust_entry.get()
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, Any] = json.load(f)
        gui_vars_dict["adjust_args"] = val
        with open(gui_paths.FILES_PATH/'gui_vars.json', 'w') as f:
            json.dump(gui_vars_dict, f, indent=4)

    def reset_ocradjust_value(self) -> None:
        """Reset adjust arguments."""
        res_raw = self.resolution_value.get().strip().split()
        res = 'res='+res_raw[0]+'x'+res_raw[2]
        adjust_args = f'{res}'
        if self.resolution.get() == 'On' and self.windowed.get() == 'On':
            adjust_args += ' win=1'
        else:
            adjust_args += ' win=0'
        adjust_args += ' monkeys=all delta=4'
        self.ocr_autoadjust_entry.delete(0, "end")
        self.ocr_autoadjust_entry.insert("end", adjust_args)

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