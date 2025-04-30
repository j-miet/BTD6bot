"""
[Hero] Sauda
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 5-2-2
boomer 0-2-4
tack 2-0-4
glue 2-2-4
ice 5-2-0

wizard 0-3-2
alch 3-2-1

spike 4-2-2
village 3-2-2
engineer 1-3-2
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
            dart1 = Monkey('dart', 0.1505208333333, 0.7574074074074)
            dart2 = Monkey('dart', 0.4151041666667, 0.8796296296296)
            dart3 = Monkey('dart', 0.6942708333333, 0.9731481481481)
        elif current_round == 7:
            change_autostart()
            wait(8.5)
            click(0.5651041666667, 0.3425925925926)
            dart4 = Monkey('dart', 0.8057291666667, 0.4759259259259)
            dart3.target('strong')
            dart1.upgrade(['0-1-0'])
            end_round()
        elif current_round == 8:
            dart5 = Monkey('dart', 0.4151041666667, 0.8268518518519)
            end_round()
        elif current_round == 9:
            end_round(9)
        elif current_round == 10:
            wait(14)
            click(0.3057291666667, 0.3416666666667)
            engi1 = Monkey('engineer', 0.1140625, 0.7527777777778)
            end_round(3)
        elif current_round == 11:
            end_round(9)
        elif current_round == 12:
            end_round(9)
        elif current_round == 13:
            hero = Hero(0.7505208333333, 0.3138888888889)
            dart4.target('strong')
            dart2.upgrade(['0-1-0'])
            dart2.target('strong')
            end_round()
        elif current_round == 14:
            dart2.upgrade(['0-2-0'])
            end_round()
        elif current_round == 15:
            wait(4)
            click(0.5651041666667, 0.3425925925926)
            click(0.3057291666667, 0.3416666666667)
            end_round(5)
        elif current_round == 16:
            dart2.upgrade(['0-3-0'])
            end_round(2)
        elif current_round == 17:
            end_round(5)
        elif current_round == 18:
            end_round(12)
        elif current_round == 19:
            engi1.upgrade(['1-0-0'])
            glue1 = Monkey('glue', 0.8119791666667, 0.8694444444444)
            glue1.upgrade(['0-1-0'])
            glue1.target('strong')
            end_round()
        elif current_round == 20:
            end_round(6)
        elif current_round == 21:
            glue1.upgrade(['1-1-0'])
            end_round(7)
        elif current_round == 22:
            glue1.upgrade(['2-1-0'])
            glue2 = Monkey('glue', 0.1848958333333, 0.8768518518519)
            glue2.target('strong')
            end_round()
        elif current_round == 23:
            glue2.upgrade(['0-1-0'])
            end_round(5)
        elif current_round == 24:
            click(0.3057291666667, 0.3416666666667)
            end_round(5)
        elif current_round == 25:
            glue2.upgrade(['1-1-0'])
            tack1 = Monkey('tack', 0.4692708333333, 0.8712962962963)
            tack1.upgrade(['0-0-1','0-0-2'])
            end_round(2)
        elif current_round == 26:
            glue2.upgrade(['2-1-0'])
            end_round()
        elif current_round == 27:
            alch1 = Monkey('alch', 0.5494791666667, 0.8231481481481)
            alch1.target('strong')
            end_round()
        elif current_round == 28:
            end_round(6)
        elif current_round == 29:
            end_round(7)
        elif current_round == 30:
            spike1 = Monkey('spike', 0.5265625, 0.4342592592593)
            end_round()
        elif current_round == 31:
            end_round(8)
        elif current_round == 32:
            spike2 = Monkey('spike', 0.0953125, 0.262037037037)
            end_round()
        elif current_round == 33:
            end_round(11)
        elif current_round == 34:
            spike2.upgrade(['0-0-1','0-0-2'])
            spike2.target('close')
            tack1.upgrade(['0-0-3'])
            end_round(2)
        elif current_round == 35:
            tack1.upgrade(['1-0-3','2-0-3'])
            dart4.upgrade(['1-0-0'])
            alch1.upgrade(['1-0-0'])
            end_round(3)
        elif current_round == 36:
            end_round(10)
        elif current_round == 37:
            alch1.target('close')
            wait(11)
            click(0.5651041666667, 0.3425925925926)
            end_round(5)
        elif current_round == 38:
            ability(1,9.75)
            tack1.upgrade(['2-0-4'])
            end_round(2)
        elif current_round == 39:
            wait(17)
            alch1.upgrade(['2-0-0','3-0-0'])
            end_round()
        elif current_round == 40:
            end_round(4)
        elif current_round == 41:
            spike1.upgrade(['1-0-0'])
            spike2.upgrade(['1-0-2'])
            dart2.upgrade(['0-3-1','0-3-2'])
            dart4.upgrade(['2-0-0','3-0-0','3-0-1','3-0-2'])
            end_round(2)
        elif current_round == 42:
            wait(2)
            click(0.5651041666667, 0.3425925925926)
            click(0.3057291666667, 0.3416666666667)
            end_round(4)
        elif current_round == 43:
            wizard2 = Monkey('wizard', 0.0994791666667, 0.3546296296296)
            wizard2.upgrade(['0-1-0'])
            ability(1,4.5)
            wizard1 = Monkey('wizard', 0.7494791666667, 0.4027777777778)
            wizard1.upgrade(['0-1-0','0-1-1','0-1-2'])
            end_round()
        elif current_round == 44:
            alch1.upgrade(['3-1-0','3-2-0'])
            alch1.target('strong')
            end_round(5)
        elif current_round == 45:
            wizard2.upgrade(['0-1-1','0-1-2'])
            wait(20)
            wizard2.upgrade(['0-2-2'])
            wizard1.upgrade(['0-2-2'])
            end_round()
        elif current_round == 46:
            end_round(8)
        elif current_round == 47:
            wait(1.5)
            click(0.5651041666667, 0.3425925925926)
            click(0.3057291666667, 0.3416666666667)
            end_round(8)
        elif current_round == 48:
            wizard2.upgrade(['0-3-2'])
            end_round(11)
        elif current_round == 49:
            dart4.upgrade(['4-0-2'])
            dart4.target('first')
            ice1 = Monkey('ice', 0.4036458333333, 0.9287037037037)
            ice1.upgrade(['1-0-0','2-0-0','3-0-0','3-1-0'])
            end_round(10)
        elif current_round == 50:
            ability(1,1.5)
            village1 = Monkey('village', 0.4786458333333, 0.9435185185185)
            village1.upgrade(['1-0-0','2-0-0','2-0-1','2-0-2'])
            end_round(3)
        elif current_round == 51:
            end_round(11)
        elif current_round == 52:
            ice1.upgrade(['4-1-0'])
            end_round(10)
        elif current_round == 53:
            end_round(14)
        elif current_round == 54:
            wait(3.5)
            click(0.3057291666667, 0.3416666666667)    
            alch2 = Monkey('alch', 0.0317708333333, 0.1472222222222)
            alch2.upgrade(['1-0-0','2-0-0','3-0-0'])
            village1.upgrade(['3-0-2'])
            end_round(5)
        elif current_round == 55:
            spike2.upgrade(['2-0-2','3-0-2'])
            end_round(2)
        elif current_round == 56:
            end_round(8)
        elif current_round == 57:
            end_round(12)
        elif current_round == 58:
            wizard1.upgrade(['0-3-2'])
            end_round(20)
        elif current_round == 59:
            dart5.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-1-0','4-2-0'])
            end_round(10)
        elif current_round == 60:
            dart6 = Monkey('dart', 0.1010416666667, 0.412037037037)
            dart6.upgrade(['1-0-0','2-0-0','3-0-0','3-1-0','3-2-0'])
            end_round(2)
        elif current_round == 61:
            change_autostart()
            dart6.upgrade(['4-2-0'])
        elif current_round == 63:
            spike1.upgrade(['2-0-0','3-0-0','3-1-0'])
        elif current_round == 64:
            spike1.upgrade(['3-2-0'])
        elif current_round == 70:
            spike2.upgrade(['4-2-0'])
        elif current_round == 71:
            alch2.upgrade(['3-0-1'])
        elif current_round == 72:
            alch3 = Monkey('alch', 0.4875, 0.4657407407407)
            alch3.upgrade(['1-0-0','2-0-0'])
        elif current_round == 73:
            alch3.upgrade(['3-0-0','3-0-1'])
        elif current_round == 75:
            wait(8)
            click(0.3057291666667, 0.3416666666667)
        elif current_round == 76:
            ability(2,0.75)
        elif current_round == 78:
            ability(2,4)
            ability(2,26.5)
        elif current_round == 79:
            dart5.upgrade(['5-2-0'])
            alch4 = Monkey('alch', 0.7286458333333, 0.2685185185185)
            village2 = Monkey('village', 0.7421875, 0.1981481481481)
            village2.upgrade(['0-0-1','0-0-2','1-0-2','2-0-2'])
        elif current_round == 81:
            alch4.upgrade(['1-0-0','2-0-0','3-0-0','3-1-0','3-2-0'])
            glue3 = Monkey('glue', 0.6708333333333, 0.2305555555556)
            glue3.upgrade(['0-0-1','0-0-2','0-0-3','0-1-3'])
            glue3.target('strong')
        elif current_round == 82:
            glue3.upgrade(['0-2-3','0-2-4'])
        elif current_round == 83:
            boomer1 = Monkey('boomer', 0.6697916666667, 0.287962962963)
            boomer1.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
            boomer1.target('strong')
        elif current_round == 84:
            boomer2 = Monkey('boomer', 0.6697916666667, 0.3490740740741)
            boomer2.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
            boomer2.target('strong')
        elif current_round == 85:
            alch5 = Monkey('alch', 0.378125, 0.8212962962963)
            alch5.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif current_round == 86:
            glue4 = Monkey('glue', 0.3682291666667, 0.9231481481481)
            glue4.upgrade(['0-0-1','0-0-2'])
            glue4.target('strong')
        elif current_round == 87:
            glue4.upgrade(['0-0-3','0-1-3','0-2-3'])
        elif current_round == 88:
            engi2 = Monkey('engineer', 0.8078125, 0.1527777777778)
            engi2.upgrade(['0-1-0','0-2-0','0-3-0','0-3-1','0-3-2'])
            engi2.special(1, 0.7786458333333, 0.4287037037037)
        elif current_round == 89:
            village2.upgrade(['3-0-2'])
        elif current_round == 91:
            glue4.upgrade(['0-2-4'])
        elif current_round == 95:
            ability(2,3)
        elif current_round == 97:
            ice1.upgrade(['5-1-0','5-2-0'])
        elif current_round == 98:
            change_autostart()
            wait(16)
            click(0.3057291666667, 0.3416666666667)
            village3 = Monkey('village', 0.3036458333333, 0.875)
            village3.upgrade(['0-1-0','0-2-0','1-2-0'])
            end_round(3)
        elif current_round == 99:
            tack2 = Monkey('tack', 0.5505208333333, 0.9731481481481)
            tack2.upgrade(['1-0-0','2-0-0','2-0-1','2-0-2','2-0-3','2-0-4'])
            tack3 = Monkey('tack', 0.5505208333333, 0.8787037037037)
            tack3.upgrade(['1-0-0','2-0-0','2-0-1','2-0-2','2-0-3','2-0-4'])
            change_autostart()
            end_round()
        elif current_round == 100:
            ability(1,2)
            ability(2,6)