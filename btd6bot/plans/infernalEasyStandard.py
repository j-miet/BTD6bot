"""
[Hero] -
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
sniper 0-2-4
heli 3-0-2
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
            sniper1 = Monkey('sniper', 0.6234375, 0.7361111111111)
            sniper2 = Monkey('sniper', 0.6484375, 0.7824074074074)
        elif round == 3:
            sniper2.target('strong')
        elif round == 4:
            sniper3 = Monkey('sniper', 0.6078125, 0.7898148148148)
        elif round == 10:
            heli = Monkey('heli', 0.8151041666667, 0.512037037037)    
            heli.special(1, 0.4411458333333, 0.5527777777778)
        elif round == 13:
            heli.upgrade(['1-0-0'])
        elif round == 15:
            heli.upgrade(['2-0-0'])
        elif round == 21:
            heli.upgrade(['3-0-0'])
        elif round == 22:
            sniper1.upgrade(['0-1-0'])
        elif round == 25:
            heli.upgrade(['3-0-1','3-0-2'])
        elif round == 28:
            sniper1.upgrade(['0-2-0','0-2-1','0-2-2'])
        elif round == 33:
            sniper1.upgrade(['0-2-3'])
        elif round == 34:
            alch = Monkey('alch', 0.8317708333333, 0.4277777777778)
        elif round == 36:
            alch.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif round == 39:
            sniper1.upgrade(['0-2-4'])