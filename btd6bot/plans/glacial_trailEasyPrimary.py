"""
[Hero] Silas
[Monkey Knowledge] -
-------------------------------------------------------------
ice 4-2-4
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
            ice1 = Monkey('ice', 0.1317708333333, 0.5092592592593)
            ice1.upgrade(['0-1-0','0-1-1'])
        elif current_round == 4:
            bomb = Monkey('bomb', 0.7213541666667, 0.6277777777778)
        elif current_round == 8:
            hero = Hero(0.1661458333333, 0.5)
        elif current_round == 10:
            ice2 = Monkey('ice', 0.1078125, 0.3759259259259)
        elif current_round == 11:
            ice1.upgrade(['0-1-2'])
        elif current_round == 17:
            ice1.upgrade(['0-1-3'])
        elif current_round == 18:
            ice1.upgrade(['0-2-3'])
        elif current_round == 21:
            ice2.upgrade(['1-0-0','2-0-0','2-1-0'])
        elif current_round == 27:
            ice2.upgrade(['3-1-0'])
        elif current_round == 31:
            ice1.upgrade(['0-2-4'])
        elif current_round == 35:
            ice2.upgrade(['4-1-0'])
        elif current_round == 40:
            ability(1)
            ability(2)