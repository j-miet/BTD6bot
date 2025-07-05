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

def play(rounds: tuple[str, str, str, int, int, str]) -> None:
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start)
        if current_round == BEGIN:     
            hero = Hero(0.6989583333333, 0.5916666666667)
        elif current_round == 9:
            sniper1 = Monkey('sniper', 0.6864583333333, 0.3805555555556)
            sniper1.target('strong')
        elif current_round == 16:
            heli1 = Monkey('heli', 0.8088541666667, 0.4129629629630)
        elif current_round == 19:
            heli1.upgrade(['1-0-0'])
        elif current_round == 22:
            heli1.upgrade(['2-0-0'])
        elif current_round == 28:
            heli1.upgrade(['3-0-0'])
        elif current_round == 32:
            village1 = Monkey('village', 0.7322916666667, 0.4824074074074)
        elif current_round == 32:
            village1.upgrade(['1-0-0'])
        elif current_round == 33:
            village1.upgrade(['1-1-0'])
        elif current_round == 36:
            village1.upgrade(['1-2-0'])
        elif current_round == 38:
            heli2 = Monkey('heli', 0.8109375000000, 0.5351851851852)
            heli2.upgrade(['1-0-0'])
        elif current_round == 39:
            heli2.upgrade(['1-0-1','2-0-1'])
        elif current_round == 42:
            heli2.upgrade(['2-0-2','2-0-3'])
            heli1.upgrade(['3-0-1','3-0-2'])
        elif current_round == 51:
            heli1.upgrade(['4-0-2'])
        elif current_round == 58:
            heli2.upgrade(['2-0-4'])
        elif current_round == 63:
            village1.upgrade(['1-2-0','2-3-0'])
        elif current_round == 83:
            heli1.upgrade(['5-0-2'])
        elif current_round == 95:
            heli2.upgrade(['2-0-5'])
            glue1 = Monkey('glue', 0.6807291666667, 0.4962962962963)
            glue1.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2'])
        elif current_round == 96:
            glue1.upgrade(['0-2-3','0-2-4'])