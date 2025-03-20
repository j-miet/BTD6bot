"""Round time data printing and recording.

Time data is for gui plotting purposes.
"""

import pathlib

from bot.bot_vars import BotVars

def _record_time(time_str: str) -> None:
    """Appends a time string to a temporary text file."""
    if BotVars.time_recording_status:
        with open(pathlib.Path(__file__).parent.parent/'Files'/'times_temp.txt', 'a') as f:
            f.write(time_str+'\n')

def time_print(start: float, end: float, str: str) -> None:
    """Prints the time passed between start and end. Used with time.time().

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
    print(f'###{str} --- {minutes}:{seconds:02d}###')
    if BotVars.time_recording_status:
        try:
            round_num = str.split()[1]
            _record_time(f'{round_num},{minutes}:{seconds:02d}')
        except IndexError:
            _record_time(f'{minutes}:{seconds:02d}')
            print('All times succesfully recorded.')

