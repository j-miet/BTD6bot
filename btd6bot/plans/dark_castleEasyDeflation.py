"""
[Hero] Gwen
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
ace 2-0-3

alch 4-2-0

village 2-2-0
_______________________________________
"""

from ._plan_imports import *

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:
            Hero(0.2973958333333, 0.4435185185185)
            village = Monkey('village', 0.3630208333333, 0.3611111111111)
            village.upgrade(['1-0-0', '2-0-0', '2-1-0', '2-2-0'])
            ace1 = Monkey('ace', 0.3828125, 0.1972222222222)
            ace1.upgrade(['1-0-0', '2-0-0', '2-0-1', '2-0-2', '2-0-3'])
            forward()
            ninja = Monkey('ninja', 0.3963541666667, 0.4148148148148)
            ninja.upgrade(['1-0-0', '2-0-0', '3-0-0', '4-0-0', '4-0-1', '4-0-2'])
            alch = Monkey('alch', 0.4257291666667, 0.2709259259259)
            alch.upgrade(['1-0-0', '2-0-0', '3-0-0', '4-0-0', '4-0-1'])