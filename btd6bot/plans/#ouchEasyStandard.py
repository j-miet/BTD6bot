"""
[Hero] Sauda
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0

sniper 1-2-4
boat 3-2-0
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
            dart = Monkey('dart', 0.2833333333333, 0.2962962962963)
            sniper = Monkey('sniper', 0.728125, 0.7740740740741)
        elif round == 2:
            sniper2 = Monkey('sniper', 0.7791666666667, 0.7777777777778)
            sniper2.target('strong')
        elif round == 4:
            dart2 = Monkey('dart', 0.2822916666667, 0.6203703703704)
        elif round == 7:
            Hero(0.2848958333333, 0.4)
        elif round == 9:
            boat = Monkey('boat', 0.4234375, 0.5037037037037)
        elif round == 11:
            boat.upgrade(['1-0-0','2-0-0'])
        elif round == 14:
            sniper.upgrade(['0-0-1','0-0-2'])
        elif round == 17:
            sniper.upgrade(['0-1-2','0-2-2'])
        elif round == 20:
            sniper2.upgrade(['1-0-0'])
        elif round == 21:
            boat.upgrade(['2-1-0'])
        elif round == 27:
            sniper.upgrade(['0-2-3'])
        elif round == 29:
            sniper2.upgrade(['1-0-1','1-0-2'])
        elif round == 35:
            boat.upgrade(['3-1-0','3-2-0'])
        elif round == 38:
            sniper.upgrade(['0-2-4'])