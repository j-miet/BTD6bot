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

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:     
            desp1 = Monkey('desperado', 0.3348958333333, 0.4833333333333)
            desp2 = Monkey('desperado', 0.5098958333333, 0.5611111111111)
            desp2.target('strong')
        elif round == 2:
            desp3 = Monkey('desperado', 0.3963541666667, 0.4055555555556)
            desp3.target('strong')
        elif round == 4:
            wizard = Monkey('wizard', 0.4380208333333, 0.5666666666667)
            wizard.target('strong')
        elif round == 6:
            sniper1 = Monkey('sniper', 0.2390625, 0.8583333333333)
            sniper1.target('strong')
        elif round == 8:
            sniper2 = Monkey('sniper', 0.2817708333333, 0.8157407407407)
            sniper2.upgrade(['0-1-0'])
        elif round == 10:
            sniper2.upgrade(['0-1-1'])
        elif round == 14:
            sniper2.upgrade(['0-1-2','0-2-2'])
        elif round == 16:
            sniper1.upgrade(['0-0-1','0-0-2'])
        elif round == 18:
            sniper1.upgrade(['1-0-2'])
        elif round == 21:
            wizard.upgrade(['1-0-0','1-0-1','2-0-1'])
            wizard.target('first')
        elif round == 27:
            wizard.upgrade(['3-0-1','3-0-2'])
        elif round == 32:
            sniper2.upgrade(['0-2-3'])
        elif round == 36:
            sniper2.upgrade(['0-2-4'])
        elif round == 39:
            sniper1.upgrade(['1-0-3','2-0-3'])