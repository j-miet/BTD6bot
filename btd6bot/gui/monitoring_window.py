"""Contains MonitoringWindow class."""

from __future__ import annotations
from typing import TYPE_CHECKING

import json
import sys
import threading
import time
import tkinter as tk
from tkinter import ttk

import pynput

import gui.gui_tools as gui_tools
import set_plan as set_plan
from utils import plan_data
from utils import timing
import gui.gui_paths as gui_paths

from bot.bot_data import BotData

if TYPE_CHECKING:
    from typing import Any, TextIO
    from pynput.keyboard import Key, KeyCode

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
            worse, these unaccessable & unusable threads could stack and execute multiple bots at the same time, which 
            of course, would break everything as they all share key & mouse inputs and all files.
        
        all_plans (list[str]): List of all plans in the queue list or a single plan if queue mode is disabled.
        replay_val (str): String with On/Off value for replay mode button.
        queue_val (str): String with On/Off value for queue mode button.
        collection (str): String with On/Off value to both display collection event status and update corresponding 
            value to gui_vars.json.
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
        bot_thread (threading.Thread): Current thread where bot iself is allocated. A placeholder thread is initially 
            created so that MainWindow can start tracking its existence and won't throw an error. After 'Run' button is 
            pressed, stop_or_run method is called and target of this thread is set to run_bot method instead.
    """
    START_STOP_HOTKEY = pynput.keyboard.Key.f9

    current_bot_thread: threading.Thread

    def __init__(self, all_plans_list: list[str], replay: str, queue: str, collection: str) -> None:
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

        self.monitoringwindow = tk.Toplevel()
        self.monitoringwindow.title("Bot Monitoring Window")
        self.monitoringwindow.geometry('800x480')
        self.monitoringwindow.minsize(800,480)
        self.monitoringwindow.maxsize(800,480)

        self.textbox = tk.Text(self.monitoringwindow, width=55, height=25, state='normal', wrap=tk.WORD)
        self.textbox.grid(column=0, columnspan=2, row=0, rowspan=4, sticky='n')
        self.textbox.insert('end', "Welcome to BTD6bot!\n"
                            "Make sure that game:\n"
                            ">Game language is set as ENGLISH\n"
                            ">Game resolution has aspect ratio 16:9\n"
                            ">Game is in fullscreen (windowed won't work)\n"
                            ">Bot hotkeys match to your in-game equivalents\n"
                            ">You have the following settings in 'Esc' menu in-game:\n"
                            " -Autostart = ON\n"
                            " -Drag & Drop = ON\n"
                            " -Disable nudge mode = ON\n"
                            "------\n"
                            "~Press 'Run'/F9 to start bot!\n"
                            "~Press 'Stop'/F9 to stop & RESET bot.\n If queue mode is enabled, your map queue will\n" 
                            " also reset, meaning that bot starts from the first\n"
                            " map again.\n"
                            "~To shut down entire program at any point, press F11.\n"
                            "#currently, there's no way to 'pause' the bot - you\n"
                            " either let it finish or reset it back to start.\n"
                            "///////////////////////////////////////////////////////")
        self.textbox['state'] = 'disabled'
        # save current stdout stream to a variable, before redirecting it to textbox
        # could use sys.__stdout__ to return to original output stream; might implement this at some point.
        self.old_stdout = sys.stdout
        sys.stdout = gui_tools.TextRedirector(self.textbox, "stdout")

        self.roundtime_label = tk.Label(self.monitoringwindow, width=15, height=3, text='Round timer', relief='sunken')
        self.roundtime_label.grid(column=0, row=4, sticky='sw', padx=10)

        self.roundtime = tk.StringVar(value='-')

        self.roundtime_display = tk.Label(self.monitoringwindow, width=8, height=3, relief='sunken', 
                                          textvariable=self.roundtime)
        self.roundtime_display.grid(column=0, row=4, sticky='s')

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
        try:
            photo = tk.PhotoImage(file=gui_paths.MAP_IMAGES_PATH+'\\'+plan_data.return_map(self.all_plans[0])+'.png')
            self.monitor_mapscreen = ttk.Label(self.monitoringwindow, image=photo, compound='top', anchor='nw', 
                                               padding="0 15 0 0", justify='left')
            self.monitor_mapscreen.image = photo # type: ignore
            self.monitor_mapscreen.grid(column=4, columnspan=2, row=0, rowspan=2, sticky='ne')
        except tk.TclError:
            self.monitor_mapscreen = ttk.Label(self.monitoringwindow, compound='top', anchor='nw',
                                              style='Style.TButton', justify='left')
            self.monitor_mapscreen.grid(column=4, columnspan=2, row=0, rowspan=2, sticky='ne')
            self.monitor_mapscreen['text'] = self.monitor_mapscreen_ascii

        self.monitor_infobox_current = tk.Label(self.monitoringwindow, width=20, height=5, 
                                                text='Current\n'+plan_data.info_display(self.all_plans[0]), anchor='nw',
                                                relief='sunken', justify='left', wraplength=330, padx=10, pady=10)
        self.monitor_infobox_current.grid(column=4, row=2, sticky='nw')

        self.monitor_infobox_next = tk.Label(self.monitoringwindow, width=20, height=5, text='-'*12, anchor='nw',
                                             relief='sunken', justify='left', padx=10, pady=10)
        self.monitor_infobox_next.grid(column=4, row=3, sticky='nw')

        monitor_collection_text = tk.Label(self.monitoringwindow, text='Collection event: '+str(self.collection_val),
                                           relief='sunken',padx=10, pady=10)
        monitor_collection_text.grid(column=5, row=2, sticky='ne')
        self.update_event_status_to_json()

        monitor_queuemode_text = tk.Label(self.monitoringwindow, text='Queue mode: '+str(self.queue_val),             
                                          relief='sunken',padx=10, pady=10)
        monitor_queuemode_text.grid(column=5, row=2, sticky='se')

        monitor_replay_text = tk.Label(self.monitoringwindow, text='Replay mode: '+str(self.replay_val),
                                       relief='sunken', padx=10, pady=10)
        monitor_replay_text.grid(column=5, row=3, sticky='e', pady=10)

        # create the initial placeholder thread for MainWindow.is_monitoringwindow.
        self.bot_thread = threading.Thread()
        MonitoringWindow.current_bot_thread = self.bot_thread

        self.monitor_run_button = tk.Button(self.monitoringwindow, text='Run', command=self.stop_or_run, state='active',
                                            padx=10, pady=10)
        self.monitor_run_button.grid(column=5, row=4, sticky='ne')

        # listener thread object sends keyboard inputs to bot_hotkey method
        self.bot_hk_listener = pynput.keyboard.Listener(on_press = self.bot_hotkey)
        self.bot_hk_listener.daemon = True
        self.bot_hk_listener.start()  

    def update_round_timer(self) -> None:
        """Update round timer value during rounds.
        
        Requires data from bot.bot_data.BotData class to function.
        """
        with open(gui_paths.FILES_PATH+'\\gui_vars.json') as f:
            gui_vars_dict = json.load(f)
        if gui_vars_dict["get_botdata"] == True:
            BotData.set_data()
            self.roundtime.set("0.00")
            while self.bot_thread.is_alive():
                if BotData.current_round == 0:
                    time.sleep(0.1)
                elif BotData.current_round < BotData.end_r+1:
                    current = time.time()-BotData.round_time
                    self.roundtime.set(f"{current:.2f}")
                else:
                    time.sleep(3)
                    BotData.set_data()
                    self.roundtime.set("0.00")
                time.sleep(0.01) 
            self.roundtime.set("-")

    def update_event_status_to_json(self) -> None:
        """Updates collection event status to gui_vars.json."""
        with open(gui_paths.FILES_PATH+'\\gui_vars.json') as f:
            gui_vars_dict = json.load(f)
        gui_vars_dict["current_event_status"] = self.collection_val
        with open(gui_paths.FILES_PATH+'\\gui_vars.json', 'w') as f:
            json.dump(gui_vars_dict, f, indent=4)

    def stop_or_run(self) -> None:
        """Handles current bot thread termination and opening of new ones."""
        if self.bot_thread.is_alive():
            gui_tools.terminate_thread(self.bot_thread)
            self.bot_thread = threading.Thread(target=self.run_bot, daemon=True)
            MonitoringWindow.current_bot_thread = self.get_bot_thread()
            self.monitor_run_button.configure(text='Run')
            print('\n#####Bot terminated#####')
            return
        self.bot_thread = threading.Thread(target=self.run_bot, daemon=True)
        MonitoringWindow.current_bot_thread = self.get_bot_thread()
        self.bot_thread.start()
        self.monitor_run_button.configure(text='Stop')
        roundtimer_thread = threading.Thread(target=self.update_round_timer, daemon=True)
        roundtimer_thread.start()

    def run_bot(self) -> None:
        """Checks if replay mode is enabled/disabled and runs the sequence of plans listed in self.all_plans.

        Queue mode enabled/disabled check is already done before creating MonitorScreen object so queue check is not
        needed again.
        """
        print('\n=====Bot running=====\n')
        if self.replay_val == 'On':
            while True:
                for plan_index in range(len(self.all_plans)):
                    self.execute(self.all_plans, plan_index)
                print('>>>Replaying all maps in queue!\nStarting in... ')
                plan_index = 0
                timing.counter(10)
                print()
        else:
            for plan_index in range(len(self.all_plans)):
                self.execute(self.all_plans, plan_index)
                self.monitor_run_button.configure(text='Run')
            if len(self.all_plans) > 1:
                print("All queued maps completed!\n")
    
    def execute(self, all_plans: list[str], index: int) -> None:
        """Updates monitoring box data before moving responsibility to set_plan module.

        Args:
            all_plans: List of all plan strings. 
            index: Integer value for finding desired plan from all_plans.
        """
        current = all_plans[index]
        try:
            next = all_plans[index+1]
            self.monitor_infobox_next.configure(text='Next:\n'+plan_data.info_display(next))
        except IndexError:
            self.monitor_infobox_next.configure(text='-'*12) 
        try:
            new_image = tk.PhotoImage(file=gui_paths.MAP_IMAGES_PATH+'\\'+plan_data.return_map(current)+'.png')
            self.monitor_mapscreen['text'] = ''
            self.monitor_mapscreen.configure(image=new_image)
            self.monitor_mapscreen.image = new_image # type: ignore
        except tk.TclError:
            self.monitor_mapscreen.configure(image='')
            self.monitor_mapscreen['text'] = self.monitor_mapscreen_ascii
        self.monitor_infobox_current.configure(text='Current\n'+plan_data.info_display(current))
        set_plan.plan_setup(current)

    def get_bot_thread(self) -> threading.Thread:
        """Return current bot thread.

        Returns:
            Currently existing thread that targets run_bot.
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

    def bot_hotkey(self, key: Key | KeyCode | None) -> None:
        """Hotkey to start/stop bot when monitoring window is open.

        Perfoms a separate winfo_exists check to ensure that previous MonitoringWindow.bot_hk_listener is
        stopped, can otherwise throw an error for refering to now non-existent attributes of that window.

        Args:
            key: Latest keyboard key the user has pressed. 
        """
        if self.monitoringwindow.winfo_exists():
            if key == MonitoringWindow.START_STOP_HOTKEY:
                self.stop_or_run()
                time.sleep(1)
        else:
            self.bot_hk_listener.stop()