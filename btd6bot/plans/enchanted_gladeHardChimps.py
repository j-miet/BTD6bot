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

def play(rounds: tuple[str, str, str, int, int, str]) -> None:
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start)
        if current_round == BEGIN:
            dart1 = Monkey('dart', 0.3744791666667, 0.8175925925926)
            sub1 = Monkey('sub', 0.5848958333333, 0.7657407407407)
        elif current_round == 8:
            engi1 = Monkey('engineer', 0.4036458333333, 0.7787037037037)
        elif current_round == 11:
            hero = Hero(0.4989583333333, 0.8305555555556)
        elif current_round == 14:
            druid1 = Monkey('druid', 0.4432291666667, 0.7731481481481)
            druid1.target('strong')
        elif current_round == 15:
            druid1.upgrade(['1-0-0'])
        elif current_round == 16:
            druid1.upgrade(['1-1-0'])
        elif current_round == 18:
            druid1.upgrade(['1-2-0'])
        elif current_round == 21:
            druid1.upgrade(['1-3-0'])
        elif current_round == 31:
            village1 = Monkey('village', 0.6786458333333, 0.8546296296296)
            village1.upgrade(['0-0-1','0-0-2'])
        elif current_round == 32:
            ace1 = Monkey('ace', 0.7578125, 0.9435185185185)
            ace1.upgrade(['0-0-1','0-0-2'])
        elif current_round == 35:
            ace1.upgrade(['0-0-3'])
        elif current_round == 37:
            ability(1,13)
        elif current_round == 38:
            ace1.upgrade(['1-0-3','2-0-3'])
        elif current_round == 39:
            alch1 = Monkey('alch', 0.7265625, 0.8787037037037)
            alch1.upgrade(['1-0-0','2-0-0'])
        elif current_round == 40:
            alch1.upgrade(['3-0-0'])
            ability(1)
        elif current_round == 41:
            village1.upgrade(['1-0-2','2-0-2'])
        elif current_round == 43:
            alch1.upgrade(['4-0-0'])
        elif current_round == 55:
            ace1.upgrade(['2-0-4'])
        elif current_round == 80:
            ability(2,2)
        elif current_round == 81:
            alch1.upgrade(['5-0-0'])
        elif current_round == 82:
            ace2 = Monkey('ace', 0.6734375, 0.9435185185185)
            ace2.upgrade(['1-0-0','2-0-0','2-0-1','2-0-2','2-0-3'])
        elif current_round == 88:
            ace2.upgrade(['2-0-4'])
        elif current_round == 89:
            ace3 = Monkey('ace', 0.7380208333333, 0.775)
            ace3.upgrade(['1-0-0','2-0-0'])
        elif current_round == 91:
            ace3.upgrade(['2-0-1','2-0-2','2-0-3'])
        elif current_round == 93:
            ability(2,3)
        elif current_round == 94:
            wait(11) # prevents bot from misinterpreting end of round too early, otherwise round 95 ability timing fails
        elif current_round == 95:
            ability(2,10)
        elif current_round == 96:
            ace3.upgrade(['2-0-4'])      
        elif current_round == 97:
            ninja1 = Monkey('ninja', 0.7609375, 0.8657407407407)
            ninja1.upgrade(['0-1-0','0-2-0','0-3-0'])
            spike1 = Monkey('spike', 0.6567708333333, 0.7342592592593)
        elif current_round == 98:
            ninja1.upgrade(['0-4-0'])
            spike1.upgrade(['1-0-0','1-1-0','1-2-0','1-3-0'])
            spike2 = Monkey('spike', 0.6223958333333, 0.7972222222222)
            spike2.upgrade(['1-0-0','1-1-0'])
        elif current_round == 99:
            ability(3,2.5)
            ability(2)
        elif current_round == 100:
            spike2.upgrade(['1-2-0','1-3-0'])