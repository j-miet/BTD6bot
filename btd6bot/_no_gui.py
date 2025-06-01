"""Gui-free lite version of BTD6bot.

Cannot change settings or enable game modes, as these are controlled via gui.

Can play any currently supported plan, though, as bot is entirely separated from gui functionality-wise. 
"""

import json
import os
from pathlib import Path
import signal
import sys

import pynput.keyboard
from pynput.keyboard import Key, KeyCode
import set_plan
import utils.plan_data

def run() -> None:
    
    def exit(key: Key | KeyCode | None) -> None:
        """Program termination via hotkey (same one is used in gui.MainWindow).

        Termination hotkey is currently F11.

        Args:
            key: Latest keyboard key the user has pressed.       
        """
        if key == Key.f11: 
            os.kill(os.getpid(), signal.SIGTERM)

    # listener thread object sends keyboard inputs to exit function
    if sys.platform == "win32":
        kb_listener = pynput.keyboard.Listener(on_press = exit)
        kb_listener.daemon = True
        kb_listener.start()

    INFO_MESSAGE = ('*This version doesn\'t support collection event/queue/replay modes. It won\'t allow user to\n '
          'change settings/hotkeys, but current values from gui are shared, so if you want to\n' 
          'adjust them, do that in gui then run this version after. Also, no pause or reset buttons exist.\n'
          '/////////\n'
          '--Commands--\n'
          'help = displays this message again\n'
          'adjust = if ocr adjust setting is enabled, runs adjusting process\n'
          'plans = list all available plans.\n'
          'run plan_name = run the plan plan_name <- replace this with an existing plan name.\n'
          '                  >Note that when you use \'run ...\' command first time after running this script, \n '
          '                   the ocr reader is loaded into memory which might take a bit, just wait.\n'
          '                  >Example: run dark_castleEasyStandard\n'
          'exit = exit program. Alternatively use F11 key: this hotkey works while bot is running, in case you \n'
          '     need a quick exit.'
          )
    print('===================================\n'
          '|   Welcome to gui-free BTD6bot   |\n'
          '===================================\n'
          '/////////\n')
    print(INFO_MESSAGE)
    plans = utils.plan_data.read_plans()
    while 1:
        user_input = input('=>')
        if len(user_input) == 0:
            ...
        elif user_input.lower() == 'help':
            print(INFO_MESSAGE)
        elif user_input.lower() == 'adjust':
            with open(Path(__file__).parent/'Files'/'gui_vars.json') as f:
                    gui_vars_dict= json.load(f)
            if gui_vars_dict["ocr_adjust_deltas"]:
                print(".-------------------------.\n"
                "| Ocr adjust mode enabled |\n"
                ".-------------------------.\n")
                set_plan.run_delta_adjust()
            else:
                print("Auto-adjusting not enabled.")
        elif user_input.lower() == 'plans':
            print('All available plans: \n')
            for p in plans:
                print(p)
        elif user_input.split()[0] == 'run':
            try:
                plan_name = user_input.split()[1]
                if plan_name in plans:
                    print("Running plan: "+"'"+plan_name+"'.\n" 
                            "1. if this is your first plan of the session, wait for the ocr reader to initialize\n"
                            "2. number countdowns don't work in non-gui version so expect their entire result to "
                            "pop after the countdown finishes.\n" 
                            "(reason for above is that all print statements are build around gui version and must "
                            "have flush=False)\n"
                            "============================================")
                    set_plan.plan_setup(plan_name)
                else:
                    print('Plan not found.')
            except (TypeError, IndexError):
                print("Invalid input.")
        elif user_input.lower() == 'exit':
            break