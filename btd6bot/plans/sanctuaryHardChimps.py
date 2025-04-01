"""
[Plan Name] sanctuaryHardChimps
[Game Version] 47
[Hero] Psi
[Monkey Knowledge] -
---------------------------------------------------------------
===Monkeys required===
dart 0-0-1
sniper 4-0-2, 4-2-0
alch 4-0-1
mermonkey 2-0-5
village 3-2-0
glue 5-2-0
boomer 5-0-2
_______________________________________
Strategy used: https://www.youtube.com/watch?v=5lw5KgJhaf4

-Can do black border. There are plenty of black-border capable strats out there, but they seem to require more micro/abilities (like using Geraldo items). So it's a trade-off between more rng + less micro, and vice versa.

-I've added some tower retargeting + extra ability uses to minimize rng, but not all of it can be removed. So bloons can randomly leak on some rounds, mainly in mid/late game (65 seems to be a common one) - if that happens, try again. Should work after a few attemps.
"""

from._plan_imports import *

def play(rounds: tuple[str, str, str, int, int, str]) -> None:
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start, rounds[2])
        if current_round == BEGIN:
            change_autostart()
            dart_mid = Monkey('dart', 0.5364583333333, 0.2583333333333)
            dart_right = Monkey('dart', 0.7442708333333, 0.1083333333333)
            dart_left = Monkey('dart', 0.1661458333333, 0.3509259259259)
            begin()
            dart_mid.upgrade(['0-0-1'], 0.46, 0.27)
            end_round()
        elif current_round == 7:
            dart_left2 = Monkey('dart', 0.3348958333333, 0.4546296296296)
            dart_left.target('strong', cpos_x=0.3078125, cpos_y=0.4157407407407)
            dart_right.target('strong', cpos_x=0.7234375, cpos_y=0.3342592592593)
            end_round()
        elif current_round == 8:
            dart_right2 = Monkey('dart', 0.6302083333333, 0.4342592592593)
            end_round()
        elif current_round == 9:
            end_round(8)
        elif current_round == 10:
            sniper1 = Monkey('sniper', 0.4072916666667, 0.0611111111111)
            end_round(2)
        elif current_round == 11:
            end_round(8)
        elif current_round == 12:
            end_round(8)
        elif current_round == 13:
            end_round(12)
        elif current_round == 14:
            hero = Hero(0.3833333333333, 0.1064814814815)
            hero.target('strong')
            end_round()
        elif current_round == 15:
            end_round(10)
        elif current_round == 16:
            end_round(8)
        elif current_round == 17:
            boomerang = Monkey('boomer', 0.5, 0.2546296296296)
            boomerang.upgrade(['1-0-0', '1-0-1'])
            end_round(2)
        elif current_round == 18:
            boomerang.upgrade(['2-0-1'], cpos_x=0.425, cpos_y=0.275)
            end_round(2)
        elif current_round == 19:
            end_round(8) 
        elif current_round == 20:
            sniper1.upgrade(['0-0-1'], cpos_x=0.40625, cpos_y=0.0564814814815)
            end_round(2)
        elif current_round == 21:
            sniper1.upgrade(['1-0-1'], cpos_x=0.488, cpos_y=0.025)
            wait(2)
            sniper1.target('strong')
            end_round()
        elif current_round == 22:
            end_round(4)
        elif current_round == 23:
            ability(1, 1)
            wait(4)
            sniper1.target('first', cpos_x=0.333, cpos_y=0.0354814814815)
            end_round()
        elif current_round == 24:
            boomerang.upgrade(['3-0-1'], cpos_x=0.4260416666667, cpos_y=0.2722222222222)
            end_round(3)
        elif current_round == 25:
            end_round(8)
        elif current_round == 26:
            sniper1.upgrade(['1-0-2'], cpos_x=0.4104166666667, cpos_y=0.0592592592593)
            end_round(5)
        elif current_round == 27:
            sniper2 = Monkey('sniper', 0.3895833333333, 0.0444444444444)
            end_round(10)
        elif current_round == 28:
            sniper2.upgrade(['1-0-0', '1-1-0'], cpos_x=0.4645833333333, cpos_y=0.0574074074074)
            sniper2.special(1)
            end_round(3)
        elif current_round == 29:
            end_round(8)
        elif current_round == 30:
            wait(5)
            sniper1.target('strong', cpos_x=0.4104166666667, cpos_y=0.0592592592593)
            end_round(3)
        elif current_round == 31:
            ability(1, 1)
            wait(6)
            sniper1.target('first', cpos_x=0.333, cpos_y=0.0354814814815)
            end_round()
        elif current_round == 32:
            end_round(10)
        elif current_round == 33: 
            end_round(10)
        elif current_round == 34:
            end_round(14)
        elif current_round == 35:
            boomerang.upgrade(['4-0-1', '4-0-2'], cpos_x=0.35, cpos_y=0.2564814814815)
            end_round(10)
        elif current_round == 36:
            sniper1.upgrade(['2-0-2'], cpos_x=0.4104166666667, cpos_y=0.0592592592593)
            end_round(3)
        elif current_round == 37:
            end_round(18)
        elif current_round == 38:
            ability(1, 1)
            end_round(12)
        elif current_round == 39:
            sniper1.upgrade(['3-0-2'], cpos_x=0.333, cpos_y=0.0354814814815)
            village = Monkey('village', 0.3729166666667, 0.125)
            end_round(2)
        elif current_round == 40: 
            ability(1, 1)
            end_round(4)
        elif current_round == 41:
            village.upgrade(['0-1-0', '0-2-0'], cpos_x=0.5260416666667, cpos_y=0.1453703703704)
            end_round(5)
        elif current_round == 42:
            mermonkey1 = Monkey('mermonkey', 0.3875, 0.2361111111111)
            end_round(5)
        elif current_round == 43:
            mermonkey1.upgrade(['1-0-0', '2-0-0', '2-0-1', '2-0-2'], cpos_x=0.3114583333333, cpos_y=0.2287037037037)
            end_round(2)
        elif current_round == 44:
            end_round(10)
        elif current_round == 45:
            mermonkey1.upgrade(['2-0-3'], cpos_x=0.4583333333333, cpos_y=0.2231481481481)
            end_round(20)
        elif current_round == 46:
             end_round(5)
        elif current_round == 47:
             end_round(10)
        elif current_round == 48:
             end_round(20)
        elif current_round == 49:
             mermonkey1.upgrade(['2-0-4'], cpos_x=0.459375, cpos_y=0.2212962962963)
             mermonkey1.special(1, 0.4395833333333, 0.3731481481481)
             alch1 = Monkey('alch', 0.5041666666667, 0.1972222222222)
             alch1.upgrade(['1-0-0', '2-0-0', '3-0-0', '3-0-1'])
             end_round(5)
        elif current_round == 50:
             alch1.upgrade(['4-0-1'], cpos_x=0.4322916666667, cpos_y=0.2064814814815)
             end_round(2)
        elif current_round == 51:
             end_round(10)
        elif current_round == 52:
             village.upgrade(['1-2-0', '2-2-0'], cpos_x=0.446375, cpos_y=0.1111037037037)
             end_round(5)
        elif current_round == 53:
            glue = Monkey('glue', 0.5385416666667, 0.2064814814815)
            end_round(15)
        elif current_round == 54:
            glue.upgrade(['1-0-0', '2-0-0', '3-0-0', '3-1-0'], cpos_x=0.4666666666667, cpos_y=0.2231481481481)
            end_round(3)
        elif current_round == 55:
            glue.upgrade(['3-2-0'], cpos_x=0.3927083333333, cpos_y=0.2027777777778)
            end_round(12)
        elif current_round == 56:
            end_round(8)
        elif current_round == 57:
            ability(1, 4)
            glue.upgrade(['4-2-0'], cpos_x=0.5416666666667, cpos_y=0.2046296296296)
            end_round(2)
        elif current_round == 58:
            village.upgrade(['3-2-0'], cpos_x=0.453125, cpos_y=0.1490740740741)
            end_round(15)
        elif current_round == 59:
            end_round(12)
        elif current_round == 60:
            end_round(10)
        elif current_round == 61:
            end_round(10)
        elif current_round == 62:
            end_round(20)
        elif current_round == 63:
            ability(1, 6.5)
            ability(2, 12)
            end_round(5)
        elif current_round == 64:
            end_round(10)
        elif current_round == 65:
            end_round(33)
        elif current_round == 66:
            ability(2, 6.5)
            ability(1, 9)
            end_round(8)
        elif current_round == 67:
            end_round(13)
        elif current_round == 68:
            end_round(11)
        elif current_round == 69:
            end_round(16)
        elif current_round == 70:
            end_round(20)
        elif current_round == 71:
            end_round(10)
        elif current_round == 72:
            end_round(16)
        elif current_round == 73:
            ability(2, 10)
            glue.upgrade(['5-2-0'], cpos_x=0.5322916666667, cpos_y=0.2231481481481)
            end_round(13)
        elif current_round == 74:
            end_round(33)
        elif current_round == 75:
            sniper1.upgrade(['4-0-2'], cpos_x=0.328125, cpos_y=0.0564814814815)
            sniper1.target('strong')
            end_round(3)
        elif current_round == 76:
            end_round(3)
        elif current_round == 77:
            end_round(23)
        elif current_round == 78:
            end_round(32)
        elif current_round == 79:
            end_round(36)
        elif current_round == 80:
            end_round(38)
        elif current_round == 81:
            end_round(18)
        elif current_round == 82:
            ability(1, 7)
            ability(2, 15)
            end_round(10)
        elif current_round == 83:
            end_round(22)
        elif current_round == 84:
            boomerang.upgrade(['5-0-2'], cpos_x=0.4348958333333, cpos_y=0.2842592592593)
            end_round(5)
        elif current_round == 85:
            end_round(34)
        elif current_round == 86:
            end_round(15)
        elif current_round == 87:
            end_round(20)
        elif current_round == 88:
            end_round(20)
        elif current_round == 89:
            end_round(16)
        elif current_round == 90:
            end_round(7)
        elif current_round == 91:
            end_round(12)
        elif current_round == 92:
            ability(2, 15)
            end_round(10)
        elif current_round == 93:
            end_round(18)
        elif current_round == 94:
            mermonkey1.upgrade(['2-0-5'], cpos_x=0.4072916666667, cpos_y=0.2342592592593)
            mermonkey2 = Monkey('mermonkey', 0.4989583333333, 0.1990740740741)
            mermonkey2.upgrade(['1-0-0', '2-0-0', '2-0-1', '2-0-2', '2-0-3'])
            end_round(4)
        elif current_round == 95:
            ability(2, 12)
            end_round(10)
        elif current_round == 96:
            mermonkey2.upgrade(['2-0-4'], cpos_x=0.5, cpos_y=0.16)
            mermonkey2.special(1, 0.4375, 0.3374814814815)
            end_round(17)
        elif current_round == 97:
            sniper2.upgrade(['2-1-0', '3-1-0'], cpos_x=0.541, cpos_y=0.022)
            end_round(22)
        elif current_round == 98:
            sniper2.upgrade(['4-1-0', '4-2-0'], cpos_x=0.464, cpos_y=0.031)
            ability(2, 10.5)
            alch2 = Monkey('alch', 0.490625, 0.1037037037037)
            alch2.upgrade(['1-0-0', '2-0-0', '3-0-0', '4-0-0', '4-0-1'])
            end_round(6)
        elif current_round == 99:
            end_round(10)
        elif current_round == END:
            ability(1, 10)
            ability(2, 13)