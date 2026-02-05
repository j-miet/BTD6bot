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

def play(rounds):
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start, rounds[2])
        if current_round == BEGIN:
            hero = Hero(0.45625, 0.5407407407407)
            dart1 = Monkey('dart', 0.3479166666667, 0.3851851851852)
        elif current_round == 5:
            ninja1 = Monkey('ninja', 0.5020833333333, 0.5574074074074)
        elif current_round == 6:
            dart1.upgrade(['0-0-1','0-0-2'])
        elif current_round == 8:
            sniper1 = Monkey('sniper', 0.775, 0.6064814814815)
            sniper1.target('strong')
        elif current_round == 10:
            sniper1.upgrade(['1-0-0'])
        elif current_round == 11:
            ninja2 = Monkey('ninja', 0.3567708333333, 0.4398148148148)
        elif current_round == 12:
            sniper1.upgrade(['1-1-0'])
        elif current_round == 14:
            boomer1 = Monkey('boomer', 0.3953125, 0.4509259259259)
            boomer1.upgrade(['0-0-1'])
        elif current_round == 15:
            ability(1)
            boomer1.upgrade(['1-0-1'])
        elif current_round == 16:
            boomer1.upgrade(['2-0-1'])
        elif current_round == 17:
            boomer1.upgrade(['2-0-2'])
        elif current_round == 19:
            boomer1.upgrade(['3-0-2'])
        elif current_round == 21:
            boomer2 = Monkey('boomer', 0.4671875, 0.6083333333333)
            boomer2.upgrade(['0-0-1'])
        elif current_round == 23:
            boomer2.upgrade(['0-0-2','1-0-2'])
        elif current_round == 24:
            boomer2.upgrade(['2-0-2'])
        elif current_round == 26:
            boomer2.upgrade(['3-0-2'])
        elif current_round == 27:
            ability(1,4)
        elif current_round == 31:
            boomer1.upgrade(['4-0-2'])
        elif current_round == 34:
            boomer2.upgrade(['4-0-2'])
        elif current_round == 35:
            engi1 = Monkey('engineer', 0.4015625, 0.3898148148148)
        elif current_round == 36:
            engi1.upgrade(['0-1-0','1-1-0','1-2-0','2-2-0'])
        elif current_round == 37:
            engi2 = Monkey('engineer', 0.428125, 0.6425925925926)
            engi2.upgrade(['0-1-0','1-1-0','1-2-0','2-2-0'])
        elif current_round == 38:
            engi2.upgrade(['3-2-0'])
        elif current_round == 39:
            engi1.upgrade(['3-2-0'])
            sniper1.upgrade(['1-2-0'])
            forward(1)
        elif current_round == 40:
            ability(1)
            sniper1.upgrade(['2-2-0'])
        elif current_round == 42:
            forward(1)
            ninja1.upgrade(['0-0-1','1-0-1','1-0-2','2-0-2'])
            ninja2.upgrade(['0-0-1','1-0-1','1-0-2','2-0-2'])
        elif current_round == 43:
            ability(1)
        elif current_round == 44:
            farm1 = Monkey('farm', 0.1869791666667, 0.6175925925926)
            move_cursor(0.1869791666667, 0.6175925925926)
            farm1.upgrade(['1-0-0','2-0-0'])
        elif current_round == 45:
            farm1.upgrade(['2-0-1','2-0-2'])
        elif current_round == 46:
            farm1.upgrade(['2-0-3'])
        elif current_round == 48:
            engi1.upgrade(['4-2-0'])
        elif current_round == 49:
            engi2.upgrade(['4-2-0'])
            ninja1.upgrade(['3-0-2'])
        elif current_round == 50:
            ability(1)
            sniper1.upgrade(['3-2-0'])
        elif current_round == 52:
            ability(1)
            sniper1.upgrade(['4-2-0'])
        elif current_round == 53:
            ability(2)
            ninja2.upgrade(['2-0-3'])
        elif current_round == 55:
            ability(2)
            ninja1.upgrade(['4-0-2'])
        elif current_round == 56:
            farm2 = Monkey('farm', 0.3, 0.8)
            move_cursor(0.3, 0.8)
            farm2.upgrade(['1-0-0','2-0-0'])
        elif current_round == 57:
            farm2.upgrade(['2-0-1','2-0-2','2-0-3'])
        elif current_round == 58:
            sniper2 = Monkey('sniper', 0.7036458333333, 0.6935185185185)
        elif current_round == 59:
            sniper2.upgrade(['1-0-0','1-0-1','1-0-2','2-2-0'])
        elif current_round == 60:
            sniper2.upgrade(['3-0-2'])
        elif current_round == 61:
            sniper2.upgrade(['4-0-2'])

        # elif current_round == 62:
        #     sniper3 = Monkey('sniper', 0.8208333333333, 0.5416666666667)
        #     sniper3.upgrade(['0-1-0','0-1-1','0-2-1','0-2-2'])
        # elif current_round == 63:
        #     sniper3.upgrade(['0-2-3'])
        # elif current_round == 65:
        #     ninja2.upgrade(['2-0-4'])
        # elif current_round == 67:
        #     sniper3.upgrade(['0-2-4'])

        elif current_round == 62:
            mermonkey1 = Monkey('mermonkey', 0.5322916666667, 0.5185185185185)
            mermonkey1.upgrade(['1-0-0','1-0-1','2-0-1','2-0-2'])
        elif current_round == 63:
            mermonkey1.upgrade(['3-0-2'])
            mermonkey2 = Monkey('mermonkey', 0.4385416666667, 0.3509259259259)
            mermonkey2.upgrade(['1-0-0','1-0-1','2-0-1','3-0-1','3-0-2'])
        elif current_round == 65:
            mermonkey1.upgrade(['4-0-2'])
        elif current_round == 67:
            mermonkey2.upgrade(['4-0-2'])
        elif current_round == 68:
            mermonkey3 = Monkey('mermonkey', 0.6307291666667, 0.4064814814815)
            mermonkey3.upgrade(['0-0-0','0-0-1','0-0-2'])
        elif current_round == 69:
            mermonkey4 = Monkey('mermonkey', 0.5213541666667, 0.2296296296296)
            mermonkey4.upgrade(['0-0-0','0-0-1','0-0-2'])
        elif current_round == 70:
            ability(2)
            sniper3 = Monkey('sniper', 0.8208333333333, 0.5416666666667)
            sniper3.upgrade(['0-1-0','0-1-1','0-2-1','0-2-2'])
        elif current_round == 71:
            sniper3.upgrade(['0-2-3'])
        elif current_round == 73:
            sniper3.upgrade(['0-2-4'])
        elif current_round == 74:
            mermonkey5 = Monkey('mermonkey', 0.3328125, 0.1731481481481)
            mermonkey5.upgrade(['0-0-0','0-0-1','0-0-2'])
            mermonkey6 = Monkey('mermonkey', 0.2479166666667, 0.275)
            mermonkey6.upgrade(['0-0-0','0-0-1','0-0-2'])
        elif current_round == 76:
            farm1.sell()
            sniper3.upgrade(['0-2-5'])
        elif current_round == 77:
            ability(2)
        elif current_round == 78:
            farm2.sell()
            ninja2.upgrade(['2-0-4'])
        elif current_round == 79:
            mermonkey7 = Monkey('mermonkey', 0.4088541666667, 0.0888888888889)
            mermonkey7.upgrade(['0-0-0','0-0-1','0-0-2'])
            mermonkey8 = Monkey('mermonkey', 0.1578125, 0.3768518518519)
            mermonkey8.upgrade(['0-0-0','0-0-1','0-0-2'])
