"""
[Hero] Obyn
[Monkey Knowledge] Yes
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0
boomer 0-2-4
bomb 4-2-0
tack 2-0-4
ice 5-1-0
glue 0-2-4
desperado 0-0-0

sniper 1-1-0

wizard 5-3-2
alch 3-0-1
druid 0-0-0
mermonkey 4-3-2

village 3-0-2
_______________________________________
Created with all monkey knowledge unlocked.
"""

from._plan_imports import *

def play(rounds):
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start, rounds[2])
        if current_round == BEGIN:
            desp1 = Monkey('desperado', 0.3151041666667, 0.5111111111111)
            desp2 = Monkey('desperado', 0.5505208333333, 0.5166666666667)
        elif current_round == 4:
            dart1 = Monkey('dart', 0.3505208333333, 0.4675925925926)
        elif current_round == 5:
            dart2 = Monkey('dart', 0.5161458333333, 0.5361111111111)
        elif current_round == 7:
            mermonkey1 = Monkey('mermonkey', 0.2859375, 0.287962962963)
            dart1.target('close')
            dart2.target('close')
        elif current_round == 11:
            dart1.target('first')
            dart2.target('first')
            hero = Hero(0.5453125, 0.4564814814815)
        elif current_round == 14:
            hero.target('close', cpos=(0.5369791666667, 0.4638888888889))
            mermonkey2 = Monkey('mermonkey', 0.340625, 0.375)
        elif current_round == 15:
            mermonkey3 = Monkey('mermonkey', 0.5833333333333, 0.6833333333333)
        elif current_round == 17:
            sniper = Monkey('sniper', 0.8276041666667, 0.5481481481481)
            sniper.target('strong')
        elif current_round == 19:
            wizard = Monkey('wizard', 0.4796875, 0.5083333333333)
            wizard.upgrade(['1-0-0'])
        elif current_round == 21:
            wizard.upgrade(['2-0-0'])
        elif current_round == 22:
            sniper.upgrade(['1-0-0'])
        elif current_round == 23:
            sniper.upgrade(['1-1-0'])
        elif current_round == 25:
            druid1 = Monkey('druid',0.5234375, 0.5916666666667)
        elif current_round == 28:
            ability(1)
        elif current_round == 29:
            wizard.upgrade(['3-0-0'])
        elif current_round == 30:
            wizard.upgrade(['3-0-1','3-0-2'])
        elif current_round == 31:
            mermonkey1.upgrade(['0-0-1'])
        elif current_round == 34:
            mermonkey1.upgrade(['0-1-1','0-2-1','0-3-1','0-3-2'])
        elif current_round == 35:
            wizard2 = Monkey('wizard', 0.3869791666667, 0.4601851851852)
            wizard2.upgrade(['0-1-0','0-1-1','0-1-2'])
        elif current_round == 36:
            ability(1)
        elif current_round == 37:
            druid2 = Monkey('druid', 0.4848958333333, 0.5712962962963)
        elif current_round == 39:
            change_autostart()
            wait(14)
            wizard2.upgrade(['0-2-2','0-3-2'])
            change_autostart()
            end_round()
        elif current_round == 40:
            ability(1)
        elif current_round == 41:
            mermonkey2.upgrade(['1-0-0','2-0-0','3-0-0','3-0-1','3-0-2'])
        elif current_round == 43:
            village1 = Monkey('village', 0.6119791666667, 0.775)
            village1.upgrade(['0-0-1','0-0-2'])
        elif current_round == 44:
            mermonkey3.upgrade(['0-0-1','0-0-2'])
            mermonkey4 = Monkey('mermonkey', 0.5494791666667, 0.7287037037037)
            mermonkey4.upgrade(['0-0-1','0-0-2'])
        elif current_round == 45:
            mermonkey3.upgrade(['0-1-2','0-2-2','0-3-2'])
        elif current_round == 46:
            mermonkey4.upgrade(['0-1-2','0-2-2','0-3-2'])
            mermonkey5 = Monkey('mermonkey', 0.6166666666667, 0.6361111111111)
        elif current_round == 47:
            mermonkey5.upgrade(['0-0-1','0-0-2','0-1-2','0-2-2','0-3-2'])
        elif current_round == 49:
            mermonkey2.upgrade(['4-0-2'])
            mermonkey6 = Monkey('mermonkey', 0.5114583333333, 0.7657407407407)
            mermonkey6.upgrade(['0-0-1','0-0-2','0-1-2','0-2-2','0-3-2'])
        elif current_round == 50:
            village1.upgrade(['1-0-2','2-0-2'])
        elif current_round == 51:
            mermonkey7 = Monkey('mermonkey', 0.6536458333333, 0.5935185185185, placement_check=False)
            mermonkey7.upgrade(['0-0-1','0-0-2','0-1-2','0-2-2','0-3-2'], cpos=(0.6541666666667, 0.5537037037037))
        elif current_round == 52:
            mermonkey8 = Monkey('mermonkey', 0.4817708333333, 0.8194444444444)
            mermonkey8.upgrade(['0-0-1','0-0-2','0-1-2','0-2-2','0-3-2'])
        elif current_round == 54:
            mermonkey9 = Monkey('mermonkey', 0.5598958333333, 0.7972222222222)
            mermonkey9.upgrade(['0-0-1','0-0-2','0-1-2','0-2-2','0-3-2'])
        elif current_round == 55:
            mermonkey10 = Monkey('mermonkey', 0.5234375, 0.8527777777778)
            mermonkey10.upgrade(['0-0-1','0-0-2','0-1-2','0-2-2','0-3-2'])
        elif current_round == 61:
            wizard.upgrade(['4-0-2'])
        elif current_round == 62:
            ability(1)
            village2 = Monkey('village', 0.4328125, 0.5638888888889)
            village2.upgrade(['1-0-0'])
        elif current_round == 63:
            village2.upgrade(['2-0-0','2-0-1','2-0-2'])
        elif current_round == 79:
            wizard.upgrade(['5-0-2'])