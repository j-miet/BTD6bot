"""Simulation of keyboard and mouse controls.

pyautogui.FAILSAFE controls build-in pyautogui fail-safe of dragging mouse to a corner of the screen, shutting down the program. This is set to "False" as there's already a hotkey or Ctrl+C for quick termination.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import time

import pyautogui
import pynput
from pynput.keyboard import Key

if TYPE_CHECKING:
    from pynput.keyboard import KeyCode

pyautogui.FAILSAFE = False      
WIDTH, HEIGHT = pyautogui.size()
"""User screen resolution metrics."""

def pixel_position(xy: tuple[float | None, float | None]) -> tuple[int, int]:
    """Reverts coordinate scalars back to pixel coordinates of user's display resolution.

    Args:
        xy: Scalar coordinates as a tuple.
        
    Returns:
        Pixel coordinates as a tuple. If scalar coordinates are not floats, return (-1, -1).
    """
    if isinstance(xy[0], float) and isinstance(xy[1], float):
        x, y = round(WIDTH*xy[0]), round(HEIGHT*xy[1])
        return x,y
    print('Error with converting scalars to pixels.')
    return -1, -1   # this was added to satisfy mypy type hints.

def click(pos: tuple[float | None, float | None], clicks: int=1) -> None:
    """Left-clicks mouse at a desired coordinate. Converts scalar coordinates to pixel coordinates to find position.

    Args:
        pos: Mouse position, in scalar coordinates.
        clicks: Amount of clicks performed. Default value is 1.
    """
    if isinstance(clicks, int) and clicks >= 1:
        for _ in range(clicks):
            time.sleep(0.1)
            old_X, old_Y = pyautogui.position()
            new_X, new_Y = pixel_position((pos[0], pos[1]))
            pyautogui.moveTo(new_X, new_Y)
            pyautogui.click(new_X, new_Y)
            pyautogui.moveTo(old_X, old_Y)

def kb_input(input: Key | KeyCode | str, times: int = 1) -> None:
    """Simulates pressing a single keyboard input by default.

    If same key must be pressed multiple times, change 'times' value.

    Args:
        input: Key that needs to be pressed.
        times: How many times key is pressed. Default value is 1.
    """
    if isinstance(times, int) and times >= 1:
        keyboard = pynput.keyboard.Controller()
        for _ in range(times):
            keyboard.press(input)
            time.sleep(0.1)
            keyboard.release(input)
            if times >= 2:
                time.sleep(0.1)

def move_cursor(xy: tuple[float, float], set_duration: float = 0.0) -> None:
    """Moves mouse to specified coordinate location.
    
    Args:
        xy: Scalar coordinate tuple of location coordinates.
    """
    x, y = pixel_position((xy[0], xy[1]))
    pyautogui.moveTo(x, y, duration=set_duration)
    time.sleep(0.1)

def press_esc() -> None:
    """Simulates Esc key press."""
    kb_input(Key.esc)
    time.sleep(0.1)