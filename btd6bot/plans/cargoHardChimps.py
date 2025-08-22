"""
[Hero] Sauda
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-3-0

sniper 2-2-5

super 3-0-2
alch 5-2-0

village 2-0-2
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
            hero = Hero(0.6255208333333, 0.3351851851852)
        elif current_round == 8:
            sniper = Monkey('sniper', 0.7151041666667, 0.3166666666667)
        elif current_round == 10:
            dart = Monkey('dart', 0.5833333333333, 0.2296296296296)
        elif current_round == 12:
            dart.upgrade(['0-1-0','0-2-0'])
        elif current_round == 13:
            dart.upgrade(['0-3-0'])
        elif current_round == 18:
            village = Monkey('village', 0.6442708333333, 0.4074074074074)
        elif current_round == 22:
            village.upgrade(['0-0-1','0-0-2'])
        elif current_round == 27:
            village.upgrade(['1-0-2'])
            sniper2 = Monkey('sniper', 0.7192708333333, 0.2648148148148) 
            sniper2.target('strong')
            sniper2.upgrade(['1-0-0'])
        elif current_round == 29:
            sniper.upgrade(['0-0-1','0-0-2'])
        elif current_round == 34:
            sniper.upgrade(['0-0-3'])
        elif current_round == 35:
            sniper.upgrade(['0-1-3','0-2-3'])
        elif current_round == 36:
            sniper2.upgrade(['1-0-1','1-0-2'])
        elif current_round == 39:
            sniper.upgrade(['0-2-4'])
            wait(4)
            click(0.6192708333333, 0.7962962962963)
            wait(0.5)
            click(0.6755208333333, 0.8611111111111)
        elif current_round == 40:
            ability(1,1)
        elif current_round == 41:
            alch = Monkey('alch', 0.7182291666667, 0.4314814814815)
            alch.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif current_round == 42:
            alch.upgrade(['3-1-0','3-2-0'])
        elif current_round == 43:
            village.upgrade(['2-0-2'])
        elif current_round == 50:
            sniper.upgrade(['0-2-5'])
        elif current_round == 52:
            super = Monkey('super', 0.6161458333333, 0.4962962962963)
        elif current_round == 55:
            super.upgrade(['1-0-0','2-0-0'])
        elif current_round == 59:
            ability(2,6.5)
        elif current_round == 63:
            ability(2,7)
        elif current_round == 66:
            super.upgrade(['3-0-0'])
        elif current_round == 68:
            super.upgrade(['3-0-1','3-0-2'])
        elif current_round == 70:
            alch.upgrade(['4-2-0'])
        elif current_round == 85:
            alch.upgrade(['5-2-0'])
        elif current_round == 92:
            super2 = Monkey('super', 0.6307291666667, 0.5907407407407)
            super2.upgrade(['1-0-0','2-0-0'])
        elif current_round == 94:
            super2.upgrade(['3-0-0','3-0-1','3-0-2'])
        elif current_round == 96:
            sniper2.upgrade(['2-0-2','2-0-3','2-0-4'])
            sniper3 = Monkey('sniper', 0.6916666666667, 0.2268518518519)
        elif current_round == 98:
            sniper3.upgrade(['0-0-1','0-0-2','0-0-3','1-0-3','2-0-3','2-0-4'])
            sniper4 = Monkey('sniper', 0.7177083333333, 0.525)
            sniper4.upgrade(['0-0-1','0-0-2','0-0-3','1-0-3','2-0-3'])
        elif current_round == 99:
            sniper4.upgrade(['2-0-4'])