"""
[Hero] Benjamin
[Monkey Knowledge] Yes
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-3

druid 1-4-0
mermonkey 5-0-2

farm 2-0-3
spike 4-0-4
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
            dart1 = Monkey('dart', 0.3057291666667, 0.3916666666667)
            dart2 = Monkey('dart', 0.5588541666667, 0.6037037037037)
            dart3 = Monkey('dart', 0.2583333333333, 0.7472222222222)
            dart4 = Monkey('dart', 0.6109375, 0.2518518518519)
        elif round == 9:
            hero = Hero(0.0671875, 0.8398148148148)
        elif round == 11:
            druid1 = Monkey('druid', 0.6614583333333, 0.6018518518519)
            druid1.upgrade(['0-1-0'])
        elif round == 12:
            druid1.upgrade(['0-2-0'])
        elif round == 14:
            druid2 = Monkey('druid', 0.2145833333333, 0.7453703703704)
        elif round == 16:
            druid1.upgrade(['0-3-0'])
        elif round == 17:
            druid2.upgrade(['0-1-0','0-2-0','0-3-0'])
        elif round == 20:
            druid2.upgrade(['0-3-0'])
        elif round == 22:
            dart1.upgrade(['0-0-1','0-0-2'])
            dart2.upgrade(['0-0-1','0-0-2'])
            druid1.upgrade(['1-3-0'])
        elif round == 23:
            druid2.upgrade(['1-3-0'])
        elif round == 25:
            dart2.upgrade(['0-0-3'])
        elif round == 27:
            mermonkey1 = Monkey('mermonkey', 0.2125, 0.5953703703704)
            mermonkey1.upgrade(['1-0-0','2-0-0'])
        elif round == 29:
            mermonkey1.upgrade(['3-0-0','3-0-1'])
        elif round == 31:
            spike1 = Monkey('spike', 0.6135416666667, 0.4685185185185)
        elif round == 32:
            spike1.upgrade(['0-0-1','0-0-2'])
            spike1.target('smart')
        elif round == 37:
            mermonkey1.upgrade(['4-0-1','4-0-2'])
        elif round == 38:
            spike2 = Monkey('spike', 0.2588541666667, 0.5916666666667)
            spike2.upgrade(['0-0-1','0-0-2'])
            spike2.target('smart')
        elif round == 39:
            spike2.upgrade(['1-0-2'])
        elif round == 41:
            spike1.upgrade(['1-0-2','2-0-2','3-0-2'])
        elif round == 43:
            spike2.upgrade(['2-0-2','2-0-3'])
        elif round == 45:
            spike2.upgrade(['2-0-4'])
            mermonkey2 = Monkey('mermonkey', 0.6640625, 0.4018518518519)
        elif round == 46:
            mermonkey2.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif round == 47:
            mermonkey2.upgrade(['3-0-1','3-0-2'])
        elif round == 49:
            mermonkey2.upgrade(['4-0-2'])
        elif round == 50:
            druid2.upgrade(['1-4-0'])
            farm1 = Monkey('farm', 0.2145833333333, 0.8435185185185)
            move_cursor(0.2145833333333, 0.8435185185185)
        elif round == 51:
            farm1.upgrade(['1-0-0','2-0-0'])
        elif round == 53:
            farm1.upgrade(['2-0-1','2-0-2','2-0-3'])
        elif round == 55:
            druid1.upgrade(['1-4-0'])
            spike3 = Monkey('spike', 0.6135416666667, 0.3944444444444)
            spike3.upgrade(['0-0-1','0-0-2'])
            spike3.target('smart')
        elif round == 57:
            spike3.upgrade(['0-0-3'])
        elif round == 58:
            spike3.upgrade(['0-0-4','1-0-4','2-0-4'])
        elif round == 59:
            spike4 = Monkey('spike', 0.2588541666667, 0.5175925925926)
            spike4.upgrade(['1-0-0','2-0-0'])
        elif round == 60:
            spike4.upgrade(['2-0-1','2-0-2'])
            spike4.target('smart')
        elif round == 61:
            spike4.upgrade(['3-0-2'])
        elif round == 64:
            spike4.upgrade(['4-0-2'])
        elif round == 66:
            spike1.upgrade(['4-0-2'])
        elif round == 75:
            mermonkey1.upgrade(['5-0-2'])
            mermonkey3 = Monkey('mermonkey', 0.6119791666667, 0.9185185185185)
            mermonkey3.upgrade(['0-0-1','0-0-2'])
            mermonkey4 = Monkey('mermonkey', 0.6140625, 0.7657407407407)
            mermonkey4.upgrade(['0-0-1','0-0-2'])
            mermonkey5 = Monkey('mermonkey', 0.7020833333333, 0.7611111111111)
            mermonkey5.upgrade(['0-0-1','0-0-2'])
        elif round == 76:
            mermonkey6 = Monkey('mermonkey', 0.7640625, 0.5944444444444)
            mermonkey6.upgrade(['0-0-1','0-0-2'])
            mermonkey7 = Monkey('mermonkey', 0.7635416666667, 0.4185185185185)
            mermonkey7.upgrade(['0-0-1','0-0-2'])
            mermonkey8 = Monkey('mermonkey', 0.6671875, 0.2453703703704)
            mermonkey8.upgrade(['0-0-1','0-0-2'])