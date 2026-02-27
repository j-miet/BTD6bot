"""
[Hero] Rosalia
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
boomer 0-0-0

sniper 0-1-0
sub 2-0-3
boat 0-0-2
ace 2-0-5

alch 3-0-1
village 2-2-2

engineer 0-0-0
_______________________________________
"""
from._plan_imports import *

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:
            change_autostart()
            boat = Monkey('boat', 0.325, 0.6259259259259)
            boat.target('strong')
            forward()
            wait(9)
            boat.target('first')
            sniper = Monkey('sniper', 0.1609375, 0.1388888888889)
            end_round()
        elif round == 7:
            wait(12)
            boat.target('strong')
            sniper.target('strong')
            end_round()
        elif round == 8:
            boomer1 = Monkey('boomer', 0.6911458333333, 0.3444444444444)
            boomer1.target('last')
            boomer1.special(1)
            boat.target('first')
            end_round()
        elif round == 9:
            wait(2)
            sniper.target('first')
            end_round(6)
        elif round == 10:
            sniper.target('strong')
            engineer1 = Monkey('engineer', 0.6182291666667, 0.5018518518519)
            end_round(7)
        elif round == 11:
            boomer2 = Monkey('boomer', 0.2432291666667, 0.362962962963)
            end_round()
        elif round == 12:
            end_round(8)
        elif round == 13:
            sub = Monkey('sub', 0.4317708333333, 0.6388888888889)
            sub.upgrade(['1-0-0'])
            end_round(2)
        elif round == 14:
            engineer1.target('strong')
            end_round(12)
        elif round == 15:
            wait(4)
            sniper.target('first')
            wait(5)
            sniper.target('strong')
            end_round()
        elif round == 16:
            sub.upgrade(['2-0-0'])
            end_round(6)
        elif round == 17:
            end_round(5)
        elif round == 18:
            sub.upgrade(['2-0-1'])
            end_round(8)
        elif round == 19:
            end_round(6)
        elif round == 20:
            end_round(4)
        elif round == 21:
            sub.upgrade(['2-0-2'])
            end_round()
        elif round == 22:
            end_round(4)
        elif round == 23:
            boat.upgrade(['0-0-1'])
            end_round(6)
        elif round == 24:
            forward(1)
            boat.upgrade(['0-0-2'])
            forward(1)
            end_round(5)
        elif round == 25:
            end_round(9)
        elif round == 26:
            end_round(7)
        elif round == 27:
            hero = Hero(0.4401041666667, 0.3481481481481)
            wait(6)
            hero.special(1)
            hero.special(2, 0.5984375, 0.2666666666667)
            end_round()
        elif round == 28:
            end_round(5)
        elif round == 29:
            wait(7)
            hero.special(2, 0.3776041666667, 0.2324074074074)
            end_round()
        elif round == 30:
            wait(6)
            hero.special(2, 0.2786458333333, 0.4046296296296)
            hero.special(1)
            end_round()
        elif round == 31:
            ability(1, 2.5)
            end_round(6)
        elif round == 32:
            end_round(12)
        elif round == 33:
            hero.special(2, 0.6005208333333, 0.275)
            village1 = Monkey('village', 0.4223958333333, 0.4916666666667)
            village1.upgrade(['0-0-1','0-0-2'])
            end_round(8)
        elif round == 34:
            sub.upgrade(['2-0-3'])
            hero.special(2, 0.4765625, 0.2768518518519)
            end_round(6)
        elif round == 35:
            wait(10)
            hero.special(2, 0.4067708333333, 0.3194444444444)
            hero.special(1)
            end_round(3)
        elif round == 36:
            village2 = Monkey('village', 0.4848958333333, 0.4916666666667)
            alch = Monkey('alch', 0.5046875, 0.6287037037037)
            alch.upgrade(['1-0-0','2-0-0'])
            sniper.upgrade(['0-1-0'])
            hero.special(2, 0.2625, 0.4231481481481)
            end_round(2)
        elif round == 37:
            wait(18)
            hero.special(1)
            end_round()
        elif round == 38:
            hero.special(1)
            alch.upgrade(['3-0-0','3-0-1'])
            wait(6)
            hero.special(2, 0.6052083333333, 0.35)
            hero.special(1)
            end_round(3)
        elif round == 39:
            village2.upgrade(['1-0-0','2-0-0'])
            end_round(5)
        elif round == 40:
            ability(1,0.75)
            end_round(5)
        elif round == 41:
            ace = Monkey('ace', 0.51875, 0.4)
            ace.upgrade(['0-0-1','0-0-2'])
            ace.center(0.421875, 0.9990740740741)
            end_round(16)
        elif round == 42:
            ace.upgrade(['0-0-3','1-0-3'])
            hero.special(2, 0.259375, 0.3907407407407)
            end_round(3)
        elif round == 43:
            ability(2, 1)
            ace.upgrade(['2-0-3'])
            end_round(5)
        elif round == 44:
            village2.upgrade(['2-1-0','2-2-0'])
            change_autostart()
            end_round()
        elif round == 48:
            change_autostart()
            end_round(22)
        elif round == 49:
            ability(2,4)
            wait(15)
            hero.special(2, 0.3848958333333, 0.4240740740741)
            hero.special(1)
            end_round(3)
        elif round == 50:
            end_round(15)
        elif round == 51:
            wait(7)
            hero.special(2, 0.6088541666667, 0.3574074074074)
            hero.special(1)
            end_round(3)
        elif round == 52:
            ability(2, 5)
            end_round(6)
        elif round == 53:
            wait(15)
            hero.special(2, 0.3072916666667, 0.2)
            hero.target('strong')
            end_round()
        elif round == 54:
            ability(1, 1.5)
            wait(7)
            hero.special(2, 0.2625, 0.4055555555556)
            hero.target('first')
            end_round(3)
        elif round == 55:
            ability(2)
            ace.upgrade(['2-0-4'])
            end_round(4)
        elif round == 56:
            change_autostart()
        elif round == 79:
            change_autostart()
            end_round(27)
        elif round == 80:
            ability(2,7)
            wait(6)
            hero.special(2, 0.4875, 0.2259259259259)
            end_round(3)
        elif round == 81:
            wait(15)
            hero.special(2, 0.6078125, 0.2962962962963)
            end_round(3)
        elif round == 82:
            ability(1,8)
            ability(2)
            end_round(10)
        elif round == 83:
            wait(19)
            hero.special(2, 0.3291666666667, 0.2851851851852)
            end_round(3)
        elif round == 84:
            ability(1,4)
            wait(12)
            hero.special(2, 0.2614583333333, 0.4166666666667)
            end_round()
        elif round == 85:
            ability(3,4.5)
            ability(2,5.5)
            ability(1,6.5)
            wait(10)
            hero.special(2, 0.2760416666667, 0.2222222222222)
            end_round(3)
        elif round == 86:
            wait(17)
            hero.special(2, 0.490625, 0.2666666666667)
            end_round(3)
        elif round == 87:
            ability(3,7)
            ability(2,7.5)
            ability(1,7.5)
            wait(8)
            hero.special(2, 0.6161458333333, 0.3537037037037)
            ace.center(0.6791666666667, 0.9990740740741)
            end_round()
        elif round == 88:
            ace.upgrade(['2-0-5'])
            end_round(8)
        elif round == 89:
            change_autostart()
        elif round == 90:
            ace.center(0.4166666666667, 0.9990740740741)