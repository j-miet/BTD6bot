"""
[Hero] -
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0

sniper 1-2-4
sub 2-0-2
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
            sniper1 = Monkey('sniper', 0.3588541666667, 0.087037037037)
            sniper2 = Monkey('sniper', 0.3598958333333, 0.1444444444444)
        elif round == 3:
            sniper3 = Monkey('sniper', 0.1473958333333, 0.1537037037037)
            sniper3.target('strong')
        elif round == 4:
            dart1 = Monkey('dart', 0.1911458333333, 0.7)
        elif round == 6:
            sub = Monkey('sub', 0.6161458333333, 0.1833333333333)
        elif round == 9:
            sub.upgrade(['1-0-0','2-0-0'])
        elif round == 10:
            sub.upgrade(['2-0-1'])
        elif round == 14:
            sub.upgrade(['2-0-2'])
        elif round == 15:
            dart2 = Monkey('dart', 0.6567708333333, 0.7333333333333)
            dart3 = Monkey('dart', 0.2411458333333, 0.3185185185185)
        elif round == 19:
            sniper2.upgrade(['0-1-0','0-2-0'])
        elif round == 21:
            sniper2.upgrade(['0-2-1','0-2-2'])
        elif round == 25:
            sniper3.upgrade(['1-0-0','1-0-1','1-0-2'])
        elif round == 31:
            sniper2.upgrade(['0-2-3'])
        elif round == 35:
            sniper3.upgrade(['1-0-3'])
        elif round == 38:
            sniper2.upgrade(['0-2-4'])