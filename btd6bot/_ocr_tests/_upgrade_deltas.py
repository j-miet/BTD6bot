"""Runs upgrade checks for all listed monkeys.

Open btd6 -> select 'in the loop' map -> sandbox mode -> run this script.

To get printed ocr string and delta values:
--Go to bot.ocr.ocr -> strong_delta_check -> uncomment the print lines to see ocr string outputs.
--Just remember to comment these back after testing is done
-->After ocr text debug setting has been added, can set it True instead by 'logging = True' or something similar.
"""

import time

from bot import kb_mouse
from bot.bot_vars import BotVars
from bot.commands.monkey import Monkey, _MonkeyConstants
from bot.ocr.ocr import weak_substring_check
from bot.ocr.ocr_reader import OCR_READER
from bot.rounds import Rounds

listed_monkeys = ['village', 'engineer']    # customize these

def adjust_upg_deltas(check_monkeys: list[str]) -> None:
    BotVars.checking_time_limit = 10
    
    while not weak_substring_check('Upgrades', Rounds.UPGRADE_TEXT, OCR_READER):
        print("Waiting map screen...")
        kb_mouse.click((0.5036458333333, 0.7064814814815))
        time.sleep(1)
    print("\n###")

    monkeys: list[str] = []
    if check_monkeys == 'all':
        monkeys = list(_MonkeyConstants._MONKEY_NAMES[:])
        monkeys.remove('hero')
        monkeys.remove('beast')  # remove this after beast merging has been implemented.
    else:
        for name in check_monkeys:
            if name in list(_MonkeyConstants._MONKEY_NAMES):
                monkeys.append(name)

    for m in monkeys:   # land monkeys (excluding village, super)
        if m == 'super':
            top_x, top_y = 0.4442708333333, 0.4185185185185
            mid_x, mid_y = 0.3078125, 0.5388888888889
            bot_x, bot_y = 0.4338541666667, 0.6277777777778
        elif m in ('sub', 'boat'):
            top_x, top_y = 0.5947916666667, 0.2638888888889
            mid_x, mid_y = 0.5416666666667, 0.2583333333333
            bot_x, bot_y = 0.5635416666667, 0.3342592592593
        else:
            top_x, top_y = 0.4442708333333, 0.4185185185185
            mid_x, mid_y = 0.4265625, 0.5555555555556
            bot_x, bot_y = 0.4213541666667, 0.7

        top = Monkey(m, top_x, top_y)
        top.upgrade(['1-0-0', '2-0-0', '3-0-0', '4-0-0', '5-0-0'])

        mid = Monkey(m, mid_x, mid_y)
        mid.upgrade(['0-1-0', '0-2-0', '0-3-0', '0-4-0', '0-5-0'])

        bot = Monkey(m, bot_x, bot_y)
        if m == 'village':
            Monkey('farm', 0.5401041666667, 0.637037037037)
        bot.upgrade(['0-0-1', '0-0-2', '0-0-3', '0-0-4', '0-0-5'])

        top.sell()
        mid.sell()
        bot.sell()

    print('--Upgrades checked--')

if __name__ == '__main__':
    adjust_upg_deltas(listed_monkeys)