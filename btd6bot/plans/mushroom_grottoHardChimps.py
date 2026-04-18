"""
[Hero] Obyn
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-2-4

sniper 2-0-5

alch 4-2-0
druid 5-1-4
mermonkey 0-0-0

village 2-0-2
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
            mermonkey1 = Monkey("mermonkey", 0.3984375, 0.3185185185185)
            mermonkey2 = Monkey("mermonkey", 0.4963541666667, 0.7157407407407)
        elif round == 8:
            dart = Monkey("dart", 0.3958333333333, 0.6046296296296)
        elif round == 9:
            dart2 = Monkey("dart", 0.4989583333333, 0.4287037037037)
        elif round == 12:
            hero = Hero(0.4625, 0.4361111111111)
        elif round == 13:
            druid1 = Monkey("druid", 0.4984375, 0.5990740740741)
        elif round == 15:
            druid2 = Monkey("druid", 0.3984375, 0.5472222222222)
        elif round == 18:
            dart.upgrade(["0-0-1", "0-0-2"])
        elif round == 19:
            dart.upgrade(["0-0-3"])
        elif round == 20:
            dart.upgrade(["0-1-3", "0-2-3"])
        elif round == 21:
            druid3 = Monkey("druid", 0.3994791666667, 0.4861111111111)
        elif round == 23:
            druid2.upgrade(["1-0-0"])
        elif round == 28:
            forward(1)
            # remove darkness
            click(0.1848958333333, 0.762037037037)
            wait(0.25)
            click(0.4911458333333, 0.6046296296296)
            wait(0.25)
            click(0.1848958333333, 0.2509259259259)
            wait(0.25)
            click(0.4911458333333, 0.6064814814815)
            wait(0.25)
            click(0.7057291666667, 0.2787037037037)
            wait(0.25)
            click(0.4880208333333, 0.5916666666667)
            wait(0.25)
            click(0.7265625, 0.7972222222222)
            wait(0.25)
            click(0.4901041666667, 0.6046296296296)
            wait(0.25)
            click(0.4546875, 0.5157407407407)
            wait(0.25)
            click(0.5140625, 0.537962962963)
            forward(1)
        elif round == 32:
            dart.upgrade(["0-2-4"])
        elif round == 35:
            village = Monkey("village", 0.4432291666667, 0.587962962963)
        elif round == 36:
            village.upgrade(["0-0-1", "0-0-2"])
            druid2.upgrade(["2-0-0", "2-0-1"])
        elif round == 39:
            druid4 = Monkey("druid", 0.4963541666667, 0.537962962963)
            druid2.upgrade(["3-0-1", "3-0-2"])
        elif round == 41:
            druid2.upgrade(["4-0-2"])
        elif round == 45:
            druid1.upgrade(["0-0-1", "0-0-2", "0-0-3", "0-0-4", "0-1-4"])
        elif round == 48:
            druid3.upgrade(["0-0-1", "0-0-2", "0-0-3", "0-0-4", "0-1-4"])
        elif round == 49:
            village.upgrade(["1-0-2", "2-0-2"])
            druid4.upgrade(["0-0-1", "0-0-2", "0-0-3", "0-0-4", "0-1-4"])
        elif round == 50:
            alch1 = Monkey("alch", 0.33125, 0.4953703703704)
            alch1.upgrade(["1-0-0", "2-0-0", "3-0-0"])
        elif round == 51:
            alch1.upgrade(["4-0-0", "4-1-0", "4-2-0"])
        elif round == 53:
            alch2 = Monkey("alch", 0.5645833333333, 0.5416666666667)
            alch2.upgrade(["1-0-0", "2-0-0", "3-0-0"])
        elif round == 55:
            alch2.upgrade(["4-0-0", "4-1-0", "4-2-0"])
        elif round == 84:
            druid2.upgrade(["5-0-2"])
        elif round == 88:
            sniper = Monkey("sniper", 0.4473958333333, 0.737962962963)
            sniper.target("strong")
            sniper.upgrade(["0-0-1", "0-0-2", "0-0-3", "0-0-4", "1-0-4", "2-0-4"])
        elif round == 92:
            sniper.upgrade(["2-0-5"])
        elif round == 95:
            sniper2 = Monkey("sniper", 0.3942708333333, 0.7333333333333)
            sniper2.target("strong")
            sniper2.upgrade(["0-0-1", "0-0-2", "0-0-3", "0-0-4", "1-0-4", "2-0-4"])
        elif round == 96:
            sniper3 = Monkey("sniper", 0.4411458333333, 0.7935185185185)
            sniper3.target("strong")
            sniper3.upgrade(["0-0-1", "0-0-2", "0-0-3", "0-0-4", "1-0-4", "2-0-4"])
        elif round == 97:
            sniper4 = Monkey("sniper", 0.4880208333333, 0.7814814814815)
            sniper4.target("strong")
            sniper4.upgrade(["0-0-1", "0-0-2", "0-0-3", "0-0-4", "1-0-4", "2-0-4"])
        elif round == 98:
            sniper5 = Monkey("sniper", 0.3578125, 0.7240740740741)
            sniper5.target("strong")
            sniper5.upgrade(["0-0-1", "0-0-2", "0-0-3", "0-0-4", "1-0-4", "2-0-4"])
