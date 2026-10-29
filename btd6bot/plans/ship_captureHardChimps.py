"""
[Hero] Striker
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-2-4
glue 0-2-5

boat 3-2-0

alch 4-2-0
druid 0-0-0

spike 2-4-5
village 2-3-0
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
            druid = Monkey("druid", 0.4348958333333, 0.8444444444444)
            dart = Monkey("dart", 0.3973958333333, 0.8398148148148)
        elif round == 8:
            druid.upgrade(["0-1-0"])
        elif round == 9:
            dart2 = Monkey("dart", 0.4713541666667, 0.8416666666667)
        elif round == 10:
            dart2.upgrade(["0-0-1", "0-0-2"])
        elif round == 13:
            dart2.upgrade(["0-0-3"])
        elif round == 14:
            dart2.upgrade(["0-1-3", "0-2-3"])
        elif round == 17:
            hero = Hero(0.4328125, 0.7759259259259)
        elif round == 26:
            dart2.upgrade(["0-2-4"])
        elif round == 29:
            click(0.4322916666667, 0.5953703703704)
            wait(1)
            click(0.4697916666667, 0.5768518518519)
        elif round == 30:
            boat = Monkey("boat", 0.4864583333333, 0.675)
        elif round == 31:
            boat.upgrade(["0-1-0"])
        elif round == 32:
            boat.upgrade(["0-2-0"])
        elif round == 33:
            boat.upgrade(["1-2-0", "2-2-0"])
        elif round == 37:
            boat.upgrade(["3-2-0"])
        elif round == 38:
            alch = Monkey("alch", 0.5760416666667, 0.6490740740741)
            alch.upgrade(["1-0-0", "2-0-0"])
        elif round == 39:
            alch.upgrade(["3-0-0", "3-1-0", "3-2-0"])
        elif round == 41:
            village = Monkey("village", 0.5192708333333, 0.8583333333333)
        elif round == 43:
            village.upgrade(["1-0-0", "2-0-0", "2-1-0"])
        elif round == 44:
            village.upgrade(["2-2-0"])
        elif round == 49:
            boat.upgrade(["4-2-0"])
        elif round == 51:
            spike = Monkey("spike", 0.4546875, 0.9046296296296)
            spike.upgrade(["1-0-0", "2-0-0", "2-0-1", "2-0-2"])
            spike.target("smart")
        elif round == 52:
            spike.upgrade(["2-0-3", "2-0-4"])
        elif round == 70:
            boat.upgrade(["5-2-0"])
            alch.upgrade(["4-2-0"])
        elif round == 82:
            spike.upgrade(["2-0-5"])
            alch2 = Monkey("alch", 0.4942708333333, 0.9268518518519)
        elif round == 83:
            alch2.upgrade(["1-0-0", "2-0-0", "3-0-0", "4-0-0", "4-1-0", "4-2-0"])
        elif round == 85:
            glue = Monkey("glue", 0.4390625, 0.587037037037)
            glue.upgrade(["0-1-0", "0-2-0", "0-2-1", "0-2-2", "0-2-3", "0-2-4"])
        elif round == 95:
            glue.upgrade(["0-2-5"])
        elif round == 96:
            alch3 = Monkey("alch", 0.4848958333333, 0.5361111111111)
            alch3.upgrade(["1-0-0", "2-0-0", "3-0-0", "4-0-0", "4-1-0", "4-2-0"])
        elif round == 97:
            spike2 = Monkey("spike", 0.5380208333333, 0.2851851851852)
            spike2.upgrade(["1-0-0", "1-1-0", "1-2-0", "1-3-0"])
        elif round == 98:
            spike2.upgrade(["1-4-0"])
            spike3 = Monkey("spike", 0.4869791666667, 0.2972222222222)
            spike3.upgrade(["1-0-0", "1-1-0", "1-2-0", "1-3-0"])
        elif round == 100:
            ability(4, 3)
