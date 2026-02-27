"""
[Hero] Etienne
[Monkey Knowledge] Yes
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-2
boomer 4-0-2

sniper 4-2-5

ninja 4-0-4
mermonkey 4-0-2

farm 2-0-3
engi 4-2-0
_______________________________________
Created with all monkey knowledge unlocked.
"""

from._plan_imports import *

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:
            hero = Hero(0.45625, 0.5607407407407)
            dart1 = Monkey('dart', 0.3479166666667, 0.3951851851852)
        elif round == 5:
            ninja1 = Monkey('ninja', 0.5020833333333, 0.5574074074074)
        elif round == 6:
            dart1.upgrade(['0-0-1','0-0-2'])
        elif round == 8:
            sniper1 = Monkey('sniper', 0.775, 0.6064814814815)
            sniper1.target('strong')
        elif round == 10:
            sniper1.upgrade(['1-0-0'])
        elif round == 11:
            ninja2 = Monkey('ninja', 0.3567708333333, 0.4598148148148)
        elif round == 12:
            sniper1.upgrade(['1-1-0'])
        elif round == 14:
            boomer1 = Monkey('boomer', 0.3953125, 0.4109259259259)
            boomer1.upgrade(['0-0-1'])
        elif round == 15:
            ability(1)
            boomer1.upgrade(['1-0-1'])
        elif round == 16:
            boomer1.upgrade(['2-0-1'])
        elif round == 17:
            boomer1.upgrade(['2-0-2'])
        elif round == 19:
            boomer1.upgrade(['3-0-2'])
        elif round == 21:
            boomer2 = Monkey('boomer', 0.4671875, 0.6283333333333)
            boomer2.upgrade(['0-0-1'])
        elif round == 23:
            boomer2.upgrade(['0-0-2','1-0-2'])
        elif round == 24:
            boomer2.upgrade(['2-0-2'])
        elif round == 26:
            boomer2.upgrade(['3-0-2'])
        elif round == 27:
            ability(1,4)
        elif round == 31:
            boomer1.upgrade(['4-0-2'])
        elif round == 34:
            boomer2.upgrade(['4-0-2'])
        elif round == 35:
            engi1 = Monkey('engineer', 0.3932291666667, 0.3481481481481)
        elif round == 36:
            engi1.upgrade(['0-1-0','1-1-0','1-2-0','2-2-0'])
        elif round == 37:
            engi2 = Monkey('engineer', 0.4255208333333, 0.6296296296296)
            engi2.upgrade(['0-1-0','1-1-0','1-2-0','2-2-0'])
        elif round == 38:
            engi2.upgrade(['3-2-0'])
        elif round == 39:
            engi1.upgrade(['3-2-0'])
            sniper1.upgrade(['1-2-0'])
            forward(1)
        elif round == 40:
            ability(1)
            sniper1.upgrade(['2-2-0'])
        elif round == 42:
            forward(1)
            ninja1.upgrade(['0-0-1','1-0-1','1-0-2','2-0-2'])
            ninja2.upgrade(['0-0-1','1-0-1','1-0-2','2-0-2'])
        elif round == 43:
            ability(1)
        elif round == 44:
            farm1 = Monkey('farm', 0.8104166666667, 0.8037037037037)
            move_cursor(0.8104166666667, 0.8037037037037)
            farm1.upgrade(['1-0-0','2-0-0'])
        elif round == 45:
            farm1.upgrade(['2-0-1','2-0-2'])
        elif round == 46:
            farm1.upgrade(['2-0-3'])
        elif round == 48:
            engi1.upgrade(['4-2-0'])
        elif round == 49:
            engi2.upgrade(['4-2-0'])
            ninja1.upgrade(['3-0-2'])
        elif round == 50:
            ability(1)
            sniper1.upgrade(['3-2-0'])
        elif round == 52:
            ability(1)
            sniper1.upgrade(['4-2-0'])
        elif round == 53:
            ability(2)
            ninja2.upgrade(['2-0-3'])
        elif round == 55:
            ability(2)
            ninja1.upgrade(['4-0-2'])
        elif round == 56:
            farm2 = Monkey('farm', 0.7208333333333, 0.9185185185185)
            move_cursor(0.7208333333333, 0.9185185185185)
            farm2.upgrade(['1-0-0','2-0-0'])
        elif round == 57:
            farm2.upgrade(['2-0-1','2-0-2','2-0-3'])
        elif round == 58:
            sniper2 = Monkey('sniper', 0.7036458333333, 0.6935185185185)
        elif round == 59:
            sniper2.upgrade(['1-0-0','1-0-1','1-0-2','2-2-0'])
        elif round == 60:
            sniper2.upgrade(['3-0-2'])
        elif round == 61:
            sniper2.upgrade(['4-0-2'])

        # elif round == 62:
        #     sniper3 = Monkey('sniper', 0.8208333333333, 0.5416666666667)
        #     sniper3.upgrade(['0-1-0','0-1-1','0-2-1','0-2-2'])
        # elif round == 63:
        #     sniper3.upgrade(['0-2-3'])
        # elif round == 65:
        #     ninja2.upgrade(['2-0-4'])
        # elif round == 67:
        #     sniper3.upgrade(['0-2-4'])

        elif round == 62:
            mermonkey1 = Monkey('mermonkey', 0.5322916666667, 0.5185185185185)
            mermonkey1.upgrade(['1-0-0','1-0-1','2-0-1','2-0-2'])
        elif round == 63:
            mermonkey1.upgrade(['3-0-2'])
            mermonkey2 = Monkey('mermonkey', 0.4369791666667, 0.3444444444444)
            mermonkey2.upgrade(['1-0-0','1-0-1','2-0-1','3-0-1','3-0-2'])
        elif round == 65:
            mermonkey1.upgrade(['4-0-2'])
        elif round == 67:
            mermonkey2.upgrade(['4-0-2'])
        elif round == 68:
            mermonkey3 = Monkey('mermonkey', 0.6307291666667, 0.4064814814815)
            mermonkey3.upgrade(['0-0-0','0-0-1','0-0-2'])
        elif round == 69:
            mermonkey4 = Monkey('mermonkey', 0.5213541666667, 0.2296296296296)
            mermonkey4.upgrade(['0-0-0','0-0-1','0-0-2'])
        elif round == 70:
            ability(2)
            sniper3 = Monkey('sniper', 0.8208333333333, 0.5416666666667)
            sniper3.upgrade(['0-1-0','0-1-1','0-2-1','0-2-2'])
        elif round == 71:
            sniper3.upgrade(['0-2-3'])
        elif round == 73:
            sniper3.upgrade(['0-2-4'])
        elif round == 74:
            mermonkey5 = Monkey('mermonkey', 0.3328125, 0.1731481481481)
            mermonkey5.upgrade(['0-0-0','0-0-1','0-0-2'])
            mermonkey6 = Monkey('mermonkey', 0.2479166666667, 0.275)
            mermonkey6.upgrade(['0-0-0','0-0-1','0-0-2'])
        elif round == 76:
            farm1.sell()
            sniper3.upgrade(['0-2-5'])
        elif round == 77:
            ability(2)
        elif round == 78:
            farm2.sell()
            ninja2.upgrade(['2-0-4'])
        elif round == 79:
            mermonkey7 = Monkey('mermonkey', 0.4088541666667, 0.0888888888889)
            mermonkey7.upgrade(['0-0-0','0-0-1','0-0-2'])
            mermonkey8 = Monkey('mermonkey', 0.1578125, 0.3768518518519)
            mermonkey8.upgrade(['0-0-0','0-0-1','0-0-2'])
