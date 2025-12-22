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
            hero = Monkey('hero', 0.2385416666667, 0.4796296296296)
        elif current_round == 8:
            sniper = Monkey('sniper', 0.2875, 0.4259259259259)
            sniper.target('strong')
        elif current_round == 15:
            heli1 = Monkey('heli', 0.2630208333333, 0.1814814814815)
        elif current_round == 21:
            heli1.upgrade(['1-0-0','2-0-0'])
        elif current_round == 25:
            sniper.upgrade(['1-0-0'])
        elif current_round == 29:
            heli1.upgrade(['3-0-0'])
        elif current_round == 31:
            heli1.upgrade(['3-0-1','3-0-2'])
        elif current_round == 34:
            village = Monkey('village', 0.2557291666667, 0.3083333333333)
        elif current_round == 36:
            village.upgrade(['0-1-0','0-2-0'])
        elif current_round == 38:
            alch = Monkey('alch', 0.3296875, 0.1444444444444)
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
            heli2 = Monkey('heli', 0.1567708333333, 0.2851851851852)
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