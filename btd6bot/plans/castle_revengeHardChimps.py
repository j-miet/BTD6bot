"""
[Hero] Gwen
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 3-2-0
tack 2-0-3

sniper 5-5-5
sub 0-0-0

alch 5-2-0

village 2-0-2
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
            dart1 = Monkey('dart', 0.6260416666667, 0.2555555555556)
            dart2 = Monkey('dart', 0.5994791666667, 0.5212962962963)
            dart3 = Monkey('dart', 0.6114583333333, 0.7231481481481)
        elif current_round == 8:
            sub = Monkey('sub', 0.1494791666667, 0.287962962963)
        elif current_round == 9:
            dart4 = Monkey('dart', 0.1401041666667, 0.7287037037037)
        elif current_round == 11:
            sniper1 = Monkey('sniper',  0.5244791666667, 0.4157407407407)
            sniper1.target('strong')
        elif current_round == 13:
            sniper2 = Monkey('sniper',  0.5234375, 0.4675925925926)
            sniper2.target('strong')
        elif current_round == 14:
            sniper3 = Monkey('sniper',  0.5229166666667, 0.5222222222222)
            sniper3.target('strong')
        elif current_round == 17:
            hero = Hero(0.5651041666667, 0.4935185185185)
            hero.target('strong')
        elif current_round == 18:
            dart3.upgrade(['1-0-0'])
        elif current_round == 19:
            dart3.upgrade(['2-0-0'])
        elif current_round == 20:
            dart3.upgrade(['3-0-0'])
        elif current_round == 21:
            dart3.upgrade(['3-1-0','3-2-0'])
        elif current_round == 23:
            sniper1.upgrade(['0-0-1'])
        elif current_round == 24:
            sniper1.upgrade(['0-1-1'])
        elif current_round == 26:
            sniper1.upgrade(['0-1-2'])
        elif current_round == 27:
            sniper1.upgrade(['0-2-2'])
            sniper1.target('first')
        elif current_round == 28:
            sniper3.upgrade(['1-0-0'])
        elif current_round == 34:
            ability(1,1)
            sniper1.upgrade(['0-2-3'])
        elif current_round == 36:
            ability(1,5)
        elif current_round == 38:
            ability(1,3)
        elif current_round == 39: 
            sniper1.upgrade(['0-2-4'])
        elif current_round == 40:
            ability(1)
        elif current_round == 41:
            village = Monkey('village', 0.5114583333333, 0.3296296296296)
            village.upgrade(['0-0-1','0-0-2'])
            sniper2.upgrade(['0-1-0','0-2-0'])
        elif current_round == 42:
            sniper2.upgrade(['0-3-0'])
            sniper2.target('first')
        elif current_round == 43:
            sniper2.upgrade(['0-3-1','0-3-2'])
        elif current_round == 44:
            alch = Monkey('alch',  0.4911458333333, 0.4333333333333)
            alch.upgrade(['1-0-0','2-0-0'])
        elif current_round == 45:
            alch.upgrade(['3-0-0','3-1-0','3-2-0'])
        elif current_round == 47:
            ability(1)
            alch.upgrade(['4-2-0'])
        elif current_round == 50:
            sniper2.upgrade(['0-4-2'])
        elif current_round == 51:
            village.upgrade(['1-0-2','2-0-2'])
        elif current_round == 59:
            sniper1.upgrade(['0-2-5'])
        elif current_round == 69:
            sniper2.upgrade(['0-5-2'])
            sniper2.target('first')
        elif current_round == 71:
            sniper3.upgrade(['1-0-0','2-0-0','3-0-0','3-1-0','3-2-0'])
        elif current_round == 75:
            sniper3.upgrade(['4-2-0'])
        elif current_round == 83:
            ability(1,8)
            ability(3,13)
        elif current_round == 89:
            ability(1,1)
            alch.upgrade(['5-2-0'])
            ability(3)
        elif current_round == 90:
            sniper4 = Monkey('sniper',  0.4734375, 0.3814814814815)
            ability(1,3)
        elif current_round == 91:
            sniper4.upgrade(['0-1-0','0-2-0','0-3-0','0-3-1','0-3-2'])
            sniper5 = Monkey('sniper',  0.4880208333333, 0.5157407407407)
        elif current_round == 92:
            sniper5.upgrade(['0-1-0','0-2-0','0-3-0','0-3-1','0-3-2'])
            sniper6 = Monkey('sniper', 0.4546875, 0.4935185185185)
        elif current_round == 93:
            sniper6.upgrade(['0-1-0','0-2-0','0-3-0','0-3-1','0-3-2'])
        elif current_round == 95:
            ability(1,10)
            ability(3,12)
        elif current_round == 99:
            sniper3.upgrade(['5-2-0'])
            tack = Monkey('tack', 0.5911458333333, 0.3027777777778)
        elif current_round == 100:
            tack.upgrade(['0-0-1','0-0-2','0-0-3','1-0-3','2-0-3'])