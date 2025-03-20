"""
[Plan Name]
[Game Version]
[Hero]
[Monkey Knowledge]
-------------------------------------------------------------
===Monkeys required===
*list all monkeys + their crosspaths here
_______________________________________
*put description/any additional comments here*
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
        current_round = Rounds.round_check(current_round, map_start)
        if current_round == BEGIN:     
            begin()
        elif current_round == END:
            ...