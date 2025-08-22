"""Gui-free lite version of BTD6bot.

Cannot change settings or enable game modes, as these are controlled via gui.

Can play any currently supported plan, though, as bot is entirely separated from gui functionality-wise. 
"""

import json
import os
from pathlib import Path
import signal
import threading
import time

import pynput.keyboard
from pynput.keyboard import Key, KeyCode

from bot.bot_vars import BotVars
from customprint import cprint, cinput
import set_plan
import utils.plan_data
import gui.gui_tools as gui_tools
from gui.guihotkeys import GuiHotkeys

class NoGui:
    def __init__(self) -> None:
        self.replay: bool = False
        self.bot_thread: threading.Thread
        self.bot_thread_active = False
        self.INFO_MESSAGE = ('*This version does not currently support collection event/queue/replay modes. To change '
            'any settings/hotkeys,\n'
            'use the gui version, make changes there and they will be shared with this version.\n'
            'Gui hotkeys \'start-stop\', \'exit\' and \'pause\' also work.\n'
            '/////////\n'
            '--Commands--\n'
            'help = displays this message again\n'
            'modes = toggle on event and replay modes\n'
            'adjust = if ocr adjust setting is enabled, runs adjusting process\n'
            'plans = lists all available plans.\n'
            'run plan_name = run the plan plan_name <- replace this with an existing plan name.\n'
            '                  >Note that when you use \'run ...\' command first time after running this script,\n'
            '                   the ocr reader is loaded into memory which might take a bit, just wait.\n'
            '                  >Example: run dark_castleEasyStandard\n'
            'queue = run all plans listed in queue_list.txt\n'
            'exit = exit program.'
            )
        self.PLANS = utils.plan_data.read_plans()

    def _toggle_modes(self) -> None:
        while 1:
            input_str = input("Change event and replay modes on/off by typing 'event' or 'replay'." 
                            " Type 'back' to return to main ui\n=>")
            match input_str:
                case 'event':
                    if BotVars.current_event_status == 'On': 
                        BotVars.current_event_status = 'Off' 
                    else:
                        BotVars.current_event_status = 'On'
                    cprint(f"Event status: {BotVars.current_event_status}.")
                case 'replay':
                    self.replay = not self.replay
                    cprint(f"Replay status: {self.replay}.")
                case 'back':
                    return

    def _run_queue(self) -> None:
        with open(Path(__file__).parent/'Files'/'text files'/'queue_list.txt') as f:
            queued_plans: list[str] = f.readlines()
        if len(queued_plans) > 0:
            for p in queued_plans:
                self._run_plan(p.replace('\n', ''))

    def _run_plan(self, plan_name: str) -> None:
        try:
            if plan_name in self.PLANS:
                cprint("Running plan: "+"'"+plan_name+"'.\n" 
                        "============================================")
                self.bot_thread = threading.Thread(target=set_plan.plan_setup, args=[plan_name], daemon=True)
                self.bot_thread.start()
                self.bot_thread_active = True
                while self.bot_thread.is_alive():
                    time.sleep(0.1)
                self.bot_thread_active = False
                print()
            else:
                cprint('Plan not found.')
        except (TypeError, IndexError):
            cprint("Invalid plan input.")

    def _perform_autoadjust(self) -> None:
        with open(Path(__file__).parent/'Files'/'gui_vars.json') as f:
            gui_vars_dict= json.load(f)
        if gui_vars_dict["ocr_adjust_deltas"]:
            print(".-------------------------.\n"
            "| Ocr adjust mode enabled |\n"
            ".-------------------------.\n")
            set_plan.run_delta_adjust()
        else:
            cprint("Auto-adjusting not enabled.")

    def run(self) -> None:
        """Main loop for no-gui version of BTD6bot."""

        def exit(key: Key | KeyCode | None) -> None:
            """Program termination via hotkey.

            Args:
                key: Latest keyboard key the user has pressed.       
            """
            if key == GuiHotkeys.exit_hotkey or (isinstance(key, KeyCode) and key.char == GuiHotkeys.exit_hotkey):
                cprint("Process terminated.")
                os.kill(os.getpid(), signal.SIGTERM)
            elif (key == GuiHotkeys.start_stop_hotkey or 
                (isinstance(key, KeyCode) and key.char == GuiHotkeys.start_stop_hotkey)):
                if self.bot_thread_active:
                    gui_tools.terminate_thread(self.bot_thread)

        kb_listener = pynput.keyboard.Listener(on_press = exit)
        kb_listener.daemon = True
        kb_listener.start()

        with open(Path(__file__).parent/'Files'/'gui_vars.json') as f:
            if json.load(f)["logging"]:
                BotVars.logging = True
        
        cprint('===================================\n'
            '|   Welcome to gui-free BTD6bot   |\n'
            '===================================\n'
            ">>> Ocr reader model is loaded into memory, please wait...")
        from bot.ocr.ocr_reader import OCR_READER
        cprint('Model loaded.')
        print(self.INFO_MESSAGE)
        while 1:
            user_input = cinput('=>')
            if len(user_input) == 0:
                ...
            elif user_input.lower() == 'help':
                print(self.INFO_MESSAGE)
            elif user_input.lower() == 'modes':
                self._toggle_modes()
            elif user_input.lower() == 'adjust':
                self._perform_autoadjust()
            elif user_input.lower() == 'plans':
                print('All available plans: \n')
                for p in self.PLANS:
                    print(p)
            elif len(user_input.split()) == 2 and user_input.split()[0].lower() == 'run':
                self._run_plan(user_input.split()[1])
            elif user_input.lower() == 'queue':
                self._run_queue()
            elif user_input.lower() == 'exit':
                break
            else:
                cprint("Unknown input")