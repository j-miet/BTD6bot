"""
[Hero] Sauda
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0
glue 0-2-4

sniper 2-5-5

alch 5-2-0

village 2-0-2
engineer 0-3-0
_______________________________________
"""

from._plan_imports import *

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:     
            dart1 = Monkey('dart', 0.3473958333333, 0.1037037037037)
            dart2 = Monkey('dart', 0.5223958333333, 0.0935185185185)
            dart3 = Monkey('dart', 0.3442708333333, 0.8564814814815)
        elif round == 8:
            sniper1 = Monkey('sniper', 0.5317708333333, 0.9657407407407)
            sniper1.target('strong')
        elif round == 11:
            hero = Hero(0.4473958333333, 0.1657407407407)
        elif round == 13:
            sniper2 = Monkey('sniper', 0.4973958333333, 0.9731481481481)
        elif round == 25:
            village = Monkey('village', 0.4473958333333, 0.9509259259259)
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
            alch = Monkey('alch', 0.4921875, 0.9175925925926)
            village.upgrade(['1-0-2','2-0-2'])
        elif round == 45:
            alch.upgrade(['1-0-0','2-0-0','3-0-0','3-1-0','3-2-0'])
        elif round == 51:
            sniper2.upgrade(['0-2-5'])
            glue = Monkey('glue', 0.4380208333333, 0.1083333333333)
            glue.target('strong')
        elif round == 54:
            glue.upgrade(['0-1-0','0-1-1','0-1-2','0-1-3'])
        elif round == 55:
            engi = Monkey('engineer', 0.4401041666667, 0.0416666666667)
            engi.upgrade(['0-1-0','0-2-0','0-3-0'])
            engi.special(1, 0.4380208333333, 0.2212962962963)
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
            sniper3 = Monkey('sniper', 0.4015625, 0.9712962962963)
        elif round == 91:
            sniper3.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2','0-2-3'])
        elif round == 92:
            sniper3.upgrade(['0-2-4'])
            sniper4 = Monkey('sniper', 0.4067708333333, 0.9064814814815)
        elif round == 94:
            sniper4.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2','0-2-3','0-2-4'])
            sniper5 = Monkey('sniper', 0.4005208333333, 0.8509259259259)
        elif round == 96:
            sniper5.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2','0-2-3','0-2-4'])
            sniper6 = Monkey('sniper', 0.4390625, 0.875)
            sniper7 = Monkey('sniper', 0.4359375, 0.812037037037)
        elif round == 98:
            sniper6.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2','0-2-3','0-2-4'])
            sniper7.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2','0-2-3','0-2-4'])