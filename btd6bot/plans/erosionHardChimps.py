"""
[Hero] Psi
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-1
glue 0-2-4

sniper 5-5-5
sub 2-0-2

ninja 0-0-0
alch 4-2-0

spike 2-0-5
village 2-2-0
_______________________________________
Gameplay-wise viable for black borders.

Bot will falsely detect round changes. Reason is there are lots of projectiles/bloons moving around round label,
especially in the later stages of game, which can cause false positives. This is not really an issue as long as there
are no abilities/targeting changes so it can stay on from start to round 79. After 79 there are retargeting/ability
requirements: to fix this, the late game rounds are timed manually to prevent round auto-detection and instead force
them after specific time has passed.

Another harmless effect is incorrectly saved round times: some display too short (0:00) and other too long round
durations (multiple minutes)
"""

from ._plan_imports import *


def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN - 1
    map_start = time()
    while round < END + 1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:
            sub1 = Monkey("sub", 0.2177083333333, 0.8157407407407)
            dart1 = Monkey("dart", 0.1911458333333, 0.5555555555556)
            forward()
            dart1.upgrade(["0-0-1"])
        elif round == 8:
            sub1.upgrade(["0-0-1"])
        elif round == 13:
            sub1.upgrade(["0-0-2"])
        elif round == 18:
            hero = Hero(0.6494791666667, 0.0537037037037)
            sub1.upgrade(["1-0-2"])
        elif round == 21:
            sub1.upgrade(["2-0-2"])
        elif round == 25:
            sniper1 = Monkey("sniper", 0.7651041666667, 0.1)
        elif round == 26:
            sniper2 = Monkey("sniper", 0.7067708333333, 0.0481481481481)
        elif round == 27:
            sniper3 = Monkey("sniper", 0.8255208333333, 0.1740740740741)
            sniper3.upgrade(["1-0-0"])
            sniper3.target("strong")
        elif round == 28:
            sniper2.upgrade(["0-1-0", "0-2-0"])
        elif round == 30:
            sniper2.upgrade(["0-2-1"])
        elif round == 31:
            sniper2.upgrade(["0-2-2"])
        elif round == 35:
            sniper2.upgrade(["0-2-3"])
            hero.target("strong")
        elif round == 36:
            ninja = Monkey("ninja", 0.1723958333333, 0.2564814814815)
        elif round == 39:
            sniper2.upgrade(["0-2-4"])
        elif round == 41:
            alch1 = Monkey("alch", 0.7390625, 0.0648148148148)
            alch1.upgrade(["1-0-0", "2-0-0", "3-0-0"])
        elif round == 43:
            alch1.upgrade(["3-1-0", "3-2-0"])
        elif round == 45:
            sniper1.upgrade(["0-1-0", "0-2-0", "0-3-0", "0-3-1", "0-3-2"])
        elif round == 47:
            village = Monkey("village", 0.8140625, 0.1018518518519)
            village.upgrade(["1-0-0", "2-0-0"])
        elif round == 49:
            sniper1.upgrade(["0-4-2"])
        elif round == 57:
            sniper1.upgrade(["0-5-2"])
            sniper1.target("first")
        elif round == 59:
            alch1.upgrade(["4-2-0"])
        elif round == 62:
            sniper3.upgrade(["2-0-0", "3-0-0", "3-1-0", "3-2-0"])
        elif round == 65:
            spike = Monkey("spike", 0.8286458333333, 0.2888888888889)
            spike.upgrade(["1-0-0", "2-0-0", "2-0-1", "2-0-2", "2-0-3"])
            spike.target("set", 0.7932291666667, 0.462962962963)
        elif round == 66:
            spike.upgrade(["2-0-4"])
        elif round == 79:
            spike.upgrade(["2-0-5"])
            change_autostart()
            end_round(8)
        elif round == 80:
            end_round(18)
        elif round == 81:
            end_round(23)
        elif round == 82:
            alch2 = Monkey("alch", 0.8369791666667, 0.2259259259259)
            alch2.upgrade(["1-0-0", "2-0-0", "3-0-0", "4-0-0", "4-1-0", "4-2-0"])
            end_round(22)
        elif round == 83:
            sniper3.upgrade(["4-2-0"])
            end_round(17)
        elif round == 84:
            end_round(21)
        elif round == 85:
            end_round(22)
        elif round == 86:
            end_round(18)
        elif round == 87:
            end_round(25)
        elif round == 88:
            spike.special(1, 0.8526041666667, 0.412962962963)
            end_round(27)
        elif round == 89:
            end_round(24)
        elif round == 90:
            end_round(10)
        elif round == 91:
            end_round(19)
        elif round == 92:
            end_round(30)
        elif round == 93:
            end_round(19)
        elif round == 94:
            ability(1, 4)
            ability(2, 7)
            sniper3.upgrade(["5-2-0"])
            glue = Monkey("glue", 0.7109375, 0.112962962963)
            glue.upgrade(["0-0-1", "0-0-2", "0-0-3", "0-1-3"])
            glue.target("strong")
            end_round(5)
        elif round == 95:
            end_round(24)
        elif round == 96:
            ability(1, 4)
            ability(2, 7)
            end_round(20)
        elif round == 97:
            end_round(18)
        elif round == 98:
            sniper2.upgrade(["0-2-5"])
            ability(1, 8)
            ability(2, 11)
            glue.upgrade(["0-1-4", "0-2-4"])
            village.upgrade(["2-1-0", "2-2-0"])
            end_round(13)
        elif round == 99:
            ability(1, 3)
            end_round(7)
        elif round == 100:
            change_autostart()
