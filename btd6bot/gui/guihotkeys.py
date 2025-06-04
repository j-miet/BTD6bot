from pynput.keyboard import Key

import gui.gui_paths as gui_paths
import bot.hotkeys as hotkeys

class GuiHotkeys():
    """Class for handling gui hotkeys."""
    exit_hotkey: Key | str
    pause_hotkey: Key | str
    start_stop_hotkey: Key | str

    start_stop_status = 0
    pause_status = 0

    @staticmethod
    def update_guihotkeys() -> None:
        with open(gui_paths.GUIHOTKEYS_PATH) as gui_hotkeys:
            try:
                GuiHotkeys.exit_hotkey = hotkeys.PYNPUT_KEYS[gui_hotkeys.readlines()[2].split('= ')[1].strip()]
            except IndexError:
                GuiHotkeys.exit_hotkey = gui_hotkeys.readlines()[2].split('= ')[2].strip()

        with open(gui_paths.GUIHOTKEYS_PATH) as gui_hotkeys:
            hotkey_vals = gui_hotkeys.readlines()
            try:
                GuiHotkeys.pause_hotkey = hotkeys.PYNPUT_KEYS[hotkey_vals[0].split('= ')[1].strip()]
            except KeyError:
                GuiHotkeys.pause_hotkey = hotkey_vals[0].split('= ')[1].strip()
            try:
                GuiHotkeys.start_stop_hotkey = hotkeys.PYNPUT_KEYS[hotkey_vals[1].split('= ')[1].strip()]
            except KeyError:
                GuiHotkeys.start_stop_hotkey = hotkey_vals[1].split('= ')[1].strip()