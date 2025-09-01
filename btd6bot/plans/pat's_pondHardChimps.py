"""
[Hero] Obyn
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
dart 0-3-2
tack 2-0-5

sniper 0-2-5

alch 5-0-0

spike 2-3-0
village 4-2-0
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
            dart1 = Monkey('dart', 0.0864583333333, 0.5675925925926)
            druid = Monkey('druid', 0.7895833333333, 0.4453703703704)
        elif current_round == 8:
            tack = Monkey('tack', 0.7791666666667, 0.5490740740741)
        elif current_round == 11:
            hero = Hero(0.8177083333333, 0.5546296296296)
        elif current_round == 13:
            dart1.upgrade(['0-1-0','0-2-0'])
        elif current_round == 15:
            dart1.upgrade(['0-3-0'])
        elif current_round == 16:
            dart1.upgrade(['0-3-1','0-3-2'])
        elif current_round == 17:
            sniper = Monkey('sniper', 0.8359375, 0.6046296296296)
        elif current_round == 19:
            druid.upgrade(['0-1-0','0-2-0'])
        elif current_round == 25:
            druid.upgrade(['0-3-0','1-3-0'])
        elif current_round == 30:
            sniper.upgrade(['0-1-0','0-2-0','0-2-1','0-2-2'])
        elif current_round == 35:
            sniper.upgrade(['0-2-3'])
        elif current_round == 39:
            click(0.6536458333333, 0.4953703703704)
            click(0.7171875, 0.5787037037037)
            wait(1)
            sniper.upgrade(['0-2-4'])
        elif current_round == 40:
            click(0.4505208333333, 0.1842592592593)
            click(0.5046875, 0.2453703703704)
        elif current_round == 41:
            click(0.4140625, 0.8046296296296)
            click(0.4557291666667, 0.8694444444444)
        elif current_round == 44:
            village = Monkey('village', 0.7942708333333, 0.6416666666667)
            village.upgrade(['1-0-0','2-0-0'])
        elif current_round == 51:
            sniper.upgrade(['0-2-5'])
            click(0.2026041666667, 0.5064814814815)
            click(0.2515625, 0.5805555555556)
        elif current_round == 54:
            village.upgrade(['3-0-0'])
            tack.upgrade(['1-0-0','2-0-0','2-0-1','2-0-2'])
        elif current_round == 58:
            tack.upgrade(['2-0-3','2-0-4'])
            alch = Monkey('alch', 0.7536458333333, 0.6027777777778)
        elif current_round == 59:
            alch.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0'])
        elif current_round == 61:
            village.upgrade(['3-1-0','3-2-0'])
        elif current_round == 81:
            alch.upgrade(['5-0-0'])
        elif current_round == 87:
            tack.upgrade(['2-0-5'])
        elif current_round == 89:
            village.upgrade(['4-2-0'])
        elif current_round == 91:
            dart2 = Monkey('dart', 0.7411458333333, 0.6527777777778)
            dart2.upgrade(['0-0-1','0-0-2','0-0-3','0-0-4','0-1-4'])
        elif current_round == 96:
            dart2.upgrade(['0-1-5','0-2-5'])
            spike1 = Monkey('spike', 0.8317708333333, 0.4435185185185)
            spike1.upgrade(['0-1-0','0-2-0','0-3-0'])
        elif current_round == 97:
            spike1.upgrade(['1-3-0','2-3-0'])
            spike2 = Monkey('spike', 0.7598958333333, 0.3490740740741)
        elif current_round == 98:
            spike2.upgrade(['0-1-0','0-2-0','0-3-0','1-3-0','2-3-0'])
            spike3 = Monkey('spike', 0.7442708333333, 0.2787037037037)
            spike3.upgrade(['0-1-0','0-2-0','0-3-0','1-3-0','2-3-0'])
