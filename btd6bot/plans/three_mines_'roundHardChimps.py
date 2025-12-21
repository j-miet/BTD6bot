"""
[Hero] Sauda
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
desperado 0-2-4

druid 2-5-0

village 2-3-0
beast 0-5-0
_______________________________________
Beast handler test plan.
"""

from._plan_imports import *

def play(rounds):
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start, rounds[2])
        if current_round == BEGIN:     
            hero = Monkey('hero', 0.3911458333333, 0.2148148148148)
        elif current_round == 8:
            beast1 = Monkey('beast', 0.3536458333333, 0.5185185185185)
        elif current_round == 9:
            beast1.upgrade(['0-1-0'])
            beast1.special(2, 0.3255208333333, 0.2981481481481)
        elif current_round == 13:
            beast1.upgrade(['0-2-0'])
            beast1.target('strong')
        elif current_round == 15:
            click(0.4151041666667, 0.8037037037037)
            wait(1)
            click(0.4796875, 0.8907407407407)
        elif current_round == 17:
            druid = Monkey('druid', 0.4505208333333, 0.3055555555556)
        elif current_round == 25:
            click(0.1213541666667, 0.5518518518519)
            wait(1)
            click(0.2369791666667, 0.6240740740741)
        elif current_round == 26:
            druid.upgrade(['1-0-0','1-1-0'])
        elif current_round == 30:
            druid.upgrade(['1-2-0','1-3-0'])
        elif current_round == 35:
            village = Monkey('village', 0.4432291666667, 0.3925925925926)
            village.upgrade(['0-1-0','0-2-0','1-2-0','2-2-0'])
        elif current_round == 36:
            beast1.upgrade(['0-3-0'])
        elif current_round == 39:
            desperado = Monkey('desperado', 0.4192708333333, 0.4851851851852)
            desperado.upgrade(['0-0-1','0-0-2','0-0-3','0-1-3','0-2-3'])
        elif current_round == 47:
            click(0.5609375, 0.6037037037037)
            wait(1)
            click(0.6130208333333, 0.6814814814815) 
        elif current_round == 50:
            beast1.upgrade(['0-4-0'])
        elif current_round == 57:
            click(0.4942708333333, 0.1666666666667)
            wait(1)
            click(0.5619791666667, 0.2537037037037)
        elif current_round == 60:
            druid.upgrade(['1-4-0'])
        elif current_round == 67:
            click(0.3859375, 0.3555555555556)
            wait(1)
            click(0.4453125, 0.4574074074074)
        elif current_round == 71:
            desperado.upgrade(['0-2-4'])
        elif current_round == 77:
            druid.upgrade(['1-5-0','2-5-0'])
            beast2 = Monkey('beast', 0.5140625, 0.337037037037)
            beast3 = Monkey('beast', 0.5463541666667, 0.3925925925926)
            beast4 = Monkey('beast', 0.5015625, 0.4351851851852)
        elif current_round == 78:
            beast2.upgrade(['0-1-0','0-2-0','0-3-0','0-4-0'])
            beast2.merge(0.3536458333333, 0.5185185185185)
        elif current_round == 79:
            beast3.upgrade(['0-1-0','0-2-0','0-3-0','0-4-0'])
            beast3.merge(0.3536458333333, 0.5185185185185)
        elif current_round == 81:
            beast4.upgrade(['0-1-0','0-2-0','0-3-0','0-4-0'])
            beast4.merge(0.3536458333333, 0.5185185185185)
        elif current_round == 89:
            village.upgrade(['2-3-0'])
        elif current_round == 95:
            beast1.upgrade(['0-5-0'])