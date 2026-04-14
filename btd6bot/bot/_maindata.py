"""Data flow of files"""

from enum import Enum
import json
from pathlib import Path
from typing import Any

from customprint import cprint


class Debug(Enum):
    """Enum class for debugging modes"""

    NONE = 0
    """No debugging, default state"""
    POS_STATIC = 1
    """static position check, assumes tower positions don't change between rounds"""
    POS_DYNAMIC = 2
    """dynamic position check, towers can move between rounds. Much slower than static checking.
    """
    SETUP_STATIC_STATE = 3
    """Executes all commands starting from a specific round and assumes static positioning of towers."""


maindata: dict[str, Any] = {}
"""Central data storage for btd6bot during runtime."""


def init_maindata(maindata_dict: dict[str, Any] = maindata) -> bool:
    """Initialize maindata dictionary by reading data from core files.

    For each missing file print a message and set return value to False. Missing files will not immediately cause
    issues, but in most cases lead to eventual crash.

    [How to use]

    First init call is always made in _maindata module i.e. where this function is defined. This alone is sufficient if
    no further file writes are performed during runtime loop. This is the default behavior for _no_gui.py as it's meant
    to operate with its initial state and not alter it, making it lightweight to operate.

    If additional file writes are done then init must be called before new data is meant to be accessed. Two clear use
    cases for this are
    1. creating and running multiple bot runtime cycles with a possibility that passed data needs to be updated between
        cycles -> BTD6bot GUI after a new  monitoring window gets created
    2. running a separate update process not part of core runtime loop, but still requiring bot tools -> _adjust_deltas
        running ocr adjusting process
    """
    maindata_dict.update({})
    failed: bool = False
    temp_dict: dict[str, Any] = {}
    try:
        with open(Path(__file__).parent.parent / "Files" / "text files" / "hotkeys.txt") as hotkeys:
            temp_dict["hotkeys"] = hotkeys.readlines()
    except FileNotFoundError:
        cprint("Can't access hotkeys.txt file")
        failed = True
    try:
        with open(Path(__file__).parent.parent / "Files" / "bot_vars.json") as botvars:
            temp_dict["bot_vars"] = json.load(botvars)
    except json.decoder.JSONDecodeError:
        cprint("Can't access bot_vars.json file")
        failed = True
    try:
        with open(Path(__file__).parent.parent / "Files" / "custom_locations.json") as custom_loc:
            temp_dict["custom_locations"] = json.load(custom_loc)
    except json.decoder.JSONDecodeError:
        cprint("Can't access custom_locations.json file")
        failed = True
    try:
        with open(Path(__file__).parent.parent / "Files" / "_ocr_upgradedata.json") as base:
            temp_dict["ocr_basedata"] = json.load(base)
    except json.decoder.JSONDecodeError:
        cprint("Can't access _ocr_upgradedata.json file")
        failed = True
    try:
        with open(Path(__file__).parent.parent / "Files" / "upgrades_current.json") as upg_data:
            temp_dict["ocr_upgradedata"] = json.load(upg_data)
    except json.decoder.JSONDecodeError:
        cprint("Can't access upgrades_current.json file")
        failed = True

    # built-in data paths (= not read from a file)
    temp_dict["times_temp"] = []  # for round times
    temp_dict["temp_upg_deltas"] = {}  # for _adjust_deltas
    temp_dict["toggle"] = {  # toggled status for collection events and farming mode
        "event_status": False,
        "farming_status": False,
    }
    temp_dict["internal"] = {
        "time_recording_status": True,
        "paused": False,
        "defeat_status": False,
        "skip_roundcheck": False,
    }
    temp_dict["debug"] = {  # preferably modify these value only via scripts
        "mode": Debug.NONE,  # TODO implement POS_DYNAMIC
        "time_limit": 5,
        # values below are only for SETUP_STATIC_STATE
        "debug_ignore": False,  # used for ignoring round forward and time-related commands
        "state_startround": -1,
        "hero_startlevel": -1,
    }

    if failed:
        return False
    else:
        maindata_dict.update(temp_dict)
        return True


def write_botvars(new_vars: dict[str, Any]) -> None:
    with open(Path(__file__).parent.parent / "Files" / "bot_vars.json", "w") as botvars_f:
        json.dump(new_vars, botvars_f, indent=4)


def write_ocr_upgrades(new_ocrvals: dict[str, Any]) -> None:
    with open(Path(__file__).parent.parent / "Files" / "upgrades_current.json", "w") as f:
        json.dump(new_ocrvals, f, indent=2)


def debug_pos() -> bool:
    if maindata["debug"]["mode"] in {Debug.POS_STATIC, Debug.POS_DYNAMIC}:
        return True
    return False


def debug_all() -> bool:
    if maindata["debug"]["mode"] in {
        Debug.POS_STATIC,
        Debug.POS_DYNAMIC,
        Debug.SETUP_STATIC_STATE,
    }:
        return True
    return False


def debug_get_ignore_flag() -> bool:
    ignored: bool = maindata["debug"]["debug_ignore"]
    return ignored


def debug_set_ignore_flag(val: bool) -> None:
    maindata["debug"]["debug_ignore"] = val


def debug_get_timelimit() -> float:
    limit: float = maindata["debug"]["time_limit"]
    return limit


def debug_get_mode() -> Debug:
    mode: Debug = maindata["debug"]["mode"]
    return mode


def debug_set_mode(val: Debug) -> None:
    """Sets debugging mode.

    Debug.NONE = disable debugging (default)

    Debug.POS_STATIC = static tower position check, all commands except tower placement & selling are ignored

    Debug.SETUP_STATIC_STATE = static tower positions, run all commands each round to setup specific round state. Then
        continue plan normally from stated round. Round must be updated u

    If you change mode to anything else than Debug.NONE, it will stay that way unless you call
    debug_set_mode(Debug.NONE) again
    """
    maindata["debug"]["mode"] = val


def debug_get_startround() -> int:
    start: int = maindata["debug"]["state_startround"]
    return start


def debug_set_startround(val: int) -> None:
    maindata["debug"]["state_startround"] = val


init_maindata()  # first init when program starts
