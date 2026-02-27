"""Tests for checking upgrade path ocr matching."""

import time

from bot import _maindata, kb_mouse
from bot.commands.monkey import Monkey
from bot.locations import get_click, get_text
from bot.menu_start import _choose_map, _choose_diff
from bot.ocr.ocr import weak_substring_check
from bot.ocr.ocr_reader import OCR_READER

# Uncomment lines below for logging purposes
#_maindata.maindata["bot_vars"]["logging"] = True
#_maindata.maindata["bot_vars"]["delta_ocrtext"] = True
#_maindata.maindata["bot_vars"]["substring_ocrtext"] = True

def test_upgrades(capsys) -> None:
    timer = time.time()
    while not weak_substring_check("Play", get_text('menu', 'menu_playtext'), OCR_READER):
        if time.time()-timer >= 10:
            assert "Failed to find main menu screen" == False # this prevents test from continuing
            return
        print("Searching for main menu screen...")
        time.sleep(1)
    print("Menu screen found!\nStarting tests - Don't touch keyboard or mouse during tests.")
    captured = capsys.readouterr()
    assert captured.out == "Menu screen found!\nStarting tests - Don't touch keyboard or mouse during tests.\n"
    for t in range(3, 0, -1):
        print(str(t), end=' ', flush=True)
        time.sleep(1)
    print()

    _choose_map('in the loop')
    _choose_diff('EASY')
    kb_mouse.click(get_click('modes', 'bottom_left'))
    _maindata.maindata["bot_vars"]["checking_time_limit"] = 10
    
    while not weak_substring_check("Upgrades", get_text('ingame','upgrade_text'), OCR_READER):
        print("Waiting map screen...")
        kb_mouse.click((0.5036458333333, 0.7064814814815))
        time.sleep(1)
    capsys.readouterr()
    print("Map screen found!")
    captured = capsys.readouterr()
    assert captured.out == "Map screen found!\n"

    monkeys = list(Monkey._MONKEY_NAMES[:])
    monkeys.remove('hero')
    monkeys.remove('beast')  # remove this after beast merging has been implemented.

    succesful_upgs: list[str] = []

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
        assert (top._name, top._pos_x, top._pos_y) == (m, top_x, top_y)
        assert top._upgrade_path == '0-0-0'
        top.upgrade(['1-0-0', '2-0-0', '3-0-0', '4-0-0', '5-0-0'])
        assert top._upgrade_path == '5-0-0'

        mid = Monkey(m, mid_x, mid_y)
        assert (mid._name, mid._pos_x, mid._pos_y) == (m, mid_x, mid_y)
        assert mid._upgrade_path == '0-0-0'
        mid.upgrade(['0-1-0', '0-2-0', '0-3-0', '0-4-0', '0-5-0'])
        assert mid._upgrade_path == '0-5-0'

        bot = Monkey(m, bot_x, bot_y)
        assert (bot._name, bot._pos_x, bot._pos_y) == (m, bot_x, bot_y)
        assert bot._upgrade_path == '0-0-0'
        if m == 'village':
            Monkey('farm', 0.5401041666667, 0.637037037037)
        bot.upgrade(['0-0-1', '0-0-2', '0-0-3', '0-0-4', '0-0-5'])
        assert bot._upgrade_path == '0-0-5'

        succesful_upgs.append(m)
        top.sell()
        mid.sell()
        bot.sell()

    assert succesful_upgs == monkeys

    print("Returning to main menu.")
    time.sleep(1)
    kb_mouse.click((0.05, 0.15))
    time.sleep(1)
    kb_mouse.press_esc()
    time.sleep(1)
    kb_mouse.click((0.4458333333333, 0.7814814814815))
    print('All upgrade tests finished.')
    captured = capsys.readouterr()
    assert captured.out == "All upgrade tests finished.\n"