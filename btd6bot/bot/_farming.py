"""Collection event farming"""

from __future__ import annotations
import time

from bot import kb_mouse
from bot.commands.hero import Hero
from bot.locations import get_click, get_text
from bot.ocr.ocr import weak_substring_check, strong_delta_check
from bot.ocr.ocr_reader import OCR_READER
from customprint import cprint

def select_rewardmap() -> str:
    """Selects map with bonus rewards."""
    loop: bool = True
    cprint('Searching for main menu screen...')
    while loop:
        for letter in ('p','l','a','y'):
            if not weak_substring_check(letter, get_text('menu', 'menu_playtext'), OCR_READER):
                time.sleep(0.3)
            else:
                loop = False
                break
    time.sleep(0.4)
    kb_mouse.click(get_click('menu', 'menu_play'))
    time.sleep(0.4)
    kb_mouse.click(get_click('menu', 'search_map'))
    time.sleep(0.4)
    kb_mouse.click(get_click('menu', 'collection_bonusrewards'))
    time.sleep(0.5)
    cprint('Selecting map with bonus rewards...')
    for mapname in ('glacial trail', 
                    'dark dungeons', 
                    'sanctuary', 
                    'ravine', 
                    'flooded valley', 
                    'infernal',
                    'bloody puddles', 
                    'workshop', 
                    'quad', 
                    'dark castle', 
                    'muddy puddles', 
                    '#ouch'):
        if not strong_delta_check(mapname, get_text('menu', 'map_namebotleft'), OCR_READER):
            time.sleep(0.3)
        else:
            cprint(f"Next map is <{mapname}>.")
            return mapname
    kb_mouse.press_esc()
    time.sleep(0.5)
    return ''

def click_rewardmap() -> None:
    """Click bottom-left location to select map with bonus rewards."""
    kb_mouse.click(get_click('menu', 'choose_map_bl'))
    time.sleep(0.3)

def select_defaulthero(hero_name: str = 'sauda') -> None:
    """Select default hero for event farming."""
    cprint('Searching menu screen...')
    loop: bool = True
    while loop:
        for letter in ('p','l','a','y'):
            if not weak_substring_check(letter, get_text('menu', 'menu_playtext'), OCR_READER):
                time.sleep(0.3)
            else:
                loop = False
                break
    cprint(f"Selecting default hero {hero_name.capitalize()}")
    kb_mouse.click(get_click('menu', 'hero_window'))
    start: float = time.time()
    loop = True
    while loop:
        for letter in ('s','e','l','e','c','t','e','d'):
            if not weak_substring_check(letter, (0.5296875, 0.5472222222222, 0.6338541666667, 0.5916666666667),
                                    OCR_READER):
                if time.time()-start >= 10:
                    return False
                time.sleep(0.3)
            else:
                loop = False
                break
    kb_mouse.click(get_click('heroes', hero_name.lower()))
    Hero.current_plan_hero_name = hero_name
    time.sleep(0.3)
    kb_mouse.click(get_click('menu', 'hero_select'))
    time.sleep(0.3)
    kb_mouse.press_esc()
    cprint("Hero selected.")