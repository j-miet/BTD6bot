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

from._plan_imports import *

def play(rounds: tuple[str, str, str, int, int, str]) -> None:
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start)
        if current_round == BEGIN:     
            hero = Hero(0.2505208333333, 0.487962962963)
        elif current_round == 8:
            sniper1 = Monkey('sniper', 0.3182291666667, 0.1194444444444)
            sniper1.target('strong')
        elif current_round == 15:
            heli1 = Monkey('heli', 0.1661458333333, 0.1546296296296)
        elif current_round == 19:
            heli1.upgrade(['1-0-0'])
        elif current_round == 21:
            heli1.upgrade(['2-0-0'])
        elif current_round == 27:
            heli1.upgrade(['3-0-0'])
        elif current_round == 31:
            village1 = Monkey('village', 0.2432291666667, 0.2157407407407)
            village1.upgrade(['0-1-0'])
        elif current_round == 35:
            village1.upgrade(['0-2-0'])
        elif current_round == 36:
            heli2 = Monkey('heli', 0.1651041666667, 0.2953703703704)
        elif current_round == 37:
            heli2.upgrade(['1-0-0','2-0-0'])
        elif current_round == 38:
            heli2.upgrade(['2-0-1','2-0-2'])
        elif current_round == 41:
            heli2.upgrade(['2-0-3'])
            heli1.upgrade(['3-0-1','3-0-2'])
        elif current_round == 48:
            heli2.upgrade(['2-0-4'])
        elif current_round == 57:
            heli1.upgrade(['4-0-2'])
        elif current_round == 62:
            village1.upgrade(['0-3-0','1-3-0'])
        elif current_round == 63:
            village1.upgrade(['2-3-0'])
        elif current_round == 64:
            glue1 = Monkey('glue', 0.2526041666667, 0.3657407407407)
            glue1.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2'])
        elif current_round == 66:
            glue1.upgrade(['0-2-3'])
        elif current_round == 84:
            heli1.upgrade(['5-0-2'])
        elif current_round == 95:
            heli2.upgrade(['2-0-5'])
        elif current_round == 96:
            glue1.upgrade(['0-2-4'])
            sniper1.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif current_round == 98:
            sniper1.upgrade(['4-0-0','4-1-0','4-2-0'])