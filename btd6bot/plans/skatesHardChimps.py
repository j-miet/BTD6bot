"""
[Hero] Sauda
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
sniper 1-0-3
heli 5-0-5

alch 4-2-0

village 2-3-0
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
            hero = Monkey('hero', 0.1734375, 0.2722222222222)
        elif current_round == 8:
            sniper = Monkey('sniper', 0.2567708333333, 0.2481481481481)
            sniper.target('strong')
        elif current_round == 15:
            heli1 = Monkey('heli', 0.1526041666667, 0.0925925925926)
        elif current_round == 21:
            heli1.upgrade(['1-0-0','2-0-0'])
        elif current_round == 25:
            sniper.upgrade(['1-0-0'])
        elif current_round == 29:
            heli1.upgrade(['3-0-0'])
        elif current_round == 31:
            heli1.upgrade(['3-0-1','3-0-2'])
        elif current_round == 34:
            village = Monkey('village', 0.2276041666667, 0.1333333333333)
        elif current_round == 36:
            village.upgrade(['0-1-0','0-2-0'])
        elif current_round == 38:
            alch = Monkey('alch', 0.0682291666667, 0.1388888888889)
            alch.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif current_round == 39:
            sniper.upgrade(['1-0-1','1-0-2'])
        elif current_round == 42:
            village.upgrade(['1-2-0','2-2-0'])
        elif current_round == 45:
            sniper.upgrade(['1-0-3'])
        elif current_round == 54:
            heli1.upgrade(['4-0-2'])
        elif current_round == 55:
            heli2 = Monkey('heli', 0.3078125, 0.112962962963)
            heli2.upgrade(['1-0-0','2-0-0','2-0-1','2-0-2'])
        elif current_round == 79:
            heli1.upgrade(['5-0-2'])
        elif current_round == 81:
            hero.target('strong')
            alch.upgrade(['4-0-0','4-1-0','4-2-0'])
        elif current_round == 83:
            village.upgrade(['2-3-0'])
        elif current_round == 85:
            heli2.upgrade(['2-0-3','2-0-4'])
        elif current_round == 96:
            heli2.upgrade(['2-0-5'])