"""
[Hero] Sauda
[Monkey Knowledge] Yes
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-3-2
boomer 4-2-4

sniper 2-2-0
ace 2-0-3

alch 3-0-0
mermonkey 4-0-2

spike 3-0-4
village 2-2-0
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
            hero = Hero(0.2026041666667, 0.3990740740741)
            dart_right = Monkey('dart', 0.5598958333333, 0.6027777777778)
            sniper_right = Monkey('sniper', 0.5177083333333, 0.5555555555556)
            dart_right.target('strong')
            sniper_right.target('strong')
        elif round == 5:
            dart_right.upgrade(['0-0-1','0-0-2'])
        elif round == 7:
            dart_right.upgrade(['0-1-2','0-2-2'])
        elif round == 9:
            dart_right.upgrade(['0-3-2'])
        elif round == 10:
            ability(1)
            sniper_left = Monkey('sniper', 0.3536458333333, 0.4916666666667)
            sniper_left.target('strong')
        elif round == 14:
            sniper_left.upgrade(['1-0-0'])
            sniper_right.upgrade(['1-0-0'])
        elif round == 16:
            sniper_left.upgrade(['1-1-0'])
            sniper_right.upgrade(['1-1-0'])
        elif round == 25:
            ace_right = Monkey('ace', 0.540625, 0.4092592592593)
        elif round == 31:
            ace_right.upgrade(['0-0-1','0-0-2','0-0-3'])
        elif round == 32:
            ace_right.upgrade(['1-0-3'])
        elif round == 33:
            sniper_right.upgrade(['1-2-0'])
        elif round == 37:
            spike_left1 = Monkey('spike', 0.2552083333333, 0.5555555555556)
            spike_left1.upgrade(['0-0-1','0-0-2'])
            spike_left1.target('smart')
        elif round == 38:
            spike_left1.upgrade(['0-0-3'])
        elif round == 39:
            spike_left1.upgrade(['0-0-4','1-0-4'])
        elif round == 40:
            ability(1,4)
            ace_right.upgrade(['2-0-3'])
        elif round == 42:
            spike_right1 = Monkey('spike', 0.6161458333333, 0.4296296296296)
            spike_right1.upgrade(['0-0-1','0-0-2'])
            spike_right1.target('smart')
            spike_right1.upgrade(['1-0-2'])
        elif round == 43:
            ability(1,4)
        elif round == 46:
            spike_right1.upgrade(['1-0-3','1-0-4'])
        elif round == 48:
            boomer_right1 = Monkey('boomer', 0.6161458333333, 0.5240740740741)
            boomer_right1.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-0-1','4-0-2'])
        elif round == 49:
            boomer_left1 = Monkey('boomer', 0.2453125, 0.4851851851852)
            boomer_left1.upgrade(['1-0-0','2-0-0','3-0-0','3-0-1','3-0-2'])
        elif round == 50:
            boomer_left1.upgrade(['4-0-2'])
        elif round == 51:
            village_right = Monkey('village', 0.5651041666667, 0.5018518518519)
            village_right.upgrade(['0-1-0','0-2-0'])
        elif round == 54:
            village_right.upgrade(['1-2-0','2-2-0'])
        elif round == 58:
            village_left = Monkey('village', 0.2958333333333, 0.4824074074074)
            village_left.upgrade(['0-1-0','0-2-0','1-2-0','2-2-0'])
        elif round == 60:
            boomer_right2 = Monkey('boomer', 0.615625, 0.5898148148148)
            boomer_right2.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
            boomer_right2.target('strong')
        elif round == 62:
            boomer_left2 = Monkey('boomer', 0.246875, 0.4157407407407)
            boomer_left2.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
            boomer_left2.target('strong')
        elif round == 71:
            mermonkey_right = Monkey('mermonkey', 0.6625, 0.5324074074074)
            mermonkey_right.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-0-1','4-0-2'])
        elif round == 72:
            mermonkey_left = Monkey('mermonkey', 0.2036458333333, 0.4638888888889)
            mermonkey_left.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-0-1','4-0-2'])
        elif round == 75:
            spike_left2 = Monkey('spike', 0.2026041666667, 0.5564814814815)
            spike_left2.upgrade(['0-0-1','0-0-2'])
            spike_left2.target('smart')
        elif round == 77:
            spike_left2.upgrade(['1-0-2','2-0-2','3-0-2','4-0-2'])
        elif round == 78:
            spike_right2 = Monkey('spike', 0.6645833333333, 0.4277777777778)
            spike_right2.upgrade(['0-0-1','0-0-2'])
            spike_right2.target('smart')
        elif round == 79:
            spike_right2.upgrade(['1-0-2','2-0-2','3-0-2'])
            alch_right = Monkey('alch', 0.7583333333333, 0.3462962962963)
            alch_right.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif round == 80:
            ability(2,4)
            ability(1,6)