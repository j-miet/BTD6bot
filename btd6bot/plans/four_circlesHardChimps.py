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
            hero = Hero(0.4234375000000, 0.4490740740741)
        elif round == 8:
            sniper1 = Monkey('sniper', 0.4541666666667, 0.4935185185185)
            sniper1.target('strong')
        elif round == 15:
            heli1 = Monkey('heli', 0.5442708333333, 0.4185185185185)
        elif round == 19:
            heli1.upgrade(['1-0-0'])
        elif round == 21:
            heli1.upgrade(['2-0-0'])
        elif round == 27:
            heli1.upgrade(['3-0-0'])
        elif round == 31:
            village1 = Monkey('village', 0.4661458333333, 0.3296296296296)
            village1.upgrade(['0-1-0'])
        elif round == 35:
            village1.upgrade(['0-2-0'])
        elif round == 36:
            heli2 = Monkey('heli', 0.5437500000000, 0.2981481481481)
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
            glue1 = Monkey('glue', 0.4833333333333, 0.4138888888889)
            glue1.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2'])
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