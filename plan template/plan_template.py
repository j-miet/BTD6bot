"""
[Hero]
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys & upgrades required===
*list all monkeys + their highest crosspaths here*
Example: sniper 5-3-1 means plan uses tier 5 top path, tier 3 middle path, and tier 1 bottom path for snipers.
_______________________________________
*put description/any additional comments here*
"""

# copy this file into btd6bot/plans, then uncomment all the code below this line
'''
from._plan_imports import *

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
        current_round = Rounds.round_check(current_round, map_start)
        if current_round == BEGIN:     
            ...
'''