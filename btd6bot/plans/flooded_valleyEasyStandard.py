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

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:
            sub1 = Monkey('sub', 0.5557291666667, 0.8203703703704)
            sub2 = Monkey('sub', 0.4817708333333, 0.1407407407407)
        elif round == 3:
            boat = Monkey('boat', 0.5276041666667, 0.7712962962963)
        elif round == 6:
            sub1.upgrade(['0-0-1'])
        elif round == 8:
            sub1.upgrade(['0-1-1'])
        elif round == 10:
            boat.upgrade(['0-0-1','0-0-2'])
        elif round == 13:
            boat.upgrade(['1-0-2', '2-0-2'])
        elif round == 16:
            sub1.upgrade(['0-2-1'])
        elif round == 18:
            sub2.upgrade(['0-1-0','0-2-0','0-2-1'])
        elif round == 27:
            boat.upgrade(['3-0-2'])
        elif round == 37:
            boat.upgrade(['4-0-2'])