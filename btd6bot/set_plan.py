"""Plan initializing.

Used for selecting
 -hero by reading it from current plan docstrings

 -rounds based on difficulty and game mode,

 -correct .py file to be imported, and then running the corresponding plan module.

Note: 'plans' package contains all playable plans. To avoid listing all of the imports, importlib's
import_module method is used instead, with module name passed as an argument to plan_setup.

Also includes round time data saving tools for roundplot plotting purposes.
Both functions (adding new time data to json and flushing contents of temp text file) are only called if time recording 
status is True.
"""

from __future__ import annotations
from typing import TYPE_CHECKING
import importlib
import json
import pathlib

import plans # shows as 'not accessed' in VS Code, because it's only used via importlib module.
from utils import plan_data
from utils.exceptions import SetPlanError, BotError

if TYPE_CHECKING:
    from typing import Any
    from types import ModuleType

def _check_if_temp_valid(begin_r: int, end_r: int) -> bool:
    """Check if times_temp has all round data + total time rows."""
    with open(pathlib.Path(__file__).parent/'Files'/'times_temp.txt') as f:
        lines = f.readlines()
    return True if len(lines) == end_r-begin_r+2 else False

def _flush_times_temp() -> None:
    """Flushes existing contents of Files//times_temp.txt to allow new plan time data to be saved."""
    with open(pathlib.Path(__file__).parent/'Files'/'times_temp.txt', 'w') as f:
        print('times_temp.txt contents cleared.')

def _read_timedata() -> dict[str, Any]:
    with open(pathlib.Path(__file__).parent/'Files'/'time_data.json') as f:
        return json.load(f)

def _read_guivars() -> dict[str, Any]:
    with open(pathlib.Path(__file__).parent/'Files'/'gui_vars.json') as varsfile:
        return json.load(varsfile)["version"]

def _update_time_data(plan_name: str) -> dict[str, Any]:
    """Adds saved times_temp.txt contents in a dictionary."""
    with open(pathlib.Path(__file__).parent/'Files'/'times_temp.txt') as f:
        times_contents = f.readlines()
    times_contents = plan_data.list_format(times_contents)
    rounds_list = []
    times_list = []
    for r_time in times_contents[:-1]:
        round_num, round_time = r_time.split(',')
        rounds_list.append(round_num)
        times_list.append(round_time)
    time_total = times_contents[-1]
    current_json: dict[str, Any] = _read_timedata()
    current_version: dict[str, Any] = _read_guivars()
    data_dict = {
        "version": current_version,
        "rounds": rounds_list,
        "times": times_list,
        "time_total": time_total
        }
    if plan_name not in current_json.keys():
        current_json.update({plan_name: data_dict})
    else:
        current_json[plan_name] = data_dict
    return current_json

def _save_to_json(plan_name: str) -> None:
    """Saves time data to time_data.json file which gui.roundplot requires when creating plots.
    
    Should only be called by plan_run.
    """
    json_data = _update_time_data(plan_name)
    with open(pathlib.Path(__file__).parent/'Files'/'time_data.json', 'w') as f:
        json.dump(json_data, f, indent=4)
    print('Plot time data for', plan_name, 'updated.\n')

def get_rounds(difficulty: str, gamemode: str) -> tuple[int, int]:
    """Returns begin and end rounds based on difficulty + game mode.

    Args:
        difficulty: Difficulty setting.
        gamemode: Game mode setting.

    Raises:
        SetPlanError: If plan string name has invalid difficulty and/or game mode syntax/name.
    """
    if difficulty == 'EASY':
        match gamemode:
            case 'STANDARD' | 'PRIMARY':
                return 1, 40
            case 'DEFLATION':
                return 31, 60
            case _:
                raise SetPlanError(3)
    elif difficulty == 'MEDIUM':
        if gamemode in {'STANDARD', 'REVERSE','MILITARY', 'APOPALYPSE'}:
            return 1, 60
        else: 
            raise SetPlanError(3)
    elif difficulty == 'HARD':
        match gamemode:
            case 'STANDARD' | 'MAGIC' | 'DOUBLE_HP' | 'HALF_CASH' | 'ALTERNATE':
                return 3, 80
            case 'IMPOPPABLE' | 'CHIMPS':
                return 6, 100
            case _:
                raise SetPlanError(3)
    else:
        raise SetPlanError(2)

def get_plan_info(plan: str) -> tuple[str, str, str, int, int]:
    """Returns map name, difficulty, game mode, begin and end rounds, and used hero.
    
    Args:
        plan: Current plan.

    Returns:
        Tuple of current plan info.
    """
    map_name = plan_data.return_map(plan)
    raw_strat = plan_data.return_strategy(plan)
    if map_name == '' or raw_strat == '':
        raise SetPlanError(1)
    split = raw_strat.split('-')
    if split[1][-1] in (str(i) for i in range(2,10)):
        diff, mode = split[0].upper(), split[1].upper()[:-1]
    else:
        diff, mode = split[0].upper(), split[1].upper()
    begin, end = get_rounds(diff, mode)
    return (map_name, diff, mode, begin, end)

def get_hero_name_from_plan(plan_name: str) -> str:
    """Return plan hero name by parsing its value from documentations of current plan.
    
    Args:
        plan_name: Name of current plan.

    Returns:
        Hero name string. Returns '-' if [Hero] is missing from plan documentation. Hero name will be tested later 
        under bot so at this point it can be anything.
    """
    plan_file_name = plan_name+'.py'
    with open(pathlib.Path(__file__).parent/'plans'/plan_file_name) as plan_file:
        plan_code = plan_data.list_format(plan_file.readlines())
    for line in plan_code:
        if '[Hero]' in line:
            return line[6:].strip()
    return '-'

def plan_run(plan_name: str, plan_module: ModuleType, info: tuple[str, str, str, int, int, str]) -> None:
    """Runs the plan file with given information.

    Also handles time recording for round plots if time_recording_status is set to True.

    Args:
        plan_name: Name of current plan.
        plan_module: Importlib module of current plan.
        info: All information required for a plan. Components are: map name, difficulty, game mode, 
            begin round, end round, hero name.
    """
    try:
        with open(pathlib.Path(__file__).parent/'Files'/'gui_vars.json') as f:
            gui_vars: dict[str, str | bool | int] = json.load(f)
        if gui_vars["time_recording_status"]:
            _flush_times_temp()
        plan_module.play(info)
        if gui_vars["time_recording_status"]:
            if _check_if_temp_valid(info[3], info[4]):
                _save_to_json(plan_name)
            else:
                print("Plan could not be finished, no time data saved.")
    except BotError as err:
        print(err)

def plan_setup(plan: str) -> None:
    """Handles and passes map, strategy and round settings to correct map module.

    Matches to correct map module, fetches plan info and passes these to plan_run function.

    Args:
        plan: Raw string of current plan name.
    """
    try:
        plan_module = importlib.import_module(name='plans.'+plan)
    except ModuleNotFoundError:
        print(f'Plan file {plan}.py doesn\'t exist OR invalid module import somewhere under bot package.')
        return
    try:
        info = get_plan_info(plan)
    except SetPlanError as e:
         print(f'{plan} - ', end='')
         print(e)
         return
    plan_run(plan, plan_module, (*info, get_hero_name_from_plan(plan)))