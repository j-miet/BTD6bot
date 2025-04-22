"""Timing functions."""

import time

def counter(seconds : int | float) -> None:
    """Counts down to 1, starting from number 'seconds'.

    Args:
        seconds: Start value as seconds. If value in int, counts the time down; if float value, no counting is done and 
            only total time is displayed.
    """
    if isinstance(seconds, int):
        for t in range(seconds, 0, -1):
            print(str(t), end=' ')
            time.sleep(1)
    elif isinstance(seconds, float):
        print(seconds)
        time.sleep(seconds)