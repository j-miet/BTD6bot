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
No corn is removed which unlocks 'No Harvest' achievement.
"""

from._plan_imports import *

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:     
            hero = Hero(0.4067708333333, 0.4537037037037)
        elif round == 8:
            dart = Monkey('dart', 0.378125, 0.9175925925926)
            dart.target('last')
        elif round == 9:
            dart.upgrade(['1-0-0','2-0-0'])
        elif round == 11:
            dart.upgrade(['3-0-0'])
        elif round == 14:
            ability(1,9)
        elif round == 19:
            ability(1,4)
        elif round == 20:
            village = Monkey('village', 0.4588541666667, 0.4555555555556)
            village.upgrade(['0-0-1','0-0-2'])
        elif round == 21:
            wizard = Monkey('wizard', 0.3921875, 0.5759259259259)
        elif round == 25:
            spike = Monkey('spike', 0.4692708333333, 0.5888888888889)
        elif round == 27:
            wizard.upgrade(['0-1-0','0-2-0'])
        elif round == 29:
            spike.upgrade(['0-0-1','0-0-2'])
            spike.target('smart')
        elif round == 31:
            wizard.upgrade(['1-2-0','2-2-0'])
        elif round == 33:
            wizard.upgrade(['3-2-0'])
            wizard.special(1, 0.3661458333333, 0.4027777777778)
        elif round == 35:
            spike.upgrade(['0-0-3'])
        elif round == 38:
            spike.upgrade(['0-0-4'])
        elif round == 39:
            spike.upgrade(['1-0-4'])
            alch = Monkey('alch', 0.3921875, 0.5148148148148)
            alch.upgrade(['1-0-0','2-0-0'])
        elif round == 41:
            alch.upgrade(['3-0-0'])
        elif round == 48:
            wizard.upgrade(['4-2-0'])
        elif round == 50:
            dart.upgrade(['4-0-0','4-0-1','4-0-2'])
        elif round == 54:
            alch2 = Monkey('alch', 0.4692708333333, 0.5277777777778)
            alch2.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif round == 63:
            ability(1,7.5)
            ability(2,13.5)
        elif round == 70:
            wizard.upgrade(['5-2-0'])
            village.upgrade(['2-0-2'])
        elif round == 76:
            ability(2,1)
        elif round == 82:
            spike.upgrade(['1-0-5', '2-0-5'])
            alch2.upgrade(['3-0-1'])
        elif round == 83:
            alch.upgrade(['4-0-0','4-1-0','4-2-0'])
        elif round == 87:
            dart.upgrade(['5-0-2'])
        elif round == 98:
            alch.upgrade(['5-2-0'])