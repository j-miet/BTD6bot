"""
[Hero] -
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-1

sniper 1-2-3
sub 2-0-3
ace 2-0-3

alch 3-0-0
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
            sniper = Monkey('sniper', 0.4348958333333, 0.2018518518519)
            sniper2 = Monkey('sniper', 0.4473958333333, 0.2703703703704)
            sniper2.target('strong')
        elif round == 3:
            sub = Monkey('sub', 0.6546875, 0.4888888888889)
        elif round == 4:
            sub.upgrade(['1-0-0'])
        elif round == 6:
            dart = Monkey('dart', 0.2307291666667, 0.5555555555556)
        elif round == 8:
            sub.upgrade(['2-0-0'])
        elif round == 9:
            sub.upgrade(['2-0-1'])
        elif round == 13:
            sub.upgrade(['2-0-2'])
        elif round == 14:
            dart.upgrade(['0-0-1'])
        elif round == 18:
            ace = Monkey('ace', 0.4515625, 0.7907407407407)
            ace.upgrade(['0-0-1'])
        elif round == 23:
            sniper.upgrade(['0-1-0'])
            ace.upgrade(['0-0-2'])
        elif round == 27:
            sniper2.upgrade(['1-0-0'])
        elif round == 28:
            ace.upgrade(['0-0-3'])
        elif round == 31:
            ace.upgrade(['1-0-3','2-0-3'])
        elif round == 34:
            sniper.upgrade(['0-2-0','0-2-1','0-2-2'])
        elif round == 36:
            sniper.upgrade(['0-2-3'])
        elif round == 37:
            alch = Monkey('alch', 0.4640625, 0.8814814814815)
            alch.upgrade(['1-0-0','2-0-0'])
        elif round == 38:
            alch.upgrade(['3-0-0'])
        elif round == 39:
            sub.upgrade(['2-0-3'])