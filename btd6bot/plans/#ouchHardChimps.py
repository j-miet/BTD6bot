"""
[Hero] Obyn
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-2
ice 4-1-0
glue 0-2-4

sniper 4-2-0

wizard 3-0-2
ninja 0-4-0
alch 4-2-0
druid 3-1-5
mermonkey 2-0-4

village 2-3-2
engi 0-4-0
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
            dart1 = Monkey('dart', 0.2927083333333, 0.3787037037037)
            dart2 = Monkey('dart', 0.590625, 0.3027777777778)
            dart3 = Monkey('dart', 0.496875, 0.6101851851852)
            forward()
            wait(7)
            forward(1)
            dart1.upgrade(['0-0-1'])
            end_round()
        elif current_round == 7:
            wait(5.75)
            dart1.target('strong')
            wait(0.1)
            dart1.target('first')
            wait(3)
            dart1.target('strong')
            forward(1)
            dart4 = Monkey('dart', 0.3708333333333, 0.6064814814815)
            end_round()
        elif current_round == 8:
            end_round(12)
        elif current_round == 9:
            sniper1 = Monkey('sniper', 0.5322916666667, 0.3027777777778)
            sniper1.target('last')
            forward()
        elif current_round == 10:
            wait(1)
            forward(1)
            wait(14)
            sniper1.target('strong')
            end_round(5)
        elif current_round == 11:
            end_round(8)
        elif current_round == 12:
            hero = Hero(0.440625, 0.6231481481481)
            end_round()
        elif current_round == 13:
            end_round(13)
        elif current_round == 14:
            sniper2 = Monkey('sniper', 0.8380208333333, 0.7175925925926)
            sniper2.target('strong')
            end_round(6)
        elif current_round == 15:
            ability(1,4)
            wizard1 = Monkey('wizard', 0.4536458333333, 0.3824074074074)
            wait(1)
            sniper2.target('first')
            wait(3)
            sniper2.target('strong')
            end_round()
        elif current_round == 16:
            wizard1.upgrade(['1-0-0'])
            end_round(6)
        elif current_round == 17:
            end_round(4)
        elif current_round == 18:
            wizard1.upgrade(['2-0-0'])
            end_round(9)
        elif current_round == 19:
            ability(1)
            engi1 = Monkey('engineer', 0.3494791666667, 0.7027777777778)
            sniper2.target('first')
            end_round(3)
        elif current_round == 20:
            sniper1.upgrade(['1-0-0'])
            sniper2.target('strong')
            end_round(2)
        elif current_round == 21:
            ability(1,1)
            wait(1)
            sniper2.target('first')
            wait(2)
            sniper2.target('strong')
            end_round(3)
        elif current_round == 22:
            ability(1)
            wait(1)
            sniper2.target('first')
            wait(2)
            sniper2.target('strong')
            end_round()
        elif current_round == 23:
            dart1.upgrade(['0-0-2'])
            end_round(5)
        elif current_round == 24:
            end_round(5)
        elif current_round == 25:
            ability(1)
            end_round(9)
        elif current_round == 26:
            ability(1,4)
            end_round(4)
        elif current_round == 27:
            wizard1.upgrade(['3-0-0','3-0-1','3-0-2'])
            end_round()
        elif current_round == 28:
            change_autostart()
        elif current_round == 31:
            wait(1)
            click(0.4208333333333, 0.462962962963)
            click(0.4947916666667, 0.5796296296296)
        elif current_round == 34:
            village1 = Monkey('village', 0.4328125, 0.4546296296296)
            village1.upgrade(['0-0-1'])
            druid_l = Monkey('druid', 0.3489583333333, 0.5601851851852)
        elif current_round == 35:
            change_autostart()
            druid_l.upgrade(['1-0-0','2-0-0'])
            change_autostart()
            end_round(3)
        elif current_round == 37:
            ability(1)
            village1.upgrade(['0-0-2'])
            druid_r = Monkey('druid', 0.5307291666667, 0.475)
            druid_r.upgrade(['1-0-0','2-0-0'])
        elif current_round == 39:
            druid_l.upgrade(['3-0-0','3-0-1'])
            druid1 = Monkey('druid', 0.4135416666667, 0.3824074074074)
            druid2 = Monkey('druid', 0.3489583333333, 0.4981481481481)
            forward(1)
            druid3 = Monkey('druid', 0.3828125, 0.4675925925926)
        elif current_round == 40:
            ability(1,4.35)
            forward(1)
        elif current_round == 41:
            village2 = Monkey('village', 0.4223958333333, 0.5490740740741)
            village2.upgrade(['0-0-1','0-0-2'])
        elif current_round == 42:
            druid_r.upgrade(['3-0-0','3-0-1','3-0-2'])
        elif current_round == 43:
            ability(1)
            druid_l.upgrade(['3-0-2'])
        elif current_round == 44:
            village2.upgrade(['1-0-2','2-0-2'])
            druid4 = Monkey('druid', 0.4713541666667, 0.5675925925926)
        elif current_round == 45:
            druid5 = Monkey('druid', 0.4703125, 0.5064814814815)
            druid6 = Monkey('druid', 0.4833333333333, 0.4472222222222)
            druid5.upgrade(['0-0-1','0-0-2','0-0-3','0-1-3'])
        elif current_round == 46:
            druid4.upgrade(['0-0-1','0-0-2','0-0-3','0-1-3'])
        elif current_round == 48:
            druid5.upgrade(['0-1-4'])
        elif current_round == 49:
            druid4.upgrade(['0-1-4'])
            druid6.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4'])
            druid3.upgrade(['0-0-1','0-0-2'])
        elif current_round == 50:
            druid3.upgrade(['0-0-3','0-1-3'])
            ability(1,9.5)
            druid3.upgrade(['0-1-4'])
        elif current_round == 52:
            hero.special(1, 0.559375, 0.6638888888889)
            ability(2)
        elif current_round == 53:
            druid2.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4'])
        elif current_round == 54:
            druid1.upgrade(['0-0-1','0-0-2','0-0-3','0-1-3'])
        elif current_round == 55:
            druid1.upgrade(['0-1-4'])
        elif current_round == 58:
            alch1 = Monkey('alch', 0.5057291666667, 0.5203703703704)
            alch1.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-1-0','4-2-0'])
        elif current_round == 59:
            alch2 = Monkey('alch', 0.346875, 0.4416666666667)
            alch2.upgrade(['1-0-0','2-0-0','3-0-0','3-1-0','3-2-0'])
        elif current_round == 61:
            village1.upgrade(['0-1-2','0-2-2'])
        elif current_round == 62:
            glue1 = Monkey('glue', 0.3770833333333, 0.3814814814815)
        elif current_round == 64:
            glue1.upgrade(['0-0-1','0-0-2','0-0-3','0-1-3'])
            glue1.target('strong')
        elif current_round == 71:
            ability(2, xy=(0.5588541666667, 0.6472222222222), delay=1)
        elif current_round == 79:
            hero.special(1, 0.3140625, 0.6583333333333)
            wait(20.5)
            ability(2, xy=(0.5588541666667, 0.6472222222222), delay=1)
        elif current_round == 80:
            hero.special(1, 0.5609375, 0.6601851851852)
        elif current_round == 81:
            wait(8)
            move_cursor(0.3140625, 0.6583333333333)
            ability(1,11)
            ability(2,13.5, xy=(0.3140625, 0.6583333333333), delay=1)
        elif current_round == 82:
            ability(1,13)
        elif current_round == 83:
            druid5.upgrade(['0-1-5'])
        elif current_round == 85:
            glue1.upgrade(['0-2-3','0-2-4'])
            village1.upgrade(['0-3-2'])
        elif current_round == 86:
            ability(2, xy=(0.559375, 0.6416666666667), delay=1)
        elif current_round == 88:
            engi1.upgrade(['0-1-0','0-2-0','0-3-0'])
        elif current_round == 90:
            ability(2, xy=(0.5583333333333, 0.6231481481481), delay=1)
        elif current_round == 92:
            engi1.upgrade(['0-4-0'])
        elif current_round == 93:
            ability(3, xy=(0.4770833333333, 0.4842592592593))
        elif current_round == 94:
            change_autostart()
            ability(3, 5, xy=(0.4770833333333, 0.4842592592593))
            ninja1 = Monkey('ninja', 0.3875, 0.7083333333333)
            ninja1.upgrade(['0-1-0','0-2-0','0-3-0','0-4-0'])
            ice1 = Monkey('ice', 0.2927083333333, 0.4416666666667)
            ice1.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-1-0'])
            wait(5)
            change_autostart()
            end_round(2)
        elif current_round == 95:
            ability(3,10, xy=(0.4770833333333, 0.4842592592593))
            ability(4,12)
        elif current_round == 96:
            ability(2, xy=(0.5588541666667, 0.6194444444444), delay=1)
            sniper1.upgrade(['2-0-0','3-0-0','4-0-0','4-1-0','4-2-0'])
        elif current_round == 97:
            ability(3, 4, xy=(0.4770833333333, 0.4842592592593))
        elif current_round == 98:
            mermonkey = Monkey('mermonkey', 0.2859375, 0.6194444444444)
            mermonkey.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','1-0-4','2-0-4'])
            mermonkey.special(1, 0.3276041666667, 0.6944444444444)
            hero.special(1, 0.3244791666667, 0.7185185185185)
        elif current_round == 99:
            ability(4,2)
            ability(3,3, xy=(0.4770833333333, 0.4842592592593))
        elif current_round == 100:
            ability(2)
            ability(1,6)