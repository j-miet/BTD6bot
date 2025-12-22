"""
[Hero] -
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
desperado 0-0-0

sniper 2-2-4

wizard 3-0-2
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
            desp1 = Monkey('desperado', 0.3348958333333, 0.4833333333333)
            desp2 = Monkey('desperado', 0.5098958333333, 0.5611111111111)
            desp2.target('strong')
        elif current_round == 2:
            desp3 = Monkey('desperado', 0.3963541666667, 0.4055555555556)
            desp3.target('strong')
        elif current_round == 4:
            wizard = Monkey('wizard', 0.4380208333333, 0.5666666666667)
            wizard.target('strong')
        elif current_round == 6:
            sniper1 = Monkey('sniper', 0.2390625, 0.8583333333333)
            sniper1.target('strong')
        elif current_round == 8:
            sniper2 = Monkey('sniper', 0.2817708333333, 0.8157407407407)
            sniper2.upgrade(['0-1-0'])
        elif current_round == 10:
            sniper2.upgrade(['0-1-1'])
        elif current_round == 14:
            sniper2.upgrade(['0-1-2','0-2-2'])
        elif current_round == 16:
            sniper1.upgrade(['0-0-1','0-0-2'])
        elif current_round == 18:
            sniper1.upgrade(['1-0-2'])
        elif current_round == 21:
            wizard.upgrade(['1-0-0','1-0-1','2-0-1'])
            wizard.target('first')
        elif current_round == 27:
            wizard.upgrade(['3-0-1','3-0-2'])
        elif current_round == 32:
            sniper2.upgrade(['0-2-3'])
        elif current_round == 36:
            sniper2.upgrade(['0-2-4'])
        elif current_round == 39:
            sniper1.upgrade(['1-0-3','2-0-3'])