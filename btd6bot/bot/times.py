"""Round time data printing and recording."""

import pathlib
import time

from bot import kb_mouse
from bot.bot_data import BotData
from bot.bot_vars import BotVars
from customprint import cprint

class PauseControl:
    pause_length: float = 0

    @staticmethod
    def pause_bot() -> None:
        """Pauses bot execution."""
        if BotVars.paused:
            pause_start = time.time()
            kb_mouse.click((0.9994791666667, 0.0))
            kb_mouse.press_esc()
            BotData.update_pause(BotVars.paused)
            cprint('>>> Bot paused')
            while BotVars.paused:
                time.sleep(0.1)
            PauseControl.pause_length += time.time() - pause_start
            kb_mouse.click((0.9994791666667, 0.0))
            kb_mouse.press_esc()
            BotData.update_pause(BotVars.paused)
            cprint('Bot unpaused')

def _record_time(time_str: str) -> None:
    """Appends a time string to a temporary text file."""
    if BotVars.time_recording_status:
        with open(pathlib.Path(__file__).parent.parent/'Files'/'times_temp.txt', 'a') as f:
            f.write(time_str+'\n')

def time_print(start: float, end: float, str: str) -> None:
    """Prints the time passed between start and end. Used with times.current_time().

    Returns the time string in 'm:ss' format (m=minutes, ss=seconds).

    Will also pass the time values to record_time function if time_recording_status is True. Data is stored to 
    Files/times_temp.txt, which can be loaded and parsed by shared_api.save_bot_times.

    Args:
        start: Start time.
        end: End time.
        str: Text value, signals what is being timed.

    Returns:
        Time in 'm:ss' string format.
    """
    total = end-start
    minutes = int(total/60)
    seconds = int(total % 60)
    cprint(f'###{str} --- {minutes}:{seconds:02d}###')
    if BotVars.time_recording_status:
        try:
            round_num = str.split()[1]
            _record_time(f'{round_num},{minutes}:{seconds:02d}')
        except IndexError:
            _record_time(f'{minutes}:{seconds:02d}')

def current_time() -> float:
    """Returns current time.
    
    Takes pauses in to account, meaning the returned value is  
    time.time() - total pause length for current bot loop.
    """
    return time.time()-PauseControl.pause_length