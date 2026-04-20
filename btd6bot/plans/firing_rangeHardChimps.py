"""
[Hero] Rosalia
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0

sniper 0-2-2
ace 2-0-5

alch 3-2-0

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
            dart1 = Monkey("dart", 0.7864583333333, 0.2351851851852)
            dart2 = Monkey("dart", 0.0947916666667, 0.2462962962963)
        elif round == 7:
            sniper = Monkey("sniper", 0.7869791666667, 0.3074074074074)
        elif round == 11:
            hero = Hero(0.5151041666667, 0.5537037037037)
            hero.special(2, 0.5994791666667, 0.5314814814815)
        elif round == 15:
            ability(1, 6)
        elif round == 16:
            click(0.4276041666667, 0.4814814814815)
            wait(0.25)
            click(0.4817708333333, 0.5851851851852)
            wait(0.5)
            hero.special(2, 0.4286458333333, 0.4148148148148)
        elif round == 19:
            sniper.upgrade(["0-0-1", "0-0-2"])
        elif round == 21:
            ability(1, 1)
        elif round == 22:
            sniper.upgrade(["0-1-2", "0-2-2"])
        elif round == 27:
            hero.special(1)
        elif round == 33:
            village1 = Monkey("village", 0.4921875, 0.6888888888889)
            village1.upgrade(["0-0-1", "0-0-2"])
        elif round == 34:
            ace = Monkey("ace", 0.4307291666667, 0.5925925925926)
            ace.upgrade(["0-0-1", "0-0-2"])
        elif round == 35:
            ace.upgrade(["0-0-3"])
        elif round == 36:
            ace.upgrade(["1-0-3", "2-0-3"])
        elif round == 39:
            alch = Monkey("alch", 0.4328125, 0.7685185185185)
            alch.upgrade(["1-0-0", "2-0-0"])
        elif round == 41:
            alch.upgrade(["3-0-0", "3-1-0", "3-2-0"])
            village2 = Monkey("village", 0.3828125, 0.7148148148148)
        elif round == 42:
            village2.upgrade(["0-1-0", "0-2-0"])
        elif round == 43:
            village2.upgrade(["1-2-0", "2-2-0"])
        elif round == 54:
            ace.upgrade(["2-0-4"])
        elif round == 87:
            ace.upgrade(["2-0-5"])
