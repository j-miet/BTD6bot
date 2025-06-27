"""
[Hero] Psi
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-3-0
boomer 0-2-4
bomb 4-2-0
glue 2-2-4

sub 0-4-0
mortar 0-0-4

wizard 5-2-0
alch 4-2-1
druid 1-3-0

spike 3-0-3
village 2-0-2
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
            change_autostart()
            dart1 = Monkey('dart', 0.1557291666667, 0.6203703703704)
            dart1.target('strong')
            dart2 = Monkey('dart', 0.5348958333333, 0.1759259259259)
            dart2.target('last')
            dart3 = Monkey('dart', 0.4484375, 0.9018518518519)
            forward()
            click(0.5552083333333, 0.0935185185185, 23)
            dart3.upgrade(['0-1-0'])
            end_round()
        elif current_round == 7:
            wait(3)
            click(0.5552083333333, 0.0935185185185)
            dart4 = Monkey('dart', 0.115625, 0.4564814814815)
            dart4.target('strong')
            end_round()
        elif current_round == 8:
            dart5 = Monkey('dart', 0.5583333333333, 0.9527777777778)
            dart5.target('strong')
            end_round()
        elif current_round == 9:
            end_round(9)
        elif current_round == 10:
            dart6 = Monkey('dart', 0.1364583333333, 0.6657407407407)
            dart7 = Monkey('dart', 0.4145833333333, 0.8916666666667)
            end_round()
        elif current_round == 11:
            end_round(8)
        elif current_round == 12:
            end_round(8)
        elif current_round == 13:
            dart1.upgrade(['0-1-0','0-2-0'])
            dart3.upgrade(['0-2-0'])
            end_round(9)
        elif current_round == 14:
            dart1.upgrade(['0-3-0'])
            end_round()
        elif current_round == 15:
            end_round(12)
        elif current_round == 16:
            dart3.upgrade(['0-3-0'])
            end_round()
        elif current_round == 17:
            end_round(5)
        elif current_round == 18:
            end_round(11)
        elif current_round == 19:
            end_round(7)
        elif current_round == 20:
            end_round(4)
        elif current_round == 21:
            wait(7)
            hero = Hero(0.3625, 0.25)
            hero.target('strong')
            end_round()
        elif current_round == 22:
            glue1 = Monkey('glue', 0.7041666666667, 0.2425925925926)
            glue1.upgrade(['1-0-0','1-1-0'])
            glue1.target('last')
            end_round()
        elif current_round == 23:
            end_round(6)
        elif current_round == 24:
            glue1.upgrade(['2-1-0'])
            end_round(3)
        elif current_round == 25:
            druid1 = Monkey('druid', 0.3234375, 0.125)
            druid1.target('strong')
            end_round()
        elif current_round == 26:
            hero.target('first')
            wait(7)
            hero.target('strong')
            end_round()
        elif current_round == 27:
            hero.target('first')
            druid1.upgrade(['1-0-0'])
            end_round(14)
        elif current_round == 28:
            end_round(4)
        elif current_round == 29:
            spike1 = Monkey('spike', 0.3890625, 0.7583333333333)
            end_round(4)
        elif current_round == 30:
            spike1.upgrade(['0-0-1'])
            end_round(7)
        elif current_round == 31:
            spike1.upgrade(['0-0-2'])
            spike1.target('smart')
            end_round(8)
        elif current_round == 32:
            end_round(12)
        elif current_round == 33:
            spike2 = Monkey('spike', 0.1708333333333, 0.762037037037)
            end_round(10)
        elif current_round == 34:
            end_round(14)
        elif current_round == 35:
            hero.target('strong')
            wait(13)
            druid1.upgrade(['1-1-0','1-2-0','1-3-0'])
            end_round()
        elif current_round == 36:
            spike2.upgrade(['0-0-1','0-0-2'])
            spike2.target('smart')
            end_round(7)
        elif current_round == 37:
            end_round(17)
        elif current_round == 38:
            village1 = Monkey('village', 0.2822916666667, 0.7462962962963)
            village1.upgrade(['0-0-1','0-0-2'])
            spike1.upgrade(['1-0-2'])
            end_round(5)
        elif current_round == 39:
            village1.upgrade(['1-0-2'])
            alch1 = Monkey('alch', 0.3567708333333, 0.6055555555556)
            alch1.upgrade(['1-0-0','2-0-0'])
            wait(8)
            druid1.target('last')
            end_round()
        elif current_round == 40:
            wait(6)
            druid1.target('strong')
            end_round()
        elif current_round == 41:
            spike2.upgrade(['1-0-2'])
            village1.upgrade(['2-0-2'])
            end_round(7)
        elif current_round == 42:
            alch1.upgrade(['3-0-0'])
            end_round(3)
        elif current_round == 43:
            alch2 = Monkey('alch', 0.1895833333333, 0.8935185185185)
            end_round(5)
        elif current_round == 44:
            alch2.upgrade(['1-0-0','2-0-0','3-0-0'])
            end_round(2)
        elif current_round == 45:
            spike1.upgrade(['2-0-2','3-0-2'])
            end_round(5)
        elif current_round == 46:
            end_round(6)
        elif current_round == 47:
            spike2.upgrade(['2-0-2','3-0-2'])
            end_round()
        elif current_round == 48:
            alch1.upgrade(['3-1-0','3-2-0'])
            end_round(10)
        elif current_round == 49:
            glue1.target('strong')
            ability(1,5.5)
            alch1.upgrade(['4-2-0'])
            wizard = Monkey('wizard', 0.2989583333333, 0.5953703703704)
            wizard.upgrade(['1-0-0','2-0-0','3-0-0','3-1-0','3-2-0'])
            wizard.special(1, 0.4390625, 0.7666666666667)
            end_round(3)
        elif current_round == 50:
            end_round(13)
        elif current_round == 51:
            village2 = Monkey('village', 0.4473958333333, 0.2305555555556)
            village2.upgrade(['0-0-1','0-0-2'])
            engi = Monkey('engineer', 0.5161458333333, 0.1231481481481)
            engi.upgrade(['0-1-0','0-2-0','0-3-0','0-3-1','0-3-2'])
            engi.special(1, 0.3651041666667, 0.0)
            end_round(2)
        elif current_round == 52:
            change_autostart()
        elif current_round == 58:
            wizard.upgrade(['4-2-0'])
            alch2.upgrade(['3-0-1'])
        elif current_round == 59:
            bomb1 = Monkey('bomb', 0.3473958333333, 0.7712962962963)
            bomb1.upgrade(['1-0-0','2-0-0','3-0-0','3-1-0','3-2-0'])
        elif current_round == 62:
            bomb1.upgrade(['4-2-0'])
            bomb2 = Monkey('bomb', 0.1682291666667, 0.6972222222222)
        elif current_round == 63:
            bomb2.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif current_round == 65:
            bomb2.upgrade(['4-0-0','4-1-0','4-2-0'])
        elif current_round == 76:
            ability(1,0.75)
        elif current_round == 78:
            ability(2, 3.5)
            ability(2,26)
        elif current_round == 79:
            engi.special(1, 0.6973958333333, 0.0814814814815)
            ability(1,11)
            ability(2,20)
            ability(1,25)
        elif current_round == 80:
            wizard.upgrade(['5-2-0'])
        elif current_round == 83:
            glue2 = Monkey('glue', 0.4265625, 0.162962962963)
            glue2.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
            glue2.target('strong')
            village2.upgrade(['1-0-2','2-0-2'])
            boomer1 = Monkey('boomer', 0.4875, 0.0796296296296)
            boomer1.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
            boomer1.target('close')
        elif current_round == 84:
            boomer2 = Monkey('boomer', 0.3979166666667, 0.2092592592593)
            boomer2.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
            boomer2.target('close')
        elif current_round == 87:
            mortar = Monkey('mortar', 0.55625, 0.3296296296296)
            mortar.upgrade(['0-0-1','0-0-2','0-0-3'])
            mortar.special(1, 0.7125, 0.1944444444444)
        elif current_round == 89:
            mortar.upgrade(['0-0-4'])
        elif current_round == 90:
            mortar.special(1, 0.3536458333333, 0.2314814814815)
            engi.special(1, 0.3703125, 0.0)
        elif current_round == 91:
            engi.special(1, 0.6526041666667, 0.0277777777778)
            mortar.special(1, 0.3682291666667, 0.0796296296296)
        elif current_round == 93:
            mortar.special(1, 0.7119791666667, 0.1981481481481)
            ninja = Monkey('ninja', 0.4140625, 0.2907407407407)
            ninja.upgrade(['0-1-0','0-2-0','0-3-0','0-4-0'])
        elif current_round == 94:
            ability(1,14)
            ability(2,18)
            alch3 = Monkey('alch', 0.2666666666667, 0.8157407407407)
            alch3.upgrade(['0-0-1','0-0-2','0-0-3','0-1-3','0-2-3'])
            alch3.target('strong')
        elif current_round == 96:
            mortar.special(1, 0.365625, 0.0898148148148)
            ability(3,4)
        elif current_round == 97:
            mortar.special(1, 0.3479166666667, 0.8157407407407)
            sub = Monkey('sub', 0.5536458333333, 0.5453703703704)
            sub.upgrade(['0-1-0','0-2-0','0-3-0','0-4-0'])
            ability(4,14)
        elif current_round == 98:
            mortar.special(1, 0.3682291666667, 0.0611111111111)
            ability(3)
            sub2 = Monkey('sub', 0.5213541666667, 0.6)
            sub2.upgrade(['0-1-0','0-2-0','0-3-0'])
            spike3 = Monkey('spike', 0.3890625, 0.1296296296296)
            spike3.target('close')
            ability(1,14)
            ability(2,19)
            spike3.upgrade(['1-0-0','1-0-1','1-0-2','1-0-3'])
        elif current_round == 99:
            ability(3,2)
            ability(1,3.5)
            sub2.upgrade(['0-4-0'])
        elif current_round == 100:
            wizard.special(1, 0.4338541666667, 0.7259259259259)
            ability(4,3)
            ability(4,10.5)
