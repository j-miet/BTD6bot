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

def play(rounds):
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start, rounds[2])
        if current_round == BEGIN:
            dart = Monkey('dart', 0.2833333333333, 0.2962962962963)
            sniper = Monkey('sniper', 0.728125, 0.7740740740741)
        elif current_round == 2:
            sniper2 = Monkey('sniper', 0.7791666666667, 0.7777777777778)
            sniper2.target('strong')
        elif current_round == 4:
            dart2 = Monkey('dart', 0.2822916666667, 0.6203703703704)
        elif current_round == 7:
            Hero(0.2848958333333, 0.4)
        elif current_round == 9:
            boat = Monkey('boat', 0.4234375, 0.5037037037037)
        elif current_round == 11:
            boat.upgrade(['1-0-0','2-0-0'])
        elif current_round == 14:
            sniper.upgrade(['0-0-1','0-0-2'])
        elif current_round == 17:
            sniper.upgrade(['0-1-2','0-2-2'])
        elif current_round == 20:
            sniper2.upgrade(['1-0-0'])
        elif current_round == 21:
            boat.upgrade(['2-1-0'])
        elif current_round == 27:
            sniper.upgrade(['0-2-3'])
        elif current_round == 29:
            sniper2.upgrade(['1-0-1','1-0-2'])
        elif current_round == 35:
            boat.upgrade(['3-1-0','3-2-0'])
        elif current_round == 38:
            sniper.upgrade(['0-2-4'])