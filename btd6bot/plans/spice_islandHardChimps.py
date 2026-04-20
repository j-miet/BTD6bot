"""
[Hero] Rosalia
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0

sub 1-0-1
sniper 1-2-2
ace 2-0-5

alch 3-2-0

village 2-2-0
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
            sub = Monkey("sub", 0.2130208333333, 0.5648148148148)
            dart = Monkey("dart", 0.3369791666667, 0.4518518518519)
        elif round == 8:
            sub.upgrade(["1-0-0"])
        elif round == 9:
            sub.upgrade(["1-0-1"])
        elif round == 13:
            hero = Hero(0.6817708333333, 0.3222222222222)
            hero.special(2, 0.6817708333333, 0.2722222222222)
        elif round == 15:
            sniper = Monkey("sniper", 0.3182291666667, 0.5259259259259)
        elif round == 18:
            sniper.upgrade(["0-1-0", "0-2-0"])
        elif round == 21:
            sniper.upgrade(["0-2-1", "0-2-2"])
        elif round == 22:
            ability(1, 3)
        elif round == 26:
            sniper2 = Monkey("sniper", 0.2182291666667, 0.4648148148148)
            sniper2.upgrade(["1-0-0"])
            sniper2.target("strong")
        elif round == 30:
            click(0.5828125, 0.512962962963)
            wait(0.25)
            click(0.6359375, 0.5851851851852)
        elif round == 32:
            ace = Monkey("ace", 0.5494791666667, 0.4777777777778)
            ace.upgrade(["0-0-1", "0-0-2"])
        elif round == 35:
            ace.upgrade(["0-0-3"])
            ace.center(0.7505208333333, 0.8777777777778)
        elif round == 37:
            ace.upgrade(["1-0-3", "2-0-3"])
        elif round == 38:
            ability(1, 5)
        elif round == 39:
            alch = Monkey("alch", 0.5786458333333, 0.562962962963)
            alch.upgrade(["1-0-0", "2-0-0", "3-0-0", "3-1-0", "3-2-0"])
        elif round == 40:
            ability(2)
            ability(1)
        elif round == 42:
            village = Monkey("village", 0.6223958333333, 0.5092592592593)
            village.upgrade(["0-1-0", "0-2-0"])
        elif round == 44:
            village.upgrade(["1-2-0", "2-2-0"])
        elif round == 55:
            ace.upgrade(["2-0-4"])
        elif round == 88:
            ace.upgrade(["2-0-5"])
