"""
[Hero] Silas
[Monkey Knowledge] -
-------------------------------------------------------------
ice 4-2-4
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
            ice1 = Monkey('ice', 0.1317708333333, 0.5092592592593)
            ice1.upgrade(['0-1-0','0-1-1'])
        elif round == 4:
            bomb = Monkey('bomb', 0.7213541666667, 0.6277777777778)
        elif round == 8:
            hero = Hero(0.1661458333333, 0.5)
        elif round == 10:
            ice2 = Monkey('ice', 0.1078125, 0.3759259259259)
        elif round == 11:
            ice1.upgrade(['0-1-2'])
        elif round == 17:
            ice1.upgrade(['0-1-3'])
        elif round == 18:
            ice1.upgrade(['0-2-3'])
        elif round == 21:
            ice2.upgrade(['1-0-0','2-0-0','2-1-0'])
        elif round == 27:
            ice2.upgrade(['3-1-0'])
        elif round == 31:
            ice1.upgrade(['0-2-4'])
        elif round == 35:
            ice2.upgrade(['4-1-0'])
        elif round == 40:
            ability(1)
            ability(2)