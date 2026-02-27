"""
[Hero] Etienne
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0

ninja 0-4-0
alch 5-0-0
druid 1-3-0

sub 0-0-0
ace 2-0-4

spike 1-3-0
village 2-0-2
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
            dart1 = Monkey('dart', 0.3744791666667, 0.8175925925926)
            sub1 = Monkey('sub', 0.5848958333333, 0.7657407407407)
        elif round == 8:
            engi1 = Monkey('engineer', 0.4036458333333, 0.7787037037037)
        elif round == 11:
            hero = Hero(0.4989583333333, 0.8305555555556)
        elif round == 14:
            druid1 = Monkey('druid', 0.4432291666667, 0.7731481481481)
            druid1.target('strong')
        elif round == 15:
            druid1.upgrade(['1-0-0'])
        elif round == 16:
            druid1.upgrade(['1-1-0'])
        elif round == 18:
            druid1.upgrade(['1-2-0'])
        elif round == 21:
            druid1.upgrade(['1-3-0'])
        elif round == 31:
            village1 = Monkey('village', 0.6786458333333, 0.8546296296296)
            village1.upgrade(['0-0-1','0-0-2'])
        elif round == 32:
            ace1 = Monkey('ace', 0.7578125, 0.9435185185185)
            ace1.upgrade(['0-0-1','0-0-2'])
        elif round == 35:
            ace1.upgrade(['0-0-3'])
        elif round == 37:
            ability(1,13)
        elif round == 38:
            ace1.upgrade(['1-0-3','2-0-3'])
        elif round == 39:
            alch1 = Monkey('alch', 0.7265625, 0.8787037037037)
            alch1.upgrade(['1-0-0','2-0-0'])
        elif round == 40:
            alch1.upgrade(['3-0-0'])
            ability(1)
        elif round == 41:
            village1.upgrade(['1-0-2','2-0-2'])
        elif round == 43:
            alch1.upgrade(['4-0-0'])
        elif round == 55:
            ace1.upgrade(['2-0-4'])
        elif round == 80:
            ability(2,2)
        elif round == 81:
            alch1.upgrade(['5-0-0'])
        elif round == 82:
            ace2 = Monkey('ace', 0.6734375, 0.9435185185185)
            ace2.upgrade(['1-0-0','2-0-0','2-0-1','2-0-2','2-0-3'])
        elif round == 88:
            ace2.upgrade(['2-0-4'])
        elif round == 89:
            ace3 = Monkey('ace', 0.7380208333333, 0.775)
            ace3.upgrade(['1-0-0','2-0-0'])
        elif round == 91:
            ace3.upgrade(['2-0-1','2-0-2','2-0-3'])
        elif round == 93:
            ability(2,3)
        elif round == 94:
            wait(11) # prevents bot from misinterpreting end of round too early, otherwise round 95 ability timing fails
        elif round == 95:
            ability(2,10)
        elif round == 96:
            ace3.upgrade(['2-0-4'])      
        elif round == 97:
            ninja1 = Monkey('ninja', 0.7609375, 0.8657407407407)
            ninja1.upgrade(['0-1-0','0-2-0','0-3-0'])
            spike1 = Monkey('spike', 0.6567708333333, 0.7342592592593)
        elif round == 98:
            ninja1.upgrade(['0-4-0'])
            spike1.upgrade(['1-0-0','1-1-0','1-2-0','1-3-0'])
            spike2 = Monkey('spike', 0.6223958333333, 0.7972222222222)
            spike2.upgrade(['1-0-0','1-1-0'])
        elif round == 99:
            ability(3,2.5)
            ability(2)
        elif round == 100:
            spike2.upgrade(['1-2-0','1-3-0'])