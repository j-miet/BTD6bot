"""
[Hero] Sauda
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
glue 0-2-4

sniper 4-0-2
heli 5-0-5

village 2-3-0
_______________________________________
Inspired by monkey_meadowHardChimps: 
    - tower position changed 
    - sniper upgraded earlier
    - different upgrade path for sniper
"""

from._plan_imports import *

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:
            hero = Hero(0.1286458333, 0.7398148148)
        elif round == 8:
            sniper1 = Monkey('sniper', 0.5687500000, 0.2046296296)
            sniper1.target('strong')
        elif round == 10:
            sniper1.upgrade(['0-0-1'])
        elif round == 13:
            sniper1.upgrade(['0-0-2'])
        elif round == 19:
            heli1 = Monkey('heli', 0.4963541667, 0.0962962963)
        elif round == 22:
            heli1.upgrade(['1-0-0'])
        elif round == 24:
            heli1.upgrade(['2-0-0'])
        elif round == 26:
            sniper1.upgrade(['1-0-2'])
        elif round == 31:
            heli1.upgrade(['3-0-0'])
        elif round == 33:
            village1 = Monkey('village', 0.4979166667, 0.2129629630)
        elif round == 34:
            village1.upgrade(['0-1-0'])
        elif round == 36:
            village1.upgrade(['0-2-0'])
        elif round == 37:
            heli2 = Monkey('heli', 0.4197916667, 0.0962962963)
        elif round == 38:
            heli2.upgrade(['1-0-0'])
            heli2.upgrade(['2-0-0'])
        elif round == 39:
            heli2.upgrade(['2-0-1'])
            heli2.upgrade(['2-0-2'])
        elif round == 42:
            heli2.upgrade(['2-0-3'])
        elif round == 43:
            heli1.upgrade(['3-0-1'])
            heli1.upgrade(['3-0-2'])
        elif round == 48:
            heli2.upgrade(['2-0-4'])
        elif round == 58:
            heli1.upgrade(['4-0-2'])
        elif round == 63:
            village1.upgrade(['0-3-0'])
            village1.upgrade(['1-3-0'])
        elif round == 64:
            village1.upgrade(['2-3-0'])
        elif round == 65:
            glue1 = Monkey('glue', 0.4286458333, 0.2527777778)
            glue1.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2'])
        elif round == 68:
            glue1.upgrade(['0-2-3'])
        elif round == 84:
            heli1.upgrade(['5-0-2'])
        elif round == 95:
            heli2.upgrade(['2-0-5'])
        elif round == 96:
            glue1.upgrade(['0-2-4'])
            sniper1.upgrade(['2-0-2'])        
            sniper1.upgrade(['3-0-2'])
        elif round == 98:
            sniper1.upgrade(['4-0-2'])