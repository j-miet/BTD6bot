"""
[Hero] Sauda
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
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
            hero = Hero(0.4333333333333, 0.5166666666667)
        elif round == 14:
            druid = Monkey("druid", 0.5119791666667, 0.5092592592593)
        elif round == 16:
            druid.upgrade(["0-1-0", "0-2-0", "0-3-0"])
        elif round == 18:
            druid.upgrade(["1-3-0"])
        elif round == 30:
            village1 = Monkey("village", 0.8161458333333, 0.6796296296296)
            village1.upgrade(["0-0-1", "0-0-2"])
        elif round == 35:
            ace = Monkey("ace", 0.7588541666667, 0.7611111111111)
            ace.upgrade(["0-0-1", "0-0-2", "0-0-3"])
        elif round == 36:
            ace.upgrade(["1-0-3", "2-0-3"])
        elif round == 38:
            alch = Monkey("alch", 0.8276041666667, 0.7648148148148)
            alch.upgrade(["1-0-0", "2-0-0", "3-0-0", "3-1-0", "3-2-0"])
        elif round == 41:
            village2 = Monkey("village", 0.8078125, 0.8462962962963)
            village2.upgrade(["0-1-0", "0-2-0"])
        elif round == 43:
            village2.upgrade(["1-2-0", "2-2-0"])
        elif round == 55:
            ace.upgrade(["2-0-4"])
        elif round == 63:
            ice = Monkey("ice", 0.3677083333333, 0.5037037037037)
            ice.upgrade(["1-0-0", "2-0-0", "3-0-0", "4-0-0", "4-1-0"])
        elif round == 90:
            ability(2, 4)
        elif round == 93:
            ability(2, 4.5)
            ace.upgrade(["2-0-5"])
