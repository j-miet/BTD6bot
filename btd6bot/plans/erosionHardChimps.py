"""
[Hero] Psi
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-1
bomb 5-2-0
glue 0-1-3

sniper 1-2-5
sub 2-0-2

ninja 0-0-0
alch 4-2-0
druid 3-0-2

spike 0-4-2
village 2-4-2
_______________________________________
Gameplay-wise, should be viable for black bordering.

For late game data (90+), bot might skip ahead and begin executing commands for upcoming data.
Reason is there's lot of projectiles/bloons moving around round label, which can cause false positives.
This should not matter, as long as 99 => 100 is detected normally; 100 requires abilities and if bot uses them earlier than intended, you will 100% lose.
Another harmless effect is incorrectly saved round times: some display too short and other too long round durations.

Should issues rise with 99 => 100 transition, solution is to use manual round ending with end_round() command. With it enabled, bot won't begin to search for the next round until countdown ends.
"""

from._plan_imports import *

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:
            sub1 = Monkey('sub', 0.2177083333333, 0.8157407407407)
            dart1 = Monkey('dart', 0.1911458333333, 0.5555555555556)
            forward()
            dart1.upgrade(['0-0-1'])
        elif round == 9:
            sub1.upgrade(['0-0-1'])
        elif round == 13:
            sub1.upgrade(['0-0-2'])
        elif round == 18:
            hero = Hero(0.6489583333333, 0.0601851851852)
            sub1.upgrade(['1-0-2'])
        elif round == 21:
            sub1.upgrade(['2-0-2'])
        elif round == 25:
            sniper1 = Monkey('sniper', 0.4729166666667, 0.0435185185185)
            sniper1.upgrade(['1-0-0'])
            sniper1.target('strong')
        elif round == 27:
            bomb = Monkey('bomb', 0.8348958333333, 0.312037037037)
            sniper2 = Monkey('sniper', 0.8380208333333, 0.2546296296296)
            sniper2.upgrade(['0-1-0','0-2-0'])
        elif round == 30:
            sniper2.upgrade(['0-2-1'])
        elif round == 31:
            sniper2.upgrade(['0-2-2'])
        elif round == 35:
            sniper2.upgrade(['0-2-3'])
            hero.target('strong')
        elif round == 36:
            ninja = Monkey('ninja', 0.1723958333333, 0.2564814814815)
        elif round == 39:
            sniper2.upgrade(['0-2-4'])
        elif round == 41:
            alch = Monkey('alch', 0.8369791666667, 0.2027777777778)
            alch.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif round == 43:
            alch.upgrade(['3-1-0','3-2-0'])
        elif round == 50:
            sniper2.upgrade(['0-2-5'])
        elif round == 53:
            village = Monkey('village', 0.8130208333333, 0.112037037037)
        elif round == 54:
            village.upgrade(['1-0-0','2-0-0'])
        elif round == 57:
            bomb.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-1-0','4-2-0'])
        elif round == 58:
            glue = Monkey('glue', 0.7036458333333, 0.112962962963)
            glue.target('strong')
        elif round == 61:
            glue.upgrade(['0-0-1','0-0-2','0-0-3','0-1-3'])
        elif round == 62:
            druid = Monkey('druid', 0.6890625, 0.3842592592593)
            druid.upgrade(['1-0-0','2-0-0','3-0-0','3-0-1','3-0-2'])
        elif round == 77:
            alch.upgrade(['4-2-0'])
        elif round == 78:
            ability(2,3.5)
        elif round == 80:
            ability(1,5)
        elif round == 81:
            ability(1,11)
            ability(2,16)
        elif round == 82:
            ability(1,12)
            ability(2,19)
        elif round == 83:
            ability(1,10)
        elif round == 84:
            ability(1,8)
            ability(2,10)
            bomb.upgrade(['5-2-0'])
        elif round == 86:
            village.upgrade(['2-1-0','2-2-0'])
        elif round == 89:
            ability(1,8)
            village.upgrade(['2-3-0'])
        elif round == 95:
            village.upgrade(['2-4-0'])
        elif round == 96:
            spike1 = Monkey('spike', 0.7432291666667, 0.1055555555556)
            spike1.upgrade(['0-1-0','0-2-0','0-3-0','0-3-1','0-3-2'])
            spike1.target('smart')
            ability(2)
            ability(3)
            spike1.upgrade(['0-4-2'])
        elif round == 97:
            spike2 = Monkey('spike', 0.6973958333333, 0.0342592592593)
            spike2.upgrade(['0-0-1','0-0-2','0-1-2'])
            ability(3)
        elif round == 98:
            spike2.upgrade(['0-2-2','0-3-2'])
        elif round == 99:
            spike2.upgrade(['0-4-2'])
            change_autostart()
            end_round(12)
        elif round == 100:
            change_autostart()
            ability(3,2)
            ability(4,3)
            ability(4,4)            