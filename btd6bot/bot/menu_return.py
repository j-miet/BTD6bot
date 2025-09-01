from __future__ import annotations
import time

from bot import kb_mouse
from bot.bot_data import BotData
from bot.bot_vars import BotVars
from bot.ocr.ocr import weak_substring_check, strong_delta_check
from bot.ocr.ocr_reader import OCR_READER
from bot.locations import get_click, get_text
from customprint import cprint

def collection_event_handler() -> None:
    """Checks if collectables window open after a game finishes and collects them.
    
    Instant monkeys are collected by clicking every possible location they can appear at. Each location is clicked 
    twice, as clicking icon will show the insta you got, which then needs to be clicked again to go away. A small 
    time window is added between click to allow collections to register.
    
    If no collection event window pops up, does nothing.

    current event status is read from BotVars.current_event_status.
    """
    cprint('\nChecking if collection event screen appears...')
    start = time.time()
    while time.time()-start <= 5:
        if strong_delta_check('collect', get_text('menu', 'collection_collect'), OCR_READER):
            cprint('Clicking all insta pop-ups location...')
            kb_mouse.click(get_click('menu', 'collection_event'), 2)
            time.sleep(3)
            kb_mouse.click(get_click('menu', 'collection_two_left'), 2)
            time.sleep(1)
            kb_mouse.click(get_click('menu', 'collection_two_right'), 2)
            time.sleep(1)
            kb_mouse.click(get_click('menu', 'collection_three_left'), 2)
            time.sleep(1)
            kb_mouse.click(get_click('menu', 'collection_three_middle'), 2)
            time.sleep(1)
            kb_mouse.click(get_click('menu', 'collection_three_right'), 2)
            time.sleep(1)
            kb_mouse.click(get_click('menu', 'collection_continue'))
            time.sleep(3)
            kb_mouse.press_esc()
            cprint('Collection of event collectables handled.')
            return

def returned(victory: bool = True) -> None:
    """Verifies bot has returned to main menu and checks for collection event status."""
    BotVars.ingame_res_enabled = False
    if BotVars.current_event_status == 'On':
        collection_event_handler()
    loop: bool = True
    while loop:
        for letter in ('p','l','a','y'):
            if not weak_substring_check(letter, get_text('menu', 'menu_playtext'), OCR_READER):
                time.sleep(0.3)
            else:
                loop = False
                break
    if victory:
        BotData.victory = True
    else:
        BotData.victory = False