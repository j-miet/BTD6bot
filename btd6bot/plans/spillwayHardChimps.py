"""
[Hero] Psi
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
ice 0-3-0

sniper 0-0-0
ace 2-0-4

wizard 5-2-0
ninja 2-0-4
alch 3-2-0

spike 2-5-0
village 2-0-2
engineer 0-3-1
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
            ninja = Monkey('ninja', 0.434375, 0.4833333333333)
        elif round == 7:
            sniper = Monkey('sniper', 0.1020833333333, 0.1648148148148)
            sniper.target('strong')
        elif round == 8:
            ninja.upgrade(['1-0-0'])
        elif round == 14:
            hero = Hero(0.2296875, 0.3509259259259)
            hero.target('strong')
        elif round == 15:
            ninja.upgrade(['1-0-1'])
        elif round == 17:
            ninja.upgrade(['1-0-2'])
        elif round == 20:
            ninja.upgrade(['2-0-2'])
        elif round == 21:
            hero.target('first')
        elif round == 22:
            hero.target('strong')
        elif round == 27:
            ninja.upgrade(['2-0-3'])
        elif round == 30:
            village = Monkey('village', 0.1869791666667, 0.5064814814815)
        elif round == 32:
            village.upgrade(['0-0-1','0-0-2'])
        elif round == 35:
            ace = Monkey('ace', 0.1494791666667, 0.4148148148148)
        elif round == 36:
            ace.upgrade(['0-0-1','0-0-2'])
        elif round == 37:
            ace.upgrade(['0-0-3'])
        elif round == 38:
            ace.upgrade(['1-0-3','2-0-3'])
            alch = Monkey('alch', 0.1151041666667, 0.512962962963)
        elif round == 39:
            alch.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif round == 41:
            village.upgrade(['1-0-2','2-0-2'])
            ice = Monkey('ice', 0.2828125, 0.4425925925926)
        elif round == 44:
            ice.upgrade(['0-1-0','0-2-0','0-3-0'])
        elif round == 45:
            engi = Monkey('engineer', 0.2505208333333, 0.4092592592593)
            engi.upgrade(['0-1-0','0-2-0','0-3-0','0-3-1'])
            engi.special(1, 0.3588541666667, 0.4648148148148)
        elif round == 47:
            wizard = Monkey('wizard', 0.2817708333333, 0.5166666666667)
            wizard.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif round == 48:
            wizard.upgrade(['3-1-0','3-2-0'])
            wizard.special(1, 0.3578125, 0.4592592592593)
        elif round == 51:
            wizard.upgrade(['4-2-0'])
        elif round == 53:
            alch2 = Monkey('alch', 0.2380208333333, 0.6666666666667)
            alch2.upgrade(['1-0-0','2-0-0','3-0-0','3-1-0','3-2-0'])
        elif round == 74:
            wizard.upgrade(['5-2-0'])
            spike = Monkey('spike', 0.2401041666667, 0.4842592592593)
            spike.upgrade(['0-1-0','0-2-0'])
        elif round == 77:
            spike.upgrade(['0-3-0','1-3-0','2-3-0'])
        elif round == 79:
            spike.upgrade(['2-4-0'])
        elif round == 91:
            spike.upgrade(['2-5-0'])
        elif round == 96:
            ace.upgrade(['2-0-4'])
        elif round == 97:
            ninja.upgrade(['2-0-4'])
        elif round == 98:
            ability(3,8)
            ability(2,11)