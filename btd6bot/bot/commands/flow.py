"""Commands for controlling round time flow.

Includes AutoStart class that tracks autostart status.

Functions:
__
    sleep: avoid further commands for specified time  
    begin: press start button twice (must be included in every plan as default is to have autostart on)  
    change_autostart: change current autostart setting, by default autostart is always on. Calling this function 
        reverts it, but can also change it back.  
    end_round: click start button once; either if autostart disabled OR if button need only be pressed once for fast 
    track (deflation) 
"""

import time

from pynput.keyboard import Key

from bot import kb_mouse
from utils import timing

class AutoStart:
    """Wrapper class for autostart values.
    
    Attributes:
        AUTOSTART_TOGGLE (tuple[float, float], class attribute): Location of in-game menu autostart toggle button.
        autostart_status (bool, class attribute): Whether bot has autostart enabled or not. Starts with initial value 
            True. But if any plan modifies this using flow.change_autostart, it's set to False. And if value if False, 
            then after loading into a game, bot will automatically revert this to True, even if it's immediately set to 
            False again by plan itself: otherwise, other plans would keep the False state and be unable to execute.
        called_forward (bool, class attribute): Whether forward() was called during first round. Default is False, 
            which means bot will automatically call it after first round block ends.
    """
    AUTOSTART_TOGGLE: tuple[float, float] = (0.69, 0.284)

    autostart_status: bool = True
    called_forward = False


def wait(timer: float | int = 0) -> None:
    """Pause everything for specified amount of time.

    Used in plans to buffer commands and avoid on executing them before certain time has passed.

    Args:
        timer: Wait timer, can be integer or float. Integer counts down, float will just display the waiting time. 
            Default value is 0.
    """    
    print('Waiting... ', end='')
    timing.counter(timer)
    print(' -> Continuing.')

def forward(speed: int=2) -> None:
    """Clicks the start button.

    Default value is 2, which double clicks the button, setting fast speed. This means, for fast settings, you only 
    need to just type forward() - but forward(2) does work, too.
     
    For normal start speed or switching current speed, you click only once and therefore type forward(1).

    In Deflation game mode, the game start automatically in normal speed. If you wish to set it on fast, you use 
    forward(1) the first time.

    Args:
        speed: Default value is 2 for fast-forward. Use value 1 for a single click. Other values do nothing.
    """
    if speed == 1:
        kb_mouse.kb_input(Key.space)
        time.sleep(0.2)
    elif speed == 2:
        kb_mouse.kb_input(Key.space)
        time.sleep(0.2)
        kb_mouse.kb_input(Key.space)
    else:
        print("Speed value must be either 1 or 2.")
        return
    AutoStart.called_forward = True

def change_autostart() -> None:
    """Change current autostart setting.

    As autostart needs to enabled by default to run the bot, this function can be used to disable/re-enable it.
     
    Called only within a plan file AND called once, preferable as the very first command on first round:
    bot.menu will handle the re-enabling of autostart before bot starts doing any in-game tower commands, as default 
    value is always 'True'.

    This is used only for harder plans where, after the round is finished, you need the end of round gold for 
    placing/upgrading towers before starting the following round and/or if tower placements are altered after start, 
    as is the case in maps like Geared or Sanctuary.
    
    Should autostart be set to 'False', you need to use end_round command on ---every single round---.
    """
    time.sleep(0.5)
    kb_mouse.kb_input(Key.esc)
    time.sleep(0.5)
    kb_mouse.click(AutoStart.AUTOSTART_TOGGLE)
    kb_mouse.kb_input(Key.esc)
    if AutoStart.autostart_status == False: 
        AutoStart.autostart_status = True
        print('Autostart enabled.')
        return
    AutoStart.autostart_status = False
    print('Autostart disabled.')

def end_round(time_limit: int = 0) -> None:
    """Used for single clicking the start button to start next round when automatic start is disabled.

    Somes specific plans require that change_autostart is called. Bot cannot detect when round end without
    autostart so you need to manually insert calls for end_round and optionally give them a max time limit after which 
    it will force start next round.

    You should check some Expert Chimps plans inside 'plans' folder for comparison, and to understand how they use it 
    in practise.

    Args:
        time_limit: Waiting period before start button is clicked. Measured in seconds. 
    """
    if time_limit >= 2:
        print('Next round in... ', end='')
        timing.counter(time_limit)
        print()
    else:
        time.sleep(time_limit)
    kb_mouse.kb_input(Key.space)
    time.sleep(0.2)