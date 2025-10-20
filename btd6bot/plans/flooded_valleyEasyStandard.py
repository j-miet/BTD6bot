"""
[Hero] -
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
sub 0-2-1
boat 5-0-2
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
            sub1 = Monkey('sub', 0.5557291666667, 0.8203703703704)
            sub2 = Monkey('sub', 0.4817708333333, 0.1407407407407)
        elif current_round == 3:
            boat = Monkey('boat', 0.5276041666667, 0.7712962962963)
        elif current_round == 6:
            sub1.upgrade(['0-0-1'])
        elif current_round == 8:
            sub1.upgrade(['0-1-1'])
        elif current_round == 10:
            boat.upgrade(['0-0-1','0-0-2'])
        elif current_round == 13:
            boat.upgrade(['1-0-2', '2-0-2'])
        elif current_round == 16:
            sub1.upgrade(['0-2-1'])
        elif current_round == 18:
            sub2.upgrade(['0-1-0','0-2-0','0-2-1'])
        elif current_round == 27:
            boat.upgrade(['3-0-2'])
        elif current_round == 37:
            boat.upgrade(['4-0-2'])