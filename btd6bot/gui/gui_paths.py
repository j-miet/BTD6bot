"""All necessary file and folder paths for GUI."""

from pathlib import Path

ROOT = Path(__file__).parent.parent
"""Location of the source root folder btd6bot. 
    Current implementation is build on string path values (= find path with pathlib, then cast it as str) because
    some gui functions need an easy access to image and plan name strings. For this it supports only Windows
    operating systems. Might rework this at some point.

    (Original implementation with os module) 
    '\\'.join(os.path.dirname(os.path.abspath(__file__)).split('\\'))"""
FILES_PATH = ROOT/'Files'
"""Location of all non-python files."""
MAP_IMAGES_PATH = FILES_PATH/'map images'
"""File path to map images."""
TEXT_FILES_PATH = FILES_PATH/'text files'
"""File path to gui text files. These store gui static data like Readme and also mutable data which 
    can be modified and saved through gui functions."""
QUEUE_LIST_PATH = TEXT_FILES_PATH/'queue_list.txt'
"""Path to currently saved plan queue data."""
HELP_PATH = TEXT_FILES_PATH/'help.txt'
"""Readme text path."""
HOTKEYS_PATH = TEXT_FILES_PATH/'hotkeys.txt'
"""Hotkeys data path."""
GUIHOTKEYS_PATH = TEXT_FILES_PATH/'guihotkeys.txt'
"""Gui hotkeys data path."""
HOTKEY_HELP_PATH = TEXT_FILES_PATH/'hotkeyhelp.txt'
"""Hotkey help text path."""
PLANS_PATH = ROOT/'plans'
"""All .py plan files."""