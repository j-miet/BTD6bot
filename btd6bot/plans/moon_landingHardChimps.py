"""
[Hero] Psi
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0
glue 0-2-4
desperado 0-0-0

heli 5-0-5

druid 1-0-0

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
            desp = Monkey("desperado", 0.5609375, 0.5712962962963)
            dart = Monkey("dart", 0.5223958333333, 0.9453703703704)
        elif round == 8:
            druid = Monkey("druid", 0.5859375, 0.6861111111111)
        elif round == 10:
            druid.upgrade(["0-1-0"])
        elif round == 13:
            hero = Hero(0.5651041666667, 0.8435185185185)
            hero.target("strong")
        elif round == 18:
            heli1 = Monkey("heli", 0.6578125, 0.6287037037037)
            heli1.special(1, 0.4473958333333, 0.7416666666667)
        elif round == 23:
            heli1.upgrade(["1-0-0"])
        elif round == 25:
            heli1.upgrade(["2-0-0"])
        elif round == 27:
            druid.upgrade(["1-0-0"])
            druid.target("strong")
        elif round == 31:
            heli1.upgrade(["3-0-0"])
        elif round == 36:
            village = Monkey("village", 0.6463541666667, 0.7453703703704)
            village.upgrade(["0-1-0", "0-2-0"])
        elif round == 37:
            heli1.upgrade(["3-0-1", "3-0-2"])
        elif round == 39:
            heli2 = Monkey("heli", 0.7276041666667, 0.7638888888889)
            heli2.upgrade(["1-0-0", "2-0-0"])
        elif round == 43:
            heli2.upgrade(["2-0-1", "2-0-2", "2-0-3"])
        elif round == 49:
            heli2.upgrade(["2-0-4"])
            village.upgrade(["1-2-0", "2-2-0"])
        elif round == 59:
            heli1.upgrade(["4-0-2"])
        elif round == 81:
            heli1.upgrade(["5-0-2"])
        elif round == 84:
            village.upgrade(["2-3-0"])
        elif round == 94:
            heli2.upgrade(["2-0-5"])
            glue = Monkey("glue", 0.5973958333333, 0.8972222222222)
            glue.target("strong")
        elif round == 95:
            glue.upgrade(["0-0-1", "0-0-2", "0-0-3", "0-1-3", "0-2-3"])
        elif round == 96:
            glue.upgrade(["0-2-4"])
