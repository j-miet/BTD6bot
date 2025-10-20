"""
[Hero] Sauda
[Monkey Knowledge] -
---------------------------------------------------------------
===Monkeys & upgrades required===
dart 1-3-1

druid 1-3-0

sniper 0-2-4

spike 0-0-2
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
            dart1 = Monkey('dart', 0.1473958333333, 0.6185185185185)
            dart2 = Monkey('dart', 0.4411458333333, 0.9)
            dart3 = Monkey('dart', 0.3515625, 0.7555555555556)
        elif current_round == 3:
            dart4 = Monkey('dart', 0.1171875, 0.45)
            dart4.upgrade(['0-1-0'])
            dart2.upgrade(['1-0-0','1-1-0'])
        elif current_round == 4:
            dart3.upgrade(['0-0-1'])
        elif current_round == 7:
            Hero(0.3880208333333, 0.7555555555556)
        elif current_round == 10:
            dart1.upgrade(['0-1-0','0-2-0','0-3-0'])
        elif current_round == 13:
            druid = Monkey('druid', 0.4036458333333, 0.1444444444444)
            druid.upgrade(['0-1-0'])
        elif current_round == 15:
            dart3.upgrade(['0-1-1','0-2-1','0-3-1'])
        elif current_round == 19:
            druid.upgrade(['0-2-0','0-3-0'])
        elif current_round == 21:
            druid.upgrade(['1-3-0'])
        elif current_round == 27:
            druid.target('strong')
            spike1 = Monkey('spike', 0.0963541666667, 0.7944444444444)
        elif current_round == 28:
            spike1.upgrade(['0-0-1','0-0-2'])
            spike1.target('close')
        elif current_round == 30:
            spike2 = Monkey('spike', 0.3078125, 0.7592592592593)
            spike2.upgrade(['0-0-1','0-0-2'])
        elif current_round == 31:
            spike2.target('smart')
            sniper = Monkey('sniper', 0.5036458333333, 0.1055555555556)
        elif current_round == 33:
            sniper.upgrade(['0-1-0','0-2-0'])
        elif current_round == 35:
            sniper.upgrade(['0-2-1','0-2-2'])
        elif current_round == 36:
            sniper.upgrade(['0-2-3'])
        elif current_round == 38:
            sniper.upgrade(['0-2-4'])