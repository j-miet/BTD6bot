"""
[Hero] Psi
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-3-2
glue 0-5-2

sub 2-5-0
heli 5-0-2

alch 4-2-0

village 2-3-0
_______________________________________
"""

from._plan_imports import *

def play(rounds):
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start, rounds[2])
        if current_round == BEGIN:
            dart1 = Monkey('dart', 0.3026041666667, 0.3231481481481) 
            dart2 = Monkey('dart', 0.5473958333333, 0.3194444444444)
            dart3 = Monkey('dart', 0.8192708333333, 0.4138888888889)
        elif current_round == 8:
            dart2.upgrade(['0-1-0','0-2-0'])
        elif current_round == 10:
            dart2.upgrade(['0-3-0'])
        elif current_round == 15:
            hero = Hero(0.7244791666667, 0.3175925925926)
            hero.target('strong')
        elif current_round == 21:
            hero.target('first')
            heli = Monkey('heli', 0.7223958333333, 0.0787037037037)
            heli.special(1, 0.2484375, 0.4138888888889)
        elif current_round == 23:
            hero.target('strong')
        elif current_round == 25:
            heli.upgrade(['1-0-0'])
        elif current_round == 26:
            sub = Monkey('sub', 0.6817708333333, 0.2768518518519)
        elif current_round == 27:
            sub.upgrade(['0-1-0','0-2-0'])
        elif current_round == 28:
            heli.upgrade(['2-0-0'])
        elif current_round == 31:
            dart2.upgrade(['0-3-1','0-3-2'])
        elif current_round == 34:
            heli.upgrade(['3-0-0'])
        elif current_round == 35:
            heli.upgrade(['3-0-1','3-0-2'])
        elif current_round == 37:
            alch = Monkey('alch', 0.7890625, 0.0731481481481)
            alch.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif current_round == 41:
            village = Monkey('village', 0.7651041666667, 0.2157407407407)
            village.upgrade(['0-1-0','0-2-0'])
        elif current_round == 43:
            village.upgrade(['1-2-0','2-2-0'])
        elif current_round == 52:
            heli.upgrade(['4-0-2'])
        elif current_round == 53:
            alch.upgrade(['3-1-0','3-2-0'])
        elif current_round == 79:
            heli.upgrade(['5-0-2'])
        elif current_round == 81:
            village.upgrade(['2-3-0'])
            alch.upgrade(['4-2-0'])
        elif current_round == 94:
            sub.upgrade(['0-3-0','0-4-0'])
        elif current_round == 95:
            sub.upgrade(['0-5-0','1-5-0','2-5-0'])
        elif current_round == 96:
            glue = Monkey('glue', 0.7723958333333, 0.3166666666667)
            glue.upgrade(['0-1-0','0-2-0','0-3-0','0-4-0'])
        elif current_round == 98:
            ability(2,10)
            glue.upgrade(['0-5-0','0-5-1','0-5-2'])
        elif current_round == 99:
            ability(4,2)
        elif current_round == 100:
            ability(3,2)