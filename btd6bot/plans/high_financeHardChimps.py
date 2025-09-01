"""
[Hero] Gwen
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-2

sub 3-0-1
boat 5-2-0
ace 5-0-2

alch 4-0-1
druid 2-5-0
mermonkey 4-0-2

village 2-2-0
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
            dart1 = Monkey('dart', 0.3645833333333, 0.8111111111111)
            sub = Monkey('sub', 0.4348958333333, 0.4212962962963)
        elif current_round == 7:
            dart2 = Monkey('dart', 0.5020833333333, 0.812962962963)
        elif current_round == 9:
            sub.upgrade(['0-0-1'])
        elif current_round == 13:
            hero = Hero(0.3703125, 0.6398148148148)
        elif current_round == 15: 
            boat = Monkey('boat', 0.4015625, 0.5953703703704)
            hero.special(1, 0.3270833333333, 0.5157407407407)
            ability(1,3.5)
        elif current_round == 17:
            boat.upgrade(['0-1-0'])
        elif current_round == 19:
            boat.upgrade(['0-2-0'])
            ability(1,2.5)
        elif current_round == 20:
            boat.upgrade(['1-2-0'])
        elif current_round == 22:
            boat.upgrade(['2-2-0'])
            desperado = Monkey('desperado', 0.4911458333333, 0.3833333333333)
        elif current_round == 23:
            ability(1,2)
        elif current_round == 25:
            sub.upgrade(['1-0-1','2-0-1'])
        elif current_round == 27:
            ability(1,9)
        elif current_round == 31:
            ability(1,1.5)
        elif current_round == 33:
            sub.upgrade(['3-0-1'])
        elif current_round == 34:
            ability(1,1.5)
            sub.special(1)
            boat.upgrade(['3-2-0'])
        elif current_round == 35:
            sub.special(1)
        elif current_round == 36:
            click(0.4432291666667, 0.7675925925926)
            click(0.4942708333333, 0.825)
        elif current_round == 37:
            ace = Monkey('ace', 0.4432291666667, 0.7490740740741)
            ace.upgrade(['1-0-0','2-0-0'])
        elif current_round == 38:
            ace.upgrade(['3-0-0'])
        elif current_round == 39:
            alch = Monkey('alch', 0.4005208333333, 0.6712962962963)
            alch.upgrade(['1-0-0','2-0-0'])
            sub.special(1)
        elif current_round == 40:
            ability(1)
        elif current_round == 41:
            sub.special(1)
            alch.upgrade(['3-0-0'])
        elif current_round == 42:
            village = Monkey('village', 0.4942708333333, 0.662037037037)
            village.upgrade(['1-0-0'])
        elif current_round == 43:
            village.upgrade(['2-0-0'])
        elif current_round == 44:
            ace.upgrade(['3-0-1','3-0-2'])
        elif current_round == 45:
            village.upgrade(['2-1-0','2-2-0'])
            sub.special(1)
        elif current_round == 49:
            ability(1,2)
            boat.upgrade(['4-2-0'])
        elif current_round == 63:
            ability(1,2)
            ability(2,7)
            boat.upgrade(['5-2-0'])
        elif current_round == 65:
            alch.upgrade(['4-0-0','4-0-1'])
        elif current_round == 68:
            ace.upgrade(['4-0-2'])
        elif current_round == 84:
            ace.upgrade(['5-0-2'])
            mermonkey = Monkey('mermonkey', 0.4453125, 0.6212962962963)
            mermonkey.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif current_round == 85:
            mermonkey.upgrade(['4-0-0','4-0-1','4-0-2'])
        elif current_round == 86:
            druid = Monkey('druid', 0.3557291666667, 0.5046296296296)
            druid.upgrade(['1-0-0','2-0-0','2-1-0','2-2-0'])
        elif current_round == 87:
            druid.upgrade(['2-3-0'])
        elif current_round == 89:
            druid.upgrade(['2-4-0'])
        elif current_round == 98:
            druid.upgrade(['2-5-0'])
        elif current_round == 100:
            ability(1,3)
            ability(2)