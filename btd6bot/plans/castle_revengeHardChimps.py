"""
[Hero] Sauda
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0
glue 0-2-3

sniper 1-1-0
sub 0-0-0

wizard 0-3-2
super 2-0-3
ninja 1-4-0
alch 4-2-0

spike 1-3-0
village 3-0-2

_______________________________________
Round 40 is bad rng-wise and usually ruins the run.
But after 40, it becomes quite minimal, but late rounds like 98 can be scary.
"""

from._plan_imports import *

def play(rounds: tuple[str, str, str, int, int, str]) -> None:
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start)
        if current_round == BEGIN:
            dart1 = Monkey('dart', 0.5921875, 0.7046296296296)
            sub1 = Monkey('sub', 0.165625, 0.2490740740741)
        elif current_round == 7:
            dart2 = Monkey('dart', 0.1322916666667, 0.7351851851852)
        elif current_round == 9:
            sniper = Monkey('sniper', 0.521875, 0.5240740740741)
            sniper.target('strong')
        elif current_round == 12:
            hero = Hero(0.4666666666667, 0.237962962963)
        elif current_round == 13:
            wizard = Monkey('wizard', 0.5489583333333, 0.6861111111111)
            dart1.target('strong')
        elif current_round == 14:
            wizard.upgrade(['0-1-0'])
        elif current_round == 18:
            spike1 = Monkey('spike', 0.128125, 0.5824074074074)
        elif current_round == 22:
            wizard.upgrade(['0-2-0'])
        elif current_round == 23:
            sniper.upgrade(['1-0-0'])
        elif current_round == 31:
            ability(1,3)
        elif current_round == 32:
            wizard.upgrade(['0-3-0'])
        elif current_round == 34:
            alch = Monkey('alch', 0.5364583333333, 0.3083333333333)
            alch.upgrade(['1-0-0'])
            alch.target('strong')
        elif current_round == 35:
            ability(1,5.75)
        elif current_round == 36:
            alch.upgrade(['2-0-0','3-0-0'])
        elif current_round == 37:
            alch.upgrade(['3-1-0','3-2-0'])
        elif current_round == 38:
            ability(1,9.75)
        elif current_round == 39:
            super1 = Monkey('super', 0.3572916666667, 0.387962962963)
        elif current_round == 40:
            ability(1,4.6)
        elif current_round == 41:
            village1 = Monkey('village', 0.4734375, 0.5231481481481)
            village1.upgrade(['0-0-1','0-0-2','1-0-2'])
            wizard.upgrade(['0-3-1','0-3-2'])
        elif current_round == 42:
            village2 = Monkey('village', 0.4260416666667, 0.387962962963)
        elif current_round == 43:
            ability(1,1.75)
            village2.upgrade(['0-0-1','0-0-2'])
        elif current_round == 44:
            super1.upgrade(['0-1-0'])
            village2.upgrade(['1-0-2'])
            sniper.upgrade(['1-1-0'])
            sniper.special(1)
        elif current_round == 45:
            super1.upgrade(['0-2-0'])
        elif current_round == 46:
            village2.upgrade(['2-0-2'])
        elif current_round == 48:
            super1.upgrade(['0-2-1','0-2-2'])
        elif current_round == 49:
            super1.upgrade(['0-2-3'])
            alch.target('first')
        elif current_round == 50:
            ability(2,xy= (0.4171875, 0.4824074074074))
        elif current_round == 51:
            super2 = Monkey('super', 0.3625, 0.5268518518519)
            super2.upgrade(['0-1-0'])
        elif current_round == 52:
            super2.upgrade(['0-2-0'])
        elif current_round == 53:
            super2.upgrade(['0-2-1'])
        elif current_round == 54:
            super2.upgrade(['0-2-2'])
        elif current_round == 55:
            super3 = Monkey('super', 0.365625, 0.4287037037037)
        elif current_round == 57:
            super3.upgrade(['0-1-0','0-2-0'])
        elif current_round == 58:
            super3.upgrade(['0-2-1','0-2-2'])
        elif current_round == 60:
            ability(1,8.5)
        elif current_round == 62:
            super3.upgrade(['0-2-3'])
            glue = Monkey('glue', 0.528125, 0.4731481481481)
            glue.target('strong')
            glue.upgrade(['0-0-1','0-0-2','0-1-2'])
        elif current_round == 63:
            ability(1,1.75)
            ability(3,8)
            ability(1,13)
        elif current_round == 64:
            glue.upgrade(['0-1-3'])
        elif current_round == 67:
            super2.upgrade(['0-2-3'])
        elif current_round == 70:
            alch.upgrade(['4-2-0'])
        elif current_round == 75:
            ability(1,9)
        elif current_round == 76:
            ability(3,1.5)
        elif current_round == 77:
            ability(1,16)
        elif current_round == 78:
            ability(3,4.5)
            ability(3,27)
        elif current_round == 80:
            ability(1,16)
            ability(3,17)
        elif current_round == 85:
            alch.upgrade(['5-2-0'])
            ability(2,xy=(0.5729166666667, 0.4064814814815))
            ability(2,xy=(0.484375, 0.3324074074074))
            ability(2,xy=(0.4864583333333, 0.4287037037037))
        elif current_round == 86:
            ability(2,xy=(0.4171875, 0.4824074074074))
            ability(2,xy=(0.3614583333333, 0.5231481481481))
            ability(2,xy=(0.36875, 0.4231481481481))
        elif current_round == 87:
            super4 = Monkey('super', 0.4885416666667, 0.4287037037037)
            super4.upgrade(['0-1-0','0-2-0'])
        elif current_round == 88:
            super4.upgrade(['0-2-1','0-2-2'])
        elif current_round == 89:
            ninja = Monkey('ninja', 0.5625, 0.475)
            ninja.upgrade(['0-1-0','0-2-0'])
            ninja.special(1)
        elif current_round == 91:
            super4.upgrade(['0-2-3'])
        elif current_round == 92:
            super5 = Monkey('super', 0.4822916666667, 0.3324074074074)
        elif current_round == 93:
            super5.upgrade(['1-0-0','2-0-0'])
        elif current_round == 94:
            super5.upgrade(['2-0-1','2-0-2','2-0-3'])
            ninja.upgrade(['1-2-0'])
        elif current_round == 95:
            glue.upgrade(['0-2-3'])
            village2.upgrade(['3-0-2'])
        elif current_round == 96:
            click(0.49375, 0.4157407407407)
            wait(0.5)
            click(0.25, 0.1861111111111)
            wait(0.5)
            click(0.30625, 0.4768518518519)
        elif current_round == 97:
            super6 = Monkey('super', 0.4895833333333, 0.4287037037037)
            super6.upgrade(['1-0-0','2-0-0','2-0-1','2-0-2'])
        elif current_round == 98:
            super6.upgrade(['2-0-3'])
            ability(1,3)
            ninja.upgrade(['1-3-0'])
            ability(3)
            ninja.upgrade(['1-4-0'])
        elif current_round == 99:
            spike2 = Monkey('spike', 0.4317708333333, 0.3064814814815)
            ability(4,2.5)
        elif current_round == 100:
            spike2.upgrade(['0-1-0','0-2-0','0-3-0','1-3-0'])
            ability(1,6)