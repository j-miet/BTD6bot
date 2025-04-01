"""Functions for parsing map and strategy data in plan files."""

import pathlib
import os

def read_plans() -> list[str]:
    """Scans all plans, removes other than plan .py file names and returns files as a new list.
    
    Returns:
        List of all plan file names without .py suffix.
    """
    namelist: list[str] = os.listdir(pathlib.Path(__file__).parent.parent / 'plans')
    try:
        namelist.remove('__init__.py')
        namelist.remove('_plan_imports.py')
    except ValueError:
        ...
    try:
        for file_name in namelist[:]:
            if '.py' not in file_name:
                namelist.remove(file_name)
        newlist = [name.replace('.py', '') for name in namelist]
        newlist.sort()
        for plan in newlist:
            if return_map(plan) == '' or return_strategy(plan) == '':
                newlist.remove(plan)
        return newlist
    except ValueError:
        return []

def return_map(plan: str) -> str:
    """Returns map name component from a plan.

    Parses map_name substring from a map_nameDifficultyMode string by finding first capital letter in a plan string: it
    separates map name and difficulty. Then replaces underscores with spaces and returns a copy of this string.

    Args:
        plan: Plan name string.

    Returns:
        Map name string.
    """
    newplan = plan.replace('_', ' ')
    for s in newplan:
        if s.isupper():
            return newplan[:newplan.index(s)]
    return ''

def return_strategy(plan: str) -> str:
    """Returns strategy name i.e. difficulty and game mode, from a plan.

    Parses DifficultyMode substring from a map_nameDifficultyMode string, adds a '-' between Difficulty and Mode and
    returns this new string.

    Args:
        plan: Plan name string.
        
    Returns:
        String in a 'Difficulty-Mode' format.
    """
    diff_and_mode = []
    diff_start_pos = 0
    mode_start_pos = 0
    try:
        for i in range(0, len(plan)):
            if plan[i].isupper():
                diff_start_pos= i
                diff_and_mode.append(i)
                for j in range(diff_start_pos+1, len(plan)):
                    if plan[j].isupper():
                        mode_start_pos = j
                        diff_and_mode.append(j)
                        break
                break
        if diff_start_pos == 0 or mode_start_pos == 0:
            return ''
        else:
            return plan[diff_start_pos:mode_start_pos]+'-'+ plan[mode_start_pos:]
    except IndexError:
        return ''

def return_maps_and_strats(data: list[str]) -> dict[str, list[str]]:
    """Creates a dictionary with maps as keys and list of different strategies as values for that map.

    Args:
        data: List of plans, parsed from 'plans' folder. 

    Returns:
        A dictionary with map names as keys, each key corresponding to a list of existing difficulty + game
            mode combinations for that map.
    """
    map_strat: dict[str, list[str]] = {}
    for d in data:
        map_name = return_map(d)
        strategy_name = return_strategy(d)
        if map_name != '' and strategy_name != '':
            if map_name in map_strat:
                map_strat[map_name].append(strategy_name)
            else:
                map_strat.update({map_name : [strategy_name]})
    return map_strat

def info_display(plan: str) -> str:
    """Returns current plan info string.

    Args:
        plan: Plan name string:

    Returns:
        Customized info string.
    """
    map_name = return_map(plan)
    diff, gamemode = return_strategy(plan).split('-')
    if gamemode[-1] in (str(i) for i in range(2,10)):
        mode = gamemode[:-1]
    else:
        mode = gamemode
    return '-'*12 +'\n'f'>Map: {map_name}\n'f'>Difficulty: {diff.lower()}\n'f'>Mode: {mode.lower()}\n'

def list_format(list_object: list[str]) -> list[str]:
    """Formats a list, such as list of all maps, by removing newline and leading/trailing whitespace characters.

    Args:
        list_object: List of strings.

    Returns:
        List of processed strings.
    """
    clean_list = []
    new: str | bytes
    for obj_str in list_object:
        new = obj_str.replace('\n', ' ').strip()
        if not new:     # if map row element is empty, don't add it.
            continue
        clean_list.append(new)
    return clean_list