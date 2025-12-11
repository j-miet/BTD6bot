"""Contains MonitoringWindow class."""

from __future__ import annotations
from typing import TYPE_CHECKING

import json
import os
import shutil
import sys
import threading
import time
import tkinter as tk
from tkinter import ttk

import pyautogui

from bot import times
from bot.bot_data import BotData
from bot.bot_vars import BotVars
from customprint import cprint
from gui.guihotkeys import GuiHotkeys
import gui.gui_paths as gui_paths
import gui.gui_tools as gui_tools
from gui.gui_tools import os_font
import set_plan as set_plan
from utils import plan_data
from utils import timing

if TYPE_CHECKING:
    from typing import Any, TextIO

class MonitoringWindow:
    """Creates a monitoring window that handles both starting/stopping of the bot and displaying bot text output.

    Handles running/stopping the bot and updating of monitoring window by redirecting stdout into it.
    Bot itself operates on a separate thread, allowing both general GUI and monitoring screen to update constantly.

    Attributes:
        START_STOP_HOTKEY (pynput.Key, class attribute): Hotkey that starts and stops current bot thread inside 
            monitoring window. Current: F9.
        current_bot_thread (threading.Thread, class attribute): Current monitoring window bot thread.
            Mainwindow.is_monitoringwindow() needs to identify a bot thread in order to terminate it, in 
            particular if monitoring window is closed while bot thread is in use. So the newest thread has to be known 
            at all times, otherwise it could leave the previous thread running. And if, for example, this thread was 
            currently performing ocr, but not finding any fitting match, it would end up eating a up A LOT of CPU. Even 
            worse, these inaccessible & unusable threads could stack and execute multiple bots at the same time, which 
            of course, would break everything as they all share key & mouse inputs and all files.
        
        all_plans (list[str]): List of all plans in the queue list or a single plan if queue mode is disabled.
        replay_val (str): String with On/Off value for replay mode button.
        queue_val (str): String with On/Off value for queue mode button.
        collection (str): String with On/Off value to both display collection event status and update corresponding 
            value to gui_vars.json.
        farming (str): String value to determine if bot is launched in normal or collection event farming mode.
        current_plans (list[str]): List of currently unfinished plans. When bot is run, all_plans contents are copied
            into this. Then after finishing a plan, it gets removed from this list. Here finishing means plan was either
            completed successfully, or failed to finish within given amount of retries.  
            Eventually, current_plans becomes an empty list. If queue mode is not on (i.e. only a single plan), bot can
            run the plan again. If queue mode is enabled, bot cannot be run again until a new monitoring window is
            opened an queue is refreshed. If replay mode is on, bot will automatically reset queue and go again no
            matter if there's a single or multiple plans.
        plans_status (list[str]): Stores status of completed plans. If queue mode is enabled, its contents are used for
            not only displaying successfully finished plans, but also any unsuccessful ones.
        roundtime (tk.StringVar): Variable storing current round timer value.
        monitoringwindow (tk.Toplevel): Window where other gui elements can be inserted.
        textbox (tk.Text): Text object that is responsible of displaying all text output during bot runtime.
        old_stdout (TextIO | Any): Original standard output stream. Program will return to it if MonitoringWindow is 
            not accessed.
        monitor_mapscreen_ascii (str): Ascii string used as default value for monitor_mapscreen.
        monitor_mapscreen (tk.Label): Displays current map image. If no image is found, use monitor_mapscreen_ascii 
            string and insert this into label instead.
        monitor_infobox_current (tk.Label): Displays current plan's info panel.
        monitor_infobox_next (tk.Label): Displays next plan's info panel.
        monitor_run_button (tk.Button): Button object required to start/stop bot. Bot is set to run on a separate 
            thread.
        bot_thread (threading.Thread): Current thread where bot itself is allocated. A placeholder thread is initially 
            created so that MainWindow can start tracking its existence and won't throw an error. After 'Run' button is 
            pressed, _stop_or_run method is called and target of this thread is set to _run_bot method instead.
    """
    current_bot_thread: threading.Thread

    def __init__(self, all_plans_list: list[str], replay: str, queue: str, collection: str, farming: str) -> None:
        """Initialize monitoring window by passing it the plans list and replay/queue mode checks.

        Args:
            all_plans: List of all plans in the queue list or a single plans if queue mode is disabled.
            replay: StringVar to set On/Off value for a replay mode button.
            queue: StringVar to set On/Off value for a queue mode button.
        """
        self.all_plans = all_plans_list
        self.replay_val = replay
        self.queue_val = queue
        self.collection_val = collection
        self.farming = farming
        self.current_plans: list[str] = []
        self.plans_status: list[str] = []
        self.roundtime = tk.StringVar(value='-')
        self.runs = tk.IntVar(value=0)

        self.monitoringwindow = tk.Toplevel()
        self.monitoringwindow.title("Bot Monitoring Window")
        self.monitoringwindow.iconbitmap(gui_paths.FILES_PATH/'btd6bot.ico')
        self.monitoringwindow.geometry('800x480')
        self.monitoringwindow.minsize(800,480)
        self.monitoringwindow.maxsize(800,480)

        self.textbox = tk.Text(self.monitoringwindow, 
                               width=55, 
                               height=25, 
                               state='normal', 
                               wrap=tk.WORD)
        self.textbox.grid(column=0, columnspan=2, row=0, rowspan=4, sticky='n')
        self.textbox.insert('end', "Welcome to BTD6bot!\n"
                            "Make sure that:\n"
                            ">Game language is set to ENGLISH\n"
                            ">Resolution has aspect ratio of ~16:9\n"
                            ">Game is preferably fullscreen (but windowed works too)\n"
                            ">Bot hotkeys match with your in-game equivalents\n"
                            ">Your Btd6 game window is on your main monitor and has\n"
                            " main menu screen opened\n"
                            "------\n"
                            "~Press 'Run'/your 'start-stop' hotkey to start bot!\n"
                            "~Press 'Stop'/'start-stop' again to stop and reset\n current plan."
                            " In order to play plan again, return to\n main menu screen, then press 'Run' again.\n"
                            "~To pause/unpause bot, press your 'pause' hotkey.\n Bot can only be paused during maps "
                            "i.e. when it's not\n navigating menu screens, but pauses as soon as it\n becomes " 
                            "possible.\n"
                            "~To close entire program at any point, press your\n"
                            " 'exit' hotkey.\n"+
                            55*"/"+"\n")
        self.textbox['state'] = 'disabled'
        # save current stdout stream to a variable, before redirecting it to textbox
        # could use sys.__stdout__ to return to original output stream; might implement this at some point.
        self.old_stdout = sys.stdout
        sys.stdout = gui_tools.TextRedirector(self.textbox, "stdout")

        self.roundtime_label = tk.Label(self.monitoringwindow, 
                                        width=15, 
                                        height=3, 
                                        text='Round timer', 
                                        relief='sunken',
                                        font=os_font)
        self.roundtime_label.grid(column=0, row=4, sticky='sw', padx=10)

        self.roundtime_display = tk.Label(self.monitoringwindow, 
                                          width=8, 
                                          height=3, 
                                          relief='sunken', 
                                          textvariable=self.roundtime, 
                                          font=os_font)
        self.roundtime_display.grid(column=0, row=4, sticky='s', padx=10)
        if self.farming == 'On':
            self.roundtime_display.grid_configure(padx=(70,0))

        scroll = tk.Scrollbar(self.monitoringwindow, orient='vertical')
        scroll.grid(column=3, row=0, rowspan=4, sticky='ns')
        self.textbox.configure(yscrollcommand=scroll.set)
        scroll.configure(command=self.textbox.yview)

        self.monitor_mapscreen_ascii = ("   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⢀⣾⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
                                        "   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣰⣿⣿⣿⣿⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
                                        "   ⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
                                        "   ⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
                                        "   ⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⡿⠿⢿⣿⣿⣶⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
                                        "   ⠀⠀⠀⠀⠀⠀⢼⡟⠉⣻⣿⣿⡏⠰⣷⠀⢹⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
                                        "   ⠀⠀⠀⠀⠀⠀⢻⣷⡀⠙⣻⣿⣿⣄⣠⣴⡿⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
                                        "   ⠀⠀⠀⠀⠀⠀⠀⣭⣉⣛⣻⣿⣿⣿⣿⣿⣿⣿⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n"
                                        "   ⠀⠀⠀⠀⠀⢠⠞⢡⣽⣿⣿⠿⢻⣿⣿⣿⣏⣿⣿⣿⣧⣤⣤⣤⣄⠀⠀⠀⠀⠀\n"
                                        "   ⠀⠀⠀⠀⠀⠘⣴⡨⠛⠋⠁⠀⣼⣿⣿⣿⡟⣿⣿⣿⣿⣯⢈⣿⣿⠂⠀⠀⠀⠀\n"
                                        "   ⠀⠀⠀⠀⠀⠘⠃⠀⠀⠀⢀⣤⣿⣷⡜⣿⣧⡉⠉⠙⠋⠁⠈⠉⠁⠀⠀⠀⠀⠀\n"
                                        "   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠁⢠⣾⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀     \n" 
                                        )
        style = ttk.Style()
        style.configure('Style.TButton', font='TkFixedFont')

        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            guivars_adjust: dict[str, Any] = json.load(f)["ocr_adjust_deltas"]
        if guivars_adjust:
            try:
                photo = tk.PhotoImage(file=gui_paths.MAP_IMAGES_PATH/'spa pits.png')
                self.monitor_mapscreen = ttk.Label(self.monitoringwindow, 
                                                   image=photo, 
                                                   compound='top', 
                                                   anchor='nw', 
                                                   justify='left')
                self.monitor_mapscreen.image = photo # type: ignore
                self.monitor_mapscreen.grid(column=4, columnspan=2, row=0, rowspan=2, sticky='ne')
            except tk.TclError:
                self.monitor_mapscreen = ttk.Label(self.monitoringwindow, 
                                                   compound='top', 
                                                   anchor='nw',
                                                   style='Style.TButton', 
                                                   justify='left')
                self.monitor_mapscreen.grid(column=4, columnspan=2, row=0, rowspan=2, sticky='ne')
                self.monitor_mapscreen['text'] = self.monitor_mapscreen_ascii
        elif self.farming == 'On':
            self.monitor_mapscreen = ttk.Label(self.monitoringwindow, 
                                               compound='top', 
                                               anchor='nw',
                                               style='Style.TButton', 
                                               justify='left')
            self.monitor_mapscreen.grid(column=4, columnspan=2, row=0, rowspan=2, sticky='ne')
            self.monitor_mapscreen.configure(image='')
            self.monitor_mapscreen['text'] = self.monitor_mapscreen_ascii
        else:
            try:
                photo = tk.PhotoImage(file=gui_paths.MAP_IMAGES_PATH/(plan_data.return_map(self.all_plans[0])+'.png'))
                self.monitor_mapscreen = ttk.Label(self.monitoringwindow, 
                                                   image=photo, 
                                                   compound='top', 
                                                   anchor='nw', 
                                                   justify='left')
                self.monitor_mapscreen.image = photo # type: ignore
                self.monitor_mapscreen.grid(column=4, columnspan=2, row=0, rowspan=2, sticky='ne')
            except tk.TclError:
                self.monitor_mapscreen = ttk.Label(self.monitoringwindow, 
                                                   compound='top', 
                                                   anchor='nw',
                                                   style='Style.TButton', 
                                                   justify='left')
                self.monitor_mapscreen.grid(column=4, columnspan=2, row=0, rowspan=2, sticky='ne')
                self.monitor_mapscreen['text'] = self.monitor_mapscreen_ascii

        self.monitor_infobox_current = tk.Label(self.monitoringwindow, 
                                                width=20, 
                                                height=5, 
                                                text='Current\n'+plan_data.info_display(self.all_plans[0]), 
                                                anchor='nw',
                                                relief='sunken', 
                                                justify='left', 
                                                wraplength=330, 
                                                padx=10, 
                                                pady=10)
        if guivars_adjust:
            self.monitor_infobox_current['text'] = 'Current\n'+plan_data.info_display('spa_pitsEasySandbox')
        elif self.farming == 'On':
            self.monitor_infobox_current['text'] = 'Current\n'+'-'*12
        self.monitor_infobox_current.grid(column=4, row=2, sticky='nw')

        if self.farming == 'Off':
            self.monitor_infobox_next = tk.Label(self.monitoringwindow, 
                                                 width=20, 
                                                 height=5, 
                                                 text='-'*12, 
                                                 anchor='nw',
                                                 relief='sunken', 
                                                 justify='left', 
                                                 padx=10, 
                                                 pady=10)
            self.monitor_infobox_next.grid(column=4, row=3, sticky='nw')
            if len(self.all_plans) > 1:
                self.monitor_infobox_next.config(text='Next\n'+plan_data.info_display(self.all_plans[1]))

        monitor_collection_text = tk.Label(self.monitoringwindow, 
                                           text='Collection event: '+str(self.collection_val),
                                           relief='sunken', 
                                           padx=10, 
                                           pady=10)
        monitor_collection_text.grid(column=5, row=2, sticky='ne')
        self._update_collection_status()
        self._update_farming_status()

        if self.farming == 'On':
            self.runs_label = tk.Label(self.monitoringwindow, 
                                        width=15, 
                                        height=3, 
                                        text='Runs completed', 
                                        relief='sunken',
                                        font=os_font)
            self.runs_label.grid(column=1, row=4, sticky='sw', padx=10)

            self.runs_display = tk.Label(self.monitoringwindow, 
                                         width=8, 
                                         height=3, 
                                         relief='sunken', 
                                         textvariable=self.runs, 
                                         font=os_font)
            self.runs_display.grid(column=1, row=4, sticky='s', padx=(75,0))

            monitor_farming_text = tk.Label(self.monitoringwindow, 
                                            text='Farm mode: On',             
                                            relief='sunken', 
                                            padx=10, 
                                            pady=10)
            monitor_farming_text.grid(column=5, row=2, sticky='e')
        else:
            monitor_queuemode_text = tk.Label(self.monitoringwindow, 
                                              text='Queue mode: '+str(self.queue_val),             
                                              relief='sunken', 
                                              padx=10, 
                                              pady=10)
            monitor_queuemode_text.grid(column=5, row=2, sticky='se')

            monitor_replay_text = tk.Label(self.monitoringwindow, 
                                           text='Replay mode: '+str(self.replay_val),
                                           relief='sunken', 
                                           padx=10, 
                                           pady=10)
            monitor_replay_text.grid(column=5, row=3, sticky='e', pady=10)

        # create the initial placeholder thread for MainWindow.is_monitoringwindow.
        self.bot_thread = threading.Thread()
        MonitoringWindow.current_bot_thread = self.bot_thread

        self.monitor_run_button = tk.Button(self.monitoringwindow, 
                                            text='Run', 
                                            command=self._stop_or_run, 
                                            state='active', 
                                            padx=10, 
                                            pady=10)
        self.monitor_run_button.grid(column=5, row=4, sticky='ne')

        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            if json.load(f)["logging"]:
                BotVars.logging = True
            else:
                BotVars.logging = False
        GuiHotkeys.start_stop_status = False
        GuiHotkeys.pause_status = False
        # listener thread object sends keyboard inputs to _bot_hotkey method
        self.bot_hk_listener = threading.Thread(target=self._bot_hotkey)
        self.bot_hk_listener.daemon = True
        self.bot_hk_listener.start()  

    def _update_round_timer(self) -> None:
        """Update round timer value during rounds."""
        BotData.set_data()
        self.roundtime.set("0.00")
        while self.bot_thread.is_alive():
            if BotData.current_round == 0:
                time.sleep(0.1)
            elif BotData.paused:
                time.sleep(0.1)
            elif BotData.current_round < BotData.end_r+1:
                current = times.current_time()-BotData.round_time
                self.roundtime.set(f"{current:.2f}")
                time.sleep(0.05)
            else:
                time.sleep(3)
                BotData.set_data()
                self.roundtime.set("0.00")
        self.roundtime.set("-")

    def _update_collection_status(self) -> None:
        BotVars.current_event_status = self.collection_val

    def _update_farming_status(self) -> None:
        BotVars.current_farming_status = self.farming

    def _stop_or_run(self) -> None:
        """Handles current bot thread termination and opening of new ones."""
        if self.bot_thread.is_alive():
            gui_tools.terminate_thread(self.bot_thread)
            self.bot_thread = threading.Thread(target=self._run_bot, daemon=True)
            MonitoringWindow.current_bot_thread = self.get_bot_thread()
            self.monitor_run_button.configure(text='Run')
            cprint('\n#####Bot terminated#####')
            return
        self.bot_thread = threading.Thread(target=self._run_bot, daemon=True)
        MonitoringWindow.current_bot_thread = self.get_bot_thread()
        self.bot_thread.start()
        self.monitor_run_button.configure(text='Stop')
        roundtimer_thread = threading.Thread(target=self._update_round_timer, daemon=True)
        roundtimer_thread.start()

    def _res_check(self, customres: bool, resolution_val: tuple[int, ...], windowed: bool, w: int, h: int,
                   ingame_shift: bool, shift_val: tuple[int, ...]) -> None:
        try:
            with open(gui_paths.FILES_PATH/'upgrades_current.json') as f:
                identifier: list[int | str] = json.load(f)["__identifier"]
        except FileNotFoundError:
            print("***\nupgrades_current.json couldn't not be found, creating one with default values\n"
                "You should perform ocr auto-adjust before continuing\n***\n")
            shutil.copy2(gui_paths.FILES_PATH/'_ocr_upgradedata.json', gui_paths.FILES_PATH/'upgrades_current.json')
            with open(gui_paths.FILES_PATH/'upgrades_current.json') as f:
                identifier: list[int | str] = json.load(f)["__identifier"]
        issue_flag: bool = False
        if customres:
            if list(resolution_val) != identifier[0:2]:
                cprint("-"*55+"\n"
                        ">Ocr data resolution differs from display resolution:\n"
                        " Ocr resolution:", identifier[0], identifier[1], "\n"
                        " Display resolution:", resolution_val[0], resolution_val[1])
                issue_flag = True
        else:
            if list((w, h)) != identifier[0:2]:
                cprint("-"*55+"\n"
                        ">Ocr data resolution differs from display resolution:\n"
                        " Ocr resolution:", identifier[0], identifier[1], "\n"
                        " Display resolution:", w, h)
                issue_flag = True
        if identifier[4] == "fullscreen" and windowed:
            cprint("-"*55+"\n"
                    ">Ocr data supports fullscreen, but you use\n windowed mode.")
            issue_flag = True
        elif identifier[4] == "windowed" and not windowed:
            cprint("-"*55+"\n"
                    ">Ocr data supports windowed mode, but you use\n fullscreen mode.")
            issue_flag = True
        if ingame_shift and list(shift_val) != identifier[2:4]:
            cprint("-"*55+"\n"
                    ">Ocr data coordinate shift differs from current value:\n"
                    " Ocr shift:", identifier[3], identifier[3], "\n"
                    " Current shift:", shift_val[0], shift_val[1])
            issue_flag = True
        if issue_flag:
            cprint(55*"-"+"\n"
                    "-->> Issues detected; see above. <<--\n" \
                    "They don't prevent bot from starting, but are very likely to cause problems with ocr text "
                    "detection.\n"+
                    27*" "+".\n"+
                    27*" "+".\n"+
                    27*" "+".\n")

    def _plantest_print(self, plan: str, attempt: int, attempt_limit: int) -> None:
        if 1 <= attempt <= attempt_limit:
            if attempt_limit == 1:
                cprint('~~~~'+plan_data.return_map(plan)+', '+
                    plan_data.return_strategy(plan).split('-')[0].lower()+', '+
                    plan_data.return_strategy(plan).split('-')[1].lower()+'~~~~')
            else:
                cprint('~~~~'+plan_data.return_map(plan)+', '+
                    plan_data.return_strategy(plan).split('-')[0].lower()+', '+
                    plan_data.return_strategy(plan).split('-')[1].lower()+
                    f' [Attempt {attempt}/{attempt_limit}]~~~~')

    def _queuemode_results(self) -> None:
        cprint("Plan queue finished.")
        cprint("Results:")
        success: int = 0
        total = len(self.plans_status)
        for name in self.plans_status:
            if 'success [' in name:
                success += 1
        cprint(f">Success rate: {((success/total)*100):.2f}%")
        for name in self.plans_status:
            cprint(name)

    def _run_plans(self, retries: int) -> None:
        if self.current_plans == []:
            self.current_plans = self.all_plans[:]
        while self.current_plans != []:
            BotData.victory = False
            attempt_number: int = 1
            while attempt_number <= retries:
                self._plantest_print(self.current_plans[0], attempt_number, retries)
                self._execute(self.current_plans, 0)
                if BotData.victory:
                    break
                attempt_number += 1
            if BotData.victory:
                if retries == 1:
                    self.plans_status.append(f"{self.current_plans[0]} -- success")
                else:
                    self.plans_status.append(
                        f"{self.current_plans[0]} -- success [{attempt_number}/{retries}]")
            else:
                self.plans_status.append(f"{self.current_plans[0]} -- failed")
            self.current_plans.pop(0)

    def _run_bot(self) -> None:
        """Checks if replay mode is enabled/disabled and runs the sequence of plans listed in self.all_plans.

        Will also check resolution settings, ocr adjusting and farm mode conditions, and performs additional steps
        depending on these conditions.

        Queue mode enabled/disabled check is already done before creating MonitorScreen object so queue check is not
        needed again.
        """
        cprint('=====Bot running=====')
        with open(gui_paths.FILES_PATH/'gui_vars.json') as f:
            gui_vars_dict: dict[str, Any] = json.load(f)
        customres: bool = gui_vars_dict["check_resolution"]
        resolution_val: tuple[int, ...] = tuple(map(int, gui_vars_dict["custom_resolution"].split('x')))
        windowed: bool = gui_vars_dict["windowed"]
        ingame_shift: bool = gui_vars_dict["check_resolution"]
        shift_val: tuple[int, ...] = tuple(map(int, gui_vars_dict["ingame_res_shift"].split('x')))
        retries_val: int = gui_vars_dict["retries"]
        w, h = pyautogui.size()

        if not gui_vars_dict["ocr_adjust_deltas"]:
            self._res_check(customres, resolution_val, windowed, w, h, ingame_shift, shift_val)
        if customres:
            cprint('[Custom Resolution] '+str(resolution_val[0])+'x'+str(resolution_val[1])+'\n'
                    '[Windowed] '+str(windowed)+'\n')
        else:
            w, h = pyautogui.size()
            cprint('[Resolution] '+str(w)+'x'+str(h)+'\n')
        if gui_vars_dict["ocr_adjust_deltas"]:
            try:
                new_image = tk.PhotoImage(file=gui_paths.MAP_IMAGES_PATH/'spa pits.png')
                self.monitor_mapscreen['text'] = ''
                self.monitor_mapscreen.configure(image=new_image)
                self.monitor_mapscreen.image = new_image # type: ignore
            except tk.TclError:
                self.monitor_mapscreen.configure(image='')
                self.monitor_mapscreen['text'] = self.monitor_mapscreen_ascii
            self.monitor_infobox_current.configure(text='Current\n'+plan_data.info_display('spa_pitsEasySandbox'))
            cprint(".-------------------------.\n"
                  "| Ocr adjust mode enabled |\n"
                  ".-------------------------.\n")
            set_plan.run_delta_adjust()
            cprint("You may now close this window.")
            self.monitor_run_button.configure(text='Run')
            self.monitor_run_button['state'] = 'disabled'
            return
        if os.path.exists(gui_paths.FILES_PATH/'.temp_upg_deltas.json'):
            os.remove(gui_paths.FILES_PATH/'.temp_upg_deltas.json')
        if self.farming == 'On':
            set_plan.farming_print()
            set_plan.select_defaulthero()
            while True:
                rewardplan: str = set_plan.select_rewardplan()
                if rewardplan == '':
                    cprint('\n#####Unable to continue farming loop, bot terminated#####')
                    self.monitor_run_button['text'] = 'Run'
                    return
                try:
                    self.monitor_mapscreen.destroy()
                    rewardmap: str = plan_data.return_map(rewardplan)
                    new_image = tk.PhotoImage(file=gui_paths.MAP_IMAGES_PATH/f'{rewardmap}.png')
                    self.monitor_mapscreen = ttk.Label(self.monitoringwindow, 
                                                       image=new_image, 
                                                       compound='top', 
                                                       anchor='nw', 
                                                       justify='left')
                    self.monitor_mapscreen.image = new_image # type: ignore
                    self.monitor_mapscreen.grid(column=4, columnspan=2, row=0, rowspan=2, sticky='ne')
                except tk.TclError:
                    self.monitor_mapscreen.configure(image='')
                    self.monitor_mapscreen['text'] = self.monitor_mapscreen_ascii
                self.monitor_infobox_current.configure(text='Current\n'+plan_data.info_display(rewardplan))
                if not set_plan.run_farming_mode(rewardplan):
                    self.runs.set(self.runs.get()+1)
        if self.replay_val == 'On':
            while True:
                self._run_plans(retries_val)
                if self.queue_val == 'On':
                    self._queuemode_results()
                    cprint('\n>>>Replaying all plans in queue. Starting in... ', end='')
                    timing.counter(3)
                    cprint()
                else:
                    cprint("Replaying the selected plan. Starting in... ", end='')
                    timing.counter(3)
                    cprint()
                self.plans_status = []
        else:
            self._run_plans(retries_val)
            self.monitor_run_button.configure(text='Run')
            if self.queue_val == 'On':
                self._queuemode_results()
                self.monitor_run_button.configure(text='Repeat queue')
            self.plans_status = []
    
    def _execute(self, plans_list: list[str], index: int) -> None:
        """Updates monitoring box data before moving responsibility to set_plan module.

        Args:
            plans_list: List of plan strings. 
            index: Integer value for finding desired plan from plans_list. If default gui configuration is used and
                this function is called via _run_bot, then plans_list is list of remaining plans and index is always 0.
        """
        current = plans_list[index]
        try:
            next = plans_list[index+1]
            self.monitor_infobox_next.configure(text='Next\n'+plan_data.info_display(next))
        except IndexError:
            self.monitor_infobox_next.configure(text='-'*12) 
        try:
            new_image = tk.PhotoImage(file=gui_paths.MAP_IMAGES_PATH/(plan_data.return_map(current)+'.png'))
            self.monitor_mapscreen['text'] = ''
            self.monitor_mapscreen.configure(image=new_image)
            self.monitor_mapscreen.image = new_image # type: ignore
        except tk.TclError:
            self.monitor_mapscreen.configure(image='')
            self.monitor_mapscreen['text'] = self.monitor_mapscreen_ascii
        self.monitor_infobox_current.configure(text='Current\n'+plan_data.info_display(current))
        set_plan.plan_setup(current)

    def _bot_hotkey(self) -> None:
        """Hotkey to start/stop bot when monitoring window is open.

        Perfoms a separate winfo_exists check to ensure that previous MonitoringWindow.bot_hk_listener is
        stopped, can otherwise throw an error for refering to now non-existent attributes of that window.

        Args:
            key: Latest keyboard key the user has pressed. 
        """
        while self.monitoringwindow.winfo_exists():
            if GuiHotkeys.start_stop_status == True:
                GuiHotkeys.start_stop_status = False
                self._stop_or_run()
                time.sleep(1)
            elif GuiHotkeys.pause_status == True:
                BotVars.paused = not BotVars.paused
                GuiHotkeys.pause_status = False
            time.sleep(0.1)
        else:
            gui_tools.terminate_thread(self.bot_hk_listener)

    def get_bot_thread(self) -> threading.Thread:
        """Return current bot thread.

        Returns:
            Currently existing thread that targets _run_bot.
        """
        return self.bot_thread

    def get_monitoringwindow(self) -> tk.Toplevel:
        """Return current monitoring window.

        Returns:
            Current Toplevel object of MonitoringWindow.
        """
        return self.monitoringwindow
    
    def get_old_output(self) -> TextIO | Any:
        """Return original standard output stream.

        Returns:
            Original stdout stream.
        """
        return self.old_stdout