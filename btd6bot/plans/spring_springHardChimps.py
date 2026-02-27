"""
[Hero] Striker
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
bomb 5-2-5

sub 2-0-4
boat 5-0-2

village 4-2-0
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
            sub1 = Monkey('sub', 0.7510416667, 0.4601851852)
            dart1 = Monkey('dart', 0.1442708333, 0.5277777778)
        elif round == 8:
            boat1 = Monkey('boat', 0.7197916667, 0.5842592593)
        elif round == 11:
            hero = Hero(0.6479166667, 0.5407407407)
            hero.target('strong')
        elif round == 12:
            boat1.upgrade(['1-0-0'])
        elif round == 14:
            boat1.upgrade(['2-0-0'])
        elif round == 15:
            boat1.upgrade(['2-0-1'])
        elif round == 17:
            sub1.upgrade(['0-0-1'])
        elif round == 21:
            sub1.upgrade(['0-0-2'])
        elif round == 23:
            boat1.upgrade(['2-0-2'])
        elif round == 32:
            boat1.upgrade(['3-0-2'])
        elif round == 34:
            sub1.upgrade(['0-0-3'])
        elif round == 37:
            sub1.upgrade(['0-0-4'])
        elif round == 43:
            boat1.upgrade(['4-0-2'])
            sub1.upgrade(['1-0-4'])
        elif round == 44:
            sub1.upgrade(['2-0-4'])
        elif round == 45:
            village1 = Monkey('village', 0.6671875000, 0.3925925926)
            village1.upgrade(['0-1-0'])
        elif round == 46:
            village1.upgrade(['0-2-0'])
        elif round == 59:
            boat1.upgrade(['5-0-2'])
            village1.upgrade(['1-2-0'])
        elif round == 60:
            village1.upgrade(['2-2-0'])
        elif round == 61:
            village1.upgrade(['3-2-0'])
        elif round == 63:
            village1.upgrade(['4-2-0'])
            bomb1 = Monkey('bomb', 0.7192708333, 0.4500000000)
            bomb1.upgrade(['1-0-0','2-0-0','2-1-0','2-2-0'])            
        elif round == 64:
            bomb1.upgrade(['3-2-0'])
        elif round == 65:
            bomb1.upgrade(['4-2-0'])
        elif round == 86:
            bomb1.upgrade(['5-2-0'])
            bomb2 = Monkey('bomb', 0.6750000000, 0.4981481481)
        elif round == 87:
            bomb2.upgrade(['0-0-1','0-0-2','1-0-2','2-0-2'])
        elif round == 89:
            bomb2.upgrade(['2-0-3','2-0-4'])
        elif round == 95:
            bomb2.upgrade(['2-0-5'])
