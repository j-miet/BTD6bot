"""
[Hero] Sauda
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
glue 0-2-4

sniper 0-0-0
heli 5-0-5

village 2-3-0
_______________________________________
If price change to heli where 3-0-0 not available for round 28, please update to pop lead bloons.
Copy of tinkertonHardChimps (tower position changed).
"""

from._plan_imports import *

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:     
            hero = Hero(0.3354166666666, 0.5074074074074)
        elif round == 9:
            sniper1 = Monkey('sniper', 0.6994791666667, 0.2555555555556)
            sniper1.target('strong')
        elif round == 16:
            heli1 = Monkey('heli', 0.2651041666667, 0.3703703703704)
        elif round == 19:
            heli1.upgrade(['1-0-0'])
        elif round == 22:
            heli1.upgrade(['2-0-0'])
        elif round == 28:
            heli1.upgrade(['3-0-0'])
        elif round == 32:
            village1 = Monkey('village', 0.2848958333333, 0.4787037037037)
        elif round == 32:
            village1.upgrade(['1-0-0'])
        elif round == 33:
            village1.upgrade(['1-1-0'])
        elif round == 36:
            village1.upgrade(['1-2-0'])
        elif round == 38:
            heli2 = Monkey('heli', 0.2614583333333, 0.5851851851852)
            heli2.upgrade(['1-0-0'])
        elif round == 39:
            heli2.upgrade(['1-0-1','2-0-1'])
        elif round == 42:
            heli2.upgrade(['2-0-2','2-0-3'])
            heli1.upgrade(['3-0-1','3-0-2'])
        elif round == 51:
            heli1.upgrade(['4-0-2'])
        elif round == 58:
            heli2.upgrade(['2-0-4'])
        elif round == 63:
            village1.upgrade(['2-2-0','2-3-0'])
        elif round == 83:
            heli1.upgrade(['5-0-2'])
        elif round == 95:
            heli2.upgrade(['2-0-5'])
            glue1 = Monkey('glue', 0.3208333333333, 0.5638888888889)
            glue1.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2'])
        elif round == 96:
            glue1.upgrade(['0-2-3','0-2-4'])