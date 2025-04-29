"""
[Hero] Pat
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
ice 0-3-1

sniper 1-2-0
sub 0-2-1
boat 5-0-2

ninja 1-0-5
alch 4-2-0
mermonkey 5-0-4

village 2-3-0
engineer 0-3-2
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
            sub1 = Monkey('sub', 0.5557291666667, 0.8203703703704)
            forward()
            sub2 = Monkey('sub', 0.4817708333333, 0.1407407407407)
        elif current_round == 10:
            hero = Hero(0.5411458333333, 0.6462962962963)
        elif current_round == 13:
            boat = Monkey('boat', 0.5276041666667, 0.7712962962963)
        elif current_round == 15:
            sub1.upgrade(['0-0-1'])
        elif current_round == 16:
            sub1.upgrade(['0-1-1'])
        elif current_round == 19:
            boat.upgrade(['0-0-1','0-0-2'])
        elif current_round == 20:
            boat.upgrade(['1-0-2'])
        elif current_round == 21:
            boat.upgrade(['2-0-2'])
        elif current_round == 27:
            sub1.upgrade(['0-2-1'])
        elif current_round == 31:
            ability(1,0.75)
            boat.upgrade(['3-0-2'])
        elif current_round == 36:
            mermonkey = Monkey('mermonkey', 0.5546875, 0.7157407407407)
            mermonkey.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif current_round == 37:
            mermonkey.upgrade(['3-0-1','3-0-2'])
        elif current_round == 39:
            mermonkey.upgrade(['4-0-2'])
        elif current_round == 40:
            ability(1,1.25)
        elif current_round == 45:
            boat.upgrade(['4-0-2'])
        elif current_round == 47:
            sniper1 = Monkey('sniper', 0.3088541666667, 0.7138888888889)
            sniper1.upgrade(['1-0-0','1-1-0','1-2-0'])
            sniper1.target('strong')
        elif current_round == 48:
            engi = Monkey('engineer', 0.3947916666667, 0.5694444444444)
            engi.upgrade(['0-1-0','0-2-0','0-3-0','0-3-1','0-3-2'])
            engi.special(1, 0.4755208333333, 0.7953703703704)
        elif current_round == 54:
            ability(1,2.5)
        elif current_round == 59:
            sniper1.special(1)
        elif current_round == 61:
            ability(1,2)
            boat.upgrade(['5-0-2'])
        elif current_round == 75:
            mermonkey.upgrade(['5-0-2'])
        elif current_round == 78:
            ice1 = Monkey('ice', 0.5369791666667, 0.6305555555556)
            ice1.upgrade(['0-1-0','0-2-0','0-3-0','0-3-1'])
            village = Monkey('village', 0.6088541666667, 0.712037037037)
            village.upgrade(['1-0-0','2-0-0','2-1-0'])
        elif current_round == 79:
            village.upgrade(['2-2-0'])
        elif current_round == 81:
            village.upgrade(['2-3-0'])
        elif current_round == 82:
            mermonkey2 = Monkey('mermonkey', 0.6026041666667, 0.6287037037037)
            mermonkey2.upgrade(['0-0-1','0-0-2','0-0-3'])
        elif current_round == 83:
            mermonkey2.upgrade(['0-0-4','1-0-4','2-0-4'])
            mermonkey2.special(1, 0.5546875, 0.7157407407407)
        elif current_round == 84:
            alch = Monkey('alch', 0.6109375, 0.5657407407407)
            alch.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-1-0','4-2-0'])
        elif current_round == 87:
            ninja = Monkey('ninja', 0.4890625, 0.6907407407407)
            ninja.upgrade(['1-0-0','1-0-1','1-0-2','1-0-3'])
        elif current_round == 88:
            ninja.upgrade(['1-0-4'])
            ninja.target('strong')
        elif current_round == 94:
            ability(1,5)
        elif current_round == 96:
            ability(1,15)
        elif current_round == 97:
            ability(2,4.5)
        elif current_round == 98:
            ability(1,5)
            ninja.upgrade(['1-0-5'])
        elif current_round == 100:
            ability(1,7)
