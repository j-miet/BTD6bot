"""
[Hero] Obyn
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0

sniper 2-2-5

super 3-2-2
ninja 2-2-0
alch 5-2-0

village 2-0-2
_______________________________________
Similar to maps like Erosion, sometimes bot can detect next round(s) too early because there are too many projectiles/bloons moving around round label, causing false positives. 
Good thing is, this doesn't affect gameplay for this particular plan as ability timings are not needed late game.
This only affects saved round times: some data could immediately skip over, causing other data falsely display extremely long durations.
"""

from._plan_imports import *

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:
            dart1 = Monkey('dart', 0.70625, 0.2490740740741)
            dart2 = Monkey('dart', 0.1875, 0.1935185185185)
        elif round == 7:
            sniper1 = Monkey('sniper', 0.2411458333333, 0.6657407407407)
            sniper1.target('strong')
        elif round == 9:
            sniper2 = Monkey('sniper', 0.4380208333333, 0.7342592592593)
        elif round == 10:
            sniper2.target('strong')
        elif round == 12:
            hero = Hero(0.2973958333333, 0.512037037037)
        elif round == 14:
            druid1 = Monkey('druid', 0.3161458333333, 0.637962962963)
        elif round == 15:
            druid1.upgrade(['0-1-0'])
        elif round == 16:
            druid1.upgrade(['0-2-0'])
        elif round == 19:
            sniper2.target('first')
            ability(1,2.25)
        elif round == 20:
            sniper2.target('strong')
        elif round == 21:
            druid1.upgrade(['0-3-0'])
        elif round == 23:
            sniper1.upgrade(['0-0-1'])
        elif round == 24:
            sniper1.upgrade(['0-1-1'])
        elif round == 25:
            sniper1.upgrade(['0-1-2'])
        elif round == 27:
            sniper1.upgrade(['0-2-2'])
            sniper1.target('first')
            druid1.upgrade(['1-3-0'])
        elif round == 30:
            druid1.upgrade(['2-3-0'])
        elif round == 35:
            sniper1.upgrade(['0-2-3'])
        elif round == 39:
            sniper1.upgrade(['0-2-4'])
        elif round == 47:
            village1 = Monkey('village', 0.1963541666667, 0.6398148148148)
            village1.upgrade(['0-0-1','0-0-2','1-0-2','2-0-2'])
        elif round == 48:
            alch1 = Monkey('alch', 0.2546875, 0.5990740740741)
            alch1.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-1-0','4-2-0'])
        elif round == 54:
            sniper1.upgrade(['0-2-5'])
        elif round == 55:
            super1 = Monkey('super', 0.24375, 0.5268518518519)
        elif round == 57:
            super1.upgrade(['1-0-0','2-0-0'])
        elif round == 68:
            super1.upgrade(['3-0-0'])
        elif round == 71:
            super1.upgrade(['3-0-1','3-0-2'])
        elif round == 86:
            alch1.upgrade(['5-2-0'])
            ninja1 = Monkey('ninja', 0.2880208333333, 0.712037037037)
        elif round == 87:
            ninja1.upgrade(['0-1-0','0-2-0','1-2-0','2-2-0'])
            ninja1.special(1)
            ninja1.target('strong')
        elif round == 88:
            super2 = Monkey('super', 0.2161458333333, 0.4416666666667)
        elif round == 89:
            super2.upgrade(['1-0-0','2-0-0'])
        elif round == 94:
            super2.upgrade(['3-0-0'])
        elif round == 95:
            super2.upgrade(['3-1-0','3-2-0'])
        elif round == 97:
            sniper3 = Monkey('sniper', 0.1453125, 0.6601851851852)
            sniper3.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','1-0-4','2-0-4'])
        elif round == 98:
            sniper4 = Monkey('sniper', 0.1473958333333, 0.5861111111111)
            sniper4.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','1-0-4','2-0-4'])