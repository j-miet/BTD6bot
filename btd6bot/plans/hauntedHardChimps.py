"""
[Hero] Sauda
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
wizard 5-0-2
druid 1-5-0

spike 2-5-0
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
            hero = Hero(0.3057291666667, 0.7166666666667)
        elif round == 8:
            wizard = Monkey("wizard", 0.5567708333333, 0.6018518518519)
        elif round == 9:
            wizard.upgrade(["1-0-0"])
        elif round == 11:
            druid = Monkey("druid", 0.3098958333333, 0.4648148148148)
        elif round == 13:
            wizard.upgrade(["2-0-0"])
        elif round == 15:
            wizard.upgrade(["2-0-1"])
            druid.upgrade(["0-1-0"])
        elif round == 18:
            druid.upgrade(["0-2-0"])
        elif round == 21:
            druid.upgrade(["0-3-0"])
        elif round == 22:
            druid.upgrade(["1-3-0"])
        elif round == 27:
            wizard.upgrade(["3-0-1"])
        elif round == 29:
            wizard.upgrade(["3-0-2"])
        elif round == 33:
            spike = Monkey("spike", 0.5557291666667, 0.4055555555556)
        elif round == 34:
            spike.upgrade(["0-1-0", "0-2-0"])
        elif round == 36:
            spike.upgrade(["1-2-0"])
        elif round == 38:
            spike.upgrade(["1-3-0", "2-3-0"])
        elif round == 40:
            ability(1, 4)
        elif round == 46:
            wizard.upgrade(["4-0-2"])
        elif round == 49:
            druid.upgrade(["1-4-0"])
        elif round == 63:
            ability(1, 7)
            ability(3, 13)
        elif round == 65:
            ability(3, 27)
        elif round == 66:
            wizard.upgrade(["5-0-2"])
        elif round == 82:
            druid.upgrade(["1-5-0"])
        elif round == 96:
            spike.upgrade(["2-4-0", "2-5-0"])
        elif round == 98:
            ability(1, 8)
            ability(3, 12)
