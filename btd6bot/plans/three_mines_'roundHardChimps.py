"""
[Hero] Sauda
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
glue 0-2-4

sniper 4-2-0
heli 5-0-5

village 2-3-0
_______________________________________
"""

from ._plan_imports import *


def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN - 1
    map_start = time()
    while round < END + 1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:
            hero = Hero(0.3895833333333, 0.2222222222222)
        elif round == 8:
            sniper1 = Monkey('sniper', 0.1677083333333, 0.787037037037)
            sniper1.target('strong')
        elif round == 15:
            heli1 = Monkey('heli', 0.5510416666667, 0.4314814814815)
        elif round == 19:
            heli1.upgrade(['1-0-0'])
        elif round == 21:
            heli1.upgrade(['2-0-0'])
        elif round == 27:
            heli1.upgrade(['3-0-0'])
        elif round == 31:
            village1 = Monkey('village', 0.4677083333333, 0.3444444444444)
            village1.upgrade(['0-1-0'])
        elif round == 35:
            village1.upgrade(['0-2-0'])
        elif round == 36:
            heli2 = Monkey('heli', 0.4614583333333, 0.4944444444444)
        elif round == 37:
            heli2.upgrade(['1-0-0','2-0-0'])
        elif round == 38:
            heli2.upgrade(['2-0-1','2-0-2'])
        elif round == 41:
            heli2.upgrade(['2-0-3'])
            heli1.upgrade(['3-0-1','3-0-2'])
        elif round == 48:
            heli2.upgrade(['2-0-4'])
        elif round == 57:
            heli1.upgrade(['4-0-2'])
        elif round == 59:
            village1.upgrade(['1-2-0','2-2-0'])
        elif round == 81:
            heli1.upgrade(['5-0-2'])
        elif round == 89:
            village1.upgrade(['2-3-0'])
        elif round == 94:
            heli2.upgrade(['2-0-5'])
        elif round == 95:
            glue1 = Monkey('glue', 0.4239583333333, 0.1648148148148)
            glue1.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2','0-2-3'])
        elif round == 96:
            glue1.upgrade(['0-2-4'])
            sniper1.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif round == 98:
            sniper1.upgrade(['4-0-0','4-1-0','4-2-0'])