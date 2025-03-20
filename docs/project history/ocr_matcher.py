"""Used in testing screen_ocr text reading from monitor and matching this output to a static string.

Press F12 to close script and stop matching.

**This script is no longer needed, use weak_ocr_test instead.
  Also imports screen_ocr, but this one is no longer used in the current version of project. 
"""

import os
import time
import signal

import screen_ocr # type: ignore
import pynput
from pynput.keyboard import Key, KeyCode
import pyautogui

WIDTH, HEIGHT = pyautogui.size()

def pixel_position(xy : tuple[float, float]) -> tuple[float, float]:
     """Reverts coordinate scalars back to pixel coordinates of user's display resolution.

     Args:
        xy: Tuple of scalar coordinates.
     Returns:
        (x,y): Tuple of pixel coordinates.
     """
     x, y = round(WIDTH*xy[0]), round(HEIGHT*xy[1])
     return (x,y)

def exit(key: Key | KeyCode | None) -> None:
    """Allows terminating scripts by pressing f12.

    Args:
        key: Latest keyboard key pressed.
    """
    if key == pynput.keyboard.Key.f12:
        print('Closing...')
        os.kill(os.getpid(), signal.SIGTERM)

def read() -> None:
    """Read text from screen box defined within match_coordinates and tests if substring match_string is found in it.
     
    You should separate words in match_string with newline character.
    """
    match_coordinates = (0.7666666666667, 0.3796296296296, 0.8553125, 0.4855555555556)
    match_string = 'continue'
    match_frequency = 0.5

    (x1, y1) = pixel_position((match_coordinates[0], match_coordinates[1]))
    (x2, y2) = pixel_position((match_coordinates[2], match_coordinates[3]))
    reader = screen_ocr.Reader.create_quality_reader()
    raw_text = reader.read_screen(bounding_box=(x1, y1, x2, y2))
    while True:
        text = raw_text.as_string()
        print(text)
        if match_string.lower() in text.lower():
            print('--MATCH--')
        time.sleep(match_frequency)

# listener for key inputs
kb_listener = pynput.keyboard.Listener(on_press = exit)
kb_listener.start()
read()