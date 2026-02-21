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
import datetime
import importlib
import json
import pathlib

from bot import _maindata
from customprint import cprint
import plans # only used via importlib module.
from utils import plan_data
from utils.exceptions import SetPlanError, BotError

if TYPE_CHECKING:
    from typing import Any
    from types import ModuleType

def _check_if_temp_valid(temp_data: list[str]) -> bool:
    """Check if times_temp has all round data + total time rows."""
    return True if len(temp_data) >= 2 and ',' not in temp_data[-1] else False

def _read_timedata() -> Any:
    with open(pathlib.Path(__file__).parent/'Files'/'time_data.json') as f:
        return json.load(f)

def _read_botvars() -> Any:
    with open(pathlib.Path(__file__).parent/'Files'/'bot_vars.json') as varsfile:
        return json.load(varsfile)["version"]

def _update_time_data(plan_name: str, temp_data: list[str]) -> dict[str, Any]:
    """Adds temporary time data contents of a plan to dictionary and return this new dict."""
    times_contents = plan_data.list_format(temp_data)
    roundstimes_dict = {}

    for r_time in times_contents[:-1]:
        round_num, round_time = r_time.split(',')
        roundstimes_dict[round_num] = round_time
    time_total = times_contents[-1]
    current_json: dict[str, Any] = _read_timedata()
    current_version: dict[str, Any] = _read_botvars()
    date: str = str(datetime.date.today()).replace('-','/')
    data_dict = {
        "update_date": date,
        "version": current_version,
        "roundtimes": roundstimes_dict,
        "time_total": time_total
        }
    if plan_name not in current_json.keys():
        current_json.update({plan_name: data_dict})
    else:
        current_json[plan_name] = data_dict
    return current_json

def _save_to_json(plan_name: str, time_data: list[str]) -> None:
    """Saves time data to time_data.json file which gui.roundplot requires when creating plots.
    
    Should only be called by plan_run.
    """
    new_times = dict(sorted(_update_time_data(plan_name, time_data).items()))
    with open(pathlib.Path(__file__).parent/'Files'/'time_data.json') as timef:
        current_times: dict[str, Any] = json.load(timef)
    with open(pathlib.Path(__file__).parent/'Files'/'time_data-backup.json', 'w') as timef:
        json.dump(current_times, timef, indent=2)
    with open(pathlib.Path(__file__).parent/'Files'/'time_data.json', 'w') as f:
        json.dump(new_times, f, indent=2)

def run_delta_adjust() -> None:
    # internal imports bot._adjust_deltas and bot._farming should only be loaded after the first function call
    # in order to prevent ocr reader's auto-initialization
    import bot._adjust_deltas
    bot._adjust_deltas.run()

def farming_print() -> None:
    """Print message when farming mode is enabled."""
    cprint("Collection event farming mode enabled.\n" \
            "Bot keeps farming expert maps with bonus rewards on Easy, Standard.\n"
            "Monkey knowledge is not required.\n"
            "Only Sauda is required as hero, make sure you have her unlocked.\n")

def select_defaulthero() -> bool:
    import bot._farming
    return bot._farming.select_defaulthero() # type: ignore[no-any-return]

def select_rewardplan() -> str:
    import bot._farming
    planname: str = bot._farming.select_rewardplan()
    return planname

def run_farming_mode(rewardplan: str) -> bool:
    import bot._farming
    bot._farming.click_rewardmap()
    return plan_setup(rewardplan, True)

def get_rounds(difficulty: str, gamemode: str) -> tuple[int, int]:
    """Returns begin and end rounds based on difficulty + game mode.

    Args:
        difficulty: Difficulty setting in all uppercase e.g. EASY
        gamemode: Game mode setting in all uppercase e.g. STANDARD

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
                raise SetPlanError("GamemodeError")
    elif difficulty == 'MEDIUM':
        if gamemode in {'STANDARD', 'REVERSE','MILITARY', 'APOPALYPSE'}:
            return 1, 60
        else: 
            raise SetPlanError("GamemodeError")
    elif difficulty == 'HARD':
        match gamemode:
            case 'STANDARD' | 'MAGIC' | 'DOUBLE_HP' | 'HALF_CASH' | 'ALTERNATE':
                return 3, 80
            case 'IMPOPPABLE' | 'CHIMPS':
                return 6, 100
            case _:
                raise SetPlanError("GamemodeError")
    else:
        raise SetPlanError("DifficultyError")

def get_plan_info(plan: str) -> tuple[str, str, str, int, int]:
    """Returns map name, difficulty, game mode, begin and end rounds, and hero.
    
    Args:
        plan: Current plan.

    Returns:
        Tuple of current plan info.
    """
    map_name = plan_data.return_map(plan)
    raw_strat = plan_data.return_strategy(plan)
    if map_name == '' or raw_strat == '':
        raise SetPlanError("SyntaxError")
    split = raw_strat.split('-')
    if split[1][-1] in (str(i) for i in range(2,10)):
        diff, mode = split[0].upper(), split[1].upper()[:-1]
    else:
        diff, mode = split[0].upper(), split[1].upper()
    begin, end = get_rounds(diff, mode)
    return (map_name, diff, mode, begin, end)

def get_hero_name_from_plan(plan_info: list[str]) -> str:
    """Finds hero name from a plan info string.
    
    Args:
        plan_info: Plan info string.

    Returns:
        Hero name string. Returns '-' if [Hero] is missing from plan documentation.
    """
    for line in plan_info:
        if '[Hero]' in line:
            return line[6:].strip()
    return '-'

def plan_run(plan_name: str, plan_module: ModuleType, info: tuple[str, str, str, int, int, str, bool]) -> None:
    """Runs the plan file with given information.

    Also handles time recording for round plots.

    Args:
        plan_name: Name of current plan.
        plan_module: Importlib module of current plan.
        info: All information required for a plan. Components are: map name, difficulty, game mode, 
            begin round, end round, hero name, farming mode status.
    """
    try:
        plan_module.play(info)
        if not info[-1] and _check_if_temp_valid(_maindata.maindata["times_temp"]):
            _save_to_json(plan_name, _maindata.maindata["times_temp"])
    except BotError as err:
        cprint(err)

def plan_setup(plan: str, farming: bool = False) -> bool:
    """Handles and passes map, strategy and round settings to correct map module.

    Matches to correct map module, fetches plan info and passes these to plan_run function.

    Args:
        plan: Raw string of current plan name.
        farming: Whether farming mode is on or not.
    
    Returns:
        Boolean False if an error occured, otherwise True
    """
    try:
        plan_module = importlib.import_module(name='plans.'+plan)
    except ModuleNotFoundError:
        cprint(f'Plan file {plan}.py doesn\'t exist OR invalid module import somewhere under bot package.')
        return False
    try:
        info = get_plan_info(plan)
    except SetPlanError as e:
         cprint(f'{plan} - ', end='')
         cprint(e)
         return False
    if farming:
        plan_run(plan, plan_module, (*info, '-', True))
    else:
        plan_file_name = plan+'.py'
        with open(pathlib.Path(__file__).parent/'plans'/plan_file_name) as plan_file:
            plan_info = plan_data.list_format(plan_file.readlines())
        plan_run(plan, plan_module, (*info, get_hero_name_from_plan(plan_info), False))
    return True