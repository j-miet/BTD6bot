"""All tools required for optical character recognition tasks.

Prior to using easyocr, it was first screen_ocr base library for the longest time. Then briefly tested screen_ocr_winrt
lib too. Then came tesseract: reason for changing to tesseract was simply lack of accuracy with upgrade texts. However,
it was much slower, like 25-30% slower with monkey upgrades than screen_ocr, but that's the price to pay for accuracy.

Now, current one is easyocr: it seems even more accurate, or at least ocr temp get very good matches from one another
so upgrading monkeys works consistently so far; obviously there could be problematic cases but only time will tell.
Also similar speedwise to tesseract; would be a lot slower with all the processing, but now for example zooming of 
images is no longer necessary which saves time. Easyocr does have the initial reader setup delay, which is done before
lauching program: it takes like 10 seconds, but isn't required afterwards as reader is loaded from ocr_reader and
passed as a variable to all implemented reader-utilizing tools.

After reader is initialized, it will reserve quite sizeable chunk in memory, about 400MB.

I have only tested easyocr with CPU. It has GPU support which would make it run much faster, but this is not really a
concern with a slower program such as this bot.

CPU-wise, ocr is quite resource-heavy if no pic is found. For example, if you start program, but put main menu screen 
away, it tries to search word 'play' constantly. That's why an artificial pause is introduced with time.sleep, both to 
start menu search but also in general, known as read_file_frequency. But even with this, CPU usage will likely jump up 
a lot. Easyocr suggests using GPU support as it will increase your ocr performance A LOT: this is because easyocr is 
build around PyTorch library, which has CUDA support for modern (Nvidia) GPUs. However, I've designed this bot around 
the CPU version of ocr, so it will work on any system capable of running BTD6. It's just that (as stated before) CPU 
version uses relatively far more utilization than the GPU version. But that shouldn't be much of an issue as you'd have 
this bot + game running, with no other major program open (barring a web browser or similar).


Constants:
    WHITE, GRAY:
    colors used in detecting text from an image. Always include the main color from upgrade texts with rgb_range = 1.
    Increasing it can increase reading accuracy but also make it worse so these are experimental. So don't pass other
    values unless you know what you're doing.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import difflib
import json
import pathlib
import time

import pyautogui
from numpy import array, repeat

from bot import kb_mouse
from bot.bot_vars import BotVars
from customprint import cprint

if TYPE_CHECKING:
    from easyocr import Reader  # type: ignore
    from PIL.ImageFile import ImageFile
    from typing import Any

class OcrValues:
    """Wrapper class: constants required for optical character recognition tools.

    Attributes:
        OCR_IMAGE_PATH (pathlib.PATH, class attribute):
            Folder location that stores temporary ocr images. Images are constantly overwritten as ocr process repeats 
            screenshotting and reading text from screenshot image.
        DELTA (float, class attribute):
            Controls OCR string matching accuracy in strong_delta_check for general strings - upgrade string are 
            handled separately. Delta value itself is included i.e. 0.8 means that all deltas on closed interval 
            [0.8, 1] are valid.
        OCR_UPGRADE_DATA (dict[str, list[str, float]], class attribute):
            Contains all upgrade names and their respective deltas for strong_delta_check. Each key 
            is a identifier for monkey and crosspath, with values being the ocr data. For example,
            OCR_UPGRADE_DATA['dart 1-x-x'] would return something similar to ["sharp shots", 0.8].
                       
        read_file_frequency (float, class attribute):
            Text recognition check rate in both find_text and check_upg_text: lower number increases rate of checking, 
            but also increases CPU usage significantly. Frequency itself is just a pause timer in seconds so 1 equals 
            to ~1 check a second, but this doesh't include the other part of process like screenshotting, reading text 
            and comparing text. This means the actual frequence to checks ratio diminishes greatly with smaller value 
            i.e. 0.01 doesn't match to 100 checks per second.

    """
    OCR_IMAGE_PATH: pathlib.Path = pathlib.Path(__file__).parent.parent.parent/'Files'/'ocr temp'
    DELTA: float = 0.75

    @staticmethod
    def _get_current_upgradedata() -> dict[str, list[str | float]]:
        with open(pathlib.Path(__file__).parent.parent.parent/'Files'/'upgrades_current.json') as f:
            return json.load(f)    
    OCR_UPGRADEDATA = _get_current_upgradedata()

    @staticmethod
    def _get_base_upgradedata() -> dict[str, list[str | float]]:
        with open(pathlib.Path(__file__).parent.parent.parent/'Files'/'_ocr_upgradedata.json') as f:
            return json.load(f)   
    _OCR_UPG_BASEDATA = _get_base_upgradedata() 

    read_file_frequency: float = 0.01
    _log_ocr_deltas: bool = False

def get_pixelcolor(x: float, y: float) -> tuple[int, int, int]:
    """Returns rgb color tuple of a coordinate location.
    
    Coordinates are passed as scalar values [0,1).
    """
    px, py = kb_mouse.pixel_position((x, y))
    return pyautogui.pixel(px,py)

def white_shades(rgb_range: int = 1) -> list[tuple[int, int, int]]:
    """Returns a list of different shades of white color. By default, only white (255,255,255) is returned.

    This color is two of the main colors in upgrade messages (other being gray). When everything but these
    two colors/shades are removed and other pixels made black, text becomes possibly easier to read by ocr
    tools. Is used with strong_image_ocr method.

    Args:
        rgb_range: Integer value that determines the range of shades. Default value is 1. 

    Returns:
        white_list: List of color tuples.
    """
    white_list = []
    for i in range(0, rgb_range):
        for j in range(0, rgb_range):
            for k in range(0, rgb_range):
                w = (255-i, 255-j, 255-k)
                white_list.extend([w])
    return white_list

def gray_shades(rgb_range: int = 1) -> list[tuple[int, int, int]]:
    """Returns a list of different shades of gray color. By default, only gray value (160,164,174) is returned.

    See documentation of white_shades for further explanation.

    Args:
        rgb_range: Integer value that determines the range of shades. Default value is 1.

    Returns:
        gray_list: List of color tuples.
    """
    gray_list = []
    for i in range(0, rgb_range):
        for j in range(0, rgb_range):
            for k in range(0, rgb_range):
                g1 = (160-i, 164-j, 174-k)
                g2 = (160+i, 164+j, 174+k)
                gray_list.extend([g1, g2])
    return gray_list

WHITE = white_shades()
GRAY = gray_shades()

def img_to_black_and_white(image: ImageFile) -> ImageFile:
    """Return an image with non-white and non-grey shades replaced with black.
      
    This leaves white text with black background and makes ocr matching possibly more accurate. 
    Used in strong_image_ocr.

    Args:
        image: A PIL.ImageFile.ImageFile object

    Returns:
        img: Original image, but with only white/gray and black colors. Type is the same, ImageFile.
    """
    img = image
    width, height = img.size[0], img.size[1] 
    for i in range(0, width): # process all pixels
        for j in range(0, height):
            data = img.getpixel((i,j))
            if data in GRAY or data in WHITE:
                img.putpixel((i,j), (255, 255, 255))              
            else:
                img.putpixel((i,j),(0, 0, 0))
    return img

def weak_image_ocr(coordinates: tuple[int, int, int, int], reader: Reader) -> str:
    """Extracts text from an image and returns this text as a string.
    
    Takes a monitor screenshot on passed coordinate location, then open this image in a format the easyocr reader
    can utilize, reads text, and finally return the extracted text string.

    Doesn't use the black and white like strong_image_ocr does because matching is done with static string and thus
    very easy to do as long as screenshot location is good.

    Args:
        coordinates: Image location, an integer-valued 4-tuple. First two values correspond to top-left (x,y)
            location, last two to bottom-right (x,y) location. Coordinates are in pixels, not scalars.
        reader: An easyocr.Reader object that handles reading text from image. Loaded from ocr_reader.py.

    Returns:
        string: Extracted text string.
    """
    tl_x, tl_y, br_x, br_y = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
    width, height = br_x - tl_x, br_y - tl_y
    # uncomment and replace 2 lines below with these if you need images; images are created in Files/ocr_temp
    #
    # pyautogui.screenshot(imageFilename=OcrValues.OCR_IMAGE_PATH/'weak_new.png', region=(tl_x, tl_y, width, height))
    # img = array(Image.open(OcrValues.OCR_IMAGE_PATH/'weak_new.png'))
    ocr_img = pyautogui.screenshot(region=(tl_x, tl_y, width, height))
    img = array(ocr_img)
    try:
        result = reader.readtext(img)
        string = ''
        for r in result:
            string += r[1]
    except ValueError:  
        string = ''
    return string

def strong_image_ocr(coordinates: tuple[int, int, int, int], reader: Reader) -> str:
    """Extracts text from an image by making them first black and white/gray-shaded, and then performing ocr on them.
     
    Similar to weak_image_ocr, but images are processed with a function that sets other but white/gray pixels to black:
    white and gray are upgrade text labels. So end results is black background with text elements in white & gray
    colors: this clears most junk so that 2 OCR image strings are easy to match.

    Args:
        coordinates: Image location, an integer-valued 4-tuple. First two values correspond to top-left (x,y)
            location, last two to bottom-right (x,y) location. Coordinates are in pixels, not scalars.
        reader: An easyocr.Reader object that handles reading from image. Loaded from ocr_reader.py.

    Returns:
        string: Extracted text string.
    """
    tl_x, tl_y, br_x, br_y = coordinates[0], coordinates[1], coordinates[2], coordinates[3]
    width, height = br_x - tl_x, br_y - tl_y
    # uncomment and replace 3 lines below with these if you need images; images are created in Files/ocr_temp
    # 
    # pyautogui.screenshot(imageFilename=OcrValues.OCR_IMAGE_PATH/'strong_new.png', region=(tl_x, tl_y, width, height))
    # blackwhite_image = img_to_black_and_white(Image.open(OcrValues.OCR_IMAGE_PATH/'strong_new.png'))
    # blackwhite_image.save(OcrValues.OCR_IMAGE_PATH/'strong_text.png')
    # final = array(Image.open(OcrValues.OCR_IMAGE_PATH/'strong_text.png'))
    ocr_img = pyautogui.screenshot(region=(tl_x, tl_y, width, height))
    blackwhite_image = img_to_black_and_white(ocr_img) # type: ignore
    final = array(blackwhite_image)
    if BotVars.windowed:
        zoom_factor = 2
        for i in range(2):             # zooming of images, quite expensive to calculate.
            final = repeat(final, zoom_factor, axis=i)
    try:
        result = reader.readtext(final)
        string = ''
        for r in result:
            string += r[1]
    except ValueError:
        string = ''
    return string
    
def weak_substring_check(input_str: str, coords: tuple[float, float, float, float], reader: Reader) -> bool:
    """Attemps to find inputed string from screenshot ocr string by substring matching.

    Tries to read the input_str from screen within specified coordinates. If it's found, returns True, otherwise False.
    Order of coordinates: (left, top, right, bottom), meaning (top_left x, top_left y, bottom_right x, bottom_right y),
    naturally topleft_x < bottomright_x and topleft_y < bottomright_y, otherwise throws error. Uses weak_image_ocr
    function as text extractor: this does far less modifying of current image, but matches much better with certain 
    static/pre-typed strings than strong_image_ocr. 
    
    Use cases:  
    -checking menu play button text,  
    -when game begins i.e. locating 'upgrade' text. Will not check game ending, however, as this still has weird 
        inconsistencies.  
    -finding the defeat screen 'bloons leaked' message.  
    
    Args:
        input_str: The substring that should be contained within ocr string.
        coords: Image location, an integer-valued 4-tuple. First two values correspond to top-left (x,y)
            location, last two to bottom-right (x,y) location.
        reader: reader: An easyocr.Reader object that handles reading text from image. Loaded from ocr_reader.py.

    Returns:
        A boolean value depending on if the substring matched ocr string or not.
    """
    (tl_x, tl_y) = kb_mouse.pixel_position((coords[0], coords[1]))
    (br_x, br_y) = kb_mouse.pixel_position((coords[2], coords[3]))
    text = weak_image_ocr((tl_x, tl_y, br_x, br_y), reader)
    if BotVars.print_substring_ocrtext:
        cprint("\nText: "+text.lower()+'\nInput: '+input_str.lower())
    if len(text) != 0 and text.lower().find(input_str.lower()) != -1:
        return True
    time.sleep(OcrValues.read_file_frequency)
    return False

def strong_delta_check(input_str: str, coords: tuple[float, float, float, float], reader: Reader, 
                       upg_match: str = '',
                       ) -> bool:
    """Attemps to match a string with strong_image_ocr string by their similarity.

    Differs from substring checking by using a delta parameter which compares similar symbols in two strings.
    This makes it powerful when matching to complex ocr like upgrade texts, or two ocr strings (latter was used before 
    but has currently no use). However, for simpler static string matching, it faces the problem of over-processing 
    inputs and thus makes bad errors, like passing rounds and creating mismatch between current round that bot sees and 
    actual game round. Thus, this responsibility is left for weak_substring_check instead.  
    To add to above, delta matching is still very effective on some simple static strings. For example, when a monkey/
    hero is placed, ocr checks this by reading the 'sell' text. But quite often this string is either missing one of 
    the letters 'l' or one gets replaced by 'i' or 1, making substring matching ineffective. But with enough delta, ocr 
    can identify them as same.
    
    'difflib' module offers ways to compare objects like strings and return a value which measures their similarity.
    SequenceMatcher matches two strings with optional junk symbol detector: this allows to ignore spaces/tabs and
    possibly other values that shouldn't be part of matching. The quick_ratio is used to return upper bound of
    difference between sequences and is much faster to calculate. Return values (= deltas) are on interval [0,1]
    where 0 is for entirely different strings and 1 for perfect matches.

    After some testing, common deltas seem to exceed 0.8 often. Shouldn't be too high either as ocr could reject valid
    strings, too. And in some cases, relatively high delta can still match two different upgrades. For this reason, all 
    upgrade strings are saved in OcrValues.OCR_UPGRADE_DATA dictionary. Not only that, each string has individual delta 
    which helps at tweaking problematic cases, but keeping majority of upgrades passable: for latter, a high delta (>= 
    0.8) is used as base value to avoid false positives, when two consecutive upgrade strings share too many symbols.

    Like mentioned, uses quick_ratio() instead of ratio() due to it being considerably faster.

    Use cases:  
    -upgrading monkeys,  
    -checking 'sell' text when placing monkeys; high enough DELTA will match even with one letter mismatch when it 
        spells 'sel' instead,  
    -end screen 'next' text (again, simple short text but can still cause error in a single letter so high DELTA 
        helps),
    -checking collection event 'Collect' text.

    Args:
        input_str: A string, extracted from an image using strong_image_ocr()s
        coords: Image location, an integer-valued 4-tuple. First two values correspond to top-left (x,y)
            location, last two to bottom-right (x,y) location.
        reader: An easyocr.Reader object that handles reading from image. Loaded from ocr_reader.py.
        upg_match: Identification string if ocr is performed for upgrade strings. Upgrades are listed under 
            OcrValues.OCR_UPGRADE_DATA

    Returns:
        A boolean value depending on if upgrade strings are similar enough (above DELTA threshold) or not.
    """
    (tl_x, tl_y) = kb_mouse.pixel_position((coords[0], coords[1]))
    (br_x, br_y) = kb_mouse.pixel_position((coords[2], coords[3]))
    text = strong_image_ocr((tl_x, tl_y, br_x, br_y), reader)
    if len(text) != 0:
        if input_str == '_upgrade_':
            match = OcrValues.OCR_UPGRADEDATA[upg_match]
            if OcrValues._log_ocr_deltas:
                match_str = match[0]
            else:
                match_str = match[0]
                delta_limit = match[1]
            d = difflib.SequenceMatcher(lambda x: x in "\t", text.lower(), match_str).quick_ratio() # type: ignore
            if BotVars.print_delta_ocrtext:
                cprint('\n-Text: '+text.lower())
                cprint("-Match delta: "+str(d))
                if OcrValues._log_ocr_deltas:
                    with open(
                        pathlib.Path(__file__).parent.parent.parent/'Files'/'.temp_upg_deltas.json'
                        ) as f:
                        temp_dict: dict[str, Any] = json.load(f)
                    if len(str(d)) <= 4:
                        add_dict = {upg_match: [match_str, d]}
                    else:
                        add_dict = {upg_match: [match_str, round(d-0.005, 2)]}
                    temp_dict.update(add_dict)
                    with open(
                        pathlib.Path(__file__).parent.parent.parent/'Files'/'.temp_upg_deltas.json',
                        'w') as f:
                        json.dump(temp_dict, f, indent=2)
                    return True
            if d >= delta_limit: # type: ignore
                return True
        elif input_str != '':
            r = difflib.SequenceMatcher(lambda x: x in "\t", text.lower(), input_str.lower()).quick_ratio()
            if BotVars.print_delta_ocrtext:
                cprint('\n-Input: '+input_str.lower()+'\n-Text: '+text.lower()+'\n-Delta: '+str(r))
            if r >= OcrValues.DELTA:
                return True
    time.sleep(OcrValues.read_file_frequency)
    return False

def strong_substring_check(input_str: str, coords: tuple[float, float, float, float], reader: Reader
                           ) -> tuple[bool, str]:
    """Attemps to find inputed string from screenshot ocr string by substring matching with black and white text box.
    
    Middle ground for weak_substring_check and strong_delta_check: uses strong_image_ocr to get black and white text
    box, but still uses substring matching instead of DELTA.

    Why this implementation? weak_substring_check can have difficulties with accurate input when map background under
    rounds is more complex, so black background makes it easier - this was particularly problematic if round message
    is shorter than, say, 'round .../100' text of impoppable/chimps.

    Use cases:  
    -checking current round text.

    Args:
        input_str: The substring that should be contained within ocr string.
        coords: Image location, an integer-valued 4-tuple. First two values correspond to top-left (x,y)
            location, last two to bottom-right (x,y) location.
        reader: An easyocr.Reader object that handles reading text from image. Loaded from ocr_reader.py.

    Returns:
        A tuple of boolean value and found ocr string in lowercase. Boolean is True if text is found as substring in 
            input, otherwise False.
    """
    (tl_x, tl_y) = kb_mouse.pixel_position((coords[0], coords[1]))
    (br_x, br_y) = kb_mouse.pixel_position((coords[2], coords[3]))
    text = strong_image_ocr((tl_x, tl_y, br_x, br_y), reader)
    text_lower = text.lower()
    if BotVars.print_substring_ocrtext:
        cprint("\nText: "+text_lower+'\nInput: '+input_str.lower())
    if len(text) != 0 and text_lower.find(input_str.lower()) != -1:
        return (True, text_lower)
    time.sleep(OcrValues.read_file_frequency)
    return (False, text_lower)