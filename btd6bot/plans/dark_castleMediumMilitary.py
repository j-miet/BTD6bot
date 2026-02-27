"""
[Hero] Obyn
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
sniper 2-3-5
sub 2-0-2
boat 4-2-0
mortar 0-2-3
_______________________________________
"""

from._plan_imports import *

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:
            hero = Hero(0.4473958333333, 0.412962962963)
            hero.target('strong')
        elif round == 4:
            boat = Monkey('boat', 0.5786458333333, 0.3981481481481)
        elif round == 8:
            boat.upgrade(['0-1-0'])
        elif round == 9:
            boat.upgrade(['1-1-0'])
        elif round == 11:
            boat.upgrade(['2-1-0'])
        elif round == 13:
            boat.upgrade(['2-2-0'])
        elif round == 15:
            sub = Monkey('sub', 0.6265625, 0.3953703703704)
        elif round == 18:
            sub.upgrade(['1-0-0','1-0-1'])
        elif round == 19:
            sub.upgrade(['2-0-1'])
        elif round == 22:
            sub.upgrade(['2-0-2'])
        elif round == 24:
            ability(1)
        elif round == 31:
            boat.upgrade(['3-2-0'])
        elif round == 32:
            sniper = Monkey('sniper', 0.7557291666667, 0.4518518518519)
        elif round == 33:
            ability(1)
            sniper.upgrade(['0-1-0','0-2-0'])
        elif round == 34:
            sniper.upgrade(['0-2-1','0-2-2'])
        elif round == 36:
            ability(1)
        elif round == 37:
            sniper.upgrade(['0-2-3'])
        elif round == 39:
            sub.sell()
            sniper.upgrade(['0-2-4'])
            ability(1)
        elif round == 40:
            ability(1)
        elif round == 49:
            sniper.upgrade(['0-2-5'])
        elif round == 50:
            sniper2 = Monkey('sniper', 0.7588541666667, 0.5277777777778)
            sniper2.upgrade(['0-1-0','0-2-0','0-3-0'])
            sniper2.target('strong')
        elif round == 51:
            sniper2.upgrade(['1-3-0','2-3-0'])
        elif round == 57:
            mortar = Monkey('mortar', 0.7307291666667, 0.2111111111111)
            mortar.special(1, 0.3484375, 0.5074074074074)
            mortar.upgrade(['0-0-1','0-0-2','0-0-3','0-1-3','0-2-3'])
        elif round == 59:
            boat.upgrade(['4-2-0'])