import json

from pynput.keyboard import Key, KeyCode

import gui.gui_paths as gui_paths
import bot.hotkeys as hotkeys


class GuiHotkeys:
    """Class for tracking gui hotkey values."""

    exit_hotkey: Key | KeyCode
    pause_hotkey: Key | KeyCode
    start_stop_hotkey: Key | KeyCode

    start_stop_status: bool = False
    pause_status: bool = False

    @staticmethod
    def update_guihotkeys() -> None:
        with open(gui_paths.GUIHOTKEYS_PATH) as gui_hotkeys:
            hks = json.load(gui_hotkeys)
            try:
                GuiHotkeys.exit_hotkey = hotkeys.PYNPUT_KEYS[hks["exit"]["display"]]
            except KeyError:
                GuiHotkeys.exit_hotkey = hks["exit"]["display"]
            try:
                GuiHotkeys.pause_hotkey = hotkeys.PYNPUT_KEYS[hks["pause"]["display"]]
            except KeyError:
                GuiHotkeys.pause_hotkey = hks["pause"]["display"]
            try:
                GuiHotkeys.start_stop_hotkey = hotkeys.PYNPUT_KEYS[hks["start-stop"]["display"]]
            except KeyError:
                GuiHotkeys.start_stop_hotkey = hks["start-stop"]["display"]
