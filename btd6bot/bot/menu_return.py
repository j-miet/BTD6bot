from __future__ import annotations
import time

from bot import _maindata, kb_mouse
from bot.bot_data import BotData
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
    """
    cprint('\nChecking if collection event screen appears...')
    start = time.time()
    while time.time()-start <= 5:
        if strong_delta_check('collect', get_text('menu', 'collection_collect'), OCR_READER):
            cprint('Clicking all insta pop-ups location...')
            kb_mouse.click(get_click('menu', 'collection_event'), 2)
            time.sleep(2)
            kb_mouse.click(get_click('menu', 'collection_two_left'))
            time.sleep(0.75)
            kb_mouse.click(get_click('menu', 'collection_two_left'))
            time.sleep(0.75)
            kb_mouse.click(get_click('menu', 'collection_two_right'))
            time.sleep(0.75)
            kb_mouse.click(get_click('menu', 'collection_two_right'))
            time.sleep(0.75)
            kb_mouse.click(get_click('menu', 'collection_three_left'))
            time.sleep(0.75)
            kb_mouse.click(get_click('menu', 'collection_three_left'))
            time.sleep(0.75)
            kb_mouse.click(get_click('menu', 'collection_three_middle'))
            time.sleep(0.75)
            kb_mouse.click(get_click('menu', 'collection_three_middle'))
            time.sleep(0.75)
            kb_mouse.click(get_click('menu', 'collection_three_right'))
            time.sleep(0.75)
            kb_mouse.click(get_click('menu', 'collection_three_right'))
            time.sleep(0.75)
            kb_mouse.click(get_click('menu', 'collection_continue'))
            time.sleep(2)
            kb_mouse.press_esc()
            cprint('Collection of event collectables handled.')
            return

def returned(victory: bool = True) -> None:
    """Verifies bot has returned to main menu and checks for collection event status."""
    _maindata.maindata["bot_vars"]["check_ingame_resolution"] = False
    if _maindata.maindata["toggle"]["event_status"]:
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