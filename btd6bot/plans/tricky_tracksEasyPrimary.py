"""
[Hero] Quincy
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-2-4
boomer 4-0-2
desperado 0-0-0
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
            hero = Hero(0.4140625, 0.4040740740741)
            dart = Monkey('dart', 0.4880208333333, 0.6196296296296)
        elif round == 3:
            desp = Monkey('desperado', 0.5171875, 0.5751851851852)
        elif round == 4:
            dart2 = Monkey('dart', 0.4411458333333, 0.3588888888889)
        elif round == 6:
            desp2 = Monkey('desperado', 0.3661458333333, 0.4633333333333)
        elif round == 10:
            dart2.upgrade(['0-0-1','0-0-2','0-0-3'])
        elif round == 11:
            dart2.upgrade(['0-1-3','0-2-3'])
        elif round == 14:
            dart.upgrade(['0-0-1','0-0-2','0-0-3'])
        elif round == 15:
            dart.upgrade(['0-1-3','0-2-3'])
        elif round == 18:
            boomer1 = Monkey('boomer', 0.4473958333333, 0.5937037037037) 
            boomer1.target('strong')
            boomer1.upgrade(['0-0-1','0-0-2'])
        elif round == 21:
            boomer2 = Monkey('boomer', 0.3661458333333, 0.3892592592593)
            boomer2.target('strong')
            boomer2.upgrade(['0-0-1','0-0-2'])
        elif round == 25:
            boomer1.upgrade(['1-0-2','2-0-2','3-0-2'])
        elif round == 27:
            boomer2.upgrade(['1-0-2','2-0-2','3-0-2'])
        elif round == 31:
            dart.upgrade(['0-2-4'])
        elif round == 34:
            dart2.upgrade(['0-2-4'])
        elif round == 35:
            boomer3 = Monkey('boomer', 0.5140625, 0.5066666666667)
            boomer3.target('close')
            boomer3.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif round == 36:
            ability(1)
        elif round == 37:
            boomer1.upgrade(['4-0-2'])
        elif round == 39:
            boomer2.upgrade(['4-0-2'])
            boomer3.upgrade(['4-0-0'])
        elif round == 40:
            ability(1)