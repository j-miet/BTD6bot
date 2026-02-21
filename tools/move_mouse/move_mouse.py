"""Script for moving mouse to specified location.

Supports both scalar and pixel coordinates.
"""

import os
import signal

import pyautogui

ACCURACY = 13

def pixel_position(sx: float, sy: float) -> tuple[float, float]:
    """Scalar coordinates to decimals. Can change accuracy of output and choose desired screen resolution.

    Args:
        sx: Scalar x value.
        sy: Scalar y value.
        
    Returns:
        Converted pixel coordinates as a tuple.
    """
    res_x, res_y = pyautogui.size()
    px, py = round(res_x*sx, ACCURACY), round(res_y*sy, ACCURACY)
    return px, py

def run() -> None:
    print("Input either 's' or 'p' for scalar/pixel coordinates, then enter value in format: X, Y.\n"
          "E.g. \n"
          "with 's' -> 0.5, 0.5 moves cursor to the middle of monitor screen\n"
          "with 'p' and 1920x1080 res -> 960, 540 would achieve the same result\n"
          "To quit script, type 'exit'.\n")
    while True:
        input_val = input("=>")
        if input_val.lower() == 's':
            try:
                pos_input = input("Give a scalar coordinate position in format X Y\n=>")
                pos_input = pos_input.strip().removesuffix('\n')
                x, y = pos_input.split(',')
                px, py = pixel_position(float(x),float(y))
                pyautogui.moveTo(px, py)
                print(f"Mouse moved to scalar location ({x}, {y})")
            except ValueError:
                print("Invalid input.")
        elif input_val.lower() == 'p':
            try:
                pos_input = input("Give a pixel coordinate position in format X Y\n=>")
                pos_input = pos_input.strip().removesuffix('\n')
                x, y = pos_input.split(',')
                pyautogui.moveTo(float(x), float(y))
                print(f"Mouse moved to pixel location ({x}, {y})")
            except ValueError:
                print("Invalid input.")
        elif input_val.lower() == 'exit':
            os.kill(os.getpid(), signal.SIGTERM)
			
if __name__ == "__main__":
	run()