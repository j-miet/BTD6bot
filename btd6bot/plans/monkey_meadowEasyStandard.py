"""
[Plan Name] monkey_meadowEasyStandard
[Game Version] 45
[Hero] Quincy
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys required===
ninja 4-0-1
alch 3-2-0
sniper 2-0-4
_______________________________________
"""

from._plan_imports import *

def play(rounds: tuple[str, str, str, int, int, str]) -> None:
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start, rounds[2])
        if current_round == BEGIN:
            hero = Hero(0.14, 0.35)
            hero.target('strong')
        elif current_round == 2:
            ninja1 = Monkey('ninja', 0.19529, 0.48333)
        elif current_round == 4: 
            ninja1.upgrade(['1-0-0'])
        elif current_round == 8:
            ninja1.upgrade(['2-0-0'])
            alch1 = Monkey('alch', 0.24277, 0.48333)
        elif current_round == 10:
            ninja1.upgrade(['2-0-1'])
        elif current_round == 15:
            ninja1.upgrade(['3-0-1'])
        elif current_round == 17:
            alch1.upgrade(['1-0-0', '2-0-0'])
        elif current_round == 25:
            alch1.upgrade(['3-0-0'])
        elif current_round == 30:
            ninja1.upgrade(['4-0-1'])
        elif current_round == 35:
            alch1.upgrade(['3-1-0', '3-2-0'])
        elif current_round == 38:
            sniper1 = Monkey('sniper', 0.76094, 0.30463)
            sniper1.target('strong')
            sniper1.upgrade(['1-0-0', '2-0-0', '2-0-1', '2-0-2', '2-0-3'])
        elif current_round == END:
            sniper1.upgrade(['2-0-4'])