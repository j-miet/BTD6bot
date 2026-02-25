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
Copy of tinkertonHardChimps:
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
            hero = Hero(0.6989583333333, 0.5916666666667)
        elif round == 8:
            sniper1 = Monkey('sniper', 0.6864583333333, 0.3805555555556)
            sniper1.target('strong')
        elif round == 15:
            heli1 = Monkey('heli', 0.8088541666667, 0.4129629629630)
        elif round == 19:
            heli1.upgrade(['1-0-0'])
        elif round == 21:
            heli1.upgrade(['2-0-0'])
        elif round == 27:
            heli1.upgrade(['3-0-0'])
        elif round == 31:
            village1 = Monkey('village', 0.7322916666667, 0.4824074074074)
            village1.upgrade(['1-0-0'])
        elif round == 35:
            village1.upgrade(['1-1-0','1-2-0'])
        elif round == 36:
            heli2 = Monkey('heli', 0.8109375000000, 0.5351851851852)
        elif round == 37:
            heli2.upgrade(['1-0-0','2-0-0'])
        elif round == 38:
            heli2.upgrade(['2-0-1','2-0-2'])
        elif round == 41:
            heli2.upgrade(['2-0-3'])
            heli1.upgrade(['3-0-1','3-0-2'])
        elif round == 48:
            heli2.upgrade(['2-0-4'])
        elif round == 58:
            heli1.upgrade(['4-0-2'])
        elif round == 63:
            village1.upgrade(['2-2-0','2-3-0'])
        elif round == 64:
            glue1 = Monkey('glue', 0.6807291666667, 0.4962962962963)
            glue1.upgrade(['0-1-0','0-2-0','0-2-1'])
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