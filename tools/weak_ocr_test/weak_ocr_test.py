"""Takes a screenshot and processes text out of it. Used to test ocr.weak_image_ocr output.

Screenshot is saved as weak_new.png.
OCR library is currently easyocr.
"""

import os

from PIL import Image
from numpy import array as narray
import pyautogui
import easyocr # type: ignore

READER = easyocr.Reader(['en'], verbose=False) # takes a while to load the reader.

PATH = os.path.dirname(os.path.abspath(__file__))
WIDTH, HEIGHT = pyautogui.size()

def pixel_position(xy: tuple[float, float]) -> tuple[int, int]:
    """Scales pixel coordinates to scalar coordinates. Can set a custom decimal rounding.

    Args:
        real_pos: Tuple of pixel coordinates.

    Returns:
        Tuple of scalar coordinates.
    """
    x, y = round(WIDTH*xy[0]), round(HEIGHT*xy[1])
    return (x,y)

def scalar_position(real_pos: tuple[int, int]) -> tuple[float, float]:
    """Scales pixel coordinates to scalar coordinates. Can set a custom decimal rounding.

    Args:
        real_pos: Tuple of pixel coordinates.
        
    Returns:
        Tuple of scalar coordinates.
    """
    ROUNDING = 13
    scalar_x, scalar_y = round(real_pos[0] / WIDTH, ROUNDING), round(real_pos[1] / HEIGHT, ROUNDING)
    return (scalar_x, scalar_y)

x1, y1, x2, y2 = 0.7666666666667, 0.3696296296296, 0.8552083333333, 0.462037037037 # coordinates of bounding box
w, h = x2-x1, y2-y1 # height and width

# need pixel coordinates for pyautogui
px1, py1 = pixel_position((x1, y1))
px2, py2 = pixel_position((x2, y2))
pw, ph = pixel_position((w, h))

# new coordinates to copy. Mostly used for assist.constants
print(str(px1)+', '+str(py1)+', '+str(px2)+', '+str(py2))
print(str(x1)+', '+str(y1)+', '+str(x2)+', '+str(y2))
print('\n')

pyautogui.screenshot(imageFilename=PATH+'\\weak_new.png', region=(px1, py1, pw, ph))
img = narray(Image.open(PATH+'\\weak_new.png'))

result = READER.readtext(img)
string = ''
for r in result:
    string += r[1]
print(string)