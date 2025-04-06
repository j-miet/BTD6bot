"""
[Plan Name] infernalMediumApopalypse
[Game Version] 47
[Hero] Psi
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
sub 2-0-4
bomb 2-0-4
alch 3-0-0
dart 0-0-2
sniper 0-2-2
druid 1-3-0
village 0-2-0
_______________________________________
Apopalypse round rng might fail you. Should work after a few tries, though.
"""

from._plan_imports import *

def play(rounds: tuple[str, str, str, int, int, str]) -> None:
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start, rounds[2])
        if current_round == BEGIN:
            sub1 = Monkey('sub', 0.2723958333333, 0.7490740740741)
            sub2 = Monkey('sub', 0.6197916666667, 0.2509259259259)
            begin('normal') # begin('normal') presses start button once because of apopalypse autostart.
            sub2.upgrade(['0-0-1'])
            sub1.upgrade(['0-0-1'])
            druid1 = Monkey('druid', 0.8333333333333, 0.637962962963)
            druid1.upgrade(['0-1-0', '0-2-0'])
            sub1.sell()
            sub2.sell()
            druid1.upgrade(['0-3-0'])
            hero = Hero(0.2552083333333, 0.1768518518519)
            hero.target('strong')
            druid1.upgrade(['1-3-0'])
            sniper = Monkey('sniper', 0.6375, 0.787962962963)
            sniper.upgrade(['0-1-0', '0-2-0', '0-2-1', '0-2-2'])
            village = Monkey('village', 0.8005208333333, 0.5287037037037)
            village.upgrade(['0-1-0', '0-2-0'])
            druid2 = Monkey('druid', 0.8333333333333, 0.4342592592593)
            druid2.upgrade(['0-1-0', '0-2-0', '0-3-0', '1-3-0'])
            sub1 = Monkey('sub', 0.2723958333333, 0.7490740740741)
            sub1.upgrade(['0-0-1', '0-0-2', '1-0-2', '2-0-2'])
            dart_top = Monkey('dart', 0.246875, 0.2583333333333)
            dart_top.upgrade(['0-0-1', '0-0-2'])
            dart_bot = Monkey('dart', 0.4333333333333, 0.6453703703704)
            dart_bot.upgrade(['0-0-1', '0-0-2'])
            sub1.upgrade(['2-0-3'])
            bomb_top = Monkey('bomb', 0.4296875, 0.3546296296296)
            bomb_top.upgrade(['0-0-1', '0-0-2', '0-0-3', '1-0-3', '2-0-3'])
            alch_top = Monkey('alch', 0.4505208333333, 0.3)
            alch_top.upgrade(['1-0-0', '2-0-0', '3-0-0'])
            bomb_top.upgrade(['2-0-4'])
            bomb_bot = Monkey('bomb', 0.41875, 0.6990740740741)
            bomb_bot.upgrade(['0-0-1', '0-0-2', '0-0-3', '1-0-3', '2-0-3'])
            alch_bot = Monkey('alch', 0.4552083333333, 0.7009259259259)
            alch_bot.upgrade(['1-0-0', '2-0-0', '3-0-0'])
            bomb_bot.upgrade(['2-0-4'])
            sub2 = Monkey('sub', 0.6197916666667, 0.2509259259259)
            sub2.upgrade(['0-0-1', '0-0-2', '1-0-2', '2-0-2', '2-0-3', '2-0-4'])
            sub1.upgrade(['2-0-4'])