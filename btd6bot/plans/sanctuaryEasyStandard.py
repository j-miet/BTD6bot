"""
[Hero] Psi
[Monkey Knowledge] -
---------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-1
boomer 4-0-2

sniper 3-1-2
_______________________________________
Derived from sanctuary_HardChimps.
"""

from._plan_imports import *

def play(rounds: tuple[str, str, str, int, int, str]) -> None:
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start, rounds[2])
        if current_round == BEGIN:
            sniper_bot1 = Monkey('sniper', 0.6453125, 0.762037037037)
            sniper_bot2 = Monkey('sniper', 0.6651041666667, 0.8074074074074)
            sniper_bot2.target('strong')
        elif current_round == 3:
            sniper_bot3 = Monkey('sniper', 0.7536458333333, 0.8796296296296)
        elif current_round == 7:
            dart_left2 = Monkey('dart', 0.3348958333333, 0.4546296296296)
        elif current_round == 8:
            dart_right2 = Monkey('dart', 0.6302083333333, 0.4342592592593)
        elif current_round == 10:
            sniper1 = Monkey('sniper', 0.4072916666667, 0.0611111111111)
        elif current_round == 14:
            hero = Hero(0.3833333333333, 0.1064814814815)
            hero.target('strong')
        elif current_round == 17:
            boomerang = Monkey('boomer', 0.5, 0.2546296296296)
        elif current_round == 18:
            boomerang.upgrade(['1-0-0', '1-0-1', '2-0-1'], cpos_x=0.425, cpos_y=0.275)
        elif current_round == 20:
            sniper1.upgrade(['0-0-1'], cpos_x=0.40625, cpos_y=0.0564814814815)
        elif current_round == 21:
            sniper1.upgrade(['1-0-1'], cpos_x=0.488, cpos_y=0.025)
            sniper1.target('strong')
        elif current_round == 23:
            ability(1, 1)
            sniper1.target('first', cpos_x=0.333, cpos_y=0.0354814814815)
        elif current_round == 24:
            boomerang.upgrade(['3-0-1'], cpos_x=0.4260416666667, cpos_y=0.2722222222222)
        elif current_round == 26:
            sniper1.upgrade(['1-0-2'], cpos_x=0.4104166666667, cpos_y=0.0592592592593)
        elif current_round == 27:
            sniper2 = Monkey('sniper', 0.3895833333333, 0.0444444444444)
        elif current_round == 28:
            sniper2.upgrade(['1-0-0', '1-1-0'], cpos_x=0.4645833333333, cpos_y=0.0574074074074)
        elif current_round == 30:
            sniper1.target('strong', cpos_x=0.4104166666667, cpos_y=0.0592592592593)
        elif current_round == 31:
            ability(1, 1)
            sniper1.target('first', cpos_x=0.333, cpos_y=0.0354814814815)
        elif current_round == 35:
            boomerang.upgrade(['4-0-1', '4-0-2'], cpos_x=0.35, cpos_y=0.2564814814815)
        elif current_round == 36:
            sniper1.upgrade(['2-0-2'], cpos_x=0.4104166666667, cpos_y=0.0592592592593)
        elif current_round == 38:
            ability(1, 1)
        elif current_round == 39:
            sniper1.upgrade(['3-0-2'], cpos_x=0.333, cpos_y=0.0354814814815)
        elif current_round == 40: 
            ability(1, 1)