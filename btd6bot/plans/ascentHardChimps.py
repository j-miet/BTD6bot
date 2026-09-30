"""
[Hero] Obyn
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0

sniper 0-2-5
sub 0-0-0
heli 5-0-2

wizard 5-2-0
alch 4-2-0
druid 0-0-0

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
            sub = Monkey("sub", 0.3927083333333, 0.162037037037)
            dart = Monkey("dart", 0.6916666666667, 0.4564814814815)
        elif round == 8:
            druid = Monkey("druid", 0.63125, 0.2138888888889)
        elif round == 10:
            sniper = Monkey("sniper", 0.4604166666667, 0.4490740740741)
        elif round == 13:
            hero = Hero(0.4114583333333, 0.4472222222222)
        elif round == 17:
            sniper.upgrade(["0-0-1", "0-0-2"])
        elif round == 20:
            sniper.upgrade(["0-1-2", "0-2-2"])
        elif round == 29:
            sniper.upgrade(["0-2-3"])
        elif round == 37:
            sniper.upgrade(["0-2-4"])
        elif round == 39:
            alch = Monkey("alch", 0.5479166666667, 0.5583333333333)
            alch.upgrade(["1-0-0", "2-0-0", "3-0-0"])
        elif round == 41:
            alch.upgrade(["4-0-0", "4-1-0", "4-2-0"])
        elif round == 50:
            sniper.upgrade(["0-2-5"])
        elif round == 54:
            village = Monkey("village", 0.459375, 0.5527777777778)
            village.upgrade(["1-0-0", "2-0-0", "2-1-0", "2-2-0"])
        elif round == 57:
            heli = Monkey("heli", 0.5302083333333, 0.6601851851852)
            heli.upgrade(["1-0-0", "2-0-0", "3-0-0", "3-0-1", "3-0-2"])
        elif round == 70:
            heli.upgrade(["4-0-2"])
        elif round == 84:
            heli.upgrade(["5-0-2"])
        elif round == 88:
            village.upgrade(["2-3-0"])
        elif round == 91:
            wizard = Monkey("wizard", 0.3651041666667, 0.4675925925926)
            wizard.upgrade(["1-0-0", "2-0-0", "3-0-0", "3-1-0", "3-2-0"])
        elif round == 93:
            wizard.upgrade(["4-2-0"])
        elif round == 98:
            wizard.upgrade(["5-2-0"])
