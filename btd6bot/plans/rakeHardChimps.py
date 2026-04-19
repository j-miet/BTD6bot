"""
[Hero] Rosalia
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0

sub 1-0-2
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
            sub = Monkey("sub", 0.4895833333333, 0.3833333333333)
            dart = Monkey("dart", 0.5604166666667, 0.5333333333333)
        elif round == 8:
            sub.upgrade(["1-0-0"])
        elif round == 9:
            sub.upgrade(["1-0-1"])
        elif round == 10:
            sniper = Monkey("sniper", 0.3791666666667, 0.9111111111111)
        elif round == 15:
            hero = Hero(0.45, 0.5537037037037)
            hero.special(2, 0.521875, 0.5425925925926)
        elif round == 18:
            ability(1, 8)
        elif round == 19:
            sub.upgrade(["1-0-2"])
        elif round == 23:
            sniper.upgrade(["0-1-0", "0-2-0"])
        elif round == 25:
            sniper.upgrade(["0-2-1", "0-2-2"])
        elif round == 27:
            hero.target("strong")
            hero.special(1)
        elif round == 33:
            village = Monkey("village", 0.3807291666667, 0.5601851851852)
            village.upgrade(["0-0-1", "0-0-2"])
        elif round == 34:
            ace = Monkey("ace", 0.3671875, 0.6703703703704)
            ace.upgrade(["0-0-1", "0-0-2"])
        elif round == 36:
            ace.upgrade(["0-0-3"])
            ace.center(0.5973958333333, 0.9166666666667)
        elif round == 37:
            bomb = Monkey("bomb", 0.5546875, 0.4037037037037)
            bomb.target("strong")
            ace.upgrade(["1-0-3", "2-0-3"])
        elif round == 38:
            ability(1, 3)
        elif round == 40:
            ability(2)
            ability(1)
        elif round == 41:
            village2 = Monkey("village", 0.3130208333333, 0.5777777777778)
            village2.upgrade(["0-1-0", "0-2-0"])
        elif round == 42:
            village2.upgrade(["1-2-0", "2-2-0"])
        elif round == 45:
            alch = Monkey("alch", 0.2848958333333, 0.6537037037037)
            alch.upgrade(["1-0-0", "2-0-0", "3-0-0", "3-1-0", "3-2-0"])
        elif round == 55:
            ace.upgrade(["2-0-4"])
        elif round == 87:
            ability(2, 3)
            ability(1, 3)
            ability(3, 8)
        elif round == 88:
            ace.upgrade(["2-0-5"])
