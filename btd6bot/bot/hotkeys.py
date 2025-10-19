"""Reads hotkeys.txt to update bot hotkeys.

Pynput docs: https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key
"""

import pathlib

from pynput.keyboard import Key

from utils import plan_data

PYNPUT_KEYS: dict[str, Key] = {
    'alt': Key.alt,
    'alt_l': Key.alt_l,
    'alt_r': Key.alt_r,
    'alt_gr': Key.alt_gr,
    'ctrl': Key.ctrl,
    'ctrl_l': Key.ctrl_l,
    'ctrl_r': Key.ctrl_r,
    'enter': Key.enter,
    'shift': Key.shift,
    'shift_l': Key.shift_l,
    'shift_r': Key.shift_r,
    'space': Key.space,
    'backspace': Key.backspace,
    'tab': Key.tab,
    'delete': Key.delete,
    'home': Key.home,
    'end': Key.end,
    'page_up': Key.page_up,
    'page_down': Key.page_down,
    'up': Key.up,
    'down': Key.down,
    'left': Key.left,
    'right': Key.right,    
    'f1': Key.f1,
    'f2': Key.f2,
    'f3': Key.f3,
    'f4': Key.f4,
    'f5': Key.f5,
    'f6': Key.f6,
    'f7': Key.f7,
    'f8': Key.f8,
    'f9': Key.f9,
    'f10': Key.f10,
    'f11': Key.f11,
    'f12': Key.f12
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
    hotkeys_dict: dict[str, str] = {k : h for (k, h) in zip(h_keys, h_values, strict=True)}

    actual_hotkeys: dict[str, str | Key] = {}
    for key, val in hotkeys_dict.items():
        if val in PYNPUT_KEYS.keys():
            actual_hotkeys.update({key: PYNPUT_KEYS[val]})
        else:
            actual_hotkeys[key] = val
    hotkey_dict.update(actual_hotkeys)

hotkeys: dict[str, str | Key] = {}
"""Dictionary of current hotkeys read from hotkeys.txt."""
generate_hotkeys(hotkeys)