"""
[Hero] Psi
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-3-2
glue 0-2-4

sniper 1-0-0
ace 2-0-4
mortar 0-2-4

alch 4-2-0
mermonkey 4-0-0

spike 2-5-0
village 2-2-0
engineer 0-3-3
_______________________________________
"""

from._plan_imports import *

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:     
            dart = Monkey('dart', 0.5864583333333, 0.6907407407407)
            engi = Monkey('engineer', 0.5614583333333, 0.7351851851852)
            engi.target('last')
        elif round == 7:
            dart.upgrade(['0-1-0'])
        elif round == 8:
            dart.upgrade(['0-2-0'])
        elif round == 10:
            dart.upgrade(['0-3-0'])
        elif round == 12:
            engi.upgrade(['0-0-1'])
        elif round == 13:
            engi.upgrade(['0-0-2'])
        elif round == 13:
            engi.upgrade(['0-0-3'])
        elif round == 19:
            hero = Hero(0.4078125, 0.0648148148148)
            hero.target('strong')
        elif round == 20:
            dart.upgrade(['0-3-1','0-3-2'])
        elif round == 23:
            sniper = Monkey('sniper', 0.4661458333333, 0.075)
            sniper.upgrade(['1-0-0'])
            sniper.target('strong')
        elif round == 31:
            ace = Monkey('ace', 0.4203125, 0.2361111111111)
            ace.upgrade(['0-0-1','0-0-2'])
        elif round == 32:
            ace.center(0.4260416666667, 0.9990740740741)
        elif round == 34:
            ace.upgrade(['0-0-3'])
        elif round == 35:
            ace.upgrade(['1-0-3'])
        elif round == 36:
            ace.upgrade(['2-0-3'])
        elif round == 38:
            alch = Monkey('alch', 0.4671875, 0.2990740740741)
        elif round == 39:
            alch.upgrade(['1-0-0','2-0-0','3-0-0','3-1-0','3-2-0'])
        elif round == 40:
            ability(1,1)
        elif round == 42:
            village = Monkey('village', 0.4369791666667, 0.1490740740741)
            village.upgrade(['0-1-0','0-2-0'])
        elif round == 44:
            village.upgrade(['1-2-0','2-2-0'])
        elif round == 45:
            alch.upgrade(['4-2-0'])
        elif round == 58:
            ace.upgrade(['2-0-4'])
        elif round == 64:
            click(0.2057291666667, 0.3712962962963)
            click(0.2640625, 0.4472222222222)
        elif round == 65:
            spike = Monkey('spike', 0.2119791666667, 0.4009259259259)
            spike.upgrade(['0-1-0','0-2-0','0-3-0','0-4-0'])
        elif round == 66:
            spike.upgrade(['1-4-0'])
        elif round == 82:
            ability(1,10)
            ability(3,12)
        elif round == 83:
            spike.upgrade(['1-5-0','2-5-0'])
        elif round == 84:
            mermonkey = Monkey('mermonkey', 0.1942708333333, 0.4990740740741)
            mermonkey.upgrade(['1-0-0','2-0-0','3-0-0'])
        elif round == 85:
            mermonkey.upgrade(['4-0-0'])
            glue = Monkey('glue', 0.2317708333333, 0.3453703703704)
            glue.target('strong')
        elif round == 87:
            glue.upgrade(['0-0-1','0-0-2','0-1-2'])
        elif round == 88:
            glue.upgrade(['0-1-3','0-1-4','0-2-4'])
        elif round == 89:
            engi2 = Monkey('engineer', 0.1942708333333, 0.3398148148148)
            engi2.upgrade(['0-1-0','0-2-0','0-3-0','0-3-1'])
            engi2.special(1, 0.2276041666667, 0.1138888888889)
        elif round == 93:
            click(0.1130208333333, 0.8787037037037) # lower island
            click(0.2380208333333, 0.8787037037037)
            wait(1)
            mortar = Monkey('mortar', 0.1088541666667, 0.875)
            mortar.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2'])
        elif round == 94:
            mortar.upgrade(['0-2-3','0-2-4'])
            mortar.special(1, 0.1859375, 0.0166666666667)
        elif round == 96:
            engi2.upgrade(['0-4-1'])
        elif round == 98:
            ability(4, xy=(0.4203125, 0.2361111111111))
            ability(2, 11)
        elif round == 100:
            ability(3,3)