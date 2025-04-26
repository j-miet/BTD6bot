"""Testing if bot.commands works (excluding flow.py) via doctests.

Files with doctests included: monkey.py, hero.py, ability.py

Open btd6 menu screen and wait until tests finish.
"""

import time

from bot import kb_mouse
from bot.bot_vars import BotVars
from bot.commands.ability import ability
from bot.commands.hero import Hero
from bot.commands.monkey import Monkey
from bot.menu_start import _choose_map, _choose_diff
from bot.menu_start import OcrLocations, MouseLocations
from bot.ocr.ocr import weak_substring_check
from bot.ocr.ocr_reader import OCR_READER
from bot.rounds import Rounds

def commands_doctest() -> None:
    timer = time.time()
    while not weak_substring_check('Play', OcrLocations.MENU_PLAYTEXT, OCR_READER):
        if time.time()-timer >= 10:
            return
        print("Searching for main menu screen...")
        time.sleep(1)

    _choose_map('monkey meadow')
    _choose_diff('EASY')
    kb_mouse.click(MouseLocations.MODES['bottom_left'])

    BotVars.checking_time_limit = 10
    while not weak_substring_check('Upgrades', Rounds.UPGRADE_TEXT, OCR_READER):
        print("Waiting map screen...")
        kb_mouse.click((0.5036458333333, 0.7064814814815))
        time.sleep(1)
    print("Map screen found, starting upgrade tests.\nStarting tests - Don't touch keyboard or mouse during tests.")
    for t in range(5, 0, -1):
        print(str(t), end=' ', flush=True)
        time.sleep(1)
    print()

    import doctest
    doctest.run_docstring_examples(Monkey, globals()); print('Monkey checked')
    doctest.run_docstring_examples(Monkey.upgrade, globals()); print('Monkey.upgrade checked')
    doctest.run_docstring_examples(Monkey.target, globals()); print('Monkey.target checked')
    doctest.run_docstring_examples(Monkey.special, globals()); print('Monkey.special checked')
    doctest.run_docstring_examples(Monkey.sell, globals()); print('Monkey.sell checked')
    doctest.run_docstring_examples(Hero, globals()); print('Hero checked')
    doctest.run_docstring_examples(Hero.target, globals()); print('Hero.target checked')
    doctest.run_docstring_examples(ability, globals()); print('ability checked')
    
    time.sleep(1)
    kb_mouse.press_esc()
    time.sleep(1)
    kb_mouse.click((0.4458333333333, 0.7814814814815))
    print('Doctests finished.')

if __name__ == '__main__':
    commands_doctest()