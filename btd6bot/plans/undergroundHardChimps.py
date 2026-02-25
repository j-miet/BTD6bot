"""
[Hero] Geraldo
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0
boomer 0-2-4
tack 5-0-2
ice 4-2-0
glue 0-2-3

sniper 1-0-0

ninja 4-0-2
alch 4-2-1

village 4-3-2
_______________________________________
Strat is build around testing Geraldo so it's bit scuffed and unoptimized.
Still, should work quite consistently with minimal rng.
"""

from._plan_imports import *

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:
            dart1 = Monkey('dart', 0.4317708333333, 0.8555555555556)
            dart2 = Monkey('dart', 0.2640625, 0.5018518518519)
            dart3 = Monkey('dart', 0.4286458333333, 0.1388888888889)
        elif round == 9:
            ninja1 = Monkey('ninja', 0.4796875, 0.4203703703704)
        elif round == 10:
            ninja1.upgrade(['1-0-0'])
        elif round == 12:
            ninja1.upgrade(['1-0-1'])
        elif round == 13:
            ninja1.upgrade(['2-0-1'])
        elif round == 16:
            hero = Hero(0.4317708333333, 0.3092592592593)
        elif round == 20:
            ninja1.upgrade(['3-0-1'])
        elif round == 22:
            ninja1.upgrade(['3-0-2'])
            tack1 = Monkey('tack', 0.5359375, 0.4851851851852)
        elif round == 27:
            sniper1 = Monkey('sniper', 0.7526041666667, 0.6351851851852)
            sniper1.upgrade(['1-0-0'])
            sniper1.target('strong')
        elif round == 32:
            ninja1.upgrade(['4-0-2'])
        elif round == 34:
            alch1 = Monkey('alch', 0.5088541666667, 0.4462962962963)
        elif round == 35:
            alch1.upgrade(['1-0-0','2-0-0'])
        elif round == 36:
            alch1.upgrade(['3-0-0'])
            ice1 = Monkey('ice', 0.5130208333333, 0.5277777777778)
        elif round == 38:
            village1 = Monkey('village', 0.4651041666667, 0.5462962962963)
            village1.upgrade(['0-0-1','0-0-2'])
        elif round == 40:
            hero.shop(10, 0.4739583333333, 0.9277777777778)
        elif round == 41:
            village1.upgrade(['1-0-2','2-0-2'])
        elif round == 42:
            alch1.upgrade(['3-1-0','3-2-0'])
        elif round == 44:
            village1.upgrade(['3-0-2','4-0-2'])
        elif round == 45:
            tack1.upgrade(['0-0-1','0-0-2','0-0-3','1-0-3','2-0-3'])
        elif round == 47:
            tack1.upgrade(['2-0-4'])
        elif round == 48:
            ice1.upgrade(['0-1-0','1-1-0','2-1-0','3-1-0'])
        elif round == 49:
            ice1.upgrade(['4-1-0'])
            alch1.upgrade(['4-0-0'])
        elif round == 51:
            hero.shop(8, 0.5359375, 0.4851851851852)
            hero.shop(8, 0.4796875, 0.4203703703704)
        elif round == 61:
            tack1.upgrade(['2-0-5'])
        elif round == 63:
            hero.shop(13, 0.4317708333333, 0.3092592592593)
        elif round == 64:
            hero.shop(13, 0.4317708333333, 0.3092592592593)
        elif round == 65:
            tack2 = Monkey('tack', 0.5567708333333, 0.5842592592593)
            tack3 = Monkey('tack', 0.5328125, 0.6212962962963)
            tack4 = Monkey('tack', 0.4463541666667, 0.4101851851852)
        elif round == 66:
            tack2.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','1-0-4','2-0-4'])
        elif round == 67:
            tack3.upgrade(['0-0-1','0-0-2','0-0-3','1-0-3','2-0-3'])
        elif round == 70:
            tack3.upgrade(['2-0-4'])
            tack4.upgrade(['0-0-1','0-0-2','0-0-3','1-0-3','2-0-3'])
        elif round == 72:
            tack4.upgrade(['2-0-4'])
        elif round == 75:
            hero.shop(8, 0.5359375, 0.4851851851852)
            hero.shop(13, 0.4317708333333, 0.3092592592593)
            hero.shop(13, 0.4317708333333, 0.3092592592593)
            hero.shop(10, 0.3671875, 0.1990740740741)
        elif round == 78:
            hero.shop(6, 0.5359375, 0.4851851851852)
        elif round == 80:
            hero.shop(4, 0.5359375, 0.4851851851852)
            wait(8)
            hero.shop(10, 0.5192708333333, 0.7787037037037)
        elif round == 82:
            village1.upgrade(['5-0-2'])
            ice1.upgrade(['4-2-0'])
        elif round == 83:
            tack5 = Monkey('tack', 0.5026041666667, 0.6453703703704)
            tack5.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','1-0-4','2-0-4'])
        elif round == 85:
            glue1 = Monkey('glue', 0.6026041666667, 0.4796296296296)
            glue1.upgrade(['0-0-1','0-0-2','0-0-3','0-1-3','0-2-3'])
            glue1.target('strong')
        elif round == 88:
            hero.shop(8, 0.5567708333333, 0.5842592592593)
            hero.shop(8, 0.5328125, 0.6212962962963)
            hero.shop(4, 0.5359375, 0.4851851851852)
            hero.shop(10, 0.3671875, 0.1990740740741)
        elif round == 89:
            village2 = Monkey('village', 0.6182291666667, 0.5527777777778)
            village2.upgrade(['0-1-0','0-2-0','0-3-0', '1-3-0'])
        elif round == 91:
            hero.shop(8, 0.5359375, 0.4851851851852)
            hero.shop(6, 0.5359375, 0.4851851851852)
        elif round == 92:
            tack6 = Monkey('tack', 0.4119791666667, 0.4157407407407)
            tack6.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','1-0-4','2-0-4'])
        elif round == 93:
            tack7 = Monkey('tack', 0.3796875, 0.4305555555556)
            tack7.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','1-0-4','2-0-4'])
            tack8 = Monkey('tack', 0.3307291666667, 0.4898148148148)
            tack8.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','1-0-4','2-0-4'])
        elif round == 94:
            ice2 = Monkey('ice', 0.4067708333333, 0.4675925925926)
            ice2.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-1-0','4-2-0'])
            boomer1 = Monkey('boomer', 0.4671875, 0.6657407407407)
            boomer1.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
            boomer1.target('strong')
        elif round == 95:
            hero.shop(10, 0.3671875, 0.1990740740741)
            alch2 = Monkey('alch', 0.5984375, 0.6638888888889)
            alch2.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-0-1'])
        elif round == 96:
            boomer2 = Monkey('boomer', 0.4276041666667, 0.6805555555556)
            boomer2.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
            boomer2.target('strong')
            hero.shop(8, 0.5567708333333, 0.5842592592593)
            tack9 = Monkey('tack', 0.3161458333333, 0.5944444444444)
            tack9.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','1-0-4','2-0-4'])
            tack10 = Monkey('tack', 0.3484375, 0.6287037037037)
        elif round == 97:
            tack10.upgrade(['0-0-1','0-0-2','0-0-3','1-0-3','2-0-3'])
        elif round == 98:
            tack10.upgrade(['2-0-4'])
            wait(4)
            forward(1)
            hero.shop(8, 0.5328125, 0.6212962962963)
            hero.shop(8, 0.5026041666667, 0.6453703703704)
            hero.shop(8, 0.4119791666667, 0.4157407407407)
            hero.shop(10, 0.3671875, 0.1990740740741)
            hero.shop(10, 0.5192708333333, 0.7787037037037)
            alch3 = Monkey('alch', 0.3557291666667, 0.5324074074074)
            alch3.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0'])
            hero.shop(6, 0.5567708333333, 0.5842592592593)
            hero.shop(6, 0.5328125, 0.6212962962963)
            forward(1)
        elif round == 100:
            hero.shop(15, 0.3822916666667, 0.7027777777778)