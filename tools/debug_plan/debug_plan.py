"""Test any plan file.

Currently only static tower position checking is supported. If map has dynamic positioning i.e. towers move between
rounds, this tool won't work.
"""

import os
from pathlib import Path
import signal
import sys
import threading
import time


import pynput.keyboard
from pynput.keyboard import Key, KeyCode

# force absolute path in order to detect any bot packages
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../btd6bot")))

from bot import _maindata
from customprint import cprint
import gui.gui_tools as gui_tools
from set_plan import plan_setup
import utils.plan_data

# set low time limit value, sandbox environment should detect tower placements pretty much instantly if valid
_maindata.maindata["debug"]["time_limit"] = 5

bot_thread: threading.Thread
bot_thread_active: bool

PLANS = utils.plan_data.read_plans()

INTRO = (
    "This tool is for debugging plan files.\n"
    "F10 to close this tool, F8 to stop current debugging loop\n"
    "How it works: give a plan name and debugging mode e.g. static)\n"
    "After pressing F8 or finishing debug loop, you are returned back here and can select another plan + debug combination\n"
    "--Also make sure to read the debug.md file in the directory of this tooling script for more complex usage--\n"
)
COMMANDS = (
    "Type\n"
    "'intro' to print introduction message\n"
    "'commands' to print these commands again\n"
    "'plans' to see all plans\n"
    "'modes' to see all supported debugging modes\n"
    "'exit' to close tool\n"
    "or type 'debug plan_name mode_name' to begin plan debugging\n"
)


def exit(key: Key | KeyCode | None) -> None:
    """Program termination via hotkey.

    Args:
        key: The last keyboard key user has pressed.
    """
    if key == Key.f10:
        cprint("Process terminated.")
        os.kill(os.getpid(), signal.SIGTERM)
    elif key == Key.f8:
        if bot_thread_active:
            gui_tools.terminate_thread(bot_thread)



def run_plan(plan_name: str, debug_mode: str, start_round: int = -1, start_herolvl=-1) -> None:
    try:
        if debug_mode == "static":
            _maindata.debug_set_mode(_maindata.Debug.POS_STATIC)
        elif debug_mode == "start":
            _maindata.debug_set_mode(_maindata.Debug.SETUP_STATIC_STATE)
            _maindata.debug_set_startround(start_round)
            _maindata.maindata["debug"]["hero_startlevel"] = start_herolvl
        else:
            cprint("Invalid debug mode input.")
            return

        if plan_name in PLANS:
            cprint("Running plan: " + "'" + plan_name + "'.\n" "============================================")
            global bot_thread
            global bot_thread_active
            bot_thread = threading.Thread(target=plan_setup, args=[plan_name], daemon=True)
            bot_thread.start()
            bot_thread_active = True
            while bot_thread.is_alive():
                time.sleep(0.1)
            bot_thread_active = False
            print()
        else:
            cprint("Plan not found.")
    except (TypeError, IndexError):
        cprint("Invalid plan input.")


def run() -> None:
    print(">>> Loading ocr model into memory...")
    from bot.ocr.ocr_reader import OCR_READER

    cprint("Model loaded.\n")

    kb_listener = pynput.keyboard.Listener(on_press=exit)
    kb_listener.start()

    print(INTRO)
    print(COMMANDS)
    while True:
        user_input = input("=>")
        if user_input.lower() == "intro":
            print(INTRO)
        elif user_input.lower() == "commands":
            print(COMMANDS)
        elif user_input.lower() == "plans":
            print("\n<All available plans>")
            for p in PLANS:
                print(p)
        elif user_input.lower() == "modes":
            print("Available modes: 'static', 'start'\n" "If you use 'start', you also provide hero level")
        elif user_input.lower() == "exit":
            return
        elif user_input.split()[0].lower() == "debug":
            with open(Path(__file__).parent / "DebugLogs.txt", "w") as logfile:
                logfile.write("")  # flush debug logs
            inputs = user_input.split()
            if len(inputs) == 3:
                run_plan(inputs[1], inputs[2].lower())
            elif len(inputs) == 4:
                run_plan(inputs[1], inputs[2].lower(), int(inputs[3]))
            elif len(inputs) == 5:
                run_plan(inputs[1], inputs[2].lower(), int(inputs[3]), int(inputs[4]))
        else:
            print("Unknown input")


# TODO
# dynamic pos -> in sandbox mode: change round, place any towers, change round to current+1, repeat
# static round state -> in 'edit challenge' page: user needs to first set total income, map, game mode and start round
#   Then after entering the map, run script and do all commands in a row until desired plan round N is reached. Now bot
#   is in a similar state it would be in normally at the end of round N-1. From here continue normally until plan is
#   finished.

if __name__ == "__main__":
    run()
