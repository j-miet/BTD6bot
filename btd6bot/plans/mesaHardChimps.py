"""
[Hero] Etienne
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0
tack 5-2-0
glue 2-5-0

sniper 1-0-0
ace 2-0-3

wizard 5-0-2
ninja 0-4-0
alch 3-2-0

spike 3-2-0
village 4-0-2
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
            dart1 = Monkey('dart', 0.1286458333333, 0.675)
            dart1.target('strong')
            dart2 = Monkey('dart', 0.5255208333333, 0.3657407407407)
            dart3 = Monkey('dart', 0.5078125, 0.4101851851852)
        elif round == 8:
            sniper1 = Monkey('sniper', 0.6307291666667, 0.55)
            sniper1.target('strong')
        elif round == 10:
            sniper2 = Monkey('sniper', 0.5973958333333, 0.5574074074074)
            sniper2.target('strong')
        elif round == 13:
            hero = Hero(0.5619791666667, 0.3703703703704)
        elif round == 15:
            wizard = Monkey('wizard', 0.5140625, 0.4666666666667)
            wait(4)
            sniper1.target('first')
            wait(2)
            sniper1.target('strong')
        elif round == 16:
            wizard.upgrade(['1-0-0'])
        elif round == 18:
            wizard.upgrade(['1-0-1'])
        elif round == 19:
            wizard.upgrade(['2-0-1'])
        elif round == 21:
            sniper3 = Monkey('sniper', 0.4338541666667, 0.05)
            sniper1.upgrade(['1-0-0'])
        elif round == 22:
            ability(1)
        elif round == 23:
            sniper2.upgrade(['1-0-0'])
        elif round == 27:
            ability(1,8)
        elif round == 29:
            village = Monkey('village', 0.5505208333333, 0.2944444444444)
        elif round == 30:
            village.upgrade(['0-0-1','0-0-2'])
            wizard.upgrade(['2-0-2'])
        elif round == 31:
            ability(1)
        elif round == 33:
            wizard.upgrade(['3-0-2'])
        elif round == 35:
            ace = Monkey('ace', 0.6697916666667, 0.2555555555556)
            ace.target('infinite')
            ace.upgrade(['0-0-1'])
        elif round == 37:
            ability(1,12)
        elif round == 38:
            ace.upgrade(['0-0-2','0-0-3'])
            ace.center(0.7791666666667, 0.1981481481481)
            ace.upgrade(['1-0-3'])
        elif round == 39:
            alch1 = Monkey('alch', 0.6208333333333, 0.1398148148148)
            alch1.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif round == 40:
            ability(1)
        elif round == 41:
            ace.upgrade(['2-0-3'])
        elif round == 42:
            village.upgrade(['1-0-0','2-0-0'])
        elif round == 43:
            alch2 = Monkey('alch', 0.478125, 0.4824074074074)
        elif round == 44:
            alch2.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif round == 49:
            wizard.upgrade(['4-0-2'])
            alch2.upgrade(['3-1-0','3-2-0'])
            tack = Monkey('tack', 0.596875, 0.3157407407407)
            tack.upgrade(['1-0-0','2-0-0','3-0-0','3-1-0','3-2-0'])
        elif round == 51:
            tack.upgrade(['4-2-0'])
        elif round == 52:
            village.upgrade(['3-0-2'])
            alch3 = Monkey('alch', 0.5927083333333, 0.2601851851852)
        elif round == 53:
            alch3.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif round == 54:
            alch3.upgrade(['3-1-0','3-2-0'])
        elif round == 63:
            ability(1)
            ability(2,7)
        elif round == 64:
            hero.force_target()
        elif round == 75:
            ability(2,3.5)
            ability(1,10.5)
        elif round == 77:
            ability(1,13)
        elif round == 78:
            ability(2)
            ability(2,26)
        elif round == 79:
            tack.upgrade(['5-2-0'])
            tack.target('strong')
        elif round == 80:
            village.upgrade(['4-0-2'])
        elif round == 89:
            wizard.upgrade(['5-0-2'])
            glue = Monkey('glue', 0.5651041666667, 0.4601851851852)
        elif round == 91:
            glue.upgrade(['1-0-0','1-1-0','1-2-0','1-3-0','1-4-0'])
        elif round == 95:
            ability(2,10)
            glue.upgrade(['1-5-0','2-5-0'])
        elif round == 96:
            ability(3,4)
            spike = Monkey('spike', 0.6682291666667, 0.1324074074074)
            spike.upgrade(['1-0-0','2-0-0','3-0-0','3-1-0','3-2-0'])
        elif round == 97:
            ability(2,4)
            ninja = Monkey('ninja', 0.6005208333333, 0.3824074074074)
            ninja.upgrade(['0-1-0','0-2-0','0-3-0'])
        elif round == 98:
            ability(3)
            ability(1,6.5)
            ninja.upgrade(['0-4-0'])
        elif round == 99:
            ability(4,2)
        elif round == 100:
            ability(3)
            ability(2)
            ability(1,9)