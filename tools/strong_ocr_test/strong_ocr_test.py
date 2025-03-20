"""Takes a screenshot, processes image, then searches text from it. Used to test ocr.strong_ocr_image's output.

Initial image is saved as strong_new.png, the processed one as strong_text.png.

Processing changes all non-white/non-gray colors to black which leaves white/gray text with black background.
Then ocr is performed on this image.
OCR library is currently easyocr.
"""

import os

from PIL import Image, ImageFile
from numpy import array as narray
import pyautogui
import easyocr # type: ignore

READER = easyocr.Reader(['en'], verbose=False) # takes a while to load the reader.

PATH = os.path.dirname(os.path.abspath(__file__))
WIDTH, HEIGHT = pyautogui.size()

def white_shades(rgb_range: int = 1) -> list[tuple[int, int, int]]:
    """Returns a list of different shades of white color

    Args:
        rgb_range: Integer, to loop over different color values. Default value is 1.

    Returns:
        white_list: List of tuples, each tuple representing a color value in rgb-format.
    """
    white_list = []
    for i in range(0, rgb_range):
        for j in range(0, rgb_range):
            for k in range(0, rgb_range):
                w = (255-i, 255-j, 255-k)
                white_list.extend([w])
    return white_list

def gray_shades(rgb_range: int = 1) -> list[tuple[int, int, int]]:
    """Returns a list of different shades of gray color.

    Args:
        rgb_range: Integer, to loop over different color values. Default value is 1.

    Returns:
        gray_list: List of tuples, each tuple representing a color value in rgb-format.
    """
    gray_list = []
    for i in range(0, rgb_range):
        for j in range(0, rgb_range):
            for k in range(0, rgb_range):
                g1 = (160-i, 164-j, 174-k)
                g2 = (160+i, 164+j, 174+k)
                gray_list.extend([g1, g2])
    return gray_list

# always include the main color from upgrade texts with rgb_range = 1. Increasing it can increase reading accuracy
# but also harm it so these are experimental. So don't pass other values unless you know what you're doing.
WHITE = white_shades()
GRAY = gray_shades()


def remove_white_and_gray(image: ImageFile.ImageFile) -> ImageFile.ImageFile:
    """Return an image with all of its colors except white and grey, replaced with black. 
    
    This leaves white text with black background and makes ocr matching more accurate.

    Args:
        image: A PIL.ImageFile.ImageFile object.

    Returns:
        img: ImageFile object, with white/gray text with black background.
    """
    img = image
    width = img.size[0] 
    height = img.size[1] 
    for i in range(0, width): # process all pixels
        for j in range(0, height):
            data = img.getpixel((i,j))
            if data in GRAY or data in WHITE:
                img.putpixel((i,j), (255, 255, 255))              
            else:
                img.putpixel((i,j),(0, 0, 0))
    return img

def pixel_position(xy: tuple[float, float]) -> tuple[int, int]:
    """Reverts coordinate scalars back to pixel coordinates of user's display resolution.

    Args:
        xy: Tuple of scalar coordinates.

    Returns:
        Pixel coordinates as a tuple.
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


x1, y1, x2, y2 = 0.1317708333333, 0.3696296296296, 0.2203125, 0.462037037037 # coordinates of bounding box
w, h = x2-x1, y2-y1 # height and width

# need pixel coordinates for pyautogui
px1, py1 = pixel_position((x1, y1))
px2, py2 = pixel_position((x2, y2))
pw, ph = pixel_position((w, h))

# new coordinates to copy. Mostly used for assist.constants
print(str(px1)+', '+str(py1)+', '+str(px2)+', '+str(py2))
print(str(x1)+', '+str(y1)+', '+str(x2)+', '+str(y2))
print('\n')

pyautogui.screenshot(imageFilename=PATH+'\\strong_new.png', region=(px1, py1, pw, ph))
blackwhite_image = remove_white_and_gray(Image.open(PATH+'\\strong_new.png'))
blackwhite_image.save(PATH+'\\strong_text.png')
final = narray(Image.open(PATH+'\\strong_new.png'))
    
result = READER.readtext(final)
string = ''
for r in result:
    string += r[1]
print(string)