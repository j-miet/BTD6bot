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

def play(rounds):
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start, rounds[2])
        if current_round == BEGIN:
            sniper = Monkey('sniper', 0.4348958333333, 0.2018518518519)
            sniper2 = Monkey('sniper', 0.4473958333333, 0.2703703703704)
            sniper2.target('strong')
        elif current_round == 3:
            sub = Monkey('sub', 0.6546875, 0.4888888888889)
        elif current_round == 4:
            sub.upgrade(['1-0-0'])
        elif current_round == 6:
            dart = Monkey('dart', 0.2307291666667, 0.5555555555556)
        elif current_round == 8:
            sub.upgrade(['2-0-0'])
        elif current_round == 9:
            sub.upgrade(['2-0-1'])
        elif current_round == 13:
            sub.upgrade(['2-0-2'])
        elif current_round == 14:
            dart.upgrade(['0-0-1'])
        elif current_round == 18:
            ace = Monkey('ace', 0.4515625, 0.7907407407407)
            ace.upgrade(['0-0-1'])
        elif current_round == 23:
            sniper.upgrade(['0-1-0'])
            ace.upgrade(['0-0-2'])
        elif current_round == 27:
            sniper2.upgrade(['1-0-0'])
        elif current_round == 28:
            ace.upgrade(['0-0-3'])
        elif current_round == 31:
            ace.upgrade(['1-0-3','2-0-3'])
        elif current_round == 34:
            sniper.upgrade(['0-2-0','0-2-1','0-2-2'])
        elif current_round == 36:
            sniper.upgrade(['0-2-3'])
        elif current_round == 37:
            alch = Monkey('alch', 0.4640625, 0.8814814814815)
            alch.upgrade(['1-0-0','2-0-0'])
        elif current_round == 38:
            alch.upgrade(['3-0-0'])
        elif current_round == 39:
            sub.upgrade(['2-0-3'])