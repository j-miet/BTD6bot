"""Testing Geraldo's shop.

Open btd6 -> select 'Geraldo' as hero -> select 'in the loop' map -> sandbox mode -> run this script.
"""

import pathlib
import sys
import time

sys.path.append(str(pathlib.Path(__file__).parent.parent))

from bot import _maindata, kb_mouse
from bot.commands.monkey import Monkey
from bot.commands.hero import Hero
from bot.locations import get_text
from bot.ocr.ocr import weak_substring_check
from bot.ocr.ocr_reader import OCR_READER

def geraldo_test() -> None:
    _maindata.maindata["bot_vars"]["checking_time_limit"] = 10
    
    while not weak_substring_check("Upgrades", get_text('ingame','upgrade_text'), OCR_READER):
        print("Waiting map screen...")
        kb_mouse.click((0.5036458333333, 0.7064814814815))
        time.sleep(1)
    print("\n###")

    Hero.current_plan_hero_name = 'geraldo'
    hero = Hero(0.5, 0.5)
    time.sleep(1)

    kb_mouse.click((0.5, 0.5))
    print('Clicked at Geraldo')
    time.sleep(1)
    kb_mouse.click((0.2395833333333, 0.1777777777778))
    print('Closed shop')
    time.sleep(1)
    kb_mouse.click((0.1203125, 0.6351851851852), 19)
    print('Upgraded Geraldo to 20')
    time.sleep(1)
    kb_mouse.click((0.2395833333333, 0.1777777777778))
    time.sleep(1)
    kb_mouse.click((0.5, 0.2))
    print('Re-opened shop')

    Monkey('dart', 0.2713541666667, 0.4731481481481)
    Monkey('farm', 0.7203125, 0.4287037037037)

    hero.shop(1, 0.3369791666667, 0.2805555555556)
    hero.shop(2, 0.0395833333333, 0.8231481481481)
    hero.shop(3, 0.1239583333333, 0.7527777777778)
    hero.shop(4, 0.2713541666667, 0.4731481481481)

    hero.shop(5, 0.4369791666667, 0.2805555555556)
    hero.shop(6, 0.2713541666667, 0.4731481481481)
    hero.shop(7, 0.2182291666667, 0.812037037037)
    hero.shop(8, 0.2713541666667, 0.4731481481481)

    hero.shop(9, 0.2713541666667, 0.4731481481481)
    hero.shop(10, 0.2505208333333, 0.8268518518519)
    hero.shop(11, 0.5, 0.5)
    hero.shop(12, 0.7203125, 0.4287037037037)

    hero.shop(13, 0.5265625, 0.6027777777778)
    hero.shop(14, 0.4119791666667, 0.4935185185185)
    hero.shop(15, 0.2901041666667, 0.6601851851852)
    hero.shop(16, 0.6036458333333, 0.6546296296296)
    print('Shop tested!')

if __name__ == '__main__':
    geraldo_test()