"""
[Hero] Etienne
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0
boomer 0-2-4
tack 2-0-4
ice 5-2-0
glue 0-2-4

sniper 4-1-2

wizard 5-3-2
alch 4-2-0
mermonkey 4-3-2

village 4-0-2
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
            dart1 = Monkey("dart", 0.3916666666667, 0.337962962963)
            dart2 = Monkey("dart", 0.4166666666667, 0.4083333333333)
            dart3 = Monkey("dart", 0.5223958333333, 0.5787037037037)
        if round == 7:
            dart3.upgrade(["0-1-0"])
        elif round == 9:
            mermonkey1 = Monkey("mermonkey", 0.4921875, 0.5231481481481)
        elif round == 10:
            mermonkey2 = Monkey("mermonkey", 0.3036458333333, 0.2435185185185)
        elif round == 13:
            hero = Hero(0.4567708333333, 0.5583333333333)
        elif round == 14:
            wizard = Monkey("wizard", 0.3864583333333, 0.4398148148148)
            wizard.target("close")
        elif round == 15:
            wizard.upgrade(["1-0-0"])
        elif round == 17:
            wizard.upgrade(["2-0-0"])
        elif round == 18:
            ability(1, 3.5)
        elif round == 19:
            sniper = Monkey("sniper", 0.3046875, 0.7342592592593)
            sniper.target("strong")
        elif round == 20:
            sniper2 = Monkey("sniper", 0.6859375, 0.7083333333333)
        elif round == 21:
            mermonkey3 = Monkey("mermonkey", 0.5609375, 0.7305555555556)
        elif round == 22:
            sniper.upgrade(["1-0-0"])
        elif round == 23:
            ability(1)
        elif round == 24:
            sniper.upgrade(["1-0-1"])
        elif round == 26:
            sniper.upgrade(["1-0-2"])
        elif round == 27:
            ability(1, 5.5)
        elif round == 30:
            wizard.upgrade(["3-0-0"])
        elif round == 31:
            mermonkey4 = Monkey("mermonkey", 0.35, 0.4768518518519)
            mermonkey4.upgrade(["0-0-1"])
        elif round == 32:
            mermonkey4.upgrade(["1-0-1", "2-0-1"])
            sniper2.upgrade(["0-1-0"])
        elif round == 34:
            mermonkey3.upgrade(["0-0-1", "0-1-1", "0-2-1"])
        elif round == 35:
            mermonkey4.upgrade(["3-0-1"])
        elif round == 36:
            ability(1)
            wizard.upgrade(["3-1-0", "3-2-0"])
            wizard.target("first")
        elif round == 38:
            sniper.upgrade(["2-0-2"])
        elif round == 39:
            sniper.upgrade(["3-0-2"])
        elif round == 40:
            ability(1)
        elif round == 41:
            village = Monkey("village", 0.4208333333333, 0.6175925925926)
            village.upgrade(["1-0-0"])
        elif round == 42:
            village.upgrade(["2-0-0"])
        elif round == 49:
            wizard.upgrade(["4-2-0"])
        elif round == 51:
            village.upgrade(["3-0-0", "4-0-0", "4-0-1", "4-0-2"])
            mermonkey4.upgrade(["3-0-2"])
            mermonkey3.upgrade(["0-3-1", "0-3-2"])
            mermonkey5 = Monkey("mermonkey", 0.3140625, 0.5194444444444)
        elif round == 52:
            ability(2, 2)
        elif round == 53:
            mermonkey5.upgrade(["0-1-0", "0-2-0", "0-3-0", "0-3-1", "0-3-2"])
            mermonkey1.upgrade(["0-1-0", "0-2-0", "0-2-1", "0-2-2"])  # skip 0-3-2
        elif round == 54:
            ability(1)
            mermonkey6 = Monkey("mermonkey", 0.5270833333333, 0.7768518518519)
            mermonkey6.upgrade(["0-1-0", "0-2-0", "0-3-0", "0-3-1", "0-3-2"])
        elif round == 55:
            mermonkey7 = Monkey("mermonkey", 0.4864583333333, 0.612037037037)
            mermonkey7.upgrade(["0-1-0", "0-2-0"])
        elif round == 56:
            ability(2)
            mermonkey7.upgrade(["0-3-0", "0-3-1", "0-3-2"])
        elif round == 60:
            ability(2)
            ability(1)
            mermonkey4.upgrade(["4-0-2"])
        elif round == 61:
            ice = Monkey("ice", 0.4260416666667, 0.6916666666667)
            ice.upgrade(["1-0-0", "2-0-0", "3-0-0"])
        elif round == 62:
            ice.upgrade(["4-0-0", "4-1-0", "4-2-0"])
        elif round == 63:
            ability(1)
            ice2 = Monkey("ice", 0.35625, 0.4046296296296)
            ice2.upgrade(["1-0-0", "2-0-0"])
            ability(2, 6.5)
            ice2.upgrade(["3-0-0", "3-1-0"])
        elif round == 65:
            ice2.upgrade(["4-1-0", "4-2-0"])
            ability(2, 16.5)
        elif round == 68:
            ability(1, 2)
            ability(2, 4)
        elif round == 75:
            ability(1)
            ability(2, 6)
        elif round == 77:
            ability(1, 6)
        elif round == 78:
            ability(2)
            ability(1, 12)
            ability(2, 27)
        elif round == 79:
            wizard.upgrade(["5-2-0"])
        elif round == 80:
            ability(1)
        elif round == 81:
            glue = Monkey("glue", 0.5203125, 0.4805555555556)
            glue.target("strong")
            glue.upgrade(["0-0-1", "0-0-2", "0-0-3", "0-1-3"])
        elif round == 87:
            ability(1)
        elif round == 88:
            ability(2)
        elif round == 89:
            ice.upgrade(["5-2-0"])
            glue.upgrade(["0-2-3"])
        elif round == 91:
            glue.upgrade(["0-2-4"])
        elif round == 93:
            ice3 = Monkey("ice", 0.4463541666667, 0.3731481481481)
            ice3.upgrade(["0-1-0", "0-2-0", "0-3-0"])
        elif round == 94:
            ability(2)
            ability(1)
            forward(1)
            ice3.upgrade(["0-4-0", "1-4-0", "2-4-0"])
            tack = Monkey("tack", 0.3765625, 0.6490740740741)
            forward(1)
            tack.upgrade(["0-0-1", "0-0-2", "0-0-3", "0-0-4", "1-0-4", "2-0-4"])
        elif round == 95:
            boomer = Monkey("boomer", 0.3442708333333, 0.6916666666667)
            boomer.target("strong")
            boomer.upgrade(["0-0-1", "0-0-2", "0-0-3"])
            ability(3, 11)
            ability(2, 14)
        elif round == 96:
            boomer.upgrade(["0-0-4", "0-1-4", "0-2-4"])
            alch = Monkey("alch", 0.39375, 0.7064814814815)
            ability(3, 12)
        elif round == 97:
            alch.upgrade(["1-0-0", "2-0-0", "3-0-0", "4-0-0", "4-1-0", "4-2-0"])
        elif round == 98:
            ability(1)
            ability(2)
            ability(3, 2.5)
            sniper.upgrade(["4-0-2"])
            forward(1)
            tack = Monkey("tack", 0.5364583333333, 0.5259259259259)
            tack.upgrade(["0-0-1", "0-0-2", "0-0-3", "0-0-4", "1-0-4", "2-0-4"])
            tack2 = Monkey("tack", 0.2854166666667, 0.5638888888889)
            tack2.upgrade(["0-0-1", "0-0-2", "0-0-3", "0-0-4", "1-0-4", "2-0-4"])
            forward(1)
        elif round == 99:
            ability(3, 2.25)
            forward(1)
            tack3 = Monkey("tack", 0.3135416666667, 0.4546296296296)
            tack3.upgrade(["0-0-1", "0-0-2", "0-0-3", "1-0-3", "2-0-3"])
            forward(1)
        elif round == 100:
            ability(1, 1)
