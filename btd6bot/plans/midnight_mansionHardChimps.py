"""
[Hero] Ezili
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0
ice 4-1-0
glue 0-2-4

sniper 1-3-2

wizard 0-2-5
ninja 1-4-5
alch 3-0-0
druid 1-5-0

village 3-0-2
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
            dart1 = Monkey('dart', 0.7151041666667, 0.2490740740741)
            dart2 = Monkey('dart', 0.1515625, 0.2546296296296)
            dart3 = Monkey('dart', 0.1536458333333, 0.3064814814815)
        elif current_round == 8:
            dart4 = Monkey('dart', 0.7140625, 0.3009259259259)
        elif current_round == 10:
            hero = Hero(0.6380208333333, 0.1768518518519)
            hero.target('strong')
        elif current_round == 13:
            click(0.1953125, 0.1324074074074)
            click(0.240625, 0.2416666666667)
            wait(1)
            sniper1 = Monkey('sniper', 0.1953125, 0.1324074074074)
        elif current_round == 15:
            sniper2 = Monkey('sniper', 0.1598958333333, 0.1324074074074)
            sniper2.target('strong')
        elif current_round == 16:
            sniper3 = Monkey('sniper', 0.1786458333333, 0.0861111111111)
            sniper3.target('strong')
        elif current_round == 18:
            sniper2.upgrade(['1-0-0'])
        elif current_round == 21:
            wizard1 = Monkey('wizard', 0.6734375, 0.2527777777778)
            wizard1.upgrade(['0-1-0'])
        elif current_round == 23:
            wizard1.upgrade(['0-2-0'])
        elif current_round == 25:
            ability(1, 6)
        elif current_round == 27:
            sniper1.upgrade(['0-1-0','0-2-0','0-2-1'])
        elif current_round == 28:
            sniper1.upgrade(['0-2-2'])
        elif current_round == 34:
            sniper1.upgrade(['0-3-2'])
        elif current_round == 37:
            wizard1.upgrade(['0-3-0','0-3-1','0-3-2'])
        elif current_round == 39:
            alch = Monkey('alch', 0.2984375, 0.1842592592593)
            change_autostart()
            wait(13)
            alch.upgrade(['1-0-0','2-0-0','3-0-0'])
            change_autostart()
            end_round()
        elif current_round == 41:
            click(0.6859375, 0.1157407407407)
            click(0.7463541666667, 0.2416666666667)
        elif current_round == 42:
            village = Monkey('village', 0.6859375, 0.1157407407407)
            village.upgrade(['0-0-1','0-0-2'])
        elif current_round == 43:
            wizard2 = Monkey('wizard', 0.6338541666667, 0.2490740740741)
            wizard2.upgrade(['0-1-0','0-2-0'])
        elif current_round == 44:
            wizard2.upgrade(['0-2-1','0-2-2'])
        elif current_round == 45:
            wizard2.upgrade(['0-2-3'])
        elif current_round == 46:
            wizard2.upgrade(['0-2-4'])
        elif current_round == 60:
            wizard2.upgrade(['0-2-5'])
            ability(3,3)
        elif current_round == 61:
            village.upgrade(['1-0-2','2-0-2'])
        elif current_round == 63:
            druid = Monkey('druid', 0.5953125, 0.2601851851852)
            druid.upgrade(['1-0-0','1-1-0','1-2-0','1-3-0'])
        elif current_round == 65:
            druid.upgrade(['1-4-0'])
        elif current_round == 80:
            ability(3,2)
        elif current_round == 81:
            druid.upgrade(['1-5-0'])
            glue = Monkey('glue', 0.6015625, 0.1842592592593)
            glue.target('strong')
            glue.upgrade(['0-1-0','0-2-0'])
        elif current_round == 83:
            glue.upgrade(['0-2-1','0-2-2','0-2-3','0-2-4'])
        elif current_round == 84:
            ninja1 = Monkey('ninja', 0.5630208333333, 0.1805555555556)
            ninja1.upgrade(['1-0-0','1-0-1','1-0-2','1-0-3'])
        elif current_round == 85:
            ability(3,5.5)
        elif current_round == 87:
            ninja1.upgrade(['1-0-4'])
            ability(3,3.5)
        elif current_round == 92:
            ability(3,6.5)
        elif current_round == 94:
            ability(3,3)
        elif current_round == 96:
            ability(3,11)
        elif current_round == 97:
            ninja1.upgrade(['1-0-5'])
            ninja2 = Monkey('ninja', 0.5796875, 0.1314814814815)
            ninja2.upgrade(['0-1-0','0-2-0','0-3-0'])
        elif current_round == 98:
            ability(3,6)
            ninja2.upgrade(['0-4-0'])
            ice = Monkey('ice', 0.6140625, 0.1324074074074)
            ice.upgrade(['0-1-0','1-1-0','2-1-0','3-1-0'])
        elif current_round == 99:
            ice.upgrade(['4-1-0'])
            ability(4,2)
            village.upgrade(['3-0-2'])
        elif current_round == 100:
            ability(3,8)
