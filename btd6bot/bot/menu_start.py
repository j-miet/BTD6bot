"""Functions that handle in-game menu navigation before and after each game.

Menu navigation is done with simulating mouse inputs on predetermined locations.
Initial start condition is to search for main menu 'Play' button using ocr.

Handles a chunk of constant values: these are wrapped under separate classes to avoid polluting module 
namespace.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import json
import pathlib
import sys
import time

import pyautogui

from bot import kb_mouse, locations
from bot.commands.flow import AutoStart
from bot.commands.hero import Hero
from bot.commands.monkey import Monkey
from bot.bot_vars import BotVars
import bot.hotkeys
from bot.kb_mouse import ScreenRes
from bot.locations import get_click, get_text, get_locationdict
from bot.ocr.ocr import OcrValues
from bot.ocr.ocr import weak_substring_check
from bot.ocr.ocr_reader import OCR_READER
from bot.rounds import Rounds
from bot.times import PauseControl
from customprint import cprint

if TYPE_CHECKING:
    from typing import Any
if sys.platform == 'win32':
    import win32gui


def _scroll_down_heroes() -> None:
    """Scrolls down hero screen allowing access to more heroes."""
    pyautogui.moveTo(kb_mouse.pixel_position(get_click('menu', 'heroscreen_scroll')))
    for _ in range(0,4):
        pyautogui.scroll(clicks=-1000)
        time.sleep(0.1)

def _choose_hero(hero_name: str | None) -> bool:
    """In menu screen, chooses the correct hero.

    Can also choose set None so hero won't change - useful in modes like deflation where hero might not be necessary.

    Updates current hero name for Hero class.

    Args:
        hero_name: Lower/uppercase doesn't matter, only that name is spelled correctly.

    Returns:
        If hero selection could be verified (even if None) return True; otherwise hero selection screen couldn't be
        processed and returns False.
    """
    hero_dict: dict[str, Any] = get_locationdict()['CLICK']
    all_heroes = (tuple(hero_dict['heroes'].keys()),
                  tuple(hero_dict['heroes2'].keys()))
    if hero_name is None or hero_name.lower() not in set().union(*all_heroes):
        cprint('No hero used in current plan')
        Hero.current_plan_hero_name = hero_name
        return True
    else:
        cprint("Selecting", hero_name.capitalize(), "as hero... ", end='')
        kb_mouse.click(get_click('menu', 'hero_window'))
        start: float = time.time()
        loop: bool = True
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
        if hero_name.lower() in hero_dict['heroes']:
            kb_mouse.click(get_click('heroes', hero_name.lower()))
            Hero.current_plan_hero_name = hero_name
        elif hero_name.lower() in hero_dict['heroes2']:
            _scroll_down_heroes()
            kb_mouse.click(get_click('heroes2', hero_name.lower()))
            Hero.current_plan_hero_name = hero_name
    time.sleep(0.3)
    kb_mouse.click(get_click('menu', 'hero_select'))
    time.sleep(0.3)
    kb_mouse.press_esc()
    cprint("Hero selected!")
    return True

def _choose_map(map_name: str) -> bool:
    """Chooses correct map by first clicking the map search bar and then typing the map name.
    
    Args:
        map_name: Map name.

    Returns:
        A boolean indicating if map selection was successful. If False value is returned, it allows for bot to return
            to main menu screen.
    """
    start: float = time.time()
    loop: bool = True
    while loop:
        for letter in ('p','l','a','y'):
            if not weak_substring_check(letter, get_text('menu', 'menu_playtext'), OCR_READER):
                if time.time()-start >= 10:
                    return False
                time.sleep(0.3)
            else:
                loop = False
                break
    time.sleep(0.5)
    map_str = map_name.replace('_', ' ')
    kb_mouse.click(get_click('menu', 'menu_play'))
    start = time.time()
    search_found = 0
    time.sleep(0.4)
    kb_mouse.click(get_click('menu', 'search_map'))
    if BotVars.windowed:
        loop = True
        while time.time()-start <= 5 and loop:
            for letter in ('s','e','a','r','c','h'):
                if weak_substring_check(letter, 
                                        get_text('menu', 'map_searchtext'),
                                        OCR_READER):
                    search_found = 1
                    loop = False
                    break
                else:
                    time.sleep(0.3)
        if not search_found:
            search_found = 0
            kb_mouse.click(get_click('menu', 'search_map'), ignore_windowed=True)
            start = time.time()
            while time.time()-start <= 5 and loop:
                for letter in ('s','e','a','r','c','h'):
                    if weak_substring_check(letter, 
                                            get_text('menu', 'map_searchtext'), 
                                            OCR_READER):
                        search_found = 1
                        loop = False
                        break
                    else:
                        time.sleep(0.3)
            if not search_found:
                return False        
    time.sleep(0.4)
    kb_mouse.click(get_click('menu', 'search_map_bar'))
    time.sleep(0.4)
    pyautogui.write(map_str) # types map name to search bar.
    kb_mouse.click(get_click('menu', 'choose_map'))
    return True

def _choose_diff(d: str) -> None:
    """Chooses correct difficulty setting.

    Difficulties are written all capitalized.

    Args:
        d: Difficulty.
    """
    kb_mouse.click(get_click('difficulty', d))

def _choose_mode(m: str) -> None:
    """Chooses correct game mode.

    Modes are written all capitalized.

    Args:
        m: Game mode.
    """
    if m == 'STANDARD':
        kb_mouse.click(get_click('modes', 'standard'))
    elif m in {'PRIMARY', 'MILITARY', 'MAGIC'}:
        kb_mouse.click(get_click('modes', 'top_left'))
    elif m in {'DEFLATION', 'APOPALYPSE', 'DOUBLE_HP'}:
        kb_mouse.click(get_click('modes', 'top_middle'))
    elif m == 'HALF_CASH':
        kb_mouse.click(get_click('modes', 'top_right'))
    elif m in {'REVERSE', 'ALTERNATE'}:
        kb_mouse.click(get_click('modes', 'bottom_left'))
    elif m == 'IMPOPPABLE':
        kb_mouse.click(get_click('modes', 'bottom_middle'))
    elif m == 'CHIMPS':                                          
        kb_mouse.click(get_click('modes', 'bottom_right'))
    kb_mouse.click(get_click('menu', 'save_overwrite'))  # if a previous save exists, overwrite it.

def _reset_global_targeting() -> None:
    Monkey._wingmonkey = False
    Monkey._elite_sniper = False

def _update_external_variables(begin_r: int, end_r: int) -> None:
    """Initializes all external class-level variables used within bot package.
    
    This function should only be called by 'load'.

    Args:
        begin_r: First round.
        end_r: Final round.
    """
    BotVars.ingame_res_enabled = False
    ScreenRes.update_shift(0, 0)
    ScreenRes.update_winpos(-1, -1)
    OcrValues._log_ocr_deltas = False
    bot.hotkeys.generate_hotkeys(bot.hotkeys.hotkeys)
    Rounds.begin_round, Rounds.end_round = begin_r, end_r
    BotVars.defeat_status = False
    Rounds.exit_type = 'defeat'
    AutoStart.called_forward = False
    PauseControl.pause_length = 0
    BotVars.paused = False 
    _reset_global_targeting()
    try:
        with open(pathlib.Path(__file__).parent.parent/'Files'/'gui_vars.json') as f:
            gui_vars_dict: dict[str, Any] = json.load(f)
    except json.decoder.JSONDecodeError:
        cprint('gui_vars.json not found or cannot be read. Defaulting to bot_vars default values.')
        return
    try:
        customres_val: bool = gui_vars_dict["check_resolution"]
        if customres_val:
            resolution_val: tuple[int, ...] = tuple(map(int, gui_vars_dict["custom_resolution"].split('x')))
            ScreenRes.update_res(resolution_val[0], resolution_val[1])
        else:
            ScreenRes.update_res(ScreenRes.BASE_RES[0], ScreenRes.BASE_RES[1])
        
        ingameres_val: bool = gui_vars_dict["check_ingame_resolution"]
        if ingameres_val:
            ingame_shift_val: tuple[int, ...] = tuple(map(int, gui_vars_dict["ingame_res_shift"].split('x')))
            ScreenRes.update_shift(ingame_shift_val[0], ingame_shift_val[1])
            locations.update_customlocations()
            cprint("#Custom location values loaded.")  
        
        windowed_val: bool = gui_vars_dict["windowed"]
        if windowed_val:
            winpos_val: str = gui_vars_dict["windowed_position"]
            if winpos_val == 'auto' and sys.platform == 'win32':
                ScreenRes.update_winpos(-2, -2)
                winrect = win32gui.GetWindowRect(ScreenRes._phandle)
                ScreenRes.update_res(winrect[2]-winrect[0], winrect[3]-winrect[1]) # auto-update window res
            elif winpos_val == 'centered':
                # ScreenRes.update_winpos(-1, -1) is already called earlier
                ...
            else:
                winpos: tuple[int, ...] = tuple(map(int, gui_vars_dict["windowed_position"].split('x')))
                ScreenRes.update_winpos(winpos[0], winpos[1])

        time_limit_val: int = gui_vars_dict["checking_time_limit"]
        frequency_val: float = gui_vars_dict["ocr_frequency"]
        verify_limit: int = gui_vars_dict["upg_verify_limit"]
        deltaocr_val: bool = gui_vars_dict["delta_ocrtext"]
        substringocr_val: bool = gui_vars_dict["substring_ocrtext"]
        BotVars.windowed = windowed_val
        BotVars.checking_time_limit = time_limit_val
        BotVars.upg_verify_limit = verify_limit
        BotVars.print_delta_ocrtext = deltaocr_val
        BotVars.print_substring_ocrtext = substringocr_val
        OcrValues.read_file_frequency = frequency_val
    except ValueError:
        cprint("Unable to read at least one of the gui_vars.json keys. Defaulting to bot_vars initial values.")

def _start_plan() -> None:
    """Resets counter if mouse moves during it."""
    cprint('Starting plan in...', end=' ')
    timer = 3
    x, y = pyautogui.position()
    while timer > 0:
        for i in range(3, 0, -1):
            if (x, y) != tuple(pyautogui.position()):
                cprint("\nMouse moved, reseting timer!")
                cprint('Starting plan in...', end=' ')
                time.sleep(0.1)
                timer = 3
                x, y = pyautogui.position()
                break
            cprint(i, end=' ', flush=True)
            time.sleep(1)
            timer -= 1
    cprint()
    cprint('--> *Bot running*')
            
def load(map_name: str, 
         diff: str, 
         mode: str, 
         begin_round: int, 
         end_round: int, 
         hero: str, 
         farm: bool = False
         ) -> tuple[int, int]:
    """Sets up pre-game conditions for the plan by choosing correct hero, map, difficulty and game mode.

    Updates begin and end rounds for bot.rounds.

    Args:
        map_name: Map name.
        diff: Difficulty setting.
        mode: Game mode.
        begin_round: First round of selected game mode.
        end_round: Final round of selected game mode.
        hero: Hero name.
        farm: ...

    Returns:
        Begin and end rounds.
    """
    _update_external_variables(begin_round, end_round)
    loop: bool = True
    if not farm:
        cprint('Searching for main menu screen...')
        while loop:
            for letter in ('p','l','a','y'):
                if not weak_substring_check(letter, get_text('menu', 'menu_playtext'), OCR_READER):
                    time.sleep(0.3)
                else:
                    loop = False
                    break
        _start_plan()
        if not _choose_hero(hero):
            return 0, 0
        if not _choose_map(map_name):
            return 0, 0
    _choose_diff(diff)
    _choose_mode(mode)
    return begin_round, end_round