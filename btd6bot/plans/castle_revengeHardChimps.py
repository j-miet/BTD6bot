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
On round 83 hero is manually leveled up to in order to increase consistency.
Some late rounds like 87, 89, 90 and 95 might also cause issues if gwen's heat up timing is off.
"""

from._plan_imports import *

def play(rounds):
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start, rounds[2])
        if current_round == BEGIN:
            dart1 = Monkey('dart', 0.6260416666667, 0.2555555555556)
            dart2 = Monkey('dart', 0.5984375, 0.5185185185185)
            dart3 = Monkey('dart', 0.6114583333333, 0.7231481481481)
        elif current_round == 8:
            sub = Monkey('sub', 0.1494791666667, 0.287962962963)
        elif current_round == 9:
            dart4 = Monkey('dart', 0.1401041666667, 0.7287037037037)
        elif current_round == 11:
            sniper1 = Monkey('sniper', 0.5276041666667, 0.3981481481481)
            sniper1.target('strong')
        elif current_round == 13:
            sniper2 = Monkey('sniper', 0.5255208333333, 0.45)
            sniper2.target('strong')
        elif current_round == 14:
            sniper3 = Monkey('sniper', 0.5223958333333, 0.5037037037037)
            sniper3.target('strong')
        elif current_round == 17:
            hero = Hero(0.5651041666667, 0.4944444444444)
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
            village = Monkey('village', 0.5005208333333, 0.3314814814815)
            village.upgrade(['0-0-1','0-0-2'])
            sniper2.upgrade(['0-1-0','0-2-0'])
        elif current_round == 42:
            sniper2.upgrade(['0-3-0'])
            sniper2.target('first')
        elif current_round == 43:
            sniper2.upgrade(['0-3-1','0-3-2'])
        elif current_round == 44:
            alch = Monkey('alch',  0.4921875, 0.4314814814815)
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
        elif current_round == 82:
            ability(1,5)
        elif current_round == 83:
            click(0.5625, 0.4935185185185)
            wait(1)
            click(0.11875, 0.6398148148148)
            wait(1)
            click(0.3104166666667, 0.4425925925926)
            ability(1,8)
            ability(3,13)
        elif current_round == 87:
            ability(1,7)
        elif current_round == 89:
            ability(1,1)
            alch.upgrade(['5-2-0'])
        elif current_round == 90:
            ability(1,2)
            ability(3)
        elif current_round == 91:
            sniper4 = Monkey('sniper', 0.4682291666667, 0.3861111111111)
            sniper4.upgrade(['0-1-0','0-2-0','0-3-0','0-3-1','0-3-2'])
            sniper5 = Monkey('sniper', 0.4869791666667, 0.4916666666667)
        elif current_round == 92:
            sniper5.upgrade(['0-1-0','0-2-0','0-3-0','0-3-1','0-3-2'])
            sniper6 = Monkey('sniper', 0.4515625, 0.4898148148148)
        elif current_round == 93:
            sniper6.upgrade(['0-1-0','0-2-0','0-3-0','0-3-1','0-3-2'])
        elif current_round == 95:
            ability(1,10)
            ability(3,12)
            ability
        elif current_round == 99:
            ability(3,1)
            sniper3.upgrade(['5-2-0'])
            tack = Monkey('tack', 0.5927083333333, 0.3)
        elif current_round == 100:
            tack.upgrade(['0-0-1','0-0-2','0-0-3','1-0-3','2-0-3'])