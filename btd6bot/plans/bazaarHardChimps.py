"""
[Hero] Rosalia
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0
boomer 0-0-0

ace 2-0-5

alch 3-2-0
druid 1-3-0

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
            dart1 = Monkey("dart", 0.1635416666667, 0.5037037037037)
            dart2 = Monkey("dart", 0.440625, 0.5018518518519)
            dart3 = Monkey("dart", 0.7072916666667, 0.5018518518519)
        elif round == 8:
            boomer = Monkey("boomer", 0.3989583333333, 0.5)
            boomer.target("strong")
        elif round == 10:
            druid = Monkey("druid", 0.4776041666667, 0.4981481481481)
        elif round == 14:
            hero = Hero(0.1177083333333, 0.6)
            hero.special(2, 0.2005208333333, 0.5018518518519)
        elif round == 16:
            druid.upgrade(["0-1-0"])
        elif round == 17:
            sniper = Monkey("sniper", 0.7401041666667, 0.4759259259259)
        elif round == 20:
            sniper.upgrade(["0-1-0", "0-2-0"])
        elif round == 22:
            ability(1, 0.5)
        elif round == 25:
            druid.upgrade(["0-2-0", "0-3-0"])
        elif round == 27:
            druid.upgrade(["1-3-0"])
        elif round == 29:
            sniper.upgrade(["0-2-1", "0-2-2"])
        elif round == 35:
            village = Monkey("village", 0.1140625, 0.4925925925926)
            village.upgrade(["0-1-0", "0-2-0"])
        elif round == 39:
            ace = Monkey("ace", 0.1140625, 0.4018518518519)
            ace.upgrade(["0-0-1", "0-0-2", "0-0-3", "1-0-3", "2-0-3"])
        elif round == 40:
            ability(2)
            ability(1)
        elif round == 42:
            alch = Monkey("alch", 0.1119791666667, 0.3342592592593)
            alch.upgrade(["1-0-0", "2-0-0", "3-0-0", "3-1-0", "3-2-0"])
        elif round == 45:
            village.upgrade(["1-2-0", "2-2-0"])
        elif round == 55:
            ace.upgrade(["2-0-4"])
        elif round == 88:
            ace.upgrade(["2-0-5"])
