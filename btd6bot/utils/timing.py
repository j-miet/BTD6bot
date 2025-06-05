"""Timing functions."""

import time

from customprint import cprint

def counter(seconds : int | float) -> None:
    """Counts down to 1, starting from number 'seconds'.

    Args:
        seconds: Start value as seconds. If value in int, counts the time down; if float value, no counting is done and 
            only total time is displayed.
    """
    if isinstance(seconds, int):
        for t in range(seconds, 0, -1):
            cprint(str(t), end=' ', flush=True)
            time.sleep(1)
    elif isinstance(seconds, float):
        cprint(seconds)
        time.sleep(seconds)