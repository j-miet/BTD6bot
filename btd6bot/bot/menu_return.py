from __future__ import annotations
import time

from bot import kb_mouse
from bot.bot_data import BotData
from bot.bot_vars import BotVars
from bot.ocr.ocr import weak_substring_check, strong_delta_check
from bot.ocr.ocr_reader import OCR_READER

class OcrLocations:
    """Wrapper class: text locations for ocr (current ocr library is easyocr).

    These correspond to an image location on screen, with first two coordinates indicating top-left point and last two 
    bottom right point.

    Attributes:
        MENU_PLAYTEXT (tuple[float, float, float, float], class attribute): 
            Start menu 'Play' text location.
    """
    MENU_PLAYTEXT: tuple[float, float, float, float] = (0.4560416666667, 0.932962962963, 0.55875, 0.9914814814815)

class CollectionEvent:
    """Wrapper class: collection events coordinates.
    
    Attributes:
        COLLECTION_BUTTONS (dict[str, tuple[float, float]], class attribute): Collection event button and insta-monkey 
            click locations. These are used only after collection event setting is toggled on in gui.
        COLLECTION_COLLECT (tuple[float, float, float, float], class attribute): Collection event 'Collect' button.
    """
    COLLECTION_BUTTONS: dict[str, tuple[float, float]] = {
        'collection_event' : (0.5, 0.63),
        'collection_continue' : (0.4953125, 0.9240740740741),

        'collection_two_left' : (0.4244791666667, 0.5074074074074),
        'collection_two_right' : (0.5807291666667, 0.5092592592593),
        'collection_three_left' : (0.3130208333333, 0.5027777777778),
        'collection_three_middle' : (0.5015625, 0.5009259259259),
        'collection_three_right' : (0.6911458333333, 0.4935185185185),
        }
    
    COLLECTION_COLLECT: tuple[float, float, float, float] = (0.43, 0.59, 0.534375, 0.6453703703704)

    @staticmethod
    def collection_event_handler() -> None:
        """Checks if collectables window open after a game finishes and collects them.
        
        Instant monkeys are collected by clicking every possible location they can appear at. Each location is clicked 
        twice, as clicking icon will show the insta you got, which then needs to be clicked again to go away. A small 
        time window is added between click to allow collections to register.
        
        If no collection event window pops up, does nothing.

        current event status is read from BotVars.current_event_status.
        """
        print('\nChecking if collection event screen appears...')
        start = time.time()
        while time.time()-start <= 5:
            if strong_delta_check('collect', CollectionEvent.COLLECTION_COLLECT, OCR_READER):
                print('Clicking all insta pop-ups location...')
                kb_mouse.click(CollectionEvent.COLLECTION_BUTTONS['collection_event'], 2)
                time.sleep(3)
                kb_mouse.click(CollectionEvent.COLLECTION_BUTTONS['collection_two_left'], 2)
                time.sleep(1)
                kb_mouse.click(CollectionEvent.COLLECTION_BUTTONS['collection_two_right'], 2)
                time.sleep(1)
                kb_mouse.click(CollectionEvent.COLLECTION_BUTTONS['collection_three_left'], 2)
                time.sleep(1)
                kb_mouse.click(CollectionEvent.COLLECTION_BUTTONS['collection_three_middle'], 2)
                time.sleep(1)
                kb_mouse.click(CollectionEvent.COLLECTION_BUTTONS['collection_three_right'], 2)
                time.sleep(1)
                kb_mouse.click(CollectionEvent.COLLECTION_BUTTONS['collection_continue'])
                time.sleep(3)
                kb_mouse.press_esc()
                print('Collection of event collectables handled.')
                return

def returned(victory: bool = True) -> None:
    """Verifies that bot has returned to main menu and checks for collection event status."""
    if BotVars.current_event_status == 'On':
        CollectionEvent.collection_event_handler()
    while not weak_substring_check('Play', OcrLocations.MENU_PLAYTEXT, OCR_READER):
        time.sleep(0.3)
    if victory:
        BotData.victory = True
    else:
        BotData.victory = False