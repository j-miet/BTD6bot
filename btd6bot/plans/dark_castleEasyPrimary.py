"""
[Hero] Quincy
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-2-4
boomer 0-4-2
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
            hero = Hero(0.3838541666667, 0.3972222222222)
        elif round == 2:
            boomer = Monkey('boomer', 0.2994791666667, 0.4490740740741)
            boomer.target('strong')
        elif round == 4:
            boomer.upgrade(['0-0-1','0-0-2'])
        elif round == 6:
            dart1 = Monkey('dart', 0.4369791666667, 0.4157407407407)
        elif round == 8:
            dart1.upgrade(['0-0-1','0-0-2'])
        elif round == 10:
            dart1.upgrade(['0-0-3','0-1-3','0-2-3'])
        elif round == 15:
            dart2 = Monkey('dart', 0.3526041666667, 0.337962962963)
            dart2.upgrade(['0-0-1','0-0-2','0-0-3'])
        elif round == 16:
            dart2.upgrade(['0-1-3','0-2-3'])
        elif round == 22:
            dart1.upgrade(['0-2-4'])
        elif round == 28:
            dart2.upgrade(['0-2-4'])
        elif round == 33:
            boomer.upgrade(['0-1-2','0-2-2','0-3-2'])
        elif round == 36:
            boomer.upgrade(['0-4-2'])
        elif round == 40:
            ability(1)
            ability(2)