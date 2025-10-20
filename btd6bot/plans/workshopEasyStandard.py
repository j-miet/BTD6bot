"""
[Hero] Sauda
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0
tack 2-0-4

alch 3-0-1
druid 2-3-0

spike 3-0-2
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
            hero = Hero(0.5291666666667, 0.4574074074074)
        elif current_round == 2:
            dart1 = Monkey('dart', 0.115625, 0.5787037037037)
        elif current_round == 3:
            dart2 = Monkey('dart', 0.3140625, 0.4648148148148)
        elif current_round == 4:
            dart3 = Monkey('dart', 0.3484375, 0.4648148148148)
        elif current_round == 9:
            spike = Monkey('spike', 0.83125, 0.6611111111111)
        elif current_round == 11:
            druid = Monkey('druid', 0.4911458333333, 0.5796296296296)
        elif current_round == 13:
            druid.upgrade(['0-1-0','0-2-0'])
        elif current_round == 16:
            druid.upgrade(['0-3-0'])
        elif current_round == 20:
            druid.upgrade(['1-3-0','2-3-0'])
        elif current_round == 22:
            spike.upgrade(['0-0-1','0-0-2'])
            spike.target('close')
        elif current_round == 26:
            spike.upgrade(['1-0-2','2-0-2'])
        elif current_round == 31:
            spike.upgrade(['3-0-2'])
        elif current_round == 33:
            alch = Monkey('alch', 0.78125, 0.6046296296296)
        elif current_round == 35:
            alch.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif current_round == 38:
            spike2 = Monkey('spike', 0.8307291666667, 0.587037037037)
            spike2.upgrade(['1-0-0','2-0-0','2-0-1','2-0-2'])
        elif current_round == 39:
            spike2.upgrade(['3-0-2'])
            spike2.target('close')
            alch.upgrade(['3-0-1'])