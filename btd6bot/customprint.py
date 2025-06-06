from pathlib import Path

from bot.bot_vars import BotVars

def cprint(*values, sep = " ", end = "\n", file = None, flush = False) -> None:
    """Custom print"""
    if BotVars.logging:
        with open(Path(__file__).parent.parent/"Logs.txt", 'a') as logfile:
            for val in values:
                logfile.write(str(val))
                if sep == " ":
                    logfile.write(" ")
            if end == "\n":
                logfile.write("\n")
    print(*values, sep=sep, end=end, file=file, flush=flush)

def cinput(prompt="") -> str:
    """Custom input"""
    value = input(prompt)
    if BotVars.logging:
        with open(Path(__file__).parent.parent/"Logs.txt", 'a') as logfile:
            logfile.write(str(prompt)+value+'\n')
    return value