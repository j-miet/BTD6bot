from pathlib import Path
from typing import Any

from bot.bot_vars import BotVars

def cprint(*values: Any, 
           sep: str = " ", 
           end: str = "\n", 
           file: str | None = None, 
           flush: bool = False) -> None:
    """Custom print"""
    if BotVars.logging:
        with open(Path(__file__).parent.parent/"Logs.txt", 'a') as logfile:
            log_value = sep.join(map(str, values)) + end
            logfile.write(log_value)
    print(*values, sep=sep, end=end, file=file, flush=flush) # type: ignore

def cinput(prompt: str = "") -> str:
    """Custom input"""
    value = input(prompt)
    if BotVars.logging:
        with open(Path(__file__).parent.parent/"Logs.txt", 'a') as logfile:
            logfile.write(str(prompt)+value+'\n')
    return value