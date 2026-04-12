"""
[Hero] Psi
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0

sniper 4-2-0
heli 5-0-5

ninja 0-0-4

village 2-3-0
engineer 1-0-0
_______________________________________
The white garder borders will unfortunately cause bad round detection issues because round number has also white color.
Now the plan itself is very simple and works just fine, but each round must be ended manually which no doubt adds
a few minutes to final time.
"""

from ._plan_imports import *


def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN - 1
    map_start = time()
    while round < END + 1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:
            change_autostart()
            engi = Monkey("engineer", 0.3473958333333, 0.3074074074074)
            dart = Monkey("dart", 0.3088541666667, 0.412962962963)
            forward()
            end_round(10)
        elif round == 7:
            end_round(12)
        elif round == 8:
            end_round(11)
        elif round == 9:
            end_round(10)
        elif round == 10:
            engi.upgrade(["1-0-0"])
            end_round(20)
        elif round == 11:
            end_round(10)
        elif round == 12:
            end_round(10)
        elif round == 13:
            hero = Hero(0.0692708333333, 0.612962962963)
            hero.target("strong")
            end_round(6)
        elif round == 14:
            end_round(13)
        elif round == 15:
            end_round(12)
        elif round == 16:
            end_round(9)
        elif round == 17:
            end_round(5)
        elif round == 18:
            end_round(13)
        elif round == 19:
            heli1 = Monkey("heli", 0.0557291666667, 0.5240740740741)
            heli1.special(1, 0.2880208333333, 0.6759259259259)
            end_round(2)
        elif round == 20:
            end_round(4)
        elif round == 21:
            end_round(8)
        elif round == 22:
            end_round(5)
        elif round == 23:
            heli1.upgrade(["1-0-0"])
            end_round(4)
        elif round == 24:
            end_round(6)
        elif round == 25:
            heli1.upgrade(["2-0-0"])
            end_round(10)
        elif round == 26:
            end_round(7)
        elif round == 27:
            sniper = Monkey("sniper", 0.0619791666667, 0.7518518518519)
            sniper.upgrade(["1-0-0"])
            sniper.target("strong")
            end_round(12)
        elif round == 28:
            end_round(5)
        elif round == 29:
            end_round(7)
        elif round == 30:
            end_round(6)
        elif round == 31:
            end_round(6)
        elif round == 32:
            heli1.upgrade(["3-0-0"])
            end_round(12)
        elif round == 33:
            end_round(10)
        elif round == 34:
            end_round(14)
        elif round == 35:
            village1 = Monkey("village", 0.0588541666667, 0.4166666666667)
            village1.upgrade(["0-1-0"])
            end_round(13)
        elif round == 36:
            village1.upgrade(["0-2-0"])
            end_round(2)
        elif round == 37:
            end_round(17)
        elif round == 38:
            heli2 = Monkey("heli", 0.0609375, 0.2944444444444)
            end_round(12)
        elif round == 39:
            heli2.upgrade(["1-0-0", "2-0-0", "2-0-1", "2-0-2"])
            end_round(5)
        elif round == 40:
            end_round(6)
        elif round == 41:
            end_round(17)
        elif round == 42:
            end_round(5)
        elif round == 43:
            heli2.upgrade(["2-0-3"])
            heli1.upgrade(["3-0-1", "3-0-2"])
            end_round(5)
        elif round == 44:
            end_round(10)
        elif round == 45:
            end_round(19)
        elif round == 46:
            end_round(5)
        elif round == 47:
            end_round(10)
        elif round == 48:
            heli2.upgrade(["2-0-4"])
            end_round(4)
        elif round == 49:
            end_round(18)
        elif round == 50:
            end_round(13)
        elif round == 51:
            end_round(10)
        elif round == 52:
            end_round(12)
        elif round == 53:
            end_round(15)
        elif round == 54:
            end_round(10)
        elif round == 55:
            end_round(14)
        elif round == 56:
            end_round(10)
        elif round == 57:
            end_round(11)
        elif round == 58:
            heli1.upgrade(["4-0-2"])
            end_round(9)
        elif round == 59:
            village1.upgrade(["1-2-0", "2-2-0"])
            end_round(10)
        elif round == 60:
            end_round(6)
        elif round == 61:
            end_round(9)
        elif round == 62:
            end_round(18)
        elif round == 63:
            end_round(16)
        elif round == 64:
            end_round(7)
        elif round == 65:
            end_round(27)
        elif round == 66:
            end_round(11)
        elif round == 67:
            end_round(12)
        elif round == 68:
            end_round(8)
        elif round == 69:
            end_round(16)
        elif round == 70:
            end_round(17)
        elif round == 71:
            end_round(8)
        elif round == 72:
            end_round(11)
        elif round == 73:
            end_round(13)
        elif round == 74:
            end_round(30)
        elif round == 75:
            end_round(17)
        elif round == 76:
            end_round(4)
        elif round == 77:
            end_round(23)
        elif round == 78:
            end_round(32)
        elif round == 79:
            end_round(30)
        elif round == 80:
            end_round(22)
        elif round == 81:
            heli1.upgrade(["5-0-2"])
            end_round(5)
        elif round == 82:
            end_round(18)
        elif round == 83:
            village1.upgrade(["2-3-0"])
            end_round(13)
        elif round == 84:
            end_round(12)
        elif round == 85:
            end_round(13)
        elif round == 86:
            end_round(12)
        elif round == 87:
            end_round(13)
        elif round == 88:
            end_round(13)
        elif round == 89:
            end_round(14)
        elif round == 90:
            end_round(7)
        elif round == 91:
            end_round(14)
        elif round == 92:
            end_round(21)
        elif round == 93:
            end_round(15)
        elif round == 94:
            heli2.upgrade(["2-0-5"])
            end_round(8)
        elif round == 95:
            end_round(22)
        elif round == 96:
            sniper.upgrade(["1-0-0", "2-0-0", "3-0-0", "4-0-0", "4-1-0", "4-2-0"])
            end_round(11)
        elif round == 97:
            end_round(12)
        elif round == 98:
            ninja = Monkey("ninja", 0.2276041666667, 0.4092592592593)
            ninja.upgrade(["0-0-1", "0-0-2", "0-0-3", "0-0-4"])
            end_round(12)
        elif round == 99:
            end_round(8)
        elif round == 100:
            change_autostart()
