"""Updates and shows coordinates of mouse location, both in actual pixels and in decimals normalized to interval [0,1).

Notice that x increases as you cursor moves right and y increases as cursor moves downwards.
"""
import os
import signal
import time

from pynput.keyboard import Key, KeyCode
import pyautogui
import pynput
import pyperclip

ACCURACY = 13
_sc_tl_pos: tuple[int, int]
_sc_winsize: tuple[int, int]

def scalar_position(real_x: float, 
                    real_y: float,
                    ) -> tuple[float, float]:
    """Pixel coordinates to decimals. Can change accuracy of output and choose desired screen resolution.

    Args:
        real_x: Pixel coordinate's x value.
        real_y: Pixel coordinate's y value.
        
    Returns:
        scalar_x, scalar_y: Converted scalar coordinates as a tuple.
    """
    scalar_x = round((real_x - _sc_tl_pos[0]) / _sc_winsize[0], ACCURACY) 
    scalar_y = round((real_y - _sc_tl_pos[1]) / _sc_winsize[1], ACCURACY)
    return scalar_x, scalar_y

def coordinates(pixel_just: int, 
                scalar_just: int
                ) -> None:
    """Displays mouse location in 2 different coordinate systems: pixels and normalized decimals.

    Args:
        pixel_just: Justification of pixel coordinates.
        scalar_just: Justification of scalar coordinates.
    """
    while True:  
        x, y = pyautogui.position()
        sx, sy = scalar_position(x, y)
        positionStr = ' '+ str(x).rjust(pixel_just) + ', ' + str(y).rjust(pixel_just) + ' '*4+' | ' \
        + str(sx).rjust(scalar_just) + ', ' + str(sy).rjust(scalar_just)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='')
        time.sleep(0.001)

def kb(key: Key | KeyCode | None) -> None:
    """Listens to keyboard inputs.

    Plus ('+'): copies current mouse location in scalar coordinates to clipboard.
    Asterisk ('*'): copies current mouse location in pixels to clipboard.
    F8: Terminate script instantly.

    Args:
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
    elif isinstance(key, KeyCode) and key.char == '*':
        px, py = pyautogui.position()
        pos_x, pos_y = str(px), str(py)
        pyperclip.copy(pos_x+', '+pos_y)
        print("--> Pixel coordinates "+pos_x+", "+pos_y+" copied to clipboard "+'#'*8)

def run() -> None:
    global _sc_tl_pos
    global _sc_winsize
    _sc_tl_pos = (0, 0)
    _sc_winsize = pyautogui.size()

    # sends every keyboard input through kb function; starts a secondary thread
    kb_listener = pynput.keyboard.Listener(on_press = kb)
    kb_listener.start()

    print("Type 'n' and press Enter for normal mode, or type 'c' then press Enter for custom mode.\n" \
    "Normal mode is for 16:9 fullscreen users, custom for windowed users. Use normal mode if possible.")
    while True:
        input_str = input("[select mode]=>")
        if input_str == 'n':
            print("Press '+' to copy current mouse location as scalar coordinate to clipboard, '*' same but for pixel " 
                    "coordinates. F8 to exit.")
            print('Pixel coordinates'.rjust(11) + ' <--- # ---> ' + 'Scalar coordinates'.rjust(10))
            coordinates(5, 16)
        elif input_str == 'c':
            input_str = input("Give top-left game window coordinate.\n[give coordinate in 'X,Y' format]=>")
            tl_pos = input_str.split(',')
            _sc_tl_pos = int(tl_pos[0]), int(tl_pos[1].strip())
            input_str = input("Now give your game window resolution.\n[give game resolution in 'X,Y' format]=>")
            size = input_str.split(',')
            _sc_winsize = int(size[0]), int(size[1].strip())
            print("Press '+' to copy current mouse location as scalar coordinate to clipboard, '*' same but for pixel " 
                    "coordinates. F8 to exit.")
            print('Pixel coordinates'.rjust(11) + ' <--- # ---> ' + 'Scalar coordinates'.rjust(10))
            coordinates(5, 16)