"""
[Hero] Sauda
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
glue 0-2-4

sniper 2-5-5

alch 5-2-0

village 2-0-2
engineer 0-3-0
_______________________________________
Sniper strat, copied from sunken columns Chimps
"""

from ._plan_imports import *


def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN - 1
    map_start = time()
    while round < END + 1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:
            hero = Hero(0.3171875, 0.3398148148148)   
        elif round == 8:
            sniper1 = Monkey('sniper', 0.4494791666667, 0.4583333333333)
            sniper1.target('strong')
        elif round == 13:
            sniper2 = Monkey('sniper', 0.4703125, 0.2546296296296)
        elif round == 25:
            village = Monkey('village', 0.4244791666667, 0.3731481481481)
            village.upgrade(['0-0-1','0-0-2'])
            sniper1.upgrade(['1-0-0','1-1-0'])
        elif round == 26:
            sniper1.upgrade(['1-2-0'])
        elif round == 31:
            sniper1.upgrade(['1-3-0'])
            sniper1.target('first')
        elif round == 34:
            sniper2.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2'])
        elif round == 37:
            sniper2.upgrade(['0-2-3'])
        elif round == 40:
            sniper2.upgrade(['0-2-4'])
        elif round == 42:
            alch = Monkey('alch', 0.4401041666667, 0.2824074074074)
            village.upgrade(['1-0-2','2-0-2'])
        elif round == 45:
            alch.upgrade(['1-0-0','2-0-0','3-0-0','3-1-0','3-2-0'])
        elif round == 51:
            sniper2.upgrade(['0-2-5'])
            glue = Monkey('glue', 0.3546875, 0.3787037037037)
            glue.target('strong')
        elif round == 54:
            glue.upgrade(['0-1-0','0-1-1','0-1-2','0-1-3'])
        elif round == 55:
            engi = Monkey('engineer', 0.3515625, 0.3083333333333)
            engi.upgrade(['0-1-0','0-2-0','0-3-0'])
            engi.special(1, 0.2036458333333, 0.3824074074074)
        elif round == 56:
            alch.upgrade(['4-2-0'])
        elif round == 81:
            alch.upgrade(['5-2-0'])
        elif round == 82:
            glue.upgrade(['0-2-4'])
        elif round == 84:
            sniper1.upgrade(['1-4-0'])
        elif round == 88:
            sniper1.upgrade(['1-5-0'])
        elif round == 89:
            sniper1.upgrade(['2-5-0'])
            sniper3 = Monkey('sniper', 0.4765625, 0.3305555555556)
        elif round == 91:
            sniper3.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2','0-2-3'])
        elif round == 92:
            sniper3.upgrade(['0-2-4'])
            sniper4 = Monkey('sniper', 0.4880208333333, 0.3898148148148)
        elif round == 94:
            sniper4.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2','0-2-3','0-2-4'])
            sniper5 = Monkey('sniper', 0.5119791666667, 0.2731481481481)
        elif round == 96:
            sniper5.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2','0-2-3','0-2-4'])
            sniper6 = Monkey('sniper', 0.5182291666667, 0.325)
            sniper7 = Monkey('sniper', 0.4890625, 0.4453703703704)
        elif round == 98:
            sniper6.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2','0-2-3','0-2-4'])
            sniper7.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2','0-2-3','0-2-4'])