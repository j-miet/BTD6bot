"""
[Hero] Psi
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-3-1
glue 0-2-4
desperado 0-0-0

sniper 4-2-0
heli 5-0-5

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
            dart = Monkey("dart", 0.4359375, 0.7231481481481)
            dart.upgrade(["0-1-0"])
            desp = Monkey("desperado", 0.4359375, 0.5657407407407)
        elif round == 7:
            dart.upgrade(["0-2-0"])
        elif round == 8:
            dart.upgrade(["0-2-1"])
        elif round == 10:
            dart.upgrade(["0-3-1"])
        elif round == 13:
            sniper = Monkey("sniper", 0.4588541666667, 0.125)
        elif round == 16:
            hero = Hero(0.4703125, 0.5027777777778)
            hero.target("strong")
        elif round == 21:
            hero.target("first")
            ability(1, 3)
        elif round == 22:
            hero.target("strong")
        elif round == 23:
            heli1 = Monkey("heli", 0.4557291666667, 0.4064814814815)
            heli1.special(1, 0.4348958333333, 0.6342592592593)
        elif round == 26:
            sniper.upgrade(["1-0-0"])
            sniper.target("strong")
        elif round == 27:
            heli1.upgrade(["1-0-0"])
        elif round == 28:
            heli1.upgrade(["2-0-0"])
        elif round == 32:
            heli1.upgrade(["3-0-0"])
            hero.target("first")
        elif round == 37:
            village = Monkey("village", 0.4369791666667, 0.2916666666667)
            village.upgrade(["0-1-0", "0-2-0"])
        elif round == 39:
            heli2 = Monkey("heli", 0.5286458333333, 0.2212962962963)
            heli2.upgrade(["1-0-0", "2-0-0"])
            heli1.upgrade(["3-0-1", "3-0-2"])
        elif round == 40:
            ability(1, 3)
        elif round == 43:
            heli2.upgrade(["2-0-1", "2-0-2", "2-0-3"])
            hero.target("strong")
        elif round == 49:
            heli2.upgrade(["2-0-4"])
            village.upgrade(["1-2-0", "2-2-0"])
        elif round == 59:
            heli1.upgrade(["4-0-2"])
        elif round == 81:
            heli1.upgrade(["5-0-2"])
        elif round == 83:
            village.upgrade(["2-3-0"])
        elif round == 94:
            heli2.upgrade(["2-0-5"])
        elif round == 95:
            glue = Monkey("glue", 0.4640625, 0.7722222222222)
            glue.upgrade(["0-0-1", "0-0-2", "0-0-3", "0-1-3", "0-2-3"])
        elif round == 96:
            glue.target("strong")
            glue.upgrade(["0-2-4"])
        elif round == 97:
            sniper.upgrade(["2-0-0", "3-0-0", "3-1-0", "3-2-0"])
        elif round == 98:
            sniper.upgrade(["4-2-0"])
            ability(2, 10)
