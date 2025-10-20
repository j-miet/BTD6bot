"""
[Hero] Sauda
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 1-3-0
tack 2-0-4

alch 3-0-0
druid 1-3-0

spike 0-0-2
engineer 1-0-0
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
            dart1 = Monkey('dart', 0.1505208333333, 0.7574074074074)
            dart2 = Monkey('dart', 0.4151041666667, 0.8796296296296)
            dart3 = Monkey('dart', 0.6942708333333, 0.9731481481481)
        elif current_round == 3:
            dart4 = Monkey('dart', 0.8057291666667, 0.4759259259259)
            dart3.target('strong')
        elif current_round == 4:
            dart1.upgrade(['0-1-0'])
            dart2.upgrade(['0-1-0'])
        elif current_round == 5:
            dart5 = Monkey('dart', 0.4151041666667, 0.8268518518519)
        elif current_round == 6:
            engi1 = Monkey('engineer', 0.1130208333333, 0.7435185185185)
        elif current_round == 9:
            Hero(0.7505208333333, 0.3138888888889)
            dart4.target('strong')
        elif current_round == 10:
            dart2.target('strong')
            dart2.upgrade(['0-2-0'])
        elif current_round == 11:
            dart2.upgrade(['0-3-0'])
        elif current_round == 13:
            engi1.upgrade(['1-0-0'])
        elif current_round == 15:
            dart4.upgrade(['1-0-0'])
        elif current_round == 18:
            spike1 = Monkey('spike', 0.0953125, 0.262037037037)
        elif current_round == 21:
            spike2 = Monkey('spike', 0.5265625, 0.4342592592593)
        elif current_round == 25:
            tack1 = Monkey('tack', 0.4692708333333, 0.8712962962963)
            tack1.upgrade(['0-0-1','0-0-2'])
        elif current_round == 26:
            tack1.upgrade(['0-0-3','1-0-3','2-0-3'])
        elif current_round == 27:
            alch1 = Monkey('alch', 0.5494791666667, 0.8231481481481)
            alch1.target('strong')
            druid = Monkey('druid', 0.1755208333333, 0.8462962962963)
            druid.upgrade(['1-0-0'])
        elif current_round == 30:
            druid.upgrade(['1-1-0','1-2-0'])
        elif current_round == 31:
            druid.upgrade(['1-3-0'])
        elif current_round == 32:
            spike1.upgrade(['0-0-1','0-0-2'])
            spike1.target('close')
        elif current_round == 33:
            spike2.upgrade(['0-0-1','0-0-2'])
        elif current_round == 35:
            alch1.upgrade(['1-0-0'])
        elif current_round == 37:
            druid.target('strong')
            dart4.upgrade(['2-0-0','3-0-0','3-1-0','3-2-0'])
            tack1.upgrade(['2-0-4'])
        elif current_round == 39:
            alch1.upgrade(['2-0-0','3-0-0'])