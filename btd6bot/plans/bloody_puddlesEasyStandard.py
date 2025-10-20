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

def play(rounds):
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start, rounds[2])
        if current_round == BEGIN:
            sniper1 = Monkey('sniper', 0.3588541666667, 0.087037037037)
            sniper2 = Monkey('sniper', 0.3598958333333, 0.1444444444444)
        elif current_round == 3:
            sniper3 = Monkey('sniper', 0.1473958333333, 0.1537037037037)
            sniper3.target('strong')
        elif current_round == 4:
            dart1 = Monkey('dart', 0.1911458333333, 0.7)
        elif current_round == 6:
            sub = Monkey('sub', 0.6161458333333, 0.1833333333333)
        elif current_round == 9:
            sub.upgrade(['1-0-0','2-0-0'])
        elif current_round == 10:
            sub.upgrade(['2-0-1'])
        elif current_round == 14:
            sub.upgrade(['2-0-2'])
        elif current_round == 15:
            dart2 = Monkey('dart', 0.6567708333333, 0.7333333333333)
            dart3 = Monkey('dart', 0.2411458333333, 0.3185185185185)
        elif current_round == 19:
            sniper2.upgrade(['0-1-0','0-2-0'])
        elif current_round == 21:
            sniper2.upgrade(['0-2-1','0-2-2'])
        elif current_round == 25:
            sniper3.upgrade(['1-0-0','1-0-1','1-0-2'])
        elif current_round == 31:
            sniper2.upgrade(['0-2-3'])
        elif current_round == 35:
            sniper3.upgrade(['1-0-3'])
        elif current_round == 38:
            sniper2.upgrade(['0-2-4'])