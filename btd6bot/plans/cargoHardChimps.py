"""
[Hero] Obyn
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-3-0

sniper 2-2-5

super 3-0-2
alch 5-2-0

village 2-0-2
_______________________________________
Some rng in early game rounds due to Obyn's totem placements
"""

from ._plan_imports import *


def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN - 1
    map_start = time()
    while round < END + 1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:
            dart = Monkey("dart", 0.2270833333333, 0.2277777777778)
            dart2 = Monkey("dart", 0.4020833333333, 0.2314814814815)
            dart3 = Monkey("dart", 0.5833333333333, 0.2296296296296)
        elif round == 7:
            dart.target("strong")
            dart3.upgrade(["0-1-0"])
        elif round == 9:
            sniper = Monkey("sniper", 0.7151041666667, 0.3166666666667)
        elif round == 10:
            dart3.upgrade(["0-2-0"])
            sniper.target("strong")
        elif round == 11:
            sniper.target("first")
        elif round == 13:
            hero = Hero(0.6255208333333, 0.3351851851852)
        elif round == 15:
            dart3.upgrade(["0-3-0"])
        elif round == 20:
            village = Monkey("village", 0.64375, 0.4083333333333)
        elif round == 21:
            ability(1)
        elif round == 24:
            ability(1)
        elif round == 25:
            village.upgrade(["0-0-1", "0-0-2"])
        elif round == 27:
            sniper.upgrade(["0-0-1", "0-0-2"])
        elif round == 28:
            sniper.upgrade(["0-1-2", "0-2-2"])
            ability(1)
        elif round == 34:
            sniper.upgrade(["0-2-3"])
        elif round == 37:
            ability(1, 10)
        elif round == 38:
            sniper.upgrade(["0-2-4"])
        elif round == 39:
            wait(1)
            click(0.6192708333333, 0.7962962962963)
            wait(0.5)
            click(0.6755208333333, 0.8611111111111)
            wait(1)
            alch = Monkey("alch", 0.7182291666667, 0.4314814814815)
            alch.upgrade(["1-0-0", "2-0-0"])
        elif round == 40:
            alch.upgrade(["3-0-0"])
            ability(1)
        elif round == 41:
            alch.upgrade(["3-1-0", "3-2-0"])
        elif round == 42:
            village.upgrade(["1-0-2", "2-0-2"])
        elif round == 50:
            sniper.upgrade(["0-2-5"])
        elif round == 51:
            super = Monkey("super", 0.6161458333333, 0.4962962962963)
        elif round == 54:
            super.upgrade(["1-0-0", "2-0-0"])
        elif round == 55:
            alch.upgrade(["4-2-0"])
        elif round == 62:
            super.upgrade(["2-0-1"])
        elif round == 63:
            ability(1, 12)
        elif round == 65:
            ability(1, 22)
        elif round == 68:
            super.upgrade(["3-0-1"])
        elif round == 70:
            super.upgrade(["3-0-2"])
        elif round == 80:
            ability(1)
        elif round == 82:
            ability(1)
        elif round == 83:
            ability(1)
        elif round == 84:
            ability(1, 8)
            alch.upgrade(["5-2-0"])
        elif round == 88:
            super2 = Monkey("super", 0.6307291666667, 0.5907407407407)
            super2.upgrade(["1-0-0", "2-0-0"])
        elif round == 94:
            super2.upgrade(["3-0-0", "3-0-1", "3-0-2"])
        elif round == 95:
            sniper2 = Monkey("sniper", 0.7192708333333, 0.2648148148148)
            sniper2.target("strong")
            sniper2.upgrade(["1-0-0", "2-0-0", "2-0-1", "2-0-2", "2-0-3"])
        elif round == 96:
            sniper2.upgrade(["2-0-4"])
        elif round == 97:
            sniper3 = Monkey("sniper", 0.6916666666667, 0.2268518518519)
            sniper3.upgrade(["0-0-1", "0-0-2", "0-0-3", "1-0-3"])
        elif round == 98:
            sniper3.upgrade(["2-0-3", "2-0-4"])
            sniper4 = Monkey("sniper", 0.7177083333333, 0.525)
            sniper4.upgrade(["0-0-1", "0-0-2", "0-0-3", "1-0-3", "2-0-3"])
        elif round == 99:
            sniper4.upgrade(["2-0-4"])
        elif round == 100:
            hero.special(1, 0.5114583333333, 0.3555555555556)
            ability(2)
            ability(1)
