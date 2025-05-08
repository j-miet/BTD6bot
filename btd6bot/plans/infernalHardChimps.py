"""
[Hero] Quincy
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-2

sniper 0-1-0
sub 2-5-0
heli 2-0-5

alch 4-0-1
mermonkey 2-0-4

village 2-3-0
_______________________________________
-Apache prime for dps  
-Pre-Emptive Strike for ddts, late game moab damage, and round 100.
"""

from._plan_imports import *

def play(rounds: tuple[str, str, str, int, int, str]) -> None:
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start)
        if current_round == BEGIN:
            hero = Hero(0.4338541666667, 0.6453703703704)
        elif current_round == 7:
            dart = Monkey('dart', 0.2505208333333, 0.2583333333333)
        elif current_round == 9:
            sniper = Monkey('sniper', 0.6463541666667, 0.7787037037037)
            sniper.target('strong')
        elif current_round == 15:
            ability(1,4.5)
        elif current_round == 16:
            heli = Monkey('heli', 0.8151041666667, 0.512037037037)    
            heli.target('lock', 0.4411458333333, 0.5527777777778)
        elif current_round == 20:
            heli.upgrade(['1-0-0'])
        elif current_round == 21:
            heli.upgrade(['2-0-0'])
        elif current_round == 27:
            heli.upgrade(['3-0-0'])
        elif current_round == 32:
            sniper.upgrade(['0-1-0'])
            sniper.target('first')
        elif current_round == 34:
            village = Monkey('village', 0.8223958333333, 0.6185185185185)
        elif current_round == 35:
            village.upgrade(['0-1-0','0-2-0'])
        elif current_round == 36:
            heli.upgrade(['3-0-1','3-0-2'])
        elif current_round == 37:
            alch1 = Monkey('alch', 0.8317708333333, 0.4277777777778)
            alch1.upgrade(['1-0-0','2-0-0'])
        elif current_round == 38:
            alch1.upgrade(['3-0-0'])
        elif current_round == 40:
            ability(1,2)
        elif current_round == 41:
            village.upgrade(['1-2-0','2-2-0'])
        elif current_round == 47:
            ability(1,1.75)
        elif current_round == 49:
            ability(1,4.5)
        elif current_round == 50:
            ability(1,8)
        elif current_round == 51:
            heli.upgrade(['4-0-2'])
        elif current_round == 53:
            alch1.upgrade(['4-0-0','4-1-0','4-2-0'])
        elif current_round == 79:
            heli.upgrade(['5-0-2'])
        elif current_round == 81:
            village.upgrade(['2-3-0'])
        elif current_round == 94:
            sub = Monkey('sub', 0.2723958333333, 0.7574074074074)
            sub.upgrade(['0-1-0','0-2-0','0-3-0','0-4-0','0-5-0','1-5-0','2-5-0'])
            dart.upgrade(['0-0-1','0-0-2'])
        elif current_round == 96:
            alch2 = Monkey('alch', 0.4536458333333, 0.6981481481481)
            alch2.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-1-0','4-2-0'])
            hero.target('strong')
        elif current_round == 97:
            mermonkey = Monkey('mermonkey', 0.4359375, 0.3518518518519)
            mermonkey.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','1-0-4','2-0-4'])
            mermonkey.special(1, 0.3723958333333, 0.4555555555556)
        elif current_round == 100:
            ability(3,2)
            ability(1,10)