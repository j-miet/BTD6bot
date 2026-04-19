"""
[Hero] Psi
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0
glue 0-2-3
bomb 2-0-5

sniper 5-5-5
sub 0-0-0

alch 4-2-0

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
            sub = Monkey("sub", 0.2588541666667, 0.2185185185185)
            dart = Monkey("dart", 0.7557291666667, 0.5703703703704)
        elif round == 8:
            sniper1 = Monkey("sniper", 0.4713541666667, 0.4203703703704)
        elif round == 13:
            hero = Hero(0.4901041666667, 0.187037037037)
            hero.target("strong")
        elif round == 14:
            sniper2 = Monkey("sniper", 0.3994791666667, 0.4240740740741)
        elif round == 16:
            sniper3 = Monkey("sniper", 0.4026041666667, 0.312962962963)
            sniper3.target("strong")
        elif round == 19:
            sniper1.upgrade(["0-0-1", "0-0-2"])
        elif round == 22:
            sniper3.upgrade(["1-0-0"])
        elif round == 25:
            sniper1.upgrade(["0-1-2", "0-2-2"])
        elif round == 32:
            sniper1.upgrade(["0-2-3"])
        elif round == 37:
            sniper1.upgrade(["0-2-4"])
        elif round == 39:
            alch = Monkey("alch", 0.4932291666667, 0.4851851851852)
            alch.upgrade(["1-0-0", "2-0-0", "3-0-0"])
        elif round == 41:
            alch.upgrade(["3-1-0", "3-2-0"])
        elif round == 44:
            village = Monkey("village", 0.4994791666667, 0.3092592592593)
            village.upgrade(["1-0-0", "2-0-0"])
        elif round == 46:
            sniper2.upgrade(["0-1-0", "0-2-0", "0-3-0", "0-3-1", "0-3-2"])
        elif round == 48:
            alch.upgrade(["4-2-0"])
        elif round == 50:
            sniper2.upgrade(["0-4-2"])
        elif round == 57:
            sniper2.upgrade(["0-5-2"])
            sniper2.target("first")
        elif round == 59:
            sniper3.upgrade(["2-0-0", "3-0-0", "3-1-0", "3-2-0"])
        elif round == 70:
            sniper1.upgrade(["0-2-5"])
        elif round == 78:
            alch2 = Monkey("alch", 0.3484375, 0.4592592592593)
            alch2.upgrade(["1-0-0", "2-0-0", "3-0-0", "4-0-0", "4-1-0", "4-2-0"])
        elif round == 80:
            sniper3.upgrade(["4-2-0"])
        elif round == 84:
            sniper3.upgrade(["5-2-0"])
        elif round == 88:
            village.upgrade(["2-1-0", "2-2-0", "2-3-0"])
        elif round == 94:
            glue = Monkey("glue", 0.4130208333333, 0.1555555555556)
            glue.upgrade(["0-0-1", "0-0-2", "0-0-3", "0-1-3", "0-2-3"])
            glue.target("strong")
        elif round == 95:
            bomb = Monkey("bomb", 0.4078125, 0.2240740740741)
            bomb.upgrade(["0-0-1", "0-0-2", "0-0-3", "0-0-4", "1-0-4", "2-0-4"])
        elif round == 98:
            ability(2, 10)
            bomb.upgrade(["2-0-5"])
