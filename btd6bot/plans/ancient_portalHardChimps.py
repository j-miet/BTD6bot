"""
[Hero] Quincy
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===

ice 0-1-4
glue 0-2-3

sub 0-5-2
dartling 2-0-5

wizard 0-3-1
alch 3-0-0

village 2-3-0
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
            hero = Hero(0.6286458333333, 0.3972222222222)
        elif current_round == 10:
            dartling1 = Monkey('dartling', 0.6640625, 0.4324074074074)
            dartling1.target('locked', 0.5276041666667, 0.1342592592593)
        elif current_round == 12:
            dartling1.upgrade(['1-0-0'])
        elif current_round == 18:
            dartling1.upgrade(['1-0-1','1-0-2'])
        elif current_round == 22:
            village1 = Monkey('village', 0.5776041666667, 0.3953703703704)
            wizard1 = Monkey('wizard', 0.6109375, 0.2453703703704)
        elif current_round == 27:
            wizard1.upgrade(['0-1-0','0-2-0'])
            wizard1.target('strong')
        elif current_round == 35:
            wizard1.upgrade(['0-3-0','0-3-1'])
        elif current_round == 37:
            village1.upgrade(['0-1-0','0-2-0'])
        elif current_round == 40:
            ability(1)
        elif current_round == 41:
            dartling1.upgrade(['1-0-3'])
        elif current_round == 48:
            dartling1.upgrade(['1-0-4'])
            dartling1.target('independent')
        elif current_round == 49:
            dartling1.upgrade(['2-0-4'])
            village1.upgrade(['1-2-0','2-2-0'])
        elif current_round == 50:
            alch1 = Monkey('alch', 0.5807291666667, 0.4712962962963)
            alch1.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif current_round == 55:
            ice1 = Monkey('ice', 0.6395833333333, 0.3074074074074)
            ice1.upgrade(['0-0-1','0-0-2','0-0-3','0-1-3'])
        elif current_round == 59:
            ice1.upgrade(['0-1-4'])
        elif current_round == 75:
            ability(1,7)
        elif current_round == 76:
            ability(2,1)
        elif current_round == 80:
            ability(1,2)
        elif current_round == 82:
            dartling1.upgrade(['2-0-5'])
        elif current_round == 84:
            village1.upgrade(['2-3-0'])
        elif current_round == 96:
            sub1 = Monkey('sub', 0.6276041666667, 0.6037037037037)
            sub1.upgrade(['0-1-0','0-2-0','0-3-0','0-4-0','0-5-0'])
        elif current_round == 97:
            sub1.upgrade(['0-5-1','0-5-2'])
            glue1 = Monkey('glue', 0.5723958333333, 0.237037037037)
            glue1.target('strong')
            glue1.upgrade(['0-0-1','0-0-2'])
        elif current_round == 98:
            glue1.upgrade(['0-0-3','0-1-3'])
            ability(1,4)
            ability(2,5)
            glue1.upgrade(['0-2-3'])
        elif current_round == 100:
            ability(3,3)
            ability(1)