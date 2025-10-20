"""
[Hero] Psi
[Monkey Knowledge] -
---------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0

sniper 1-5-5
sub 2-0-2

alch 4-2-0

village 2-0-2
_______________________________________
Some lives will be lost in early game.
"""

from._plan_imports import *

def play(rounds):
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start, rounds[2])
        if current_round == BEGIN:
            sniper1 = Monkey('sniper', 0.7494791666667, 0.8333333333333)
            sniper1.target('strong')
            dart1 = Monkey('dart', 0.6463541666667, 0.4018518518519)
        elif current_round == 5:
            sub = Monkey('sub', 0.5588541666667, 0.1555555555556)
        elif current_round == 6:
            sub.upgrade(['1-0-0'], cpos=(0.4828125, 0.1796296296296))
        elif current_round == 9:
            sub.upgrade(['1-0-1'], cpos=(0.5640625, 0.162962962963))
        elif current_round == 10:
            sniper1.target('first', cpos=(0.7484375, 0.8222222222222))
        elif current_round == 11:
            sub.upgrade(['2-0-1'], cpos=(0.4140625, 0.1722222222222))
        elif current_round == 12:
            dart2 = Monkey('dart', 0.1442708333333, 0.2796296296296)
        elif current_round == 16:
            hero = Hero(0.3828125, 0.1074074074074)
            hero.target('strong')
        elif current_round == 21:
            sub.upgrade(['2-0-2'], cpos=(0.5567708333333, 0.1759259259259))
        elif current_round == 25:
            sniper1.upgrade(['0-0-1','0-0-2'], cpos=(0.6859375, 0.7925925925926))
        elif current_round == 26:
            sniper2 = Monkey('sniper', 0.4234375, 0.9111111111111)
        elif current_round == 27:
            sniper2.upgrade(['1-0-0'], cpos=(0.5036458333333, 0.9))
        elif current_round == 29:
            sniper1.upgrade(['0-1-2','0-2-2'], cpos=(0.6890625, 0.7759259259259))
        elif current_round == 34:
            sniper1.upgrade(['0-2-3'], cpos=(0.7484375, 0.8388888888889))
        elif current_round == 38:
            sniper1.upgrade(['0-2-4'], cpos=(0.7442708333333, 0.8277777777778))
        elif current_round == 39:
            village = Monkey('village', 0.7546875, 0.9148148148148)
        elif current_round == 41:
            village.upgrade(['0-0-1','0-0-2','1-0-2','2-0-2'], cpos=(0.6442708333333, 0.8462962962963))
        elif current_round == 43:
            alch = Monkey('alch', 0.7036458333333, 0.8444444444444)
        elif current_round == 45:
            alch.upgrade(['1-0-0','2-0-0','3-0-0','3-1-0','3-2-0'], cpos=(0.8114583333333, 0.9064814814815))
        elif current_round == 46:
            alch.upgrade(['4-2-0'], cpos=(0.7734375, 0.8944444444444))
        elif current_round == 53:
            sniper1.upgrade(['0-2-5'], cpos=(0.6869791666667, 0.7796296296296))
        elif current_round == 54:
            sniper3 = Monkey('sniper', 0.6432291666667, 0.8638888888889)
        elif current_round == 55:
            sniper3.upgrade(['0-0-1','0-0-2','0-1-2','0-2-2','0-3-2'], cpos=(0.6776041666667,  0.8944444444444))
        elif current_round == 59:
            sniper3.upgrade(['0-4-2'], cpos=(0.6765625, 0.9166666666667))
        elif current_round == 69:
            sniper3.upgrade(['0-5-2'], cpos=(0.7869791666667, 0.9722222222222))
            sniper3.target('first')