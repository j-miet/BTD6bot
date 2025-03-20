"""
[Plan Name] glacial_trailHardChimps
[Game Version] 47
[Hero] Sauda
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys required===
dart 5-2-0
engineer 5-2-0
druid 1-3-0
mortar 0-2-3
spike 2-0-5
alch 4-2-0
glue 0-2-4
ice 5-2-0
sub 0-4-0
_______________________________________
Original: https://www.youtube.com/watch?v=2OuH8JLDeBo

-Should be rng-free so black border is quaranteed.
"""

from time import time

from bot.commands.flow import begin, end_round, change_autostart, wait
from bot.commands.monkey import Monkey
from bot.commands.hero import Hero
from bot.commands.ability import ability, click
import bot.menu_start as menu_start
from bot.rounds import Rounds

def play(rounds: tuple[str, str, str, int, int, str]) -> None:
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start, rounds[2])
        if current_round == BEGIN:
            Hero(0.1651041666667, 0.5027777777778)
            begin()
        elif current_round == 8:
            dart = Monkey('dart', 0.1239583333333, 0.5055555555556)
            dart.target('strong')
        elif current_round == 14:
            engi = Monkey('engineer', 0.7151041666667, 0.6138888888889)
            engi.upgrade(['1-0-0', '2-0-0'])
            dart.upgrade(['0-1-0'])
        elif current_round == 22:
            druid = Monkey('druid', 0.6135416666667, 0.9546296296296)
            druid.upgrade(['0-1-0'])
        elif current_round == 23:
            druid.upgrade(['0-2-0'])
        elif current_round == 24:
            druid.upgrade(['0-3-0'])
        elif current_round == 25:
            druid.upgrade(['1-3-0'])
        elif current_round == 31:
            mortar = Monkey('mortar', 0.1802083333333, 0.9148148148148)
            mortar.special(1, 0.2369791666667, 0.4490740740741)
        elif current_round == 32:
            spike = Monkey('spike', 0.753125, 0.687037037037)
            spike.upgrade(['0-0-1', '0-0-2'])
            spike.target('smart')
        elif current_round == 35:
            spike.upgrade(['0-0-3', '1-0-3', '2-0-3'])
        elif current_round == 39:
            engi.upgrade(['3-0-0', '4-0-0', '4-1-0', '4-2-0'])
        elif current_round == 42:
            mortar.upgrade(['0-0-1', '0-0-2', '0-0-3'])
        elif current_round == 43:
            mortar.upgrade(['0-1-3', '0-2-3'])
            dart.upgrade(['1-1-0'])
        elif current_round == 44:
            dart.upgrade(['2-1-0', '3-1-0', '4-1-0'])
        elif current_round == 45:
            dart.upgrade(['4-2-0'])
        elif current_round == 46:
            spike.upgrade(['2-0-4'])
        elif current_round == 47:
            alch = Monkey('alch', 0.7109375, 0.6759259259259)
            alch.upgrade(['1-0-0', '2-0-0', '3-0-0'])
        elif current_round == 54:
            dart.upgrade(['5-2-0'])
        elif current_round == 74:
            spike.upgrade(['2-0-5'])
        elif current_round == 81:
            glue = Monkey('glue', 0.109375, 0.3759259259259)
            glue.target('strong')
            glue.upgrade(['0-0-1','0-0-2', '0-0-3', '0-1-3', '0-2-3'])
        elif current_round == 85:
            engi.upgrade(['5-2-0'])
        elif current_round == 88:
            alch.upgrade(['4-0-0', '4-1-0', '4-2-0'])
            ice = Monkey('ice', 0.6088541666667, 0.5351851851852)
            ice.upgrade(['1-0-0', '2-0-0', '3-0-0'])
        elif current_round == 89:
            ice.upgrade(['4-0-0', '4-1-0'])
        elif current_round == 94:
            glue.upgrade(['0-2-4'])
        elif current_round == 96:
            ice.upgrade(['5-1-0', '5-2-0'])
        elif current_round == 97:
            sub = Monkey('sub', 0.20, 0.77)
        elif current_round == 98:
            sub.upgrade(['0-1-0', '0-2-0', '0-3-0'])
        elif current_round == 99:
            sub.upgrade(['0-4-0'])
        elif current_round == 100:
            ability(3, 9)