"""Data flow of files"""

import json
from pathlib import Path
from typing import Any

from customprint import cprint

maindata: dict[str, Any] = {}

def init_readvalues(maindata_dict: dict[str, Any] = maindata) -> bool:
    maindata_dict.update({})
    failed: bool = False
    temp_dict: dict[str, Any] = {}
    try:
        with open(Path(__file__).parent.parent/'Files'/'text files'/'hotkeys.txt') as hotkeys:
            temp_dict["hotkeys"] = hotkeys.readlines()
    except FileNotFoundError:
        cprint("Can't access hotkeys.txt file")
        failed = True
    try:
        with open(Path(__file__).parent.parent/'Files'/'bot_vars.json') as botvars:
            temp_dict["bot_vars"] = json.load(botvars)
    except json.decoder.JSONDecodeError:
        cprint("Can't access bot_vars.json file")
        failed = True
    try:
        with open(Path(__file__).parent.parent/'Files'/'custom_locations.json') as custom_loc:
            temp_dict["custom_locations"] = json.load(custom_loc)
    except json.decoder.JSONDecodeError:
        cprint("Can't access custom_locations.json file")
        failed = True
    try:
        with open(Path(__file__).parent.parent/'Files'/'_ocr_upgradedata.json') as base:
            temp_dict["ocr_basedata"] = json.load(base)
    except json.decoder.JSONDecodeError:
        cprint("Can't access _ocr_upgradedata.json file")
        failed = True
    try:
        with open(Path(__file__).parent.parent/'Files'/'upgrades_current.json') as upg_data:
            temp_dict["ocr_upgradedata"] = json.load(upg_data)
    except json.decoder.JSONDecodeError:
        cprint("Can't access upgrades_current.json file")
        failed = True

    temp_dict["times_temp"] = [] # for round times
    temp_dict["temp_upg_deltas"] = {} # for _adjust_deltas
    temp_dict["toggle"] = {"event_status": False, # toggled status for collection events and farming mode
                            "farming_status": False}
    temp_dict["internal"] = {"time_recording_status": True,
                            "paused": False,
                            "defeat_status": False}
    if failed:
        return False
    else:
        maindata_dict.update(temp_dict)
        return True

def write_botvars(new_vars: dict[str, Any]) -> None:
    with open(Path(__file__).parent.parent/'Files'/'bot_vars.json', 'w') as guivars_f:
        json.dump(new_vars, guivars_f, indent=4)

def write_ocr_upgrades(new_ocrvals: dict[str, Any]) -> None:
    with open(Path(__file__).parent.parent/'Files'/'upgrades_current.json', 'w') as f:
        json.dump(new_ocrvals, f, indent=2)

init_readvalues()