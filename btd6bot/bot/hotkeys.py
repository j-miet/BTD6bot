"""Reads hotkeys.txt to update hotkeys for monkey.py.

Pynput docs: https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key
"""

import pathlib

from pynput.keyboard import Key

from utils import plan_data

PYNPUT_KEYS: dict[str, Key] = {
        'Key.alt': Key.alt,  
        'Key.ctrl': Key.ctrl,  
        'Key.enter': Key.enter,
        'Key.shift': Key.shift,
        'Key.backspace': Key.backspace,
        'Key.tab': Key.tab,
        'Key.delete': Key.delete,
        'Key.home': Key.home,
        'Key.end': Key.end,
        'Key.page_up': Key.page_up,
        'Key.page_down': Key.page_down,
        'Key.up': Key.up,
        'Key.down': Key.down,
        'Key.left': Key.left,
        'Key.right': Key.right,    
        'Key.f1': Key.f1,
        'Key.f2': Key.f2,
        'Key.f3': Key.f3,
        'Key.f4': Key.f4,
        'Key.f5': Key.f5,
        'Key.f6': Key.f6,
        'Key.f7': Key.f7,
        'Key.f8': Key.f8,
        'Key.f9': Key.f9,
        'Key.f10': Key.f10,
        'Key.f11': Key.f11,
        'Key.f12': Key.f12
        }
"""Dictionary of supported pynput special keys."""

def generate_hotkeys(hotkey_dict: dict[str, str | Key]) -> None:
    """Reads hotkey.txt file from 'text files' folder and saves these to dictionary.

    Because this program uses pynput library to handle key presses, it needs to convert special/modifier keys
    to specific 'Key' type. 

    This function is run every time a new monitoring window is created, updating any hotkey changes.

    Returns:
        actual_hotkeys: Dictionary with keys as strings and values as string or Key type.
    """
    with open(pathlib.Path(__file__).parent.parent/'Files'/'text files'/'hotkeys.txt') as file_read: 
        hotkeys_text = plan_data.list_format(file_read.readlines())
    h_keys: list[str] = []
    h_values: list[str] = []
    for text_line in hotkeys_text:
        text_line_split = text_line.split('=')
        h_keys.append(text_line_split[0].rstrip())
        h_values.append(text_line_split[1].lstrip())
    hotkeys_dict: dict[str, str] = {k : h for (k, h) in zip(h_keys, h_values)}

    actual_hotkeys: dict[str, str | Key] = {}
    for key, val in hotkeys_dict.items():
        if val in PYNPUT_KEYS.keys():
            actual_hotkeys.update({key: PYNPUT_KEYS[val]})
        else:
            actual_hotkeys[key] = val
    hotkey_dict.update(actual_hotkeys)

hotkeys: dict[str, str | Key] = {}
"""Dictionary of current hotkeys read from a hotkeys.txt file."""
generate_hotkeys(hotkeys)