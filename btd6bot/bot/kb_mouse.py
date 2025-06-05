"""Simulation of keyboard and mouse controls."""

from __future__ import annotations
import time

import pyautogui
import pynput
from pynput.keyboard import Key, KeyCode

from bot.bot_vars import BotVars
from customprint import cprint

pyautogui.FAILSAFE = False
# pyautogui.FAILSAFE controls build-in pyautogui fail-safe of dragging mouse to a corner of the screen, shutting down 
# the program. This is set to "False" as there's already a custom hotkey (or Ctrl+C) for quick termination.

class ScreenRes:
    """ScreenRes class for tracking current screen resolution.
    
    Base value is monitor's resolution.

    Attributes:
        BASE_RES (int, class attribute): Base/native resolution.
        width (int, class attribute): Screen width. 
        height (int, class attribute): Screen height.
    """
    controller: pynput.keyboard.Controller = pynput.keyboard.Controller()
    BASE_RES: tuple[int, int] = pyautogui.size()
    width, height = pyautogui.size()

    @staticmethod
    def update_res(w: int, h: int) -> None:
        """Updates screen resolution."""
        ScreenRes.width = w
        ScreenRes.height = h

    @staticmethod
    def set_baseres() -> None:
        ScreenRes.width, ScreenRes.height = ScreenRes.BASE_RES


def pixel_position(xy: tuple[float | None, float | None], ignore_windowed: bool = False) -> tuple[int, int]:
    """Reverts coordinate scalars back to pixel coordinates of user's display resolution.

    Args:
        xy: Scalar coordinates as a tuple.
        ignore_windowed: Ignores windowed mode coordinate scaling. Default is False. Currently only use case for True is
            to click map search bar top left if ultrawide resolution is used.
        
    Returns:
        Pixel coordinates as a tuple. If scalar coordinates are not floats, return (-1, -1).
    """
    if (isinstance(xy[0], float) or isinstance(xy[0], int)) and (isinstance(xy[1], float) or isinstance(xy[1], int)):
        x: int
        y: int
        if ignore_windowed:
            x, y = round(ScreenRes.BASE_RES[0]*xy[0]), round(ScreenRes.BASE_RES[1]*xy[1])
        elif BotVars.windowed:
            x = round(ScreenRes.width*xy[0] + (ScreenRes.BASE_RES[0] - ScreenRes.width)/2)
            y = round(ScreenRes.height*xy[1] + (ScreenRes.BASE_RES[1] - ScreenRes.height)/2)
        else:
            x, y = round(ScreenRes.width*xy[0]), round(ScreenRes.height*xy[1])
        return x, y
    cprint('Error with converting scalars to pixels.')
    return -1, -1   # this was added to satisfy mypy type hints.

def click(pos: tuple[float | None, float | None], clicks: int=1, ignore_windowed: bool = False) -> None:
    """Left-clicks mouse at a desired coordinate. Converts scalar coordinates to pixel coordinates to find position.

    Args:
        pos: Mouse position, in scalar coordinates.
        clicks: Amount of clicks performed. Default value is 1.
        ignore_windowed: Ignores windowed mode coordinate scaling. Default is False. Currently only use case for True is
            to click map search bar top left if ultrawide resolution is used.
    """
    if isinstance(clicks, int) and clicks >= 1:
        for _ in range(clicks):
            time.sleep(0.1)
            old_X, old_Y = pyautogui.position()
            new_X, new_Y = pixel_position((pos[0], pos[1]), ignore_windowed)
            pyautogui.moveTo(new_X, new_Y)
            pyautogui.click(new_X, new_Y)
            pyautogui.moveTo(old_X, old_Y)

def move_cursor(xy: tuple[float, float], set_duration: float = 0.0) -> None:
    """Moves mouse to specified coordinate location.
    
    Args:
        xy: Scalar coordinate tuple of location coordinates.
        set_duration: How long it takes to drag mouse to target position. Default is 0 to move instantly.
            If value is 1 for example, dragging speed is automatically scaled to take 1 second.
    """
    x, y = pixel_position((xy[0], xy[1]))
    pyautogui.moveTo(x, y, duration=set_duration)
    time.sleep(0.1)

def kb_input(input: Key | KeyCode | str, 
             times: int = 1, 
             controller: pynput.keyboard.Controller = ScreenRes.controller) -> None:
    """Simulates pressing a single keyboard input by default.

    If same key must be pressed multiple times, change 'times' value.

    Args:
        input: Key that needs to be pressed.
        times: How many times key is pressed. Default value is 1.
    """
    if isinstance(times, int) and times >= 1:
        keyboard = controller
        if isinstance(input, str) and input.strip("<>") in {f"{num}" for num in range(96, 106)}: # numpad keys
            input_key = int(input.strip("<>"))
            for _ in range(times):
                keyboard.press(KeyCode(input_key)) # type: ignore
                time.sleep(0.1)
                keyboard.release(KeyCode(input_key)) # type: ignore
                if times >= 2:
                    time.sleep(0.1)
        else:
            for _ in range(times):
                keyboard.press(input)
                time.sleep(0.1)
                keyboard.release(input)
                if times >= 2:
                    time.sleep(0.1)

def press_esc() -> None:
    """Simulates Esc key press."""
    kb_input(Key.esc)
    time.sleep(0.1)