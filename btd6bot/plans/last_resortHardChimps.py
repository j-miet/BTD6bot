"""
[Hero] Adora
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0
glue 0-2-4

sniper 4-0-2

alch 3-3-0
druid 4-0-2

village 2-0-2
engineer 5-2-0
spike 4-0-5
_______________________________________
Some data can get skipped because bot incorrectly detects different value.
This should mostly happen in early/mid game and thus not affect later data where ability timings are important.
"""

from._plan_imports import *

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:    
            change_autostart() 
            dart1 = Monkey('dart', 0.7255208333333, 0.0509259259259, False)
            engi1 = Monkey('engineer', 0.5453125, 0.0490740740741)
            forward()
            engi1.target('strong')
            end_round(10)
        elif round == 7:
            end_round(12)
        elif round == 8:
            sniper1 = Monkey('sniper', 0.353125, 0.0490740740741)
            sniper1.target('strong')
            end_round(8)
        elif round == 9:
            engi1.target('first')
            end_round(10)
        elif round == 10:
            engi1.upgrade(['1-0-0'])
            end_round(6)
        elif round == 11:
            end_round(8)
        elif round == 12:
            end_round(7)
        elif round == 13:
            end_round(13)
        elif round == 14:
            end_round(12)
        elif round == 15:
            hero = Hero(0.5057291666667, 0.0472222222222)
            change_autostart()
        elif round == 19:
            spike1 = Monkey('spike', 0.6869791666667, 0.0342592592593)
        elif round == 21:
            druid1 = Monkey('druid', 0.1473958333333, 0.0481481481481, False)
            druid1.target('strong', cpos=(0.1328125, 0.0592592592593))
        elif round == 22:
            druid1.upgrade(['0-1-0'])
        elif round == 25:
            druid1.upgrade(['0-2-0'])
        elif round == 27:
            druid1.upgrade(['0-3-0', '1-3-0'])
        elif round == 32:
            village1 = Monkey('village', 0.6338541666667, 0.0490740740741)
            village1.upgrade(['0-0-1'])
            spike1.upgrade(['0-0-1','0-0-2'])
            spike1.target('smart')
        elif round == 34:
            village1.upgrade(['0-0-2'])
        elif round == 35:
            spike1.upgrade(['1-0-2','2-0-2'])
        elif round == 36:
            ability(1)
        elif round == 37:
            spike1.upgrade(['3-0-2'])
        elif round == 38:
            druid2 = Monkey('druid', 0.5838541666667, 0.0333333333333)
            druid2.upgrade(['1-0-0','2-0-0'])
        elif round == 39:
            druid2.upgrade(['3-0-0'])
            spike1.target('close')
        elif round == 41:
            ability(2, xy=(0.7255208333333, 0.0722222222222))
            wait(1)
            alch1 = Monkey('alch', 0.7265625, 0.05, False)
            alch1.upgrade(['1-0-0','2-0-0','3-0-0'], cpos=(0.7239583333333, 0.075))
        elif round == 43:
            village1.upgrade(['1-0-2','2-0-2'])
        elif round == 49:
            spike1.upgrade(['4-0-2'])
            engi1.upgrade(['2-0-0','3-0-0','3-1-0','3-2-0','4-2-0'])
        elif round == 52:
            druid2.upgrade(['4-0-0','4-0-1','4-0-2'])
        elif round == 53:
            alch1.upgrade(['3-1-0','3-2-0'])
        elif round == 74:
            engi1.upgrade(['5-2-0'])
        elif round == 84:
            ability(2, xy=(0.6895833333333, 0.0490740740741))
            spike2 = Monkey('spike', 0.6875, 0.0416666666667)
            spike2.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-0-5','1-0-5','2-0-5'])
            spike2.target('smart')
        elif round == 85:
            village2 = Monkey('village', 0.3046875, 0.05, False)
            village2.upgrade(['0-0-1','0-0-2'], cpos=(0.3041666666667, 0.062962962963))
        elif round == 86:
            druid3 = Monkey('druid', 0.3911458333333, 0.0490740740741)
            druid3.upgrade(['1-0-0','2-0-0','3-0-0','3-0-1','3-0-2'])
        elif round == 88:
            druid3.upgrade(['4-0-2'])
            glue1 = Monkey('glue', 0.2567708333333, 0.0490740740741, False)
            glue1.target('strong', cpos=(0.2598958333333, 0.0740740740741))
            glue1.upgrade(['0-0-1','0-0-2'])
        elif round == 89:
            glue1.upgrade(['0-0-3','0-1-3'])
        elif round == 91:
            alch2 = Monkey('alch', 0.2234375, 0.0416666666667, False)
            alch2.target('strong', cpos=(0.2140625, 0.0824074074074))
            alch2.upgrade(['0-1-0','0-2-0','0-3-0','1-3-0'])
        elif round == 92:
            village2.upgrade(['1-0-2','2-0-2'])
            glue1.upgrade(['0-2-3'])
        elif round == 93:
            sniper1.upgrade(['1-0-0','2-0-0','3-0-0','3-0-1','3-0-2'])
        elif round == 94:
            sniper1.upgrade(['4-0-2'])
            sniper1.target('last')
        elif round == 95:
            druid4 = Monkey('druid', 0.3640625, 0.1962962962963)
            druid4.upgrade(['1-0-0','2-0-0','3-0-0','3-0-1','3-0-2'])
        elif round == 96:
            druid4.upgrade(['4-0-2'])
            druid5 = Monkey('druid', 0.3244791666667, 0.1944444444444)
            druid5.upgrade(['1-0-0','2-0-0','3-0-0','3-0-1','3-0-2'])
        elif round == 97:
            druid5.upgrade(['4-0-2'])
        elif round == 98:
            ability(2, 9, xy=(0.1317708333333, 0.0444444444444))
            ability(1)
            ability(3)
            ability(2, 13.5, xy=(0.2182291666667, 0.0777777777778))
            druid6 = Monkey('druid', 0.2848958333333, 0.1944444444444)
            druid6.upgrade(['1-0-0','2-0-0','3-0-0','3-0-1','3-0-2','4-0-2'])
        elif round == 99:
            sniper1.target('strong')
            alch3 = Monkey('alch', 0.4625, 0.05)
            alch3.upgrade(['0-1-0','0-2-0','0-3-0'])
        elif round == 100:
            ability(2, 5, xy=(0.246875, 0.0675925925926))
            ability(3)
            ability(1)