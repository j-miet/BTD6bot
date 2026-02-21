"""Simulation of keyboard and mouse controls."""

from __future__ import annotations
import sys
import time

import pyautogui
import pynput
from pynput.keyboard import Key, KeyCode, Controller

from bot import _maindata
from customprint import cprint

# pyautogui.FAILSAFE controls build-in pyautogui fail-safe of dragging mouse to a corner of the screen, shutting down 
# the program. This is set to "False" as there's already a custom hotkey (or Ctrl+C) for quick termination.
# However for Mac systems gui hotkeys are disabled so Ctrl+C and mouse dragging become only ways to halt bot
if sys.platform == 'darwin':
    pyautogui.FAILSAFE = True
else:
    if sys.platform == 'win32':
        import win32gui
    pyautogui.FAILSAFE = False

class ScreenRes:
    """ScreenRes class for tracking current screen resolution.
    
    Base value is monitor's resolution.

    Attributes:
        BASE_RES (int, class attribute): Base/native resolution.
    """
    BASE_RES: tuple[int, int] = pyautogui.size()
    _controller: pynput.keyboard.Controller = Controller()
    _width, _height = pyautogui.size()
    _win_w, _win_h = 0, 0
    _winpos_status = "centered"
    _w_shift, _h_shift = 0, 0

    if sys.platform == 'win32':
        _phandle: int = win32gui.FindWindow(None, "BloonsTD6")

    @staticmethod
    def update_res(w: int, h: int) -> None:
        """Updates screen resolution."""
        ScreenRes._width = w
        ScreenRes._height = h

    @staticmethod
    def update_winpos(w: int, h: int) -> None:
        """Updates windowed top-left coordinate position."""
        ScreenRes._win_w = w
        ScreenRes._win_h = h

    @staticmethod
    def get_winpos() -> tuple[int, int]:
        """Returns game window location in pixel coordinates."""
        return ScreenRes._win_w, ScreenRes._win_h

    @staticmethod
    def update_winpos_status(status: str) -> None:
        """Update winpos status.
        
        Status defines which windowed mode bot uses: 'auto', 'centered' or 'custom' for custom coordinate value.
        """
        ScreenRes._winpos_status = status

    @staticmethod
    def get_winpos_status() -> str:
        """Returns winpos status."""
        return ScreenRes._winpos_status

    @staticmethod
    def update_shift(w_pixels: int, h_pixels: int) -> None:
        """Updates pixel shift values."""
        ScreenRes._w_shift = w_pixels
        ScreenRes._h_shift = h_pixels

    @staticmethod
    def get_shift() -> tuple[int, int]:
        return ScreenRes._w_shift, ScreenRes._h_shift

    @staticmethod
    def set_baseres() -> None:
        ScreenRes._width, ScreenRes._height = ScreenRes.BASE_RES

def pixel_position(xy: tuple[float | None, float | None], 
                   ignore_windowed: bool = False, 
                   shifted: bool = False
                   ) -> tuple[int, int]:
    """Reverts coordinate scalars back to pixel coordinates of user's display resolution.

    Args:
        xy: Scalar coordinates as a tuple.
        ignore_windowed: Ignores windowed mode coordinate scaling. Default is False. Currently only use case for True is
            to click map search bar top left if ultrawide resolution is used.
        shifted: Whether coordinate shifting is applied when ingame_res_enabled is set to True.
        
    Returns:
        Pixel coordinates as a tuple. If scalar coordinates get other than int or float values, return (-1, -1).
    """
    if (isinstance(xy[0], float) or isinstance(xy[0], int)) and (isinstance(xy[1], float) or isinstance(xy[1], int)):
        x: int
        y: int
        if ignore_windowed:
            x, y = round(ScreenRes.BASE_RES[0]*xy[0]), round(ScreenRes.BASE_RES[1]*xy[1])
        elif _maindata.maindata["bot_vars"]["windowed"]:
            if ScreenRes.get_winpos_status() == 'auto' and sys.platform == 'win32':
                # if OS is Windows bot can automatically get window location
                winrect = win32gui.GetWindowRect(ScreenRes._phandle)
                ScreenRes.update_winpos(winrect[0], winrect[1])
            if (ScreenRes.get_winpos_status() in ('custom', 'auto') and 
                not (_maindata.maindata["bot_vars"]["check_ingame_resolution"] and shifted)):
                x = round(ScreenRes._win_w + ScreenRes._width*xy[0])
                y = round(ScreenRes._win_h + ScreenRes._height*xy[1])
            elif (ScreenRes.get_winpos_status() in ('custom', 'auto') and 
                _maindata.maindata["bot_vars"]["check_ingame_resolution"] and shifted):
                x = round(ScreenRes._win_w + ScreenRes._w_shift + (ScreenRes._width-2*ScreenRes._w_shift)*xy[0])
                y = round(ScreenRes._win_h + ScreenRes._h_shift + (ScreenRes._height-2*ScreenRes._h_shift)*xy[1])
            elif (ScreenRes.get_winpos_status() == 'centered' and 
                  _maindata.maindata["bot_vars"]["check_ingame_resolution"] 
                  and shifted):
                x = round((ScreenRes.BASE_RES[0]-ScreenRes._width)/2 + ScreenRes._w_shift +
                            (ScreenRes._width-2*ScreenRes._w_shift)*xy[0])
                y = round((ScreenRes.BASE_RES[1]-ScreenRes._height)/2 + ScreenRes._h_shift +
                            (ScreenRes._height-2*ScreenRes._h_shift)*xy[1])
            else: # window position centered and coordinates not shifted
                x = round((ScreenRes.BASE_RES[0] - ScreenRes._width)/2 + ScreenRes._width*xy[0])
                y = round((ScreenRes.BASE_RES[1] - ScreenRes._height)/2 + ScreenRes._height*xy[1])
        else:
            if _maindata.maindata["bot_vars"]["check_ingame_resolution"] and shifted:
                x = round((ScreenRes._width-2*ScreenRes._w_shift)*xy[0] + ScreenRes._w_shift)
                y = round((ScreenRes._height-2*ScreenRes._h_shift)*xy[1] + ScreenRes._h_shift)
            else:
                x, y = round(ScreenRes._width*xy[0]), round(ScreenRes._height*xy[1])
        return x, y
    cprint('Error with converting scalars to pixels.')
    return -1, -1

def click(pos: tuple[float | None, float | None], 
          clicks: int = 1, 
          ignore_windowed: bool = False, 
          shifted: bool = False
          ) -> None:
    """Left-clicks mouse at a desired coordinate. Converts scalar coordinates to pixel coordinates to find position.

    Args:
        pos: Mouse position, in scalar coordinates.
        clicks: Amount of clicks performed. Default value is 1.
        ignore_windowed: Ignores windowed mode coordinate scaling. Default is False. Currently only use case for True is
            to click map search bar top left if ultrawide resolution is used.
        shifted: When in-game coordinate shifting is used, apply it to current click. Only non-menu commands should 
        primarly use this i.e. those under commands interface.
    """
    if isinstance(clicks, int) and clicks >= 1:
        for _ in range(clicks):
            time.sleep(0.1)
            old_X, old_Y = pyautogui.position()
            new_X, new_Y = pixel_position((pos[0], pos[1]), ignore_windowed, shifted)
            pyautogui.moveTo(new_X, new_Y)
            pyautogui.click(new_X, new_Y)
            pyautogui.moveTo(old_X, old_Y)

def move_cursor(xy: tuple[float, float], set_duration: float = 0.0, shifted: bool = True) -> None:
    """Moves mouse to specified coordinate location.
    
    Args:
        xy: Scalar coordinate tuple of location coordinates.
        set_duration: How long it takes to drag mouse to target position. Default is 0 to move instantly.
            If value is 1 for example, dragging speed is automatically scaled to take 1 second.
        shifted: Apply in-game coordinate shift. Default is True as this function is only used in in-game environment.
    """
    x, y = pixel_position((xy[0], xy[1]), shifted)
    pyautogui.moveTo(x, y, duration=set_duration)
    time.sleep(0.1)

def kb_input(input: Key | KeyCode | str, 
             times: int = 1, 
             kb_controller: pynput.keyboard.Controller = ScreenRes._controller) -> None:
    """Simulates pressing a single keyboard input by default.

    If same key must be pressed multiple times, change 'times' value.

    Args:
        input: Key that needs to be pressed.
        times: How many times key is pressed. Default value is 1.
        kb_controller: pynput keyboard controller object.
    """
    if isinstance(times, int) and times >= 1:
        if isinstance(input, str) and input.strip("<>") in {f"{num}" for num in range(96, 106)}: # numpad keys
            input_key = int(input.strip("<>"))
            for _ in range(times):
                kb_controller.press(KeyCode(input_key)) # type: ignore[arg-type]
                time.sleep(0.1)
                kb_controller.release(KeyCode(input_key)) # type: ignore[arg-type]
                if times >= 2:
                    time.sleep(0.1)
        else:
            for _ in range(times):
                kb_controller.press(input)
                time.sleep(0.1)
                kb_controller.release(input)
                if times >= 2:
                    time.sleep(0.1)

def press_esc() -> None:
    """Simulates Esc key press."""
    kb_input(Key.esc)
    time.sleep(0.1)