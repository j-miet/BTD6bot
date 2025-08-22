"""
[Hero] Striker
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0
bomb 0-5-1
glue 0-2-3

sniper 0-1-0
mortar 4-5-5

druid 1-3-0

village 2-2-0
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
            dart1 = Monkey('dart', 0.828125, 0.2481481481481)
            sniper1 = Monkey('sniper', 0.6005208333333, 0.6638888888889)
            sniper1.target('strong')
        elif current_round == 8:
            sniper2 = Monkey('sniper', 0.6348958333333, 0.7175925925926)
        elif current_round == 10:
            druid = Monkey('druid', 0.5338541666667, 0.3009259259259)
        elif current_round == 13:
            Hero(0.4713541666667, 0.2842592592593)
        elif current_round == 14:
            druid.upgrade(['0-1-0'])
        elif current_round == 20:
            druid.upgrade(['0-2-0','0-3-0'])
        elif current_round == 22:
            sniper1.upgrade(['0-1-0'])
        elif current_round == 24:
            druid.upgrade(['1-3-0'])
        elif current_round == 27:
            mortar1 = Monkey('mortar', 0.6744791666667, 0.1416666666667)
            mortar1.special(1, 0.4994791666667, 0.4805555555556)
        elif current_round == 31:
            mortar1.upgrade(['0-0-1','0-0-2','0-0-3'])
        elif current_round == 35:
            mortar2 = Monkey('mortar', 0.6119791666667, 0.0935185185185)
            mortar2.special(1, 0.4546875, 0.4935185185185)
            mortar2.upgrade(['0-1-0','0-2-0','0-3-0','1-3-0'])
        elif current_round == 36:
            mortar2.upgrade(['2-3-0'])
        elif current_round == 37:
            mortar3 = Monkey('mortar', 0.5536458333333, 0.0472222222222)
            mortar3.special(1, 0.4546875, 0.4935185185185)
            mortar3.upgrade(['1-0-0','2-0-0'])
        elif current_round == 39:
            bomb = Monkey('bomb', 0.4526041666667, 0.2268518518519)
            bomb.target('strong')
            bomb.upgrade(['0-1-0','0-2-0','0-3-0','0-3-1'])
        elif current_round == 40:
            mortar3.upgrade(['3-0-0'])
            ability(1,2)
        elif current_round == 41:
            mortar3.upgrade(['3-1-0','3-2-0'])
            mortar1.upgrade(['0-1-3','0-2-3'])
        elif current_round == 46:
            mortar2.upgrade(['2-4-0'])
        elif current_round == 49:
            mortar3.upgrade(['4-2-0'])
        elif current_round == 50:
            village = Monkey('village', 0.5630208333333, 0.2175925925926)
            village.upgrade(['0-1-0','0-2-0'])
        elif current_round == 51:
            village.upgrade(['1-2-0','2-2-0'])
        elif current_round == 75:
            mortar2.upgrade(['2-5-0'])
        elif current_round == 79:
            mortar1.upgrade(['0-2-4'])
        elif current_round == 80:
            ability(4,12)
        elif current_round == 85:
            ability(4,14)
        elif current_round == 87:
            ability(4,14)
            ability(3)
        elif current_round == 88:
            ability(4,14)
        elif current_round == 91:
            mortar1.upgrade(['0-2-5'])
        elif current_round == 92:
            glue = Monkey('glue', 0.5994791666667, 0.2675925925926)
            glue.target('strong')
            glue.upgrade(['0-0-1','0-0-2','0-0-3'])
        elif current_round == 93:
            glue.upgrade(['0-1-3','0-2-3'])
        elif current_round == 94:
            bomb.upgrade(['0-4-1'])
        elif current_round == 98:
            ability(4,14)
        elif current_round == 99:
            bomb.upgrade(['0-5-1'])
            ability(1,3)
        elif current_round == 100:
            ability(5,1)
            ability(5,5)
            ability(5,9)
            ability(5,13)
            ability(4,14)