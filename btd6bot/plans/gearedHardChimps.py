"""
[Hero] Rosalia
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0

sniper 1-3-2
heli 5-0-5

ninja 0-4-0
alch 3-2-0

village 2-4-2
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
            change_autostart()
            dart1 = Monkey('dart', 0.1833333333333, 0.5722222222222)
            sniper1 = Monkey('sniper', 0.2854166666667, 0.5796296296296)
            sniper1.target('strong')
            forward()
            end_round(13)
        elif current_round == 7:
            dart2 = Monkey('dart', 0.1838541666667, 0.5685185185185)
            end_round(12)
        elif current_round == 8:
            wait(15)
            sniper2 = Monkey('sniper', 0.5776041666667, 0.3611111111111)
            sniper2.target('strong')
            end_round()
        elif current_round == 9:
            end_round(11)
        elif current_round == 10:
            dart3 = Monkey('dart', 0.1822916666667, 0.5703703703704)
            end_round(16)
        elif current_round == 11:
            wait(13)
            sniper3 = Monkey('sniper', 0.5494791666667, 0.7546296296296)
            sniper3.target('strong')
            end_round()
        elif current_round == 12:
            change_autostart()
        elif current_round == 13:
            wait(2)
            sniper4 = Monkey('sniper', 0.43125, 0.8916666666667)
        elif current_round == 15:
            wait(2)
            sniper5 = Monkey('sniper', 0.54375, 0.7509259259259)
        elif current_round == 17:
            change_autostart()
            end_round(6)
        elif current_round == 18:
            hero = Hero(0.4395833333333, 0.9361111111111)
            wait(8)
            hero.special(2, x=0.1864583333333, y=0.6175925925926, cpos=(0.2677083333333, 0.8324074074074))
            hero.special(1)
            end_round(3)
        elif current_round == 19:
            wait(10)
            sniper1.upgrade(['1-0-0'], cpos=(0.4380208333333, 0.8))
            end_round()
        elif current_round == 20:
            wait(7)
            hero.special(2, x=0.1890625, y=0.5611111111111, cpos=(0.2697916666667, 0.3194444444444))
            end_round(3)
        elif current_round == 21:
            end_round(8)
        elif current_round == 22:
            ability(1,1)
            wait(7)
            sniper5.upgrade(['0-1-0','0-2-0'], cpos=(0.5427083333333, 0.7388888888889))
            end_round()
        elif current_round == 23:
            end_round(6)
        elif current_round == 24:
            wait(8)
            sniper5.upgrade(['0-2-1'], cpos=(0.3260416666667, 0.7407407407407))
            end_round()
        elif current_round == 25:
            end_round(10)
        elif current_round == 26:
            sniper5.upgrade(['0-2-2'], cpos=(0.2822916666667, 0.5759259259259))
            wait(9)
            hero.special(2, x=0.1895833333333, y=0.6138888888889, cpos=(0.2729166666667, 0.8305555555556))
            end_round(3)
        elif current_round == 27:
            end_round(15)
        elif current_round == 28:
            wait(7)
            hero.special(2, x=0.1859375, y=0.5472222222222, cpos=(0.2697916666667, 0.3342592592593))
            end_round(3)
        elif current_round == 29:
            end_round(6)
        elif current_round == 30:
            end_round(12)
        elif current_round == 31:
            wait(2)
            sniper5.upgrade(['0-3-2'], cpos=(0.5421875, 0.7462962962963))
            end_round(5)
        elif current_round == 32:
            end_round(11)
        elif current_round == 33:
            end_round(13)
        elif current_round == 34:
            wait(15)
            hero.special(2, x=0.1869791666667, y=0.6222222222222, cpos=(0.2703125, 0.8296296296296))
            heli1 = Monkey('heli', 0.4348958333333, 0.837962962963)
            heli1.special(1, 0.1354166666667, 0.5527777777778)
            end_round(3)
        elif current_round == 35:
            heli1.upgrade(['1-0-0','2-0-0'], cpos=(0.4385416666667, 0.8101851851852))
            end_round(6)
        elif current_round == 36:
            wait(11)
            hero.special(2, x=0.1848958333333, y=0.5564814814815, cpos=(0.2723958333333, 0.3398148148148))
            end_round(3)
        elif current_round == 37:
            end_round(17)
        elif current_round == 38:
            end_round(14)
        elif current_round == 39:
            wait(18)
            village1 = Monkey('village', 0.59375, 0.5564814814815)
            village1.upgrade(['0-0-1','0-0-2'])
            heli1.upgrade(['2-0-1','2-0-2','2-0-3'], cpos=(0.5520833333333, 0.3990740740741))
            end_round()
        elif current_round == 40:
            ability(1,3)
            end_round(5)
        elif current_round == 41:
            end_round(16)
        elif current_round == 42:
            wait(10)
            village2 = Monkey('village', 0.3447916666667, 0.8657407407407)
            village2.upgrade(['1-0-0','2-0-0'])
            end_round()
        elif current_round == 43:
            ability(1,1.75)
            wait(8)
            hero.special(2, x=0.15, y=0.437962962963, cpos=(0.203125, 0.5638888888889))
            end_round()
        elif current_round == 44:
            wait(12)
            village2.upgrade(['2-0-1','2-0-2'], cpos=(0.246875, 0.4546296296296))
            alch1 = Monkey('alch', 0.3552083333333, 0.3898148148148)
            heli2 = Monkey('heli', 0.34375, 0.2898148148148)
            end_round()
        elif current_round == 45:
            heli2.upgrade(['1-0-0','2-0-0','2-0-1','2-0-2','3-0-2'])
            end_round(3)
        elif current_round == 46:
            end_round(7)
        elif current_round == 47:
            ability(1)
            alch1.upgrade(['1-0-0','2-0-0','3-0-0'], cpos=(0.559375, 0.4657407407407))
            end_round(8)
        elif current_round == 48:
            end_round(20)
        elif current_round == 49:
            ability(1,5)
            wait(16)
            heli1.upgrade(['2-0-4'], cpos=(0.5510416666667, 0.762037037037))
            hero.special(1, cpos=(0.44375, 0.9564814814815))
            hero.target('strong')
            end_round()
        elif current_round == 50:
            village1.upgrade(['0-1-2','0-2-2'], cpos=(0.4489583333333, 0.787962962963))
            change_autostart()
        elif current_round == 62:
            wait(2)
            heli2.upgrade(['4-0-2'], cpos=(0.509375, 0.2722222222222))
            alch1.upgrade(['3-1-0','3-2-0'], cpos=(0.4697916666667, 0.3805555555556))
        elif current_round == 76:
            ability(1)
        elif current_round == 78:
            ability(1,3.5)
            ability(1,25.5)
        elif current_round == 80:
            ability(3,1)
            ability(1,5)
        elif current_round == 81:
            ability(2,2)
            heli2.upgrade(['5-0-2'], cpos=(0.521875, 0.8731481481481))
        elif current_round == 82:
            wait(3)
            village1.upgrade(['0-3-2'], cpos=(0.4541666666667, 0.8175925925926))
        elif current_round == 89:
            ability(1,2)
            ability(2,5)
        elif current_round == 92:
            ability(3,7)
            ability(1,10)
        elif current_round == 93:
            ability(2,1)
            wait(2)
            heli1.upgrade(['2-0-5'], cpos=(0.2682291666667, 0.5768518518519))
        elif current_round == 96:
            change_autostart()
            wait(20)
            village1.upgrade(['0-4-2'], cpos=(0.5614583333333, 0.7268518518519))
            end_round()
        elif current_round == 97:
            wait(13)
            ninja = Monkey('ninja', 0.5479166666667, 0.9212962962963)
            ninja.upgrade(['0-1-0','0-2-0','0-3-0'])
            change_autostart()
            end_round(2)
        elif current_round == 98:
            ability(3)
            ability(4,2)
            ability(2,3)
            ability(1,4)
            ninja.upgrade(['0-4-0'])
        elif current_round == 99:
            ability(5,2)
        elif current_round == 100:
            ability(3,4)
            ability(4,5)
            ability(1,6)
            ability(2,7)
