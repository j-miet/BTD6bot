"""Ability use for monkeys.

Ability usage is implemented through 'ability' function call. This function is not tied to Monkey or Hero class, as 
abilities depend on the order they become available, not the type of monkey.
"""

import time

from bot import kb_mouse
from bot.hotkeys import hotkeys
from bot.rounds import Rounds

def ability(key: int, timer: float = 0) -> None:
    """Presses the specified ability hotkey.
    
    Has an optional argument for timing abilities. Ability is then used after 'timer' amount of seconds have passed
    after the round start.

    This function needs the current round start time to time abilities. Therefore, a separate variable named
    'current_round_begin_time' is updated via a plan module and can be used here.
    
    Args:
        key: Ability hotkey number, values in range 1-10.
        timer: Ability timer - ability is used after this amount of time has passed. Accepts float values. 
            Default value is 0, which means ability is used the moment 'ability' call is processed.

    Examples:
        Use ability number 2 immediately after command is processed.
        >>> ability(2)
        Using ability 2 with timer 0... Ability used.
        >>> 
            ability(2, 0)   # identical in functionality to above.

        Use ability number 1, 5.5 seconds after round starts AND command has been processed. If over 5.5 seconds have 
        already passed after command is processed, ability is used immediately.
        >>> ability(1, 5.5)
        Using ability 1 with timer 5.5... Ability used.
    """
    if Rounds.defeat_status:
        return
    print(f'Using ability {key} with timer {timer}... ', end='')
    begin_time = Rounds.current_round_begin_time
    if timer == 0:
        kb_mouse.kb_input(hotkeys['ability '+str(key)])
        print('Ability used.')
        return
    while time.time()-begin_time < timer:     
        time.sleep(0.01)    # small sleep timer to avoid constant processing of time.time
    kb_mouse.kb_input(hotkeys['ability '+str(key)])
    print('Ability used.')

def click(x: float, y: float) -> None:
    """Clicks selected position once.
    
    Used in removing obstacles and clicking other map objects (such as Workshop machines).

    Obstacle removing depends on their position so implementing a general command would be a bit tedious.

    Args:
        x: X-coordinate.
        y: Y-coordinate.
    """
    if Rounds.defeat_status:
        return
    kb_mouse.click((x, y), clicks=1)