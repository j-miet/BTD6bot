"""
[Hero] Rosalia
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0

sub 0-0-0
sniper 0-2-2
ace 2-0-5

alch 3-2-0
druid 1-3-0

village 2-2-2
_______________________________________
"""

from ._plan_imports import *


def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN - 1
    map_start = time()
    while round < END + 1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:
            dart = Monkey("dart", 0.2609375, 0.3888888888889)
            dart.target("strong")
            dart2 = Monkey("dart", 0.4817708333333, 0.7685185185185)
        elif round == 7:
            sub = Monkey("sub", 0.6682291666667, 0.4407407407407)
        elif round == 8:
            dart3 = Monkey("dart", 0.3703125, 0.812962962963)
        elif round == 10:
            sniper = Monkey("sniper", 0.5828125, 0.9675925925926)
            sniper.target("strong")
        elif round == 14:
            hero = Hero(0.3171875, 0.212962962963)
            hero.special(2, 0.2442708333333, 0.2944444444444)
        elif round == 16:
            druid = Monkey("druid", 0.6223958333333, 0.7740740740741)
            druid.upgrade(["0-1-0"])
        elif round == 19:
            hero.special(2, 0.4609375, 0.1592592592593)
        elif round == 20:
            hero.special(2, 0.2442708333333, 0.2944444444444)
        elif round == 21:
            ability(1)
            hero.special(1)
            hero.target("strong")
        elif round == 22:
            forward(1)
            druid.upgrade(["0-2-0", "0-3-0"])
            forward(1)
        elif round == 23:
            sniper.upgrade(["0-1-0"])
        elif round == 25:
            druid.upgrade(["1-3-0"])
        elif round == 28:
            sniper.upgrade(["0-1-1", "0-1-2", "0-2-2"])
        elif round == 29:
            sniper.target("first")
        elif round == 34:
            village1 = Monkey("village", 0.3171875, 0.1064814814815)
        elif round == 38:
            ace = Monkey("ace", 0.2307291666667, 0.2101851851852)
            ace.upgrade(["0-0-1", "0-0-2", "0-0-3", "1-0-3", "2-0-3"])
            ace.center(0.5239583333333, 0.9842592592593)
        elif round == 39:
            hero.special(1)
            hero.special(2, 0.1666666666667, 0.2592592592593)
        elif round == 40:
            ability(2)
            ability(1)
        elif round == 41:
            alch = Monkey("alch", 0.2375, 0.1444444444444)
            village2 = Monkey("village", 0.2572916666667, 0.0666666666667)
            village2.upgrade(["0-1-0", "0-2-0"])
        elif round == 42:
            village2.upgrade(["1-2-0", "2-2-0"])
        elif round == 45:
            alch.upgrade(["1-0-0", "2-0-0", "3-0-0", "3-1-0", "3-2-0"])
        elif round == 55:
            ace.upgrade(["2-0-4"])
        elif round == 88:
            ace.upgrade(["2-0-5"])
