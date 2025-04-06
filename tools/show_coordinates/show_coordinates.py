"""Updates and shows coordinates of mouse location, both in actual pixels and in decimals normalized to interval [0,1].

Notice that x increases as you cursor moves right and y increases as cursor moves downwards.

Press F10 to stop this script.
"""
import os
import signal
import time

from pynput.keyboard import Key, KeyCode
import pyautogui
import pynput
import pyperclip

def scalar_position(real_x: float, real_y: float) -> tuple[float, float]:
    """Pixel coordinates to decimals. Can change accuracy of output and choose desired screen resolution.

    Args:
        real_x: Pixel coordinate's x value.
        real_y: Pixel coordinate's y value.
        
    Returns:
        scalar_x, scalar_y: Converted scalar coordinates as a tuple.
    """
    accuracy = 13
    res_x, res_y = pyautogui.size()
    scalar_x, scalar_y = round(real_x / res_x, accuracy), round(real_y / res_y, accuracy)
    return scalar_x, scalar_y

def coordinates(pixel_just: int, scalar_just: int) -> None:
    """Displays mouse location in 2 different coordinate systems: pixels and normalized decimals.

    Args:
        pixel_just: Justification of pixel coordinates.
        scalar_just: Justification of scalar coordinates.
    """
    while True:  
        x, y = pyautogui.position()
        sx, sy = scalar_position(x,y)
        positionStr = ' '+ str(x).rjust(pixel_just) + ', ' + str(y).rjust(pixel_just) + ' '*4+' | ' \
        + str(sx).rjust(scalar_just) + ', ' + str(sy).rjust(scalar_just)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='')
        time.sleep(0.001)

def kb(key: Key | KeyCode | None) -> None:
    """Listens to keyboard inputs.

    Plus ('+'): copies current mouse location in scalar coordinates to clipboard.
    Minus ('-'): copies current mouse location in pixels to clipboard.
    F8: Terminate script instantly.

    Args:c
        key: Latest keyboard key pressed.
    """
    if key == Key.f8:
        print('Closing...')
        os.kill(os.getpid(), signal.SIGTERM)
    elif isinstance(key, KeyCode) and key.char == '+':
        x, y = pyautogui.position()
        sx, sy = scalar_position(x,y)
        pos_x, pos_y = str(sx), str(sy)
        pyperclip.copy(pos_x+', '+pos_y)
        print("--> Coordinates "+pos_x+", "+pos_y+" copied to clipboard " +"#"*8)
    elif isinstance(key, KeyCode) and key.char == '-':
        px, py = pyautogui.position()
        pos_x, pos_y = str(px), str(py)
        pyperclip.copy(pos_x+', '+pos_y)
        print("--> Pixel coordinates "+pos_x+", "+pos_y+" copied to clipboard "+'#'*8)

def run() -> None:
    # sends every keyboard input through kb function; starts a secondary thread
    kb_listener = pynput.keyboard.Listener(on_press = kb)
    kb_listener.start()

    print("Press '+' to copy current mouse location as scalar coordinate to clipboard, or F8 to exit.")
    print('Pixel coordinates'.rjust(11) + ' <--- # ---> ' + 'Scalar coordinates'.rjust(10))
    coordinates(5, 16)