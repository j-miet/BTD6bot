"""
[Hero] Sauda
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 5-2-0

mortar 0-2-3

alch 3-0-0
druid 1-3-0

spike 2-0-5
engineer 4-2-0
_______________________________________
Derived from glacial_trailHardChimps.
"""

from._plan_imports import *

def play(rounds: tuple[str, str, str, int, int, str]) -> None:
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start, rounds[2])
        if current_round == BEGIN:
            engi_temp = Monkey('engineer', 0.1651041666667, 0.5027777777778)
            dart_temp = Monkey('dart', 0.7151041666667, 0.6138888888889)
        elif current_round == 6:
            engi_temp.sell()
            Hero(0.1651041666667, 0.5027777777778)
        elif current_round == 7:
            dart_temp.sell()
        elif current_round == 8:
            dart = Monkey('dart', 0.1239583333333, 0.5055555555556)
            dart.target('strong')
        elif current_round == 14:
            engi = Monkey('engineer', 0.7151041666667, 0.6138888888889)
            engi.upgrade(['1-0-0', '2-0-0'])
            dart.upgrade(['0-1-0'])
        elif current_round == 22:
            druid = Monkey('druid', 0.6135416666667, 0.9546296296296)
            druid.upgrade(['0-1-0'])
        elif current_round == 23:
            druid.upgrade(['0-2-0'])
        elif current_round == 24:
            druid.upgrade(['0-3-0'])
        elif current_round == 25:
            druid.upgrade(['1-3-0'])
        elif current_round == 31:
            mortar = Monkey('mortar', 0.1802083333333, 0.9148148148148)
            mortar.special(1, 0.2369791666667, 0.4490740740741)
        elif current_round == 32:
            spike = Monkey('spike', 0.753125, 0.687037037037)
            spike.upgrade(['0-0-1', '0-0-2'])
            spike.target('smart')
        elif current_round == 35:
            spike.upgrade(['0-0-3', '1-0-3', '2-0-3'])
        elif current_round == 39:
            engi.upgrade(['3-0-0', '4-0-0', '4-1-0', '4-2-0'])
        elif current_round == 42:
            mortar.upgrade(['0-0-1', '0-0-2', '0-0-3'])
        elif current_round == 43:
            mortar.upgrade(['0-1-3', '0-2-3'])
            dart.upgrade(['1-1-0'])
        elif current_round == 44:
            dart.upgrade(['2-1-0', '3-1-0', '4-1-0'])
        elif current_round == 45:
            dart.upgrade(['4-2-0'])
        elif current_round == 46:
            spike.upgrade(['2-0-4'])
        elif current_round == 47:
            alch = Monkey('alch', 0.7109375, 0.6759259259259)
            alch.upgrade(['1-0-0', '2-0-0', '3-0-0'])
        elif current_round == 54:
            dart.upgrade(['5-2-0'])
        elif current_round == 74:
            spike.upgrade(['2-0-5'])