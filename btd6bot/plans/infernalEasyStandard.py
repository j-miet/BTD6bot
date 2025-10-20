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

def play(rounds):
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start, rounds[2])
        if current_round == BEGIN:     
            sniper1 = Monkey('sniper', 0.6234375, 0.7361111111111)
            sniper2 = Monkey('sniper', 0.6484375, 0.7824074074074)
        elif current_round == 3:
            sniper2.target('strong')
        elif current_round == 4:
            sniper3 = Monkey('sniper', 0.6078125, 0.7898148148148)
        elif current_round == 10:
            heli = Monkey('heli', 0.8151041666667, 0.512037037037)    
            heli.special(1, 0.4411458333333, 0.5527777777778)
        elif current_round == 13:
            heli.upgrade(['1-0-0'])
        elif current_round == 15:
            heli.upgrade(['2-0-0'])
        elif current_round == 21:
            heli.upgrade(['3-0-0'])
        elif current_round == 22:
            sniper1.upgrade(['0-1-0'])
        elif current_round == 25:
            heli.upgrade(['3-0-1','3-0-2'])
        elif current_round == 28:
            sniper1.upgrade(['0-2-0','0-2-1','0-2-2'])
        elif current_round == 33:
            sniper1.upgrade(['0-2-3'])
        elif current_round == 34:
            alch = Monkey('alch', 0.8317708333333, 0.4277777777778)
        elif current_round == 36:
            alch.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif current_round == 39:
            sniper1.upgrade(['0-2-4'])