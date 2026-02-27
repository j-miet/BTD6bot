"""
[Hero] Etienne
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-0-0
boomer 0-2-4
tack 0-0-0
glue 0-2-4
desperado 5-4-0

sniper 3-2-2
ace 2-0-3

wizard 1-0-5
alch 4-2-0
druid 3-0-2
mermonkey 0-1-4

village 3-0-2
engineer 4-0-2
_______________________________________
Round 50 is the round with most rng.
"""

from._plan_imports import *

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:     
            desp1 = Monkey('desperado', 0.1994791666667, 0.5083333333333)
            desp2 = Monkey('desperado', 0.6703125, 0.5157407407407)
        elif round == 9:
            tack = Monkey('tack', 0.1984375, 0.387962962963)
            dart1 = Monkey('dart', 0.6109375, 0.2509259259259)
        elif round == 10:
            desp2.target('strong')
            dart2 = Monkey('dart', 0.6463541666667, 0.2490740740741)
        elif round == 13:
            hero = Hero(0.2395833333333, 0.512037037037)
        elif round == 15:
            sniper1 = Monkey('sniper', 0.6072916666667, 0.1953703703704)
            sniper1.target('strong')
        elif round == 16:
            sniper2 = Monkey('sniper', 0.1979166666667, 0.5657407407407)
            sniper2.target('strong')
        elif round == 18:
            engi = Monkey('engineer', 0.6692708333333, 0.3916666666667)
        elif round == 20:
            engi.upgrade(['1-0-0'])
        elif round == 21:
            sniper2.upgrade(['1-0-0'])
        elif round == 22:
            sniper1.upgrade(['1-0-0'])
        elif round == 25:
            engi.upgrade(['2-0-0'])
        elif round == 26:
            engi.upgrade(['3-0-0'])
        elif round == 28:
            engi.upgrade(['3-0-1','3-0-2'])
        elif round == 30:
            sniper2.upgrade(['1-0-1','1-0-2'])
        elif round == 32:
            sniper1.upgrade(['1-1-0','1-2-0'])
        elif round == 34:
            druid = Monkey('druid', 0.2625, 0.7453703703704)
            druid.upgrade(['1-0-0'])
            hero.target('first')
        elif round == 35:
            druid.upgrade(['2-0-0'])
        elif round == 36:
            desp1.upgrade(['0-1-0'])
            sniper2.upgrade(['2-0-2'])
        elif round == 38:
            sniper2.upgrade(['3-0-2'])
        elif round == 39:
            druid.upgrade(['3-0-0'])
        elif round == 42:
            engi.upgrade(['4-0-2'])
        elif round == 44:
            village1 = Monkey('village', 0.2859375, 0.5546296296296)
            village1.upgrade(['0-0-1','0-0-2'])
        elif round == 45:
            village1.upgrade(['1-0-2','2-0-2'])
            druid.upgrade(['3-0-1','3-0-2'])
        elif round == 48:
            wizard = Monkey('wizard', 0.3546875, 0.3546296296296)
            wizard.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','1-0-4'])
        elif round == 49:
            alch1 = Monkey('alch', 0.3567708333333, 0.4157407407407)
            alch1.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif round == 50:
            alch1.upgrade(['4-0-0'])
        elif round == 51:
            ace = Monkey('ace', 0.2963541666667, 0.4083333333333)
            ace.upgrade(['0-0-1','0-0-2','0-0-3'])
            ace.target('infinite')
        elif round == 52:
            ace.upgrade(['1-0-3','2-0-3'])
        elif round == 53:
            alch1.upgrade(['4-1-0','4-2-0'])
        elif round == 54:
            glue1 = Monkey('glue', 0.6723958333333, 0.6027777777778)
            glue1.target('strong')
        elif round == 55:
            glue1.upgrade(['0-0-1','0-0-2','0-0-3','0-1-3'])
        elif round == 63:
            ability(2,1)
        elif round == 73:
            wizard.upgrade(['1-0-5'])
            village1.upgrade(['3-0-2'])
            glue2 = Monkey('glue', 0.2390625, 0.387962962963)
            glue2.target('strong')
        elif round == 75:
            glue2.upgrade(['0-0-1','0-0-2','0-0-3','0-1-3'])
        elif round == 76:
            ability(2)
        elif round == 77:
            glue2.upgrade(['0-2-3','0-2-4'])
        elif round == 78:
            boomer1 = Monkey('boomer', 0.2026041666667, 0.4472222222222)
            boomer1.target('strong')
            boomer1.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-3'])
        elif round == 79:
            boomer1.upgrade(['0-2-4'])
            village2 = Monkey('village', 0.6192708333333, 0.5101851851852)
            village2.upgrade(['0-0-1','0-0-2','1-0-2','2-0-2','3-0-2'])
        elif round == 81:
            glue1.upgrade(['0-1-4','0-2-4'])
            boomer2 = Monkey('boomer', 0.6348958333333, 0.5953703703704)
            boomer2.target('strong')
        elif round == 82:
            boomer2.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
        elif round == 83:
            boomer3 = Monkey('boomer', 0.5921875, 0.5953703703704)
            boomer3.target('strong')
            boomer3.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
        elif round == 84:
            boomer4 = Monkey('boomer', 0.5682291666667, 0.5064814814815)
            boomer4.target('strong')
            boomer4.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
        elif round == 85:
            boomer5 = Monkey('boomer', 0.5536458333333, 0.5638888888889)
            boomer5.target('strong')
            boomer5.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
        elif round == 87:
            desp3 = Monkey('desperado', 0.3088541666667, 0.4824074074074)
        elif round == 88:
            desp3.upgrade(['4-0-0','4-1-0','4-2-0'])
        elif round == 94:
            desp3.upgrade(['5-2-0'])
            desp3.special(1)
        elif round == 95:
            boomer6 = Monkey('boomer', 0.3484375, 0.4861111111111)
            boomer6.target('strong')
            boomer6.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4','0-2-4'])
        elif round == 97:
            mermonkey = Monkey('mermonkey', 0.6192708333333, 0.3972222222222)
            mermonkey.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4'])
        elif round == 98:
            desp1.upgrade(['0-2-0','0-3-0'])
            ability(1,7)
            desp1.upgrade(['1-3-0','2-3-0','2-4-0'])
        elif round == 99:
            mermonkey.special(1, 0.7130208333333, 0.3490740740741)
            ability(2)
        elif round == 100:
            ability(1)
            ability(3, xy=(0.3067708333333, 0.4787037037037))
            ability(4,2)
