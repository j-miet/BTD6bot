"""Reads hotkeys.txt to update bot hotkeys.

Pynput docs: https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key
"""

from copy import deepcopy

from pynput.keyboard import Key, KeyCode

from bot import _maindata

PYNPUT_KEYS: dict[str, Key] = {
    "alt": Key.alt,
    "alt_l": Key.alt_l,
    "alt_r": Key.alt_r,
    "alt_gr": Key.alt_gr,
    "ctrl": Key.ctrl,
    "ctrl_l": Key.ctrl_l,
    "ctrl_r": Key.ctrl_r,
    "enter": Key.enter,
    "shift": Key.shift,
    "shift_l": Key.shift_l,
    "shift_r": Key.shift_r,
    "space": Key.space,
    "backspace": Key.backspace,
    "tab": Key.tab,
    "delete": Key.delete,
    "home": Key.home,
    "end": Key.end,
    "page_up": Key.page_up,
    "page_down": Key.page_down,
    "up": Key.up,
    "down": Key.down,
    "left": Key.left,
    "right": Key.right,
    "f1": Key.f1,
    "f2": Key.f2,
    "f3": Key.f3,
    "f4": Key.f4,
    "f5": Key.f5,
    "f6": Key.f6,
    "f7": Key.f7,
    "f8": Key.f8,
    "f9": Key.f9,
    "f10": Key.f10,
    "f11": Key.f11,
    "f12": Key.f12,
}
"""Dictionary of supported pynput special keys."""


def generate_hotkeys(hotkey_dict: dict[str, KeyCode | Key], source: dict[str, dict[str, str]]) -> None:
    """Reads hotkey.json file from 'Files' folder and writes formatted hotkey data into hotkey_dict dictionary.

    For pynput library to handle key presses, it needs convert 1. normal keys into 'KeyCode' type and 2.
    special/modifier keys into 'Key' type.

    This function runs every time a new monitoring window is created, updating any hotkey changes.
    """
    modifierKeys = PYNPUT_KEYS.keys()
    dict_copy = deepcopy(source)

    actual_hotkeys: dict[str, KeyCode | Key] = {}
    for name, fields in dict_copy.items():
        value: str = fields["value"]

        # - KeyCode types are stored as a string "N", Keys as text.
        # first check allows theoretical Mac users to enter modifier keys if they include "m_" prefix when manually
        # typing the hotkey e.g. "m_enter". Later else handles KeyCode types normally as long as number is correct.
        # However this feature is pretty much obsolete as BTD6bot has no official Mac support, but it can stay for now.
        if value in modifierKeys:
            actual_hotkeys.update({name: PYNPUT_KEYS[value]})
        else:
            keycode = KeyCode.from_vk(int(value))
            actual_hotkeys[name] = keycode

    hotkey_dict.update(actual_hotkeys)


hotkeys: dict[str, KeyCode | Key] = {}
"""Dictionary of current hotkeys read from hotkeys.txt."""
generate_hotkeys(hotkeys, _maindata.maindata["hotkeys"])
