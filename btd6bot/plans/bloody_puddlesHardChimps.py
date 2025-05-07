"""
[Hero] Gwen
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-2
boomer 2-0-4
tack 2-0-4
glue 0-2-4
ice 4-1-0

sniper 4-5-5
sub 2-0-3

wizard 3-0-2
ninja 1-0-4
alch 4-2-1

village 3-2-2
_______________________________________
Minimal rng involved: round 23 is the most common to fail although still relatively rare.
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
            sub1 = Monkey('sub', 0.5244791666667, 0.8638888888889)
            dart1 = Monkey('dart', 0.1828125, 0.6361111111111)
            dart1.target('last')
            forward()
            end_round(10)
        elif current_round == 7:
            dart2 = Monkey('dart', 0.2078125, 0.4694444444444)
            dart2.target('strong')
            dart1.target('first')
            end_round(12)
        elif current_round == 8:
            sub2 = Monkey('sub', 0.6234375, 0.1787037037037)
            end_round()
        elif current_round == 9:
            end_round(9)
        elif current_round == 10:
            sniper1 = Monkey('sniper', 0.3651041666667, 0.1805555555556)
            end_round(7)
        elif current_round == 11:
            dart3 = Monkey('dart', 0.4817708333333, 0.525)
            wait(5)
            sniper1.target('strong')
            end_round()
        elif current_round == 12:
            end_round(9)
        elif current_round == 13:
            sniper2 = Monkey('sniper', 0.3651041666667, 0.1277777777778)
            sniper2.target('strong')
            end_round(8)
        elif current_round == 14:
            wait(12)
            sniper3 = Monkey('sniper', 0.1619791666667, 0.0268518518519, placement_check=False)
            sniper3.target('strong', cpos_x=0.1291666666667, cpos_y=0.0601851851852)
            end_round()
        elif current_round == 15:
            sub2.upgrade(['1-0-0'])
            end_round(9)
        elif current_round == 16:
            wait(8)
            sniper2.target('first')
            end_round()
        elif current_round == 17:
            sub2.upgrade(['2-0-0'])
            wait(4)
            sniper2.target('strong')
            end_round()
        elif current_round == 18:
            sub2.upgrade(['2-0-1'])
            end_round()
        elif current_round == 19:
            end_round(8)
        elif current_round == 20:
            dart4 = Monkey('dart', 0.6802083333333, 0.8009259259259)
            dart5 = Monkey('dart', 0.653125, 0.5305555555556)
            end_round()
        elif current_round == 21:
            sniper1.upgrade(['1-0-0'])
            end_round()
        elif current_round == 22:
            dart6 = Monkey('dart', 0.3604166666667, 0.6972222222222)
            dart6.target('strong')
            dart3.target('strong')
            end_round()
        elif current_round == 23:
            sniper2.upgrade(['0-1-0'])
            end_round(4)
        elif current_round == 24:
            end_round(5)
        elif current_round == 25:
            end_round(10)
        elif current_round == 26:
            end_round(7)
        elif current_round == 27:
            sub2.upgrade(['2-0-2'])
            end_round(7)
        elif current_round == 28:
            hero = Hero(0.3729166666667, 0.2361111111111)
            end_round()
        elif current_round == 29:
            end_round(7)
        elif current_round == 30:
            end_round(7)
        elif current_round == 31:
            ability(1,2.5)
            end_round(6)
        elif current_round == 32:
            dart4.upgrade(['0-0-1','0-0-2'])
            end_round(9)
        elif current_round == 33:
            wizard1 = Monkey('wizard', 0.2770833333333, 0.4138888888889)
            wizard1.upgrade(['1-0-0','2-0-0'])
            end_round(7)
        elif current_round == 34:
            wizard1.upgrade(['3-0-0'])
            end_round(3)
        elif current_round == 35:
            wizard1.upgrade(['3-0-1','3-0-2'])
            wait(7)
            sub2.target('close')
            end_round()
        elif current_round == 36:
            wait(9)
            sub2.target('first')
            sub2.upgrade(['2-0-3'])
            sniper3.upgrade(['1-0-0'])
            end_round()
        elif current_round == 37:
            end_round(17)
        elif current_round == 38:
            end_round(12)
        elif current_round == 39:
            ability(1,8)
            alch1 = Monkey('alch', 0.6104166666667, 0.2324074074074)
            glue1 = Monkey('glue', 0.26875, 0.3564814814815)
            glue1.upgrade(['1-0-0','1-1-0'])
            glue2 = Monkey('glue', 0.2510416666667, 0.312037037037)
            glue2.upgrade(['1-0-0','1-1-0'])
            glue2.target('last')
            alch1.upgrade(['1-0-0','2-0-0','3-0-0'])
            end_round()
        elif current_round == 40:
            end_round(5)
        elif current_round == 41:
            village1 = Monkey('village', 0.31875, 0.2037037037037)
            village1.upgrade(['0-0-1','0-0-2'])
            sniper2.upgrade(['0-2-0','0-2-1'])
            sniper2.target('first')
            end_round()
        elif current_round == 42:
            change_autostart()
            sniper2.upgrade(['0-2-2'])
        elif current_round == 44:
            sniper2.upgrade(['0-3-2'])
            alch2 = Monkey('alch', 0.3666666666667, 0.0759259259259)
        elif current_round == 45:
            alch2.upgrade(['1-0-0','2-0-0','3-0-0','3-0-1'])
        elif current_round == 46:
            sniper1.upgrade(['1-0-1','1-0-2'])
        elif current_round == 48:
            sniper1.upgrade(['1-0-3','2-0-3'])
        elif current_round == 49:
            village1.upgrade(['1-0-2','2-0-2'])
        elif current_round == 52:
            sniper2.upgrade(['0-4-2'])
            glue1.target('strong')
            glue2.target('strong')
        elif current_round == 60:
            ability(3,3.75)
        elif current_round == 61:
            sniper2.upgrade(['0-5-2'])
            sniper2.target('first')
        elif current_round == 63:
            sniper1.upgrade(['2-0-4'])
        elif current_round == 64:
            sniper1.target('first')
        elif current_round == 65:
            click(0.4666666666667, 0.6453703703704)
            click(0.525, 0.7175925925926)
            wait(1)
            click(0.3760416666667, 0.4157407407407)
            click(0.4260416666667, 0.5398148148148)
            village2 = Monkey('village', 0.3932291666667, 0.3101851851852)
        elif current_round == 66:
            village2.upgrade(['0-0-1','0-0-2'])
            sniper3 = Monkey('sniper', 0.428125, 0.1287037037037)
        elif current_round == 67:
            sniper3.upgrade(['0-1-0','0-2-0'])
        elif current_round == 68:
            sniper3.upgrade(['1-2-0','2-2-0'])
        elif current_round == 69:
            sniper3.upgrade(['3-2-0'])
            sniper3.target('strong')
        elif current_round == 73:
            sniper3.upgrade(['4-2-0'])
            alch3 = Monkey('alch', 0.4333333333333, 0.0768518518519)
        elif current_round == 74:
            alch3.upgrade(['1-0-0','2-0-0','3-0-0','3-0-1'])
            sniper4 = Monkey('sniper', 0.4333333333333, 0.1805555555556)
        elif current_round == 75:
            sniper4.upgrade(['0-0-1','0-0-2','0-1-2','0-2-2'])
        elif current_round == 77:
            sniper4.upgrade(['0-3-2'])
            alch4 = Monkey('alch', 0.465625, 0.1953703703704)
            alch4.upgrade(['1-0-0','2-0-0','3-0-0','3-1-0','3-2-0'])
        elif current_round == 81:
            sniper1.upgrade(['2-0-5'])
            sniper5 = Monkey('sniper', 0.4572916666667, 0.2472222222222)
        elif current_round == 82:
            sniper5.upgrade(['0-1-0','0-2-0','0-3-0','0-3-1','0-3-2'])
            alch4.upgrade(['4-2-0'])
        elif current_round == 83:
            sniper6 = Monkey('sniper', 0.4296875, 0.3583333333333)
            sniper6.upgrade(['0-1-0','0-2-0','0-3-0','0-3-1','0-3-2'])
            alch5 = Monkey('alch', 0.4015625, 0.387037037037)
        elif current_round == 84:
            alch5.upgrade(['1-0-0','2-0-0','3-0-0','3-1-0','3-2-0'])
            glue3 = Monkey('glue', 0.303125, 0.2731481481481)
            ice1 = Monkey('ice', 0.3479166666667, 0.2768518518519)
            tack1 = Monkey('tack', 0.3239583333333, 0.3148148148148)
        elif current_round == 85:
            tack2 = Monkey('tack', 0.3375, 0.362962962963)
            sniper7 = Monkey('sniper', 0.3677083333333, 0.3861111111111)
            sniper7.upgrade(['0-1-0','0-2-0','0-3-0','0-3-1','0-3-2'])
            alch5.upgrade(['4-2-0'])
        elif current_round == 86:
            glue3.target('strong')
            glue3.upgrade(['0-0-1','0-0-2','0-1-2','0-2-2'])
        elif current_round == 87:
            glue3.upgrade(['0-2-3'])
        elif current_round == 88:
            glue3.upgrade(['0-2-4'])
        elif current_round == 89:
            village2.upgrade(['0-1-2','0-2-2'])
        elif current_round == 91:
            boomer1 = Monkey('boomer', 0.2703125, 0.1805555555556)
            boomer1.target('strong')
            boomer1.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','1-0-4','2-0-4'])
        elif current_round == 92:
            boomer2 = Monkey('boomer', 0.2234375, 0.275)
            boomer2.target('strong')
            boomer2.upgrade(['0-0-1','0-0-2','0-0-3','1-0-3','2-0-3'])
        elif current_round == 93:
            ability(3,2.5)
            boomer2.upgrade(['2-0-4'])
        elif current_round == 94: 
            ice1.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-1-0'])
        elif current_round == 95:
            village1.upgrade(['3-0-2'])
            ability(3,12)
        elif current_round == 96:
            glue4 = Monkey('glue', 0.5703125, 0.6453703703704)
            glue4.target('strong')
            glue4.upgrade(['0-0-1','0-0-2','0-0-3','0-1-3','0-2-3'])
            boomer3 = Monkey('boomer', 0.2098958333333, 0.2175925925926)
            boomer3.target('strong')
            boomer3.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','1-0-4','2-0-4'])
        elif current_round == 97:
            tack1.upgrade(['1-0-0','2-0-0','2-0-1','2-0-2','2-0-3','2-0-4'])
            tack2.upgrade(['1-0-0','2-0-0','2-0-1','2-0-2'])
        elif current_round == 98:
            tack2.upgrade(['2-0-3','2-0-4'])
            ninja = Monkey('ninja', 0.2401041666667, 0.387962962963)
            ninja.upgrade(['1-0-0','1-0-1','1-0-2','1-0-3','1-0-4'])
        elif current_round == 99:
            alch6 = Monkey('alch', 0.3359375, 0.4231481481481)
        elif current_round == 100:
            alch6.upgrade(['1-0-0','2-0-0','3-0-0','3-1-0','3-2-0'])
            ability(3,7.5)