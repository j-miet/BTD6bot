"""
[Hero] -
[Monkey Knowledge] -
---------------------------------------------------------------
===Monkeys & upgrades required===
druid 1-3-0

sniper 2-2-4
_______________________________________
"""

from._plan_imports import *

def play(rounds):
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start, rounds[2])
        if current_round == BEGIN:
            sniper1 = Monkey('sniper', 0.6161458333333, 0.7648148148148)
            sniper2 = Monkey('sniper', 0.6505208333333, 0.7925925925926)
            sniper2.target('strong')
        elif current_round == 3:
            sniper3 = Monkey('sniper', 0.7567708333333, 0.9324074074074)
        elif current_round == 6:
            druid = Monkey('druid', 0.2328125, 0.4416666666667)
        elif current_round == 10:
            druid.upgrade(['0-1-0'], cpos=(0.1307291666667, 0.287962962963))
        elif current_round == 12:
            druid.upgrade(['0-2-0','0-3-0'], cpos=(0.1359375, 0.2990740740741))
        elif current_round == 13:
            druid.upgrade(['1-3-0'], cpos=(0.1619791666667, 0.3842592592593))
            druid.target('strong')
        elif current_round == 16:
            sniper1.upgrade(['0-1-0','0-2-0'], cpos=(0.7234375, 0.8194444444444))
        elif current_round == 19:
            sniper1.upgrade(['0-2-1','0-2-2'], cpos=(0.6567708333333, 0.7824074074074))
        elif current_round == 27:
            sniper1.upgrade(['0-2-3'], cpos=(0.7619791666667, 0.8509259259259))
        elif current_round == 34:
            sniper1.upgrade(['0-2-4'], cpos=(0.7203125, 0.825))
        elif current_round == 38:
            sniper2.upgrade(['1-0-0','1-0-1','1-0-2','1-0-3'], cpos=(0.7619791666667, 0.8601851851852))
        elif current_round == 39:
            sniper2.upgrade(['2-0-3'], cpos=(0.8026041666667, 0.8953703703704))