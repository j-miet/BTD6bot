"""Creates a file of adjusted upgrade delta values."""

from typing import Any
import pathlib
import json
import os
import time

from bot import kb_mouse
from bot.bot_vars import BotVars
from bot.commands.monkey import Monkey
from bot.locations import get_click, get_text
from bot.kb_mouse import ScreenRes
from bot.menu_start import _choose_map, _choose_diff
from bot.ocr.ocr import weak_substring_check, OcrValues
from bot.ocr.ocr_reader import OCR_READER
from customprint import cprint
from utils import timing

_TEMPFILE_PATH = pathlib.Path(__file__).parent.parent/'Files'/'.temp_upg_deltas.json'

def _get_positions(monkey: str, panel_loc: str) -> tuple[float, float, float, float, float, float]:
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
    else:
        return 0, 0, 0, 0, 0, 0

def _check_ocr(m: str, 
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
        beast_mid1 = Monkey('beast', 0.5265625, 0.0472222222222)
        beast_mid2 = Monkey('beast', 0.5807291666667, 0.0564814814815)
        beast_mid3 = Monkey('beast', 0.5473958333333, 0.1212962962963)
        beast_mid1.upgrade(['0-1-0','0-2-0','0-3-0','0-4-0'])
        beast_mid2.upgrade(['0-1-0','0-2-0','0-3-0','0-4-0'])
        beast_mid3.upgrade(['0-1-0','0-2-0','0-3-0','0-4-0'])
        beast_bot1 = Monkey('beast', 0.3130208333333, 0.2314814814815)
        beast_bot2 = Monkey('beast', 0.2661458333333, 0.2)
        beast_bot3 = Monkey('beast', 0.2130208333333, 0.2074074074074)
        beast_bot1.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4'])
        beast_bot2.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4'])
        beast_bot3.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4'])

        top = Monkey(m, top_x, top_y)
        top.upgrade(['1-0-0', '2-0-0', '3-0-0', '4-0-0'])
        beast_top1.merge(top_x, top_y)
        beast_top2.merge(top_x, top_y)
        beast_top3.merge(top_x, top_y)
        top.upgrade(['5-0-0'])

        mid = Monkey(m, mid_x, mid_y)
        mid.upgrade(['0-1-0', '0-2-0', '0-3-0', '0-4-0'])
        beast_mid1.merge(mid_x, mid_y)
        beast_mid2.merge(mid_x, mid_y)
        beast_mid3.merge(mid_x, mid_y)
        mid.upgrade(['0-5-0'])

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

def _adjust_upg_deltas(check_monkeys: list[str], delta_adjust: int) -> None:
    """Check if upgrade_current.json dictionary has all required keys and values.

    If not, use _ocr_upgradedata.json base values instead. This also means all monkeys are adjusted,
    even if list of checked monkeys was a sublist.
    """
    base_dict: dict[str, Any] = {}
    current_dict: dict[str, Any] = {}
    with open(pathlib.Path(__file__).parent.parent/'Files'/'_ocr_upgradedata.json') as base:
        base_dict = json.load(base)
    try:
        with open(pathlib.Path(__file__).parent.parent/'Files'/'upgrades_current.json') as current:
            current_dict = json.load(current)
    except FileNotFoundError:
        ...
    base_keys = base_dict.keys()
    current_keys = current_dict.keys()
    baseval_flag = 0
    for key in base_keys:
        if key not in current_keys:
            cprint("Current upgrades file has missing keys.\nALL monkeys will be adjusted.\n///")
            with open(_TEMPFILE_PATH, 'w') as tempf:
                json.dump(base_dict, tempf, indent=2)
            baseval_flag = 1
            break
        elif current_dict[key][0] != base_dict[key][0]:
            cprint("Mismatch in one or more current upgrade names.\nALL monkeys will be adjusted.\n///")
            with open(_TEMPFILE_PATH, 'w') as tempf:
                json.dump(base_dict, tempf, indent=2)
            baseval_flag = 1
            break
    if not baseval_flag:
        with open(_TEMPFILE_PATH, 'w') as tempf:
            json.dump(current_dict, tempf, indent=2)
        
    monkeys: list[str] = []
    if check_monkeys == ['all'] or baseval_flag:
        monkeys = list(Monkey._MONKEY_NAMES[:])
        monkeys.remove('hero')
    else:
        for name in check_monkeys:
            if name in list(Monkey._MONKEY_NAMES):
                monkeys.append(name)
    if monkeys == []:
        return
    
    BotVars.print_delta_ocrtext = True
    BotVars.checking_time_limit = 10
    OcrValues._log_ocr_deltas = True

    cprint("\nSearching for main menu screen...", end='')
    while not weak_substring_check('Play', get_text('menu', 'menu_playtext'), OCR_READER):
        time.sleep(0.5)
    cprint(" <Menu detected>\n")
    cprint("-Updating values will take a while.\n"
            "-Do not use mouse or keyboard during this process.")
    cprint("Starting in... ", end='')
    timing.counter(5)
    cprint("\n--Begin--")

    _choose_map('spa pits')
    _choose_diff('EASY')
    kb_mouse.click(get_click('modes','bottom_left')) # sandbox mode

    start = time.time()
    cprint("\nWaiting for map screen...")
    while not weak_substring_check('Upgrades', get_text('ingame','upgrade_text'), OCR_READER):
        if time.time()-start > 20:
            cprint("Could not find map screen in 20 seconds, script halted.")
            return
        kb_mouse.click((0.5036458333333, 0.7064814814815))
        time.sleep(0.5)
    cprint("\n###")
    kb_mouse.click((0.5036458333333, 0.7064814814815))
    time.sleep(1)

    # left upgrade panel
    for m in monkeys:
        cprint(f"=={m}==")
        _check_ocr(m, *_get_positions(m, 'left'))
    left_deltas: dict[str, Any] = {}
    with open(_TEMPFILE_PATH) as f:
        left_deltas = json.load(f)

    # right upgrade panel
    for m in monkeys:
        cprint(f"=={m}==")
        _check_ocr(m, *_get_positions(m, 'right'))
    right_deltas: dict[str, Any] = {}
    with open(_TEMPFILE_PATH) as f:
        right_deltas = json.load(f)

    # final deltas i.e. pick the smaller of left and right value
    delta_dict: dict[str, Any] = left_deltas.copy()
    for key in left_deltas.keys():
        minval = min(left_deltas[key][1], right_deltas[key][1])
        delta_dict[key][1] = minval
    with open(_TEMPFILE_PATH, 'w') as f:
        json.dump(delta_dict, f, indent=2)

    # adjusted final deltas
    if delta_adjust > 0:
        adjust_val = delta_adjust*0.01
        cprint("---------------------------------------------------\n"
                "Adjusting ocr deltas based on delta value...")
        with open(_TEMPFILE_PATH) as f:
            adjusted_dict: dict[str, Any] = json.load(f)
        for key in adjusted_dict.keys():
            for m in monkeys:
                if m in str(key):
                    adjusted_dict[key][1] = round(adjusted_dict[key][1] - adjust_val, 2)
                    break
        with open(_TEMPFILE_PATH, 'w') as f:
            json.dump(adjusted_dict, f, indent=2)

    # update identifier key
    with open(_TEMPFILE_PATH) as f:
        upg_dict: dict[str, Any] = json.load(f)
    if BotVars.windowed:
        win = "windowed"
    else:
        win = "fullscreen"
    upg_dict["__identifier"] = [ScreenRes._width, ScreenRes._height, ScreenRes._w_shift, ScreenRes._h_shift, 
                                win, f"delta={delta_adjust}"]
    with open(_TEMPFILE_PATH, 'w') as f:
        json.dump(upg_dict, f, indent=2)

    with open(pathlib.Path(__file__).parent.parent/'Files'/'upgrades_current.json', 'w') as f:
        json.dump(upg_dict, f, indent=2)
    cprint("-Deltas updated in upgrades_current.json")
    warning_flag = 1
    for monkey_vals in upg_dict.keys():
        if monkey_vals != "__identifier" and upg_dict[monkey_vals][1] <= 0.5:
            if warning_flag:
                cprint("#!# Following deltas are unusually low #!#")
                warning_flag = 0
            cprint(f"{monkey_vals}, {upg_dict[monkey_vals][0]}: {upg_dict[monkey_vals][1]}")

    # automatically reset toggle value from settings after updating
    with open(pathlib.Path(__file__).parent.parent/'Files'/'gui_vars.json') as guivars_f:
        guivars_dict: dict[str, Any] = json.load(guivars_f)
    guivars_dict["ocr_adjust_deltas"] = False
    with open(pathlib.Path(__file__).parent.parent/'Files'/'gui_vars.json', 'w') as guivars_f:
        json.dump(guivars_dict, guivars_f, indent=4)
    cprint("-Auto-adjust set to False.\n")

    os.remove(_TEMPFILE_PATH)   # delete temp file .temp_upg_deltas.json
    time.sleep(2)
    kb_mouse.press_esc()
    time.sleep(1)
    kb_mouse.click((0.4442708333333, 0.7759259259259))

    while not weak_substring_check('Play', get_text('menu', 'menu_playtext'), OCR_READER):
        time.sleep(0.5)
    cprint("Adjusting process complete!")

def run() -> None:
    with open(pathlib.Path(__file__).parent.parent/'Files'/'gui_vars.json') as f:
        gui_vars_adjust_args: str = json.load(f)["adjust_args"]
    args_list = gui_vars_adjust_args.split()
    monkey_list: list[str]
    delta: int
    for args in args_list:
        if 'res=' in args:
            res_vals = args[4:].split('x')
            ScreenRes.update_res(int(res_vals[0]), int(res_vals[1]))
        elif 'win=' in args:
            win_val = int(args[4])
            if win_val == 1:
                BotVars.windowed = True
            elif win_val == 0:
                BotVars.windowed = False
        elif 'shift=' in args:
            shift_vals = args[6:].split('x')
            ScreenRes.update_shift(int(shift_vals[0]), int(shift_vals[1]))
        elif 'monkeys=' in args:
            monkey_list = args[8:].split(",")
        elif 'delta=' in args:
            delta_val = int(args[6:])
            if 0 <= delta_val <= 9:
                delta = delta_val       
    cprint("Updating upgrade deltas with following arguments:\n" \
            f"Resolution: {res_vals[0]}x{res_vals[1]}\n"
            f"Windowed: {BotVars.windowed}\n"
            f"Coordinate shift: {shift_vals[0]}x{shift_vals[1]}\n"
            f"Monkeys: {monkey_list}\n"
            f"Delta: {delta}\n\n"
            "=>Bot will next enter 'spa pits' map in sandbox mode.")
    _adjust_upg_deltas(monkey_list, delta)