"""Timing functions."""

import time

def counter(seconds : int) -> None:
    """Counts down to 1, starting from number 'seconds'.

    Args:
        seconds: Start value as seconds, a non-negative integer.
    """
    for t in range(seconds, 0, -1):
        print(str(t), end=' ')
        time.sleep(1)   