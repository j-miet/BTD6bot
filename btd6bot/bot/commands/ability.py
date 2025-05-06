"""Ability use for monkeys.

Ability usage is implemented through 'ability' function call. This function is not tied to Monkey or Hero class, as 
abilities depend on the order they become available, not the type of monkey.
"""

import time

from bot import kb_mouse, times
from bot.hotkeys import hotkeys
from bot.rounds import Rounds

def ability(key: int, timer: float = 0, xy: tuple[float, float] | None = None, delay: float = 0) -> None:
    """Presses the specified ability hotkey.
    
    Has an optional argument for timing abilities. Ability is then used after 'timer' amount of seconds have passed
    after the round start.

    Can also target ability by giving the target location x and y coordinates.
    
    Args:
        key: Ability hotkey number, values in range 1-10.
        timer: Ability timer - ability is used after this amount of time has passed. Accepts float values. 
            Default value is 0, which means ability is used the moment 'ability' call is processed.
        xy: Target coordinate, a tuple of floats. Default is None.
        delay: If value is set greater than 0, then stands for time waited before mouse is moved to location xy. If
            value is 0, which is also the default value, no cursor movement is done afterwards.
            Only reasonable use case is when reseting Obyn's trees: bananas have short animation during which they 
            cannot be collected, so setting a value of 1 or similar, will let bananas finish spreading animation, then moves cursor on top of tree location (which is given xy value) to collect them.

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

        To target an ability, for example engineer overclock, add coordinates with xy argument.
        >>>  
            ability(2, 5, xy=(0.5, 0.5))
        Targeting can be also used to quickly click mouse over Obyn's trees and collect the bananas. For this, 'delay'
        argument is useful: it will wait for specified time before moving mouse. As bananas have short animation before 
        they can be collected, setting a delay of 1 second should collect them properly.
        >>>
            ability(2, 10, xy=(0.5, 0.5), delay=1)
    """
    times.pause_bot()
    if Rounds.defeat_status:
        return
    print(f'Using ability {key} with timer {timer}... ', end='')
    begin_time = Rounds.current_round_begin_time
    if timer == 0:
        kb_mouse.kb_input(hotkeys['ability '+str(key)])
        if xy is not None:
            if delay > 0:
                time.sleep(delay)
                move_cursor(xy[0], xy[1])
            else:
                kb_mouse.click(xy)
        print('Ability used.')
        return
    while times.current_time()-begin_time < timer:     
        time.sleep(0.01)    # small sleep timer to avoid constant processing of time.time
    kb_mouse.kb_input(hotkeys['ability '+str(key)])
    if xy is not None:
        if delay > 0:
            time.sleep(delay)
            move_cursor(xy[0], xy[1])
        else:
            kb_mouse.click(xy)
    print('Ability used.')

def click(x: float, y: float, N: int = 1) -> None:
    """Clicks selected position N times.
    
    Used in removing obstacles and clicking other map objects (such as Workshop machines).

    Obstacle removing depends on their position so implementing a general command would be a bit tedious.

    Args:
        x: X-coordinate.
        y: Y-coordinate.
    """
    times.pause_bot()
    if Rounds.defeat_status:
        return
    kb_mouse.click((x, y), clicks=N)
    if N > 1:
        print(f"Clicked at ({x}, {y}) {N} times")
    else:
        print(f"Clicked at ({x}, {y})")

def move_cursor(x: float, y: float) -> None:
    """Move mouse cursor to target location"""
    times.pause_bot()
    if Rounds.defeat_status:
        return
    kb_mouse.move_cursor((x, y))