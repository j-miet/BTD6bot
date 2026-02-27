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
If price changes to heli make 3-0-0 not available for round 28, please update to pop lead bloons.
Copy of monkey_meadowHardChimps:
    - tower position changed
"""

from._plan_imports import *

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:     
            hero = Hero(0.1364583333, 0.4407407407)
        elif round == 8:
            sniper1 = Monkey('sniper', 0.1140625000, 0.6759259259)
            sniper1.target('strong')
        elif round == 15:
            heli1 = Monkey('heli', 0.0562500000, 0.4740740741)
        elif round == 19:
            heli1.upgrade(['1-0-0'])
        elif round == 21:
            heli1.upgrade(['2-0-0'])
        elif round == 27:
            heli1.upgrade(['3-0-0'])
        elif round == 31:
            village1 = Monkey('village', 0.0921875000, 0.5916666667)
            village1.upgrade(['0-1-0'])
        elif round == 35:
            village1.upgrade(['0-2-0'])
        elif round == 36:
            heli2 = Monkey('heli', 0.0546875000, 0.7000000000)
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
        elif round == 62:
            village1.upgrade(['0-3-0','1-3-0'])
        elif round == 63:
            village1.upgrade(['2-3-0'])
        elif round == 64:
            glue1 = Monkey('glue', 0.1223958333, 0.5055555556)
            glue1.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2'])
        elif round == 65:
            glue1.upgrade(['0-2-2'])
        elif round == 66:
            glue1.upgrade(['0-2-3'])
        elif round == 84:
            heli1.upgrade(['5-0-2'])
        elif round == 95:
            heli2.upgrade(['2-0-5'])
        elif round == 96:
            glue1.upgrade(['0-2-4'])
            sniper1.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif round == 98:
            sniper1.upgrade(['4-0-0','4-1-0','4-2-0'])
