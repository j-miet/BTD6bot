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
            hero = Hero(0.4348958333333, 0.3592592592593)
        elif round == 9:
            click(0.3838541666667, 0.2981481481481)
            wait(0.25)
            click(0.4442708333333, 0.3759259259259)
        elif round == 10:
            wizard = Monkey("wizard", 0.4026041666667, 0.3240740740741)
        elif round == 11:
            druid = Monkey("druid", 0.3744791666667, 0.2777777777778)
        elif round == 12:
            wizard.upgrade(["1-0-0"])
        elif round == 13:
            druid.upgrade(["0-1-0"])
        elif round == 14:
            wizard.upgrade(["2-0-0"])
        elif round == 21:
            druid.upgrade(["0-2-0", "0-3-0"])
        elif round == 23:
            druid.upgrade(["1-3-0"])
        elif round == 27:
            wizard.upgrade(["3-0-0"])
        elif round == 29:
            wizard.upgrade(["3-0-1", "3-0-2"])
        elif round == 33:
            click(0.4848958333333, 0.2962962962963)
            wait(0.25)
            click(0.5369791666667, 0.387037037037)
        elif round == 37:
            spike = Monkey("spike", 0.4765625, 0.3055555555556)
        elif round == 38:
            spike.upgrade(["1-0-0", "2-0-0", "2-1-0", "2-2-0", "2-3-0"])
        elif round == 46:
            wizard.upgrade(["4-0-2"])
        elif round == 55:
            druid.upgrade(["1-4-0"])
        elif round == 70:
            druid.upgrade(["1-5-0"])
        elif round == 81:
            wizard.upgrade(["5-0-2"])
        elif round == 96:
            spike.upgrade(["2-4-0", "2-5-0"])
