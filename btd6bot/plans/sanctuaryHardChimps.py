"""
[Hero] Churchill
[Monkey Knowledge] -
---------------------------------------------------------------
===Monkeys & upgrades required===
boomer 0-2-4
glue 5-2-0
desperado 0-1-0

sniper 1-1-0
sub 2-0-3
mortar 0-2-4

alch 4-2-0

spike 1-0-5
village 4-2-0
engineer 0-0-0
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
            change_autostart()
            desp1 = Monkey('desperado', 0.5359375, 0.2546296296296)
            desp2 = Monkey('desperado', 0.1661458333333, 0.3694444444444)
            forward()
            wait(9)
            desp2.target('strong', cpos=(0.2333333333333, 0.4203703703704))
            end_round()
        elif round == 7:
            wait(11)
            desp2.target('first', cpos=(0.3203125, 0.4194444444444))
            end_round()
        elif round == 8:
            sniper1 = Monkey('sniper', 0.7161458333333, 0.8472222222222)
            sniper1.target('strong')
            end_round(5)
        elif round == 9:
            end_round(8)
        elif round == 10:
            engi = Monkey('engineer', 0.6484375, 0.3990740740741)
            engi.target('strong')
            end_round(13)
        elif round == 11:
            end_round(8)
        elif round == 12:
            wait(7)
            sub = Monkey('sub', 0.4854166666667, 0.1768518518519)
            sub.upgrade(['1-0-0'])
            end_round()
        elif round == 13:
            end_round(13 )
        elif round == 14:
            wait(10)
            sub.upgrade(['2-0-0'], cpos=(0.4895833333333, 0.162037037037))
            end_round()
        elif round == 15:
            wait(2)
            sniper1.target('first', cpos=(0.7614583333333, 0.8712962962963))
            wait(7)
            sniper1.target('strong')
            end_round()
        elif round == 16:
            wait(8)
            sub.upgrade(['2-0-1'], cpos=(0.4927083333333, 0.1731481481481))
            end_round()
        elif round == 17:
            end_round(4)
        elif round == 18:
            end_round(12)
        elif round == 19:
            wait(8)
            sniper1.target('first', cpos=(0.6479166666667, 0.7935185185185))
            end_round() 
        elif round == 20:
            wait(3)
            sub.upgrade(['2-0-2'], cpos=(0.490625, 0.1712962962963))
            end_round()
        elif round == 21:
            wait(7)
            sniper1.upgrade(['1-0-0'], cpos=(0.7583333333333, 0.8675925925926))
            sniper1.target('strong') 
            end_round()
        elif round == 22:
            end_round(5)
        elif round == 23:
            wait(4)
            desp1.upgrade(['0-1-0'], cpos=(0.3916666666667, 0.2564814814815))
            boomer = Monkey('boomer', 0.2760416666667, 0.4259259259259)
            boomer.target('last')
            boomer.special(1)
            end_round()
        elif round == 24:
            end_round(4)
        elif round == 25:
            end_round(9)
        elif round == 26:
            wait(7)
            sniper1.target('first', cpos=(0.71875, 0.8481481481481))
            end_round()
        elif round == 27:
            wait(14)
            sniper1.target('strong', cpos=(0.71875, 0.8481481481481))
            end_round()
        elif round == 28:
            end_round(5)
        elif round == 29:
            wait(7)
            hero = Hero(0.4921875, 0.2518518518519)
            end_round()
        elif round == 30:
            end_round(7)
        elif round == 31:
            end_round(7)
        elif round == 32:
            sub.upgrade(['2-0-3'], cpos=(0.4848958333333, 0.1722222222222))
            sniper1.upgrade(['1-1-0'], cpos=(0.7223958333333, 0.8351851851852))
            end_round(4)
        elif round == 33: 
            end_round(10)
        elif round == 34:
            wait(14)
            click(0.4088541666667, 0.2740740740741)
            wait(1)
            click(0.7546875, 0.6296296296296)
            click(0.5, 0.5)
            end_round()
        elif round == 35:
            end_round(13)
        elif round == 36:
            wait(9)
            alch = Monkey('alch', 0.4671875, 0.0648148148148)
            alch.upgrade(['1-0-0','2-0-0'])
            end_round()
        elif round == 37:
            end_round(17)
        elif round == 38:
            wait(2)
            village = Monkey('village', 0.4380208333333, 0.1462962962963)
            village.upgrade(['1-0-0','2-0-0','3-0-0'])
            end_round(5)
        elif round == 39:
            wait(14)
            alch.upgrade(['3-0-0'], cpos=(0.3880208333333, 0.0407407407407))
            end_round()
        elif round == 40: 
            ability(1)
            wait(3)
            alch.upgrade(['3-1-0','3-2-0'], cpos=(0.4671875, 0.0574074074074))
            end_round()
        elif round == 41:
            end_round(17)
        elif round == 42:
            village.upgrade(['4-0-0'], cpos=(0.4369791666667, 0.1481481481481))
            end_round(3)
        elif round == 43:
            wait(1)
            glue = Monkey('glue', 0.4161458333333, 0.2185185185185)
            glue.upgrade(['1-0-0','2-0-0','2-1-0'])
            end_round(1)
        elif round == 44:
            glue.upgrade(['3-1-0'], cpos=(0.4953125, 0.2333333333333))
            end_round(3)
        elif round == 45:
            end_round(20)
        elif round == 46:
            end_round(5)
        elif round == 47:
            end_round(10)
        elif round == 48:
            wait(2)
            glue.upgrade(['4-1-0','4-2-0'], cpos=(0.5020833333333, 0.2462962962963))
            end_round(6)
        elif round == 49:
            wait(18)
            sub.target('strong', cpos=(0.5640625, 0.1462962962963))
            change_autostart()
            end_round()
        elif round == 57:
            ability(1, 1)
        elif round == 59:
            wait(1)
            glue.upgrade(['5-2-0'], cpos=(0.421875, 0.212962962963))
        elif round == 65:
            wait(2)
            village2 = Monkey('village', 0.4583333333333, 0.9444444444444)
            village2.upgrade(['0-0-1','0-0-2'])
            spike = Monkey('spike', 0.4854166666667, 0.8592592592593)
            spike.upgrade(['0-0-1','0-0-2','0-0-3','1-0-3'])
            spike.target('automatic')
            alch2 = Monkey('alch', 0.5104166666667, 0.9314814814815)
            alch2.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif round == 68:
            wait(1)
            alch2.upgrade(['4-0-0'], cpos=(0.4359375, 0.9305555555556))
        elif round == 69:
            wait(1)
            spike.upgrade(['1-0-4'])
        elif round == 71:
            wait(1)
            village.upgrade(['4-1-0','4-2-0'], cpos=(0.3614583333333, 0.15))
        elif round == 82:
            wait(2)
            spike.upgrade(['1-0-5'], cpos=(0.3984375, 0.8407407407407))
            village2.upgrade(['1-0-2','2-0-2'], cpos=(0.3723958333333, 0.9287037037037))
        elif round == 83:
            wait(2)
            alch.upgrade(['4-2-0'], cpos=(0.3932291666667, 0.0490740740741))
        elif round == 84:
            wait(1)
            boomer2 = Monkey('boomer', 0.3796875, 0.2287037037037)
            forward()
            boomer2.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
            boomer2.target('strong')
            boomer.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'], cpos=(0.1296875, 0.2101851851852))
            boomer.target('strong')
            forward()
        elif round == 87:
            wait(1)
            boomer3 = Monkey('boomer', 0.7067708333333, 0.3990740740741)
            boomer3.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
            boomer3.target('strong')
        elif round == 91:
            wait(1)
            mortar = Monkey('mortar', 0.2536458333333, 0.7787037037037)
            mortar.special(1, 0.4390625, 0.3694444444444)
            mortar.upgrade(['0-0-1','0-0-2','0-0-3'])
        elif round == 92:
            wait(1)
            mortar.upgrade(['0-0-4','0-1-4','0-2-4'], cpos=(0.2161458333333, 0.812037037037))
        elif round == 93:
            wait(1)
            boomer4 = Monkey('boomer', 0.1005208333333, 0.3287037037037)
            boomer4.target('strong')
            boomer4.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
        elif round == 94:
            wait(1)
            boomer5 = Monkey('boomer', 0.7682291666667, 0.212037037037)
            boomer5.target('strong')
            boomer5.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
        elif round == 95:
            wait(1)
            boomer6 = Monkey('boomer', 0.3359375, 0.487962962963)
            boomer6.target('strong')
            boomer6.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
        elif round == 96:
            wait(1)
            boomer7 = Monkey('boomer', 0.6484375, 0.5101851851852)
            boomer7.target('strong')
            boomer7.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
        elif round == 97:
            wait(1)
            boomer8 = Monkey('boomer', 0.5817708333333, 0.5027777777778)
            boomer8.target('strong')
            boomer8.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
        elif round == END:
            ability(2,2)
            ability(1,3)