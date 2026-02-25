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

def play(data: tuple[str, str, str, int, int, str]) -> None:
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start)
        if round == BEGIN:     
            desp0 = Monkey('desperado', 0.2213541666667, 0.6138888888889)
            desp1 = Monkey('desperado', 0.5463541666667, 0.612037037037)
        elif round == 8:
            tack = Monkey('tack', 0.440625, 0.1305555555556)
        elif round == 12:
            hero = Hero(0.4401041666667, 0.1861111111111)
        elif round == 14:
            druid = Monkey('druid', 0.4786458333333, 0.1388888888889)
        elif round == 15:
            druid.upgrade(['1-0-0'])
        elif round == 16:
            druid.upgrade(['1-1-0'])
        elif round == 18:
            druid.upgrade(['1-2-0'])
        elif round == 21:
            ability(1)
        elif round == 22:
            druid.upgrade(['1-3-0'])
            ability(1,3)
        elif round == 24:
            ice0 = Monkey('ice', 0.4041666666667, 0.1407407407407)
            ice0.upgrade(['1-0-0'])
        elif round == 26:
            ice0.upgrade(['2-0-0','2-1-0'])
        elif round == 30:
            ice0.upgrade(['3-1-0'])
        elif round == 33:
            ability(1)
        elif round == 35:
            ice0.upgrade(['4-1-0'])
            tack.upgrade(['1-0-0','1-0-1','1-0-2','2-0-2'])
        elif round == 36:
            tack.upgrade(['2-0-3'])
        elif round == 37:
            sniper = Monkey('sniper', 0.3333333333333, 0.2925925925926)
            sniper.upgrade(['0-1-0'])
        elif round == 39:
            tack.upgrade(['2-0-4'])
        elif round == 40:
            village0 = Monkey('village', 0.4234375, 0.2592592592593)
        elif round == 41:
            village0.upgrade(['0-0-1','0-0-2','0-1-2'])
        elif round == 42:
            ability(2)
        elif round == 43:
            village0.upgrade(['0-2-2'])
        elif round == 45:
            village1 = Monkey('village', 0.4828125, 0.2851851851852)
            village1.upgrade(['0-0-1','0-0-2','1-0-2','2-0-2'])
        elif round == 46:
            village1.upgrade(['3-0-2'])
        elif round == 47:
            village1.upgrade(['4-0-2'])
        elif round == 49:
            ice1 = Monkey('ice', 0.5151041666667, 0.1481481481481)
            ice1.upgrade(['0-1-0','0-1-1','0-2-1','0-2-2','0-2-3','0-2-4'])
        elif round == 61:
            tack.upgrade(['2-0-5'])
        elif round == 65:
            village0.upgrade(['0-3-2'])
            alch = Monkey('alch', 0.3973958333333, 0.1925925925926)
            alch.upgrade(['1-0-0','2-0-0'])
        elif round == 67:
            alch.upgrade(['3-0-0'])
        elif round == 68:
            alch.upgrade(['4-0-0'])
        elif round == 84:
            alch.upgrade(['5-0-0'])
        elif round == 93:
            ice0.upgrade(['5-1-0'])
        elif round == 98:
            ice1.upgrade(['0-2-5'])
            mermonkey = Monkey('mermonkey', 0.5026041666667, 0.2074074074074)
            mermonkey.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-1-0','4-2-0'])