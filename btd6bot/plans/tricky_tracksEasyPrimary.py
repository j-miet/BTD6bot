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

def play(rounds):
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start, rounds[2])
        if current_round == BEGIN:     
            hero = Hero(0.4140625, 0.4240740740741)
            dart = Monkey('dart', 0.4880208333333, 0.6296296296296)
        elif current_round == 3:
            desp = Monkey('desperado', 0.5171875, 0.5851851851852)
        elif current_round == 4:
            dart2 = Monkey('dart', 0.4411458333333, 0.3888888888889)
        elif current_round == 6:
            desp2 = Monkey('desperado', 0.3661458333333, 0.4833333333333)
        elif current_round == 10:
            dart2.upgrade(['0-0-1','0-0-2','0-0-3'])
        elif current_round == 11:
            dart2.upgrade(['0-1-3','0-2-3'])
        elif current_round == 14:
            dart.upgrade(['0-0-1','0-0-2','0-0-3'])
        elif current_round == 15:
            dart.upgrade(['0-1-3','0-2-3'])
        elif current_round == 18:
            boomer1 = Monkey('boomer', 0.4473958333333, 0.6037037037037) 
            boomer1.target('strong')
            boomer1.upgrade(['0-0-1','0-0-2'])
        elif current_round == 21:
            boomer2 = Monkey('boomer', 0.3661458333333, 0.4092592592593)
            boomer2.target('strong')
            boomer2.upgrade(['0-0-1','0-0-2'])
        elif current_round == 25:
            boomer1.upgrade(['1-0-2','2-0-2','3-0-2'])
        elif current_round == 27:
            boomer2.upgrade(['1-0-2','2-0-2','3-0-2'])
        elif current_round == 31:
            dart.upgrade(['0-2-4'])
        elif current_round == 34:
            dart2.upgrade(['0-2-4'])
        elif current_round == 35:
            boomer3 = Monkey('boomer', 0.5140625, 0.5166666666667)
            boomer3.target('close')
            boomer3.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif current_round == 37:
            boomer1.upgrade(['4-0-2'])
        elif current_round == 39:
            boomer2.upgrade(['4-0-2'])
            boomer3.upgrade(['4-0-2'])
        elif current_round == 40:
            ability(1)