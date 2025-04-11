"""
[Plan Name] infernalHardChimps
[Game Version] 48
[Hero] Quincy
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0
sniper 4-2-0
sub 2-0-2
alch 3-2-0
super 0-5-2
glue 0-2-4
mermonkey 2-0-4
spike 1-4-0
_______________________________________
Strategy: https://www.youtube.com/watch?v=vXuRW2ItaJI

-Very reliant on ability usage, but should have minimal rng nontheless.

-In original, round 99 absolutely requires anti-bloon ability. This has been replaced with a x-x-4 mermonkey as that can grab ddts.
"""

from._plan_imports import *

def play(rounds: tuple[str, str, str, int, int, str]) -> None:
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start)
        if current_round == BEGIN:
            hero = Hero(0.4359375, 0.6435185185185)
        elif current_round == 7:
            dart1 = Monkey('dart', 0.2515625, 0.2592592592593)
            dart1.target('strong')
        elif current_round == 9:
            sniper1 = Monkey('sniper', 0.6473958333333, 0.7925925925926)
        elif current_round == 10:
            sniper1.target('strong')
        elif current_round == 11:
            sub1 = Monkey('sub', 0.6078125, 0.2425925925926)
            sub1.upgrade(['1-0-0'])
        elif current_round == 13:
            sub1.upgrade(['2-0-0'])
        elif current_round == 15:
            sub1.upgrade(['2-0-1'])
        elif current_round == 19:
            sub1.upgrade(['2-0-2'])
        elif current_round == 21:
            sniper1.upgrade(['1-0-0'])
        elif current_round == 29:
            super = Monkey('super', 0.434375, 0.3425925925926)
        elif current_round == 32:
            super.upgrade(['0-1-0'])
        elif current_round == 35:
            alch1 = Monkey('alch', 0.4109375, 0.6861111111111)
        elif current_round == 36:
            alch1.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif current_round == 37:
            alch1.upgrade(['3-1-0','3-2-0'])
        elif current_round == 39:
            super.upgrade(['0-1-1'])
        elif current_round == 40:
            ability(1, 3)
        elif current_round == 41:
            super.upgrade(['0-2-1','0-2-2'])
        elif current_round == 47:
            super.upgrade(['0-3-2'])
        elif current_round == 48:
            super.target_robo('left', 1)    # change second arm 'last' -> 'close'
        elif current_round == 59:
            ability(1, 4.5)
        elif current_round == 62:
            super.upgrade(['0-4-2'])
        elif current_round == 63:
            ability(1, 1)
            ability(2, 6.5)
            ability(3, 12.5)
        elif current_round == 75:
            ability(3, 14.5)
        elif current_round == 76:
            ability(2, 1)
        elif current_round == 77:
            ability(3, 17)
        elif current_round == 78:
            ability(2, 3.5)
            ability(1, 20)
            ability(2, 27)
        elif current_round == 79:
            ability(1, 9)
            ability(3, 19)
        elif current_round == 80:
            ability(3, 15.5)
        elif current_round == 81:
            ability(3, 15.5)
        elif current_round == 82:
            ability(1, 7.5)
            ability(2, 8.5)
            ability(3, 18)
        elif current_round == 83:
            ability(1, 10)
            ability(2, 13)
        elif current_round == 84:
            ability(1, 5.5)
            ability(2, 11)
            ability(3, 13)
        elif current_round == 85:
            super.target('last')
            ability(3, 21)
        elif current_round == 86:
            super.target('first')
            ability(1, 8)
        elif current_round == 87:
            super.target('last')
            ability(3, 18.5)
        elif current_round == 88:
            super.target('first')
            ability(1, 5.5)
            ability(3, 18.5)
        elif current_round == 89:
            ability(1, 2)
            super.upgrade(['0-5-2'])
        elif current_round == 93:
            sniper1.upgrade(['2-0-0','3-0-0','4-0-0','4-1-0','4-2-0'])
        elif current_round == 94:
            glue1 = Monkey('glue', 0.0817708333333, 0.5277777777778)
            glue1.upgrade(['0-0-1','0-0-2','0-0-3'])
        elif current_round == 95:
            glue1.upgrade(['0-0-4','0-1-4','0-2-4'])
            glue1.target('strong')
            ability(3, 15.5)
        elif current_round == 97:
            mermonkey = Monkey('mermonkey', 0.2453125, 0.1981481481481)
            mermonkey.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','1-0-4','2-0-4'])
            mermonkey.special(1, 0.2942708333333, 0.3)
        elif current_round == 98:
            spike = Monkey('spike', 0.0598958333333, 0.6046296296296)
            spike.upgrade(['0-1-0','0-2-0'])
            ability(3,12)
        elif current_round == 99:
            spike.upgrade(['0-3-0','1-3-0'])
        elif current_round == 100:
            spike.upgrade(['1-4-0'])
            ability(4, 10)
            ability(1, 11)
            ability(3, 18.5)