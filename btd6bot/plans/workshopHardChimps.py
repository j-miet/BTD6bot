"""
[Hero] Gwen
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0
boomer 2-0-4
tack 2-0-5
ice 4-1-0
glue 0-2-5

mortar 1-0-4

alch 4-2-1
druid 2-3-0

spike 4-2-5
village 3-0-2
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
            dart1 = Monkey('dart', 0.1161458333333, 0.5759259259259)
            dart1.target('last')
            dart2 = Monkey('dart', 0.3140625, 0.4648148148148)
            dart2.target('strong')
            dart3 = Monkey('dart', 0.3484375, 0.4648148148148)
        elif round == 7:
            dart4 = Monkey('dart', 0.0817708333333, 0.5759259259259)
            dart4.target('strong')
        elif round == 10:
            druid1 = Monkey('druid', 0.4911458333333, 0.5796296296296)
            dart2.target('first')
            dart4.target('first')
        elif round == 14:
            spike = Monkey('spike', 0.83125, 0.6611111111111)
        elif round == 17:
            hero = Hero(0.5307291666667, 0.4611111111111)
        elif round == 19:
            spike.upgrade(['0-0-1','0-0-2'])
            spike.target('close')
        elif round == 20:
            druid1.upgrade(['1-0-0'])
            druid1.target('strong')
        elif round == 22:
            druid1.upgrade(['1-1-0'])
        elif round == 25:
            spike.upgrade(['1-0-2'])
        elif round == 27:
            druid1.upgrade(['2-1-0'])
        elif round == 31:
            druid1.upgrade(['2-2-0','2-3-0'])
        elif round == 34:
            spike.upgrade(['1-0-3'])
        elif round == 37:
            spike.upgrade(['1-0-4'])
        elif round == 39:
            village1 = Monkey('village', 0.7317708333333, 0.637037037037)
            village1.upgrade(['0-0-1','0-0-2'])
        elif round == 40:
            alch1 = Monkey('alch', 0.7619791666667, 0.5796296296296)
            alch1.upgrade(['1-0-0','2-0-0'])
        elif round == 41:
            alch1.upgrade(['3-0-0','3-0-1'])
        elif round == 43:
            village1.upgrade(['1-0-2','2-0-2'])
        elif round == 45:
            alch1.upgrade(['4-0-1'])
        elif round == 46:
            spike2 = Monkey('spike', 0.8317708333333, 0.587037037037)
        elif round == 47:
            spike2.upgrade(['1-0-0','2-0-0'])
        elif round == 48:
            spike2.upgrade(['3-0-0','3-1-0','3-2-0'])
        elif round == 52:
            spike2.upgrade(['4-2-0'])
        elif round == 54:
            village2 = Monkey('village', 0.6276041666667, 0.3888888888889)
            village2.upgrade(['0-0-1','0-0-2'])
        elif round == 56:
            tack = Monkey('tack', 0.5317708333333, 0.4037037037037)
        elif round == 57:
            tack.upgrade(['1-0-0','2-0-0','2-0-1','2-0-2','2-0-3','2-0-4'])
        elif round == 58:
            alch2 = Monkey('alch', 0.5317708333333, 0.3518518518519)
            alch2.upgrade(['1-0-0','2-0-0','3-0-0','3-1-0','3-2-0'])
        elif round == 59:
            village2.upgrade(['1-0-2','2-0-2'])
        elif round == 60:
            ice = Monkey('ice', 0.6171875, 0.3111111111111)
        elif round == 61:
            ice.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif round == 62:
            ice.upgrade(['4-0-0','4-1-0'])
        elif round == 71:
            hero.special(1, 0.5744791666667, 0.5055555555556)
            ability(1,2)
        elif round == 75:
            tack.upgrade(['2-0-5'])
            village2.upgrade(['3-0-2'])
        elif round == 76:
            ability(2,0.5)
        elif round == 78:
            ability(2,3.5)
            alch2.upgrade(['4-2-0'])
            glue = Monkey('glue', 0.6171875, 0.2592592592593)
            glue.upgrade(['0-1-0','0-1-1','0-1-2','0-1-3'])
            glue.target('strong')
        elif round == 85:
            spike.upgrade(['1-0-5','2-0-5'])
        elif round == 88:
            glue.upgrade(['0-1-4','0-2-4'])
        elif round == 92:
            mortar = Monkey('mortar', 0.7192708333333, 0.8342592592593)
            mortar.special(1, 0.5734375, 0.1898148148148)
        elif round == 93:
            mortar.upgrade(['1-0-0','1-0-1','1-0-2','1-0-3','1-0-4'])
        elif round == 97:
            glue.upgrade(['0-2-5'])
        elif round == 98:
            boomer = Monkey('boomer', 0.7265625, 0.3194444444444)
            boomer.target('strong')
            boomer.upgrade(['1-0-0','2-0-0','2-0-1','2-0-2','2-0-3','2-0-4'])
            boomer2 = Monkey('boomer', 0.6640625, 0.3222222222222)
            boomer2.target('strong')
            boomer2.upgrade(['1-0-0','2-0-0','2-0-1','2-0-2','2-0-3','2-0-4'])
        elif round == 99:
            alch3 = Monkey('alch', 0.6338541666667, 0.2111111111111)
        elif round == 100:
            alch3.upgrade(['1-0-0','2-0-0','3-0-0','3-0-1'])
