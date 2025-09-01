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

def play(rounds: tuple[str, str, str, int, int, str]) -> None:
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start)
        if current_round == BEGIN:
            sub1 = Monkey('sub', 0.7510416667, 0.4601851852)
            dart1 = Monkey('dart', 0.1442708333, 0.5277777778)
        elif current_round == 8:
            boat1 = Monkey('boat', 0.7197916667, 0.5842592593)
        elif current_round == 11:
            hero = Hero(0.6479166667, 0.5407407407)
            hero.target('strong')
        elif current_round == 12:
            boat1.upgrade(['1-0-0'])
        elif current_round == 14:
            boat1.upgrade(['2-0-0'])
        elif current_round == 15:
            boat1.upgrade(['2-0-1'])
        elif current_round == 17:
            sub1.upgrade(['0-0-1'])
        elif current_round == 21:
            sub1.upgrade(['0-0-2'])
        elif current_round == 23:
            boat1.upgrade(['2-0-2'])
        elif current_round == 32:
            boat1.upgrade(['3-0-2'])
        elif current_round == 34:
            sub1.upgrade(['0-0-3'])
        elif current_round == 37:
            sub1.upgrade(['0-0-4'])
        elif current_round == 43:
            boat1.upgrade(['4-0-2'])
            sub1.upgrade(['1-0-4'])
        elif current_round == 44:
            sub1.upgrade(['2-0-4'])
        elif current_round == 45:
            village1 = Monkey('village', 0.6671875000, 0.3925925926)
            village1.upgrade(['0-1-0'])
        elif current_round == 46:
            village1.upgrade(['0-2-0'])
        elif current_round == 59:
            boat1.upgrade(['5-0-2'])
            village1.upgrade(['1-2-0'])
        elif current_round == 60:
            village1.upgrade(['2-2-0'])
        elif current_round == 61:
            village1.upgrade(['3-2-0'])
        elif current_round == 63:
            village1.upgrade(['4-2-0'])
            bomb1 = Monkey('bomb', 0.7192708333, 0.4500000000)
            bomb1.upgrade(['1-0-0','2-0-0','2-1-0','2-2-0'])            
        elif current_round == 64:
            bomb1.upgrade(['3-2-0'])
        elif current_round == 65:
            bomb1.upgrade(['4-2-0'])
        elif current_round == 86:
            bomb1.upgrade(['5-2-0'])
            bomb2 = Monkey('bomb', 0.6750000000, 0.4981481481)
        elif current_round == 87:
            bomb2.upgrade(['0-0-1','0-0-2','1-0-2','2-0-2'])
        elif current_round == 89:
            bomb2.upgrade(['2-0-3','2-0-4'])
        elif current_round == 95:
            bomb2.upgrade(['2-0-5'])
