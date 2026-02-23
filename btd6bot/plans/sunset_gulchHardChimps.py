"""
[Hero] Churchill
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-2-5
ice 0-1-4
glue 0-2-4
desperado 2-5-0

sniper 1-0-0

alch 3-2-1
druid 3-0-2

spike 4-4-2
village 2-0-2
engineer 0-4-0
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
            desp1 = Monkey('desperado', 0.6854166666667, 0.4407407407407)
            dart1 = Monkey('dart', 0.1333333333333, 0.6944444444444)
        elif round == 7:
            dart2 = Monkey('dart', 0.740625, 0.4388888888889)
        elif round == 9:
            sniper1 = Monkey('sniper', 0.6614583333333, 0.9731481481481)
            sniper1.target('strong')
        elif round == 11:
            druid1 = Monkey('druid', 0.66875, 0.4953703703704)
        elif round == 13:
            sniper1.upgrade(['1-0-0'])
        elif round == 14:
            druid1.upgrade(['1-0-0'])
        elif round == 18:
            druid1.upgrade(['2-0-0'])
        elif round == 21:
            sniper1.target('first')
        elif round == 22:
            sniper1.target('strong')
        elif round == 23:
            desp1.upgrade(['0-1-0'])
        elif round == 26:
            hero = Hero(0.6822916666667, 0.2824074074074)
        elif round == 29:
            spike1 = Monkey('spike', 0.8161458333333, 0.2842592592593)
        elif round == 30:
            spike1.upgrade(['0-0-1','0-0-2'])
            spike1.target('set')
            spike1.special(1, 0.7203125, 0.3583333333333)
        elif round == 33:
            village1 = Monkey('village', 0.7359375, 0.275)
        elif round == 35:
            village1.upgrade(['0-0-1','0-0-2'])
            spike1.upgrade(['1-0-2','2-0-2'])
        elif round == 38:
            spike1.upgrade(['3-0-2'])
            alch1 = Monkey('alch', 0.8036458333333, 0.2268518518519)
            alch1.upgrade(['1-0-0','2-0-0'])
        elif round == 39:
            alch1.upgrade(['2-0-1'])
            change_autostart()
            wait(12)
            alch1.upgrade(['3-0-1'])
            change_autostart()
            end_round(2)
        elif round == 40:
            ability(1,0.5)
        elif round == 41:
            alch2 = Monkey('alch', 0.7161458333333, 0.1925925925926)
            alch2.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif round == 42:
            alch2.upgrade(['3-1-0','3-2-0'])
        elif round == 43:
            ability(1,2.5)
        elif round == 44:
            village1.upgrade(['1-0-2','2-0-2'])
        elif round == 45:
            desp1.upgrade(['0-2-0','0-3-0'])
        elif round == 49:
            spike1.upgrade(['4-0-2'])
        elif round == 50:
            ability(2, xy=(0.6770833333333, 0.2953703703704))
            ability(1)
        elif round == 55:
            desp1.upgrade(['0-4-0'])
            glue1 = Monkey('glue', 0.6359375, 0.2898148148148)
            glue1.target('strong')
        elif round == 56:
            glue1.upgrade(['0-0-1','0-0-2'])
        elif round == 57:
            glue1.upgrade(['0-0-3','0-1-3'])
        elif round == 60:
            ability(2, 4, xy=(0.6770833333333, 0.2953703703704))
            ability(1)
        elif round == 63:
            ability(2, 1, xy=(0.6770833333333, 0.2953703703704))
            ability(1)
        elif round == 64:
            ability(2, xy=(0.6770833333333, 0.2953703703704))
            ability(1)
        elif round == 71:
            ability(2, 1, xy=(0.6770833333333, 0.2953703703704))
            ability(1)
        elif round == 73:
            ability(2, xy=(0.6770833333333, 0.2953703703704))
            ability(1)
        elif round == 75:
            ability(4,1)
            ability(2, 3, xy=(0.6770833333333, 0.2953703703704))
            ability(1)
        elif round == 76:
            ability(3)
            ability(2, xy=(0.6770833333333, 0.2953703703704))
            ability(1)
        elif round == 78:
            ability(2, 3, xy=(0.6770833333333, 0.2953703703704))
            ability(1)
        elif round == 79:
            ability(2, 7, xy=(0.6770833333333, 0.2953703703704))
            ability(1)
            desp1.upgrade(['0-5-0','1-5-0','2-5-0'])
            desp1.target('strong')
        elif round == 80:
            village1.upgrade(['3-0-2'])
            glue1.upgrade(['0-2-3'])
            ability(3,9)
            ability(4)
        elif round == 81:
            village1.upgrade(['4-0-2'])
        elif round == 82:
            ice1 = Monkey('ice', 0.775, 0.4388888888889)
            ice1.upgrade(['0-1-0','0-1-1','0-1-2','0-1-3','0-1-4'])
            dart2.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2','0-2-3','0-2-4'])
        elif round == 87:
            ability(2, 8, xy=(0.6770833333333, 0.2953703703704))
            ability(1)
        elif round == 89:
            dart2.upgrade(['0-2-5'])
        elif round == 91:
            glue1.upgrade(['0-2-4'])
        elif round == 92:
            engi1 = Monkey('engineer', 0.1953125, 0.2796296296296)
            ability(2, 10, xy=(0.6770833333333, 0.2953703703704))
            ability(1)
        elif round == 93:
            engi1.upgrade(['0-1-0','0-2-0','0-3-0'])
            engi1.special(1, 0.0484375, 0.2685185185185)
        elif round == 94:
            ability(2, 7, xy=(0.6770833333333, 0.2953703703704))
            ability(1)
        elif round == 95:
            engi1.upgrade(['0-4-0'])
            druid1.upgrade(['3-0-0','3-0-1','3-0-2'])
        elif round == 96:
            ability(2, 1, xy=(0.6770833333333, 0.2953703703704))
            ability(1)
            druid1.upgrade(['4-0-2'])
            ability(5, 12, xy=(0.6770833333333, 0.2953703703704))
            ability(2, xy=(0.6770833333333, 0.2953703703704))
            ability(1)
        elif round == 97:
            spike2 = Monkey('spike', 0.6458333333333, 0.2305555555556)
            spike2.upgrade(['1-0-0','2-0-0','2-1-0','2-2-0','2-3-0'])
        elif round == 98:
            ability(5, 3, xy=(0.6770833333333, 0.2953703703704))
            ability(2, xy=(0.6770833333333, 0.2953703703704))
            ability(1)
            spike2.upgrade(['2-4-0'])
            forward(1)
            alch3 = Monkey('alch', 0.5552083333333, 0.1638888888889)
            alch3.upgrade(['1-0-0','2-0-0','3-0-0','3-1-0','3-2-0'])
            forward(1)
        elif round == 99:
            ability(1,2)
        elif round == 100:
            ability(5, 3, xy=(0.6854166666667, 0.4407407407407))
            ability(2, 3, xy=(0.6854166666667, 0.4407407407407))
            ability(3, 5)
            ability(4)
            ability(1)
            ability(6, 6)