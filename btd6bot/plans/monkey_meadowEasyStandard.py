"""
[Hero] Quincy
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
sniper 2-0-4

ninja 4-0-1
alch 3-2-0
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
            hero = Hero(0.14, 0.35)
            hero.target('strong')
        elif round == 2:
            ninja1 = Monkey('ninja', 0.19529, 0.48332)
        elif round == 4: 
            ninja1.upgrade(['1-0-0'])
        elif round == 8:
            ninja1.upgrade(['2-0-0'])
            alch1 = Monkey('alch', 0.24277, 0.48333)
        elif round == 10:
            ninja1.upgrade(['2-0-1'])
        elif round == 15:
            ninja1.upgrade(['3-0-1'])
        elif round == 17:
            alch1.upgrade(['1-0-0', '2-0-0'])
        elif round == 25:
            alch1.upgrade(['3-0-0'])
        elif round == 30:
            ninja1.upgrade(['4-0-1'])
        elif round == 35:
            alch1.upgrade(['3-1-0', '3-2-0'])
        elif round == 38:
            sniper1 = Monkey('sniper', 0.76094, 0.30463)
            sniper1.target('strong')
            sniper1.upgrade(['1-0-0', '2-0-0', '2-0-1', '2-0-2', '2-0-3'])
        elif round == END:
            sniper1.upgrade(['2-0-4'])