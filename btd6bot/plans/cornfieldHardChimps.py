"""
[Hero] Sauda
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 5-0-2

wizard 5-2-0
alch 5-2-1

spike 2-0-5
village 2-0-2
_______________________________________
'No Harvest' achievement can be obtained as no corn is removed
"""

from._plan_imports import *

def play(rounds: tuple[str, str, str, int, int, str]) -> None:
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start)
        if current_round == BEGIN:     
            hero = Hero(0.4067708333333, 0.4537037037037)
        elif current_round == 8:
            dart = Monkey('dart', 0.378125, 0.9175925925926)
            dart.target('last')
        elif current_round == 9:
            dart.upgrade(['1-0-0','2-0-0'])
        elif current_round == 11:
            dart.upgrade(['3-0-0'])
        elif current_round == 14:
            ability(1,9)
        elif current_round == 19:
            ability(1,4)
        elif current_round == 20:
            village = Monkey('village', 0.4588541666667, 0.4555555555556)
            village.upgrade(['0-0-1','0-0-2'])
        elif current_round == 21:
            wizard = Monkey('wizard', 0.3921875, 0.5759259259259)
        elif current_round == 25:
            spike = Monkey('spike', 0.4692708333333, 0.5888888888889)
        elif current_round == 27:
            wizard.upgrade(['0-1-0','0-2-0'])
        elif current_round == 29:
            spike.upgrade(['0-0-1','0-0-2'])
            spike.target('smart')
        elif current_round == 31:
            wizard.upgrade(['1-2-0','2-2-0'])
        elif current_round == 33:
            wizard.upgrade(['3-2-0'])
            wizard.special(1, 0.3661458333333, 0.4027777777778)
        elif current_round == 35:
            spike.upgrade(['0-0-3'])
        elif current_round == 38:
            spike.upgrade(['0-0-4'])
        elif current_round == 39:
            spike.upgrade(['1-0-4'])
            alch = Monkey('alch', 0.3921875, 0.5148148148148)
            alch.upgrade(['1-0-0','2-0-0'])
        elif current_round == 41:
            alch.upgrade(['3-0-0'])
        elif current_round == 48:
            wizard.upgrade(['4-2-0'])
        elif current_round == 50:
            dart.upgrade(['4-0-0','4-0-1','4-0-2'])
        elif current_round == 54:
            alch2 = Monkey('alch', 0.4692708333333, 0.5277777777778)
            alch2.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif current_round == 63:
            ability(1,7.5)
            ability(2,13.5)
        elif current_round == 70:
            wizard.upgrade(['5-2-0'])
            village.upgrade(['2-0-2'])
        elif current_round == 76:
            ability(2,1)
        elif current_round == 82:
            spike.upgrade(['1-0-5', '2-0-5'])
            alch2.upgrade(['3-0-1'])
        elif current_round == 83:
            alch.upgrade(['4-0-0','4-1-0','4-2-0'])
        elif current_round == 87:
            dart.upgrade(['5-0-2'])
        elif current_round == 98:
            alch.upgrade(['5-2-0'])