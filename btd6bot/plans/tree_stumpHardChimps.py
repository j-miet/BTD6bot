"""
[Hero] Corvus
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
desperado 0-0-0

super 2-0-4
alch 5-0-0
druid 1-3-0
mermonkey 0-3-2

village 2-0-0
_______________________________________
Uses Corvus as hero and a 0-2-4 super so saving money requires a lot of ability and spellbook usage.
"""

from._plan_imports import *

def play(data):
    BEGIN, END = menu_start.load(*data)
    round = BEGIN-1
    map_start = time()
    while round < END+1:
        round = Rounds.round_check(round, map_start, data[2])
        if round == BEGIN:     
            desp = Monkey('desperado', 0.3942708333333, 0.312962962963)
            mermonkey = Monkey('mermonkey', 0.2640625, 0.2490740740741)
        elif round == 13:
            hero = Hero(0.2526041666667, 0.1435185185185)
        elif round == 14:
            hero.spellbook([13])
        elif round == 18:
            ability(1,2)
            hero.spellbook([13])
        elif round == 20:
            mermonkey.upgrade(['0-0-1','0-0-2'])
        elif round == 21:
            ability(1,1)
        elif round == 22:
            mermonkey.upgrade(['0-1-2','0-2-2','0-3-2'])
        elif round == 23:
            druid = Monkey('druid', 0.2807291666667, 0.5009259259259)
        elif round == 25:
            ability(1,7)
        elif round == 26:
            hero.spellbook([13])
        elif round == 27:
            mermonkey.target('strong')
        elif round == 28:
            ability(1,1)
        elif round == 30:
            hero.spellbook([13])
        elif round == 31:
            super = Monkey('super', 0.4015625, 0.3972222222222)
        elif round == 32:
            ability(1,2)
        elif round == 34:
            ability(1,2)
            hero.spellbook([13])
        elif round == 36:
            ability(1)
            hero.spellbook([13])
        elif round == 37:
            super.upgrade(['0-0-1','0-0-2'])
        elif round == 38:
            hero.spellbook([13])
            ability(1,5.5)
        elif round == 40:
            ability(1)
            hero.spellbook([13])
        elif round == 41:
            ability(1,8)
        elif round == 40:
            hero.spellbook([13])
        elif round == 43:
            ability(1,3)
        elif round == 44:
            ability(1,4)
        elif round == 45:
            hero.spellbook([13])
            ability(1)
        elif round == 47:
            super.upgrade(['0-0-3'])
        elif round == 49:
            hero.spellbook([13])
            ability(1)
        elif round == 51:
            hero.spellbook([13])
        elif round == 52:
            ability(1,1)
            super.upgrade(['0-1-3','0-2-3'])
        elif round == 54:
            ability(1,1)
        elif round == 55:
            hero.spellbook([13])
            ability(1,4)
        elif round == 57:
            wait(2)
            hero.spellbook([13])
            ability(1)
        elif round == 59:
            hero.spellbook([13])
            ability(1,4)
        elif round == 60:
            druid.upgrade(['1-0-0','1-1-0'])
        elif round == 61:
            ability(1,1)
            wait(3)
            hero.spellbook([8])
        elif round == 62:
            druid.upgrade(['1-2-0','1-3-0'])
            wait(6)
            hero.spellbook([15])
        elif round == 63:
            ability(4,3)
            wait(1)
            hero.spellbook([10])
            wait(4)
            hero.spellbook([8])
        elif round == 64:
            wait(2)
            hero.spellbook([11])
            ability(1)
        elif round == 65:
            wait(12)
            ability(1)
            hero.special([7])
            hero.spellbook([13])
        elif round == 66:
            ability(1,3)
            hero.spellbook([13])
        elif round == 68:
            ability(1,5)
            hero.spellbook([13])
        elif round == 69:
            ability(1,7)
        elif round == 70:
            wait(2)
            hero.spellbook([13])
        elif round == 71:
            wait(3)
            hero.spellbook([8])
            ability(1)
        elif round == 72:
            wait(1)
            hero.spellbook([13])
        elif round == 73:
            ability(1,10)
        elif round == 74:
            ability(1,6)
            hero.spellbook([13])
            ability(1,20)
            hero.spellbook([10])
        elif round == 75:
            hero.spellbook([13])
            ability(1,7)
            ability(4,9)
            wait(3)
            hero.spellbook([10,5,7])
        elif round == 76:
            ability(1)
            hero.spellbook([8])
        elif round == 77:
            hero.spellbook([13])
            ability(1,12)
            wait(4)
            hero.spellbook([8])
        elif round == 78:
            super.upgrade(['0-2-4'])
        elif round == 79:
            hero.spellbook([13])
        elif round == 80:
            village = Monkey('village', 0.3755208333333, 0.2009259259259)
            village.upgrade(['1-0-0','2-0-0'])
        elif round == 81:
            ability(1,4)
            hero.spellbook([13])
        elif round == 83:
            ability(1,2)
            hero.spellbook([13])
        elif round == 84:
            hero.spellbook([13])
        elif round == 88:
            ability(1,3)
            hero.spellbook([13])
        elif round == 91:
            ability(1,1)
            hero.spellbook([13])
        elif round == 93:
            hero.spellbook([13])
        elif round == 94:
            alch = Monkey('alch', 0.2786458333333, 0.3287037037037)
            alch.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','5-0-0'])
        elif round == 96:
            hero.spellbook([13])
        elif round == 97:
            ability(1,7)
            hero.spellbook([13])
        elif round == 98:
            ability(4,3)
        elif round == 100:
            hero.spellbook([11, 4, 1])
            ability(1)