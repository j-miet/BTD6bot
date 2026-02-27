"""
[Hero] Psi
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-1
boomer 4-0-2
glue 4-2-0

sniper 3-1-2

alch 4-0-1
mermonkey 2-0-4

village 3-2-0
_______________________________________
"""

from._plan_imports import *

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:
            sniper_bot1 = Monkey('sniper', 0.6453125, 0.762037037037)
        elif round == 2:
            sniper_bot2 = Monkey('sniper', 0.7171875, 0.8462962962963)
            sniper_bot2.target('strong')
        elif round == 4:
            sniper_bot3 = Monkey('sniper', 0.7671875, 0.9)
        elif round == 7:
            dart_left2 = Monkey('dart', 0.3348958333333, 0.4546296296296)
        elif round == 8:
            dart_right2 = Monkey('dart', 0.6302083333333, 0.4342592592593)
        elif round == 10:
            sniper1 = Monkey('sniper', 0.4072916666667, 0.0611111111111)
        elif round == 14:
            hero = Hero(0.3833333333333, 0.1064814814815)
            hero.target('strong')
        elif round == 17:
            boomerang = Monkey('boomer', 0.5, 0.2546296296296)
        elif round == 18:
            boomerang.upgrade(['1-0-0', '1-0-1', '2-0-1'], cpos=(0.425, 0.275))
        elif round == 20:
            sniper1.upgrade(['0-0-1'], cpos=(0.40625, 0.0564814814815))
        elif round == 21:
            sniper1.upgrade(['1-0-1'], cpos=(0.488, 0.025))
            sniper1.target('strong')
        elif round == 23:
            ability(1, 1)
            sniper1.target('first', cpos=(0.333, 0.0354814814815))
        elif round == 24:
            boomerang.upgrade(['3-0-1'], cpos=(0.4260416666667, 0.2722222222222))
        elif round == 26:
            sniper1.upgrade(['1-0-2'], cpos=(0.4104166666667, 0.0592592592593))
        elif round == 27:
            sniper2 = Monkey('sniper', 0.3895833333333, 0.0444444444444)
            sniper2.special(1)
        elif round == 28:
            sniper2.upgrade(['1-0-0', '1-1-0'], cpos=(0.4645833333333, 0.0574074074074))
        elif round == 30:
            sniper1.target('strong', cpos=(0.4104166666667, 0.0592592592593))
        elif round == 31:
            ability(1, 1)
            sniper1.target('first', cpos=(0.333, 0.0354814814815))
        elif round == 35:
            boomerang.upgrade(['4-0-1', '4-0-2'], cpos=(0.35, 0.2564814814815))
        elif round == 36:
            sniper1.upgrade(['2-0-2'], cpos=(0.4104166666667, 0.0592592592593))
        elif round == 38:
            ability(1, 1)
        elif round == 39:
            sniper1.upgrade(['3-0-2'], cpos=(0.333, 0.0354814814815))
            village = Monkey('village', 0.3729166666667, 0.125)
        elif round == 40: 
            ability(1, 1)
        elif round == 41:
            village.upgrade(['0-1-0', '0-2-0'], cpos=(0.5260416666667, 0.1453703703704))
        elif round == 42:
            mermonkey1 = Monkey('mermonkey', 0.3875, 0.2361111111111)
        elif round == 43:
            mermonkey1.upgrade(['1-0-0', '2-0-0', '2-0-1', '2-0-2'], cpos=(0.3114583333333, 0.2287037037037))
        elif round == 45:
            mermonkey1.upgrade(['2-0-3'], cpos=(0.4583333333333, 0.2231481481481))
        elif round == 49:
             mermonkey1.upgrade(['2-0-4'], cpos=(0.459375, 0.2212962962963))
             mermonkey1.special(1, 0.4395833333333, 0.3731481481481)
             alch1 = Monkey('alch', 0.5041666666667, 0.1972222222222)
             alch1.upgrade(['1-0-0', '2-0-0', '3-0-0', '3-0-1'])
        elif round == 50:
             alch1.upgrade(['4-0-1'], cpos=(0.4322916666667, 0.2064814814815))
        elif round == 52:
             village.upgrade(['1-2-0', '2-2-0'], cpos=(0.446375, 0.1111037037037))
        elif round == 53:
            glue = Monkey('glue', 0.5385416666667, 0.2064814814815)
        elif round == 54:
            glue.upgrade(['1-0-0', '2-0-0', '3-0-0', '3-1-0'], cpos=(0.4666666666667, 0.2231481481481))
        elif round == 55:
            glue.upgrade(['3-2-0'], cpos=(0.3927083333333, 0.2027777777778))
        elif round == 57:
            ability(1, 4)
            glue.upgrade(['4-2-0'], cpos=(0.5416666666667, 0.2046296296296))
        elif round == 58:
            village.upgrade(['3-2-0'], cpos=(0.453125, 0.1490740740741))