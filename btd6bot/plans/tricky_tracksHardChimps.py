"""
[Hero] Obyn
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0
boomer 0-2-4
bomb 4-2-0
tack 2-0-4
ice 5-1-0
glue 0-2-4
desperado 0-0-0

sniper 1-1-0

wizard 5-3-2
alch 3-0-1
druid 0-0-0
mermonkey 4-3-2

village 3-0-2
_______________________________________
In version 53 this map got changed so there's less space to put towers. For this reason placements have been
adjusted, but same strat doesn't seem to be black border viable anymore: it always ends up failing on round 99. Funnily
enough it passes round 99 on second try and 100 is also beatable, making this gold border viable if you want to manually
finish the last 2 rounds.

Plan will be updated on next bot version.
"""

from._plan_imports import *

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:     
            desp1 = Monkey('desperado', 0.3151041666667, 0.5111111111111)
            desp2 = Monkey('desperado', 0.553125, 0.537962962963)
        elif round == 8:
            dart1 = Monkey('dart', 0.3505208333333, 0.4675925925926)
        elif round == 9:
            dart2 = Monkey('dart', 0.5161458333333, 0.5361111111111)
        elif round == 10:
            mermonkey1 = Monkey('mermonkey', 0.2859375, 0.2638888888889)
            dart1.target('close')
            dart2.target('close')
        elif round == 11:
            dart1.target('first')
            dart2.target('first')
        elif round == 13:
            hero = Hero(0.540625, 0.462037037037)
        elif round == 14:
            hero.target('close', cpos=(0.5369791666667, 0.4638888888889))
            mermonkey2 = Monkey('mermonkey', 0.34375, 0.4009259259259)
        elif round == 15:
            mermonkey3 = Monkey('mermonkey', 0.5828125, 0.7064814814815)
        elif round == 17:
            sniper = Monkey('sniper', 0.8276041666667, 0.5481481481481)
            sniper.target('strong')
        elif round == 19:
            wizard = Monkey('wizard', 0.4776041666667, 0.5333333333333)
            wizard.upgrade(['1-0-0'])
        elif round == 21:
            wizard.upgrade(['2-0-0'])
        elif round == 22:
            sniper.upgrade(['1-0-0'])
        elif round == 23:
            sniper.upgrade(['1-1-0'])
        elif round == 25:
            druid1 = Monkey('druid', 0.5057291666667, 0.5898148148148)
        elif round == 28:
            ability(1)
        elif round == 29:
            wizard.upgrade(['3-0-0'])
        elif round == 30:
            wizard.upgrade(['3-0-1','3-0-2'])
        elif round == 31:
            mermonkey1.upgrade(['0-0-1'])
        elif round == 34:
            mermonkey1.upgrade(['0-1-1','0-2-1','0-3-1','0-3-2'])
        elif round == 35:
            wizard2 = Monkey('wizard', 0.3848958333333, 0.4416666666667)
            wizard2.upgrade(['0-1-0','0-1-1','0-1-2'])
        elif round == 36:
            ability(1)
        elif round == 37:
            druid2 = Monkey('druid', 0.465625, 0.5916666666667)
        elif round == 39:
            change_autostart()
            wait(14)
            wizard2.upgrade(['0-2-2','0-3-2'])
            change_autostart()
            end_round()
        elif round == 40:
            ability(1)
        elif round == 41:
            mermonkey2.upgrade(['1-0-0','2-0-0','3-0-0','3-0-1','3-0-2'])
        elif round == 43:
            village1 = Monkey('village', 0.5640625, 0.7842592592593)
            village1.upgrade(['0-0-1','0-0-2'])
        elif round == 44:
            mermonkey3.upgrade(['0-0-1','0-0-2'])
            mermonkey4 = Monkey('mermonkey', 0.5109375, 0.7925925925926)
            mermonkey4.upgrade(['0-0-1','0-0-2'])
        elif round == 45:
            mermonkey3.upgrade(['0-1-2','0-2-2','0-3-2'])
        elif round == 46:
            mermonkey4.upgrade(['0-1-2','0-2-2','0-3-2'])
            mermonkey5 = Monkey('mermonkey', 0.6208333333333, 0.6648148148148)
        elif round == 47:
            mermonkey5.upgrade(['0-0-1','0-0-2','0-1-2','0-2-2','0-3-2'])
        elif round == 49:
            mermonkey2.upgrade(['4-0-2'])
            mermonkey6 = Monkey('mermonkey', 0.4776041666667, 0.8388888888889)
            mermonkey6.upgrade(['0-0-1','0-0-2','0-1-2','0-2-2','0-3-2'])
        elif round == 50:
            village1.upgrade(['1-0-2','2-0-2'])
        elif round == 51:
            mermonkey7 = Monkey('mermonkey', 0.6822916666667, 0.6888888888889)
            mermonkey7.upgrade(['0-0-1','0-0-2','0-1-2','0-2-2','0-3-2'])
        elif round == 52:
            mermonkey8 = Monkey('mermonkey', 0.4697916666667, 0.9074074074074)
            mermonkey8.upgrade(['0-0-1','0-0-2','0-1-2','0-2-2','0-3-2'])
        elif round == 54:
            mermonkey9 = Monkey('mermonkey', 0.7239583333333, 0.5648148148148)
            mermonkey9.upgrade(['0-0-1','0-0-2','0-1-2','0-2-2','0-2-2'])
        elif round == 55:
            mermonkey10 = Monkey('mermonkey', 0.4255208333333, 0.8916666666667)
            mermonkey10.upgrade(['0-0-1','0-0-2','0-1-2','0-2-2','0-2-2'])
        elif round == 61:
            ability(1)
            wizard.upgrade(['4-0-2'])
        elif round == 62:
            ability(1)
            village2 = Monkey('village', 0.4177083333333, 0.6240740740741)
            village2.upgrade(['1-0-0'])
        elif round == 63:
            village2.upgrade(['2-0-0','2-0-1','2-0-2'])
        elif round == 79:
            wizard.upgrade(['5-0-2'])
        elif round == 81:
            village2.upgrade(['3-0-2'])
            ice = Monkey('ice', 0.3901041666667, 0.3842592592593)
            ice.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-1-0'])
        elif round == 82:
            boomer = Monkey('boomer', 0.4072916666667, 0.7)
            boomer.target('strong')
            boomer.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
        elif round == 83:
            bomb = Monkey('bomb', 0.4276041666667, 0.3916666666667)
            bomb.upgrade(['1-0-0','2-0-0','3-0-0','3-1-0','3-2-0'])
        elif round == 88:
            ability(1)
        elif round == 92:
            ice.upgrade(['5-1-0'])
        elif round == 94:
            alch = Monkey('alch', 0.4036458333333, 0.3361111111111)
            alch.upgrade(['1-0-0','2-0-0','3-0-0','3-0-1'])
            boomer2 = Monkey('boomer', 0.6234375, 0.7305555555556)
            boomer2.target('strong')
            glue = Monkey('glue', 0.4630208333333, 0.6490740740741)
            glue.target('strong')
        elif round == 95:
            boomer2.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
            glue.upgrade(['0-0-1','0-0-2','0-0-3','0-1-3','0-2-3'])
        elif round == 96:
            glue.upgrade(['0-2-4'])
            hero.special(1, 0.428125, 0.4981481481481)
        elif round == 97:
            tack = Monkey('tack', 0.4630208333333, 0.3527777777778)
            tack.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','1-0-4','2-0-4'])
            tack2 = Monkey('tack', 0.5135416666667, 0.2935185185185)
            tack3 = Monkey('tack', 0.3739583333333, 0.6555555555556)
            tack4 = Monkey('tack', 0.434375, 0.2935185185185)
        elif round == 98:
            tack2.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','1-0-4','2-0-4'])
            tack3.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','1-0-4','2-0-4'])
            tack4.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','1-0-4','2-0-4'])
        elif round == 99:
            ability(2)
            wizard.target('strong')
            tack5 = Monkey('tack', 0.290625, 0.5574074074074)
        elif round == 100:
            ability(1)
            wizard.target('first')
            tack5.upgrade(['0-0-1','0-0-2','0-0-3','1-0-3'])