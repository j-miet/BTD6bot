"""
[Hero] Sauda
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
sub 2-0-4

ninja 4-0-2
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
            dart = Monkey('dart', 0.5239583333333, 0.6185185185185)
            dart.upgrade(['0-1-0','0-2-0'])
        elif current_round == 3:
            dart.upgrade(['0-3-0','0-3-1'])
        elif current_round == 6:
            hero = Hero(0.2927083333333, 0.45)
        elif current_round == 8:
            ninja = Monkey('ninja', 0.3067708333333, 0.5648148148148)
        elif current_round == 10:
            ninja.upgrade(['1-0-0'])
        elif current_round == 12:
            ninja.upgrade(['2-0-0','2-0-1'])
        elif current_round == 15:
            ninja.upgrade(['3-0-1'])
        elif current_round == 18:
            sub = Monkey('sub', 0.5661458333333, 0.3990740740741)
            sub.upgrade(['1-0-0', '2-0-0'])
        elif current_round == 21:
            sub.upgrade(['2-0-1'])
        elif current_round == 23:
            sub.upgrade(['2-0-2'])
        elif current_round == 27:
            sub.upgrade(['2-0-3'])
            alch = Monkey('alch', 0.4625, 0.3814814814815)
            alch.target('strong')
        elif current_round == 33:
            sub.upgrade(['2-0-4'])
        elif current_round == 34:
            alch.upgrade(['1-0-0', '2-0-0'])
        elif current_round == 35:
            alch.upgrade(['3-0-0'])
        elif current_round == 37:
            ninja.upgrade(['4-0-1', '4-0-2'])
            alch2 = Monkey('alch', 0.2776041666667, 0.5935185185185)
        elif current_round == 39:
            alch2.upgrade(['1-0-0', '2-0-0', '3-0-0'])