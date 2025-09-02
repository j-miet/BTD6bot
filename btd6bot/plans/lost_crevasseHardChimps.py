"""
[Hero] Silas
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
tack 2-0-5
ice 5-2-5
desperado 0-0-0

sniper 0-1-0

alch 5-0-0
druid 1-3-0
mermonkey 4-2-0

village 3-3-2
_______________________________________
Possible RNG pre-round 40
"""

from._plan_imports import *

def play(rounds: tuple[str, str, str, int, int, str]) -> None:
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start)
        if current_round == BEGIN:     
            desp0 = Monkey('desperado', 0.2333333333333, 0.6)
            desp1 = Monkey('desperado', 0.5661458333333, 0.6148148148148)
        elif current_round == 8:
            tack = Monkey('tack', 0.4385416666667, 0.1101851851852)
        elif current_round == 12:
            hero = Hero(0.4401041666667, 0.175)
        elif current_round == 14:
            druid = Monkey('druid', 0.475, 0.1185185185185)
        elif current_round == 15:
            druid.upgrade(['1-0-0'])
        elif current_round == 16:
            druid.upgrade(['1-1-0'])
        elif current_round == 18:
            druid.upgrade(['1-2-0'])
        elif current_round == 22:
            druid.upgrade(['1-3-0'])
            ability(1,3)
        elif current_round == 24:
            ice0 = Monkey('ice', 0.4036458333333, 0.1194444444444)
            ice0.upgrade(['1-0-0'])
        elif current_round == 26:
            ice0.upgrade(['2-0-0','2-1-0'])
        elif current_round == 30:
            ice0.upgrade(['3-1-0'])
        elif current_round == 35:
            ice0.upgrade(['4-1-0'])
            tack.upgrade(['1-0-0','1-0-1','1-0-2','2-0-2'])
        elif current_round == 36:
            tack.upgrade(['2-0-3'])
        elif current_round == 37:
            sniper = Monkey('sniper', 0.33125, 0.3092592592593)
            sniper.upgrade(['0-1-0'])
        elif current_round == 39:
            tack.upgrade(['2-0-4'])
        elif current_round == 40:
            village0 = Monkey('village', 0.4234375, 0.2592592592593)
        elif current_round == 41:
            village0.upgrade(['0-0-1','0-0-2','0-1-2'])
        elif current_round == 43:
            village0.upgrade(['0-2-2'])
        elif current_round == 45:
            village1 = Monkey('village', 0.4838541666667, 0.2787037037037)
            village1.upgrade(['0-0-1','0-0-2','1-0-2','2-0-2'])
        elif current_round == 46:
            village1.upgrade(['3-0-2'])
        elif current_round == 47:
            village1.upgrade(['4-0-2'])
        elif current_round == 49:
            ice1 = Monkey('ice', 0.509375, 0.137037037037)
            ice1.upgrade(['0-1-0','0-1-1','0-2-1','0-2-2','0-2-3','0-2-4'])
        elif current_round == 61:
            tack.upgrade(['2-0-5'])
        elif current_round == 65:
            village0.upgrade(['0-3-2'])
            alch = Monkey('alch', 0.4052083333333, 0.1731481481481)
            alch.upgrade(['1-0-0','2-0-0'])
        elif current_round == 67:
            alch.upgrade(['3-0-0'])
        elif current_round == 68:
            alch.upgrade(['4-0-0'])
        elif current_round == 84:
            alch.upgrade(['5-0-0'])
        elif current_round == 93:
            ice0.upgrade(['5-1-0'])
        elif current_round == 98:
            ice1.upgrade(['0-2-5'])
            mermonkey = Monkey('mermonkey', 0.4791666666667, 0.187962962963)
            mermonkey.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-1-0','4-2-0'])
