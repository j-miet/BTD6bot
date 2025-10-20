"""
[Hero] Sauda
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0

sniper 1-2-4
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
            dart1 = Monkey('dart', 0.2088541666667, 0.5185185185185)
            dart2 = Monkey('dart', 0.6677083333333, 0.5259259259259)
            dart3 = Monkey('dart', 0.4072916666667, 0.237037037037)
        elif current_round == 4:
            sniper = Monkey('sniper', 0.284375, 0.2712962962963)
            sniper.target('strong')
        elif current_round == 6:
            Hero(0.4614583333333, 0.2351851851852)
        elif current_round == 9:
            sniper2 = Monkey('sniper', 0.2380208333333, 0.3166666666667)
        elif current_round == 11:
            sniper2.upgrade(['0-0-1','0-0-2'])
        elif current_round == 14:
            sniper2.upgrade(['0-1-2','0-2-2'])
        elif current_round == 21:
            sniper.upgrade(['0-0-1','0-0-2'])
        elif current_round == 25:
            sniper2.upgrade(['0-2-3'])
        elif current_round == 27:
            sniper.upgrade(['1-0-2'])
        elif current_round == 34:
            sniper2.upgrade(['0-2-4'])
        elif current_round == 36:
            sniper.upgrade(['1-0-3'])
        elif current_round == 39:
            sniper.upgrade(['2-0-3'])

