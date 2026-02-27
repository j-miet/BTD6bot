"""
[Hero] Etienne
[Monkey Knowledge] Yes
-------------------------------------------------------------
===Monkeys & upgrades required===
boat 5-2-0
sub 2-3-4

ninja 0-0-0
mermonkey 5-0-3

farm 2-0-3
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
            hero = Hero(0.3578125, 0.3888888888889)
            sub1 = Monkey('sub', 0.4921875, 0.5537037037037)
        elif round == 6:
            ninja1 = Monkey('ninja', 0.5171875, 0.3981481481481)
        elif round == 8:
            ninja2 = Monkey('ninja', 0.3578125, 0.6018518518519)
        elif round == 12:
            sub1.upgrade(['0-1-0','0-2-0'])
        elif round == 15:
            sub1.upgrade(['1-2-0','2-2-0'])
            sub1.target('strong')
        elif round == 16:
            sub2 = Monkey('sub', 0.396875, 0.4240740740741)
        elif round == 18:
            sub2.upgrade(['1-0-0','2-0-0'])
        elif round == 20:
            sub2.upgrade(['2-0-1'])
        elif round == 25:
            sub2.upgrade(['2-0-2'])
        elif round == 27:
            sub2.upgrade(['2-0-3'])
        elif round == 33:
            sub2.upgrade(['2-0-4'])
        elif round == 35:
            boat1 = Monkey('boat', 0.4484375, 0.5092592592593)
        elif round == 36:
            boat1.upgrade(['0-1-0','0-2-0','1-2-0','2-2-0'])
        elif round == 38:
            boat1.upgrade(['3-2-0'])
        elif round == 39:
            sub1.upgrade(['2-3-0'])
        elif round == 40:
            ability(1)
        elif round == 41:
            farm1 = Monkey('farm', 0.2348958333333, 0.212037037037)
            move_cursor(0.2348958333333, 0.212037037037)
        elif round == 42:
            farm1.upgrade(['1-0-0','2-0-0','2-0-1','2-0-2'])
        elif round == 44:
            farm1.upgrade(['2-0-3'])
        elif round == 46:
            farm2 = Monkey('farm', 0.6229166666667, 0.7583333333333)
            move_cursor(0.6229166666667, 0.7583333333333)
            farm2.upgrade(['1-0-0','2-0-0','2-0-1','2-0-2'])
        elif round == 47:
            farm2.upgrade(['2-0-3'])
        elif round == 50:
            ability(2)
            boat1.upgrade(['4-2-0'])
        elif round == 51:
            mermonkey1 = Monkey('mermonkey', 0.403125, 0.5092592592593)
        elif round == 52:
            mermonkey1.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0'])
        elif round == 53:
            mermonkey1.upgrade(['4-0-1','4-0-2'])
        elif round == 54:
            mermonkey2 = Monkey('mermonkey', 0.4901041666667, 0.4759259259259)
            mermonkey2.upgrade(['0-0-1','0-0-2'])
            mermonkey3 = Monkey('mermonkey', 0.4364583333333, 0.287962962963)
            mermonkey3.upgrade(['0-0-1','0-0-2'])
            mermonkey4 = Monkey('mermonkey', 0.3979166666667, 0.5851851851852)
            mermonkey4.upgrade(['0-0-1','0-0-2'])
            mermonkey5 = Monkey('mermonkey', 0.4505208333333, 0.5944444444444)
            mermonkey5.upgrade(['0-0-1','0-0-2'])
        elif round == 55:
            mermonkey6 = Monkey('mermonkey', 0.5973958333333, 0.5083333333333)
            mermonkey6.upgrade(['0-0-1','0-0-2'])
        elif round == 63:
            ability(1,2)
            ability(2,4)
            boat1.upgrade(['5-2-0'])
        elif round == 75:
            mermonkey1.upgrade(['5-0-2'])
        elif round == 77:
            mermonkey2.upgrade(['0-0-3','0-0-4'])
        elif round == 79:
            mermonkey4.upgrade(['0-0-3','0-0-4'])