"""
[Hero] Psi
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0
glue 0-2-4
desperado 5-2-0

sniper 1-0-0
boat 5-2-0
ace 5-0-2

alch 4-0-1
mermonkey 4-0-0

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
            sub = Monkey('sub', 0.2057291666667, 0.5222222222222)
            dart = Monkey('dart', 0.6984375, 0.4981481481481)
        elif current_round == 8:
            sub.upgrade(['0-0-1'])
        elif current_round == 13:
            hero = Hero(0.2182291666667, 0.4111111111111)
            hero.target('strong')
        elif current_round == 16:
            boat = Monkey('boat', 0.2546875, 0.537037037037)
            boat.upgrade(['1-0-0'])
        elif current_round == 18:
            boat.upgrade(['2-0-0'])
        elif current_round == 21:
            hero.target('first')
            sniper = Monkey('sniper', 0.3255208333333, 0.2722222222222)
            sniper.target('strong')
        elif current_round == 22:
            sniper.upgrade(['1-0-0'])
        elif current_round == 23:
            hero.target('strong')
        elif current_round == 31:
            boat.upgrade(['3-0-0'])
        elif current_round == 33:
            boat.upgrade(['3-1-0','3-2-0'])
        elif current_round == 41:
            village = Monkey('village', 0.3151041666667, 0.4018518518519)
            village.upgrade(['0-1-0','0-2-0'])
        elif current_round == 45:
            boat.upgrade(['4-2-0'])
        elif current_round == 57:
            boat.upgrade(['5-2-0'])
        elif current_round == 58:
            village.upgrade(['1-2-0','2-2-0'])
        elif current_round == 65:
            ace = Monkey('ace', 0.4130208333333, 0.4388888888889)
            ace.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-0-1','4-0-2'])
        elif current_round == 77:
            mermonkey = Monkey('mermonkey', 0.3338541666667, 0.5277777777778)
            mermonkey.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0'])
        elif current_round == 83:
            ace.upgrade(['5-0-2'])
        elif current_round == 89:
            village.upgrade(['2-3-0'])
        elif current_round == 93:
            desperado = Monkey('desperado', 0.2588541666667, 0.4018518518519)
            desperado.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0'])
        elif current_round == 94:
            desperado.upgrade(['5-0-0','5-1-0','5-2-0'])
            glue = Monkey('glue', 0.2109375, 0.4407407407407)
            glue.target('strong')
        elif current_round == 95:
            glue.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2','0-2-3'])
        elif current_round == 96:
            glue.upgrade(['0-2-4'])
        elif current_round == 97:
            alch = Monkey('alch', 0.4692708333333, 0.3537037037037)
            alch.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-0-1'])
        elif current_round == 98:
            ability(2,9)