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

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:
            dart = Monkey('dart', 0.5239583333333, 0.6185185185185)
            dart.upgrade(['0-1-0','0-2-0'])
        elif round == 3:
            dart.upgrade(['0-3-0','0-3-1'])
        elif round == 6:
            hero = Hero(0.2927083333333, 0.45)
        elif round == 8:
            ninja = Monkey('ninja', 0.3067708333333, 0.5648148148148)
        elif round == 10:
            ninja.upgrade(['1-0-0'])
        elif round == 12:
            ninja.upgrade(['2-0-0','2-0-1'])
        elif round == 15:
            ninja.upgrade(['3-0-1'])
        elif round == 18:
            sub = Monkey('sub', 0.5661458333333, 0.3990740740741)
            sub.upgrade(['1-0-0', '2-0-0'])
        elif round == 21:
            sub.upgrade(['2-0-1'])
        elif round == 23:
            sub.upgrade(['2-0-2'])
        elif round == 27:
            sub.upgrade(['2-0-3'])
            alch = Monkey('alch', 0.4625, 0.3814814814815)
            alch.target('strong')
        elif round == 33:
            sub.upgrade(['2-0-4'])
        elif round == 34:
            alch.upgrade(['1-0-0', '2-0-0'])
        elif round == 35:
            alch.upgrade(['3-0-0'])
        elif round == 37:
            ninja.upgrade(['4-0-1', '4-0-2'])
            alch2 = Monkey('alch', 0.2776041666667, 0.5935185185185)
        elif round == 39:
            alch2.upgrade(['1-0-0', '2-0-0', '3-0-0'])