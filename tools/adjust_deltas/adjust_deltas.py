"""Creates a file of adjusted upgrade delta values.

Created file can be copied to btd6bot/Files to overwrite ocr_upgrade_data.json.

** HOW TO USE **
-enter 'Spa Pits' map in sandbox mode (difficulty doesn't matter) first
-then run this script and wait until it displays the text "Done! Press Enter to close this script." and press enter

User is asked two inputs:  
-list of monkeys they wish to adjust deltas for, each name separated with a space.  
 =>To check all monkeys, type 'all' and nothing else.  
-delta adjust value which is used to lower all delta values equally. This is not useful but actually required, as when  
 running an actual plan, it's unlikely you can match the exact deltas. So lowering them all by few tenths of a decimal
 keeps majority of deltas high enough and avoids matching errors. However, some upgrade paths might still cause issues
 because they have very similar names: 0-1-0 dart 'quick shots' and '0-2-0' 'very quick shots' would be such example.
 You might need to adjust these manually afterwards by increasing their respective deltas by 0.01-0.02.  

Notes:
-ocr checks are performed both on right and left upgrade panels so all monkeys and their paths are upgraded twice. The 
 reason is that on some upgrades, side matter quite a bit and gives different delta. After upgrades on both sides have 
 been done, the smaller delta value is ultimately saved.
"""

import sys
import pathlib
import json
import time

sys.path.append(str(pathlib.Path(__file__).parent.parent.parent/'btd6bot'))

from bot import kb_mouse
from bot.bot_vars import BotVars
from bot.commands.monkey import Monkey, _MonkeyConstants
from bot.kb_mouse import ScreenRes
from bot.ocr.ocr import weak_substring_check, OcrValues
from bot.ocr.ocr_reader import OCR_READER
from bot.rounds import Rounds

def get_positions(monkey: str, panel_loc: str) -> tuple[float, float, float, float, float, float]:
    if panel_loc == 'left':
        if monkey == 'super':
            lefttop_x, lefttop_y = 0.7609375, 0.4666666666667
            leftmid_x, leftmid_y = 0.7557291666667, 0.6407407407407
            leftbot_x, leftbot_y = 0.6859375, 0.7314814814815
        elif monkey in ('sub', 'boat'):
            lefttop_x, lefttop_y = 0.6036458333333, 0.387037037037
            leftmid_x, leftmid_y = 0.6734375, 0.4333333333333
            leftbot_x, leftbot_y = 0.6130208333333, 0.5055555555556
        else:
            lefttop_x, lefttop_y = 0.7911458333333, 0.4537037037037
            leftmid_x, leftmid_y = 0.7494791666667, 0.5888888888889
            leftbot_x, leftbot_y = 0.6932291666667, 0.7277777777778
        return lefttop_x, lefttop_y, leftmid_x, leftmid_y, leftbot_x, leftbot_y
    elif panel_loc == 'right':
        if monkey == 'super':
            righttop_x, righttop_y = 0.1213541666667, 0.5092592592593
            rightmid_x, rightmid_y = 0.2140625, 0.6555555555556
            rightbot_x, rightbot_y = 0.1109375, 0.7203703703704
        elif monkey in ('sub', 'boat'):
            righttop_x, righttop_y = 0.2067708333333, 0.3574074074074
            rightmid_x, rightmid_y = 0.2786458333333, 0.3925925925926
            rightbot_x, rightbot_y = 0.2151041666667, 0.4962962962963
        else:
            righttop_x, righttop_y = 0.0890625, 0.5018518518519
            rightmid_x, rightmid_y = 0.1921875, 0.6444444444444
            rightbot_x, rightbot_y = 0.1651041666667, 0.8435185185185
        return righttop_x, righttop_y, rightmid_x, rightmid_y, rightbot_x, rightbot_y

def check_ocr(m: str, 
              top_x: float, top_y: float,
              mid_x: float, mid_y: float, 
              bot_x: float, bot_y: float
              ) -> None:
    if m == 'beast':
        beast_top1 = Monkey('beast', 0.5348958333333, 0.3351851851852)
        beast_top2 = Monkey('beast', 0.5734375, 0.2537037037037)
        beast_top3 = Monkey('beast', 0.6338541666667, 0.2277777777778)
        beast_top1.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0'])
        beast_top2.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0'])
        beast_top3.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0'])
        top = Monkey(m, top_x, top_y)
        top.upgrade(['1-0-0', '2-0-0', '3-0-0', '4-0-0'])
        beast_top1.merge(top_x, top_y)
        beast_top2.merge(top_x, top_y)
        beast_top3.merge(top_x, top_y)
        top.upgrade(['5-0-0'])

        beast_mid1 = Monkey('beast', 0.5265625, 0.0472222222222)
        beast_mid2 = Monkey('beast', 0.5807291666667, 0.0564814814815)
        beast_mid3 = Monkey('beast', 0.5473958333333, 0.1212962962963)
        beast_mid1.upgrade(['0-1-0','0-2-0','0-3-0','0-4-0'])
        beast_mid2.upgrade(['0-1-0','0-2-0','0-3-0','0-4-0'])
        beast_mid3.upgrade(['0-1-0','0-2-0','0-3-0','0-4-0'])
        mid = Monkey(m, mid_x, mid_y)
        mid.upgrade(['0-1-0', '0-2-0', '0-3-0', '0-4-0'])
        beast_mid1.merge(mid_x, mid_y)
        beast_mid2.merge(mid_x, mid_y)
        beast_mid3.merge(mid_x, mid_y)
        mid.upgrade(['0-5-0'])

        beast_bot1 = Monkey('beast', 0.3130208333333, 0.2314814814815)
        beast_bot2 = Monkey('beast', 0.2661458333333, 0.2)
        beast_bot3 = Monkey('beast', 0.2130208333333, 0.2074074074074)
        beast_bot1.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4'])
        beast_bot2.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4'])
        beast_bot3.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4'])
        bot = Monkey(m, bot_x, bot_y)
        bot.upgrade(['0-0-1', '0-0-2', '0-0-3', '0-0-4'])
        beast_bot1.merge(bot_x, bot_y)
        beast_bot2.merge(bot_x, bot_y)
        beast_bot3.merge(bot_x, bot_y)
        bot.upgrade(['0-0-5'])

        beast_top1.sell()
        beast_top2.sell()
        beast_top3.sell()
        beast_mid1.sell()
        beast_mid2.sell()
        beast_mid3.sell()
        beast_bot1.sell()
        beast_bot2.sell()
        beast_bot3.sell()
    
    else:
        top = Monkey(m, top_x, top_y)
        top.upgrade(['1-0-0', '2-0-0', '3-0-0', '4-0-0', '5-0-0'])

        mid = Monkey(m, mid_x, mid_y)
        mid.upgrade(['0-1-0', '0-2-0', '0-3-0', '0-4-0', '0-5-0'])

        bot = Monkey(m, bot_x, bot_y)
        if m == 'village':
            if bot_x >= 0.65:
                Monkey('farm', 0.8109375, 0.7574074074074)
            else:
                Monkey('farm', 0.0630208333333, 0.7277777777778)
        bot.upgrade(['0-0-1', '0-0-2', '0-0-3', '0-0-4', '0-0-5'])
    top.sell()
    mid.sell()
    bot.sell()

def adjust_upg_deltas(check_monkeys: list[str], delta_adjust: int, wipe: bool = False) -> None:
    monkeys: list[str] = []
    if check_monkeys == ['all']:
        monkeys = list(_MonkeyConstants._MONKEY_NAMES[:])
        monkeys.remove('hero')
    else:
        for name in check_monkeys:
            if name in list(_MonkeyConstants._MONKEY_NAMES):
                monkeys.append(name)
    if monkeys == []:
        return
    
    if wipe:
        if BotVars.windowed == True:
            win = "windowed"
        else:
            win = "fullscreen"
        with open(pathlib.Path(__file__).parent/'ocr_deltas.json', 'w') as f:
            json.dump({"__identifier": [ScreenRes.width, ScreenRes.height, win]}, f, indent=2)
    
    BotVars.print_delta_ocrtext = True
    BotVars.checking_time_limit = 10
    OcrValues._log_ocr_deltas = True

    start = time.time()
    while not weak_substring_check('Upgrades', Rounds.UPGRADE_TEXT, OCR_READER):
        if time.time()-start > 20:
            print("Could not find map screen in 20 seconds, script halted.")
            return
        print("Waiting for map screen...")
        kb_mouse.click((0.5036458333333, 0.7064814814815))
        time.sleep(1)
    print("\n###")

    for m in monkeys:
        check_ocr(m, *get_positions(m, 'left'))
    left_deltas: dict = {}
    with open(pathlib.Path(__file__).parent/'ocr_deltas.json') as f:
        left_deltas = json.load(f) # left upgrade panel

    for m in monkeys:
        check_ocr(m, *get_positions(m, 'right'))
    right_deltas: dict = {}
    with open(pathlib.Path(__file__).parent/'ocr_deltas.json') as f:
        right_deltas: dict = json.load(f)  # right upgrade panel

    delta_dict: dict = left_deltas.copy()
    for key in left_deltas.keys():
        minval = min(left_deltas[key][1], right_deltas[key][1])
        delta_dict[key][1] = minval
    with open(pathlib.Path(__file__).parent/'ocr_deltas.json', 'w') as f:
        json.dump(delta_dict, f, indent=2)  # final deltas

    if delta_adjust > 0:
        adjust_val = delta_adjust*0.01
        print("---------------------------------------------------\n"
                "Adjusting deltas by given delta adjusting number...")
        with open(pathlib.Path(__file__).parent/'ocr_deltas.json') as f:
            adjusted_dict: dict = json.load(f)
        for key in adjusted_dict.keys():
            for m in monkeys:
                if m in str(key):
                    adjusted_dict[key][1] = round(adjusted_dict[key][1] - adjust_val, 2)
                    break
        with open(pathlib.Path(__file__).parent/'ocr_deltas.json', 'w') as f:
            json.dump(adjusted_dict, f, indent=2)  # adjusted final deltas

    input("Done! Press [Enter] to close this script.\n")

def run() -> None:
    screenres_input = input("Give screen resolution: format is WIDTH HEIGHT e.g. 1920 1080. Leave this empty to use "
                            "maximum monitor resolution.\n[resolution]=>")
    windowed_input = input("Windowed mode? Type 'YES' if you use windowed mode, or press [Enter] with empty input if "
                            "not.\n[windowed?]=>")
    monkeys_input = input(">Type the names of monkeys, each separated with space. Or type 'all' to check all monkeys. "
                          "\n[monkeys]=>")
    delta_input = input(">Give the delta adjusting number, an integer 0-9.\n This will decrease all deltas by flat "
                        "amount 0.01*delta e.g. 4 means 0.04.\nRecommended values: 3, 4 or 5.\n[delta value]=>")
    wipe_input = input(">Wipe all existing data from ocr_deltas.json?\nType 'YES' to wipe, or "
                        "anything else to continue without wipe\nWiping should be done if you have changed resolution "
                        "and/or windowed setting.\n[wipe data?]")
    wipe_val = False
    res = screenres_input.strip().split()
    if len(res) == 2:
        ScreenRes.width, ScreenRes.height = int(res[0]), int(res[1])
    if windowed_input == 'YES':
        BotVars.windowed = True
    if wipe_input == 'YES':
        wipe_val = True
    if delta_input == '':
        delta_input = 0
    elif 0 <= int(delta_input) <= 9:
        monkey_list = monkeys_input.split()
        input("Setup complete. Make sure you have BTD6 opened and entered 'Spa Pits' map in sandbox mode.\n"
                "Then press [Enter] to begin.")
        adjust_upg_deltas(monkey_list, int(delta_input), wipe_val)