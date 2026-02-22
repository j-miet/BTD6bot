"""Unit tests for btd6bot/set_plan.py

Be careful with mock patching: if you don't patch the file saving operations, they could override time_data.json. Times
can of course be recorded again easily should such an incident occur, but it would take some time to do this with all 
plans.
"""

from typing import Any

import pytest

import set_plan
from utils.exceptions import SetPlanError

@pytest.mark.parametrize("temp_data, expected", [
    (["1,0:12", "2,0:05", "3,0:30", "0:47"], True),
    (["1,0:12", "2,0:05", "3,0:30", "0:47,"], False),
    (["1,0:10"], False),
    (["0:10"], False),
])
def test_check_if_temp_valid(temp_data: list[str], expected: bool):
    assert set_plan._check_if_temp_valid(temp_data) == expected

def test_update_time_data(mocker):
    time_data = ["1,0:12", "2,0:05", "3,0:30", "0:47"]
    version = 10
    date = "2025-02-12"

    mock_timedata = mocker.patch("set_plan._read_timedata")
    mock_timedata.return_value = {
        "logsEasyStandard": {
            "update_date": "2025/01/01",
            "version": 1,
            "roundtimes": {"1": "0:08", "2": "0:12", "3": "0:02", "4": "0:22", "5": "0:15"},
            "time_total": "0:59"
            },
        "quadHardImpoppable": {
            "update_date": "2025/05/20",
            "version": 48,
            "roundtimes": {"10": "0:24", "11": "0:32", "12": "0:42", "13": "0:12", "14": "0:11"},
            "time_total": "2:01"
            },
    }
    mock_version = mocker.patch("set_plan._read_version")
    mock_version.return_value = version
    mock_datetime = mocker.patch("set_plan.datetime.date")
    mock_datetime.today.return_value = date
    date_string = date.replace('-','/')

    add_first: dict[str, Any] = set_plan._update_time_data("monkey_meadowMediumMilitary", time_data)
    assert add_first == {
        "logsEasyStandard": {
            "update_date": "2025/01/01",
            "version": 1,
            "roundtimes": {"1": "0:08", "2": "0:12", "3": "0:02", "4": "0:22", "5": "0:15"},
            "time_total": "0:59"
            },
        "quadHardImpoppable": {
            "update_date": "2025/05/20",
            "version": 48,
            "roundtimes": {"10": "0:24", "11": "0:32", "12": "0:42", "13": "0:12", "14": "0:11"},
            "time_total": "2:01"
            },
        "monkey_meadowMediumMilitary": {
            "update_date": date_string,
            "version": version,
            "roundtimes": {"1": "0:12", "2": "0:05", "3": "0:30"},
            "time_total": "0:47"
            }
    }
    assert set_plan._update_time_data("dark_castleHardAlternate", time_data) == {
        "logsEasyStandard": {
            "update_date": "2025/01/01",
            "version": 1,
            "roundtimes": {"1": "0:08", "2": "0:12", "3": "0:02", "4": "0:22", "5": "0:15"},
            "time_total": "0:59"
            },
        "quadHardImpoppable": {
            "update_date": "2025/05/20",
            "version": 48,
            "roundtimes": {"10": "0:24", "11": "0:32", "12": "0:42", "13": "0:12", "14": "0:11"},
            "time_total": "2:01"
            },
        "monkey_meadowMediumMilitary": {
            "update_date": date_string,
            "version": version,
            "roundtimes": {"1": "0:12", "2": "0:05", "3": "0:30"},
            "time_total": "0:47"
            },
        "dark_castleHardAlternate": {
            "update_date": date_string,
            "version": version,
            "roundtimes": {"1": "0:12", "2": "0:05", "3": "0:30"},
            "time_total": "0:47"
            },
    }

    assert mock_timedata.call_count == 2
    assert mock_version.call_count == 2

def test_save_to_json(mocker):
    mock_open = mocker.patch("set_plan.open", mocker.mock_open())
    mock_load = mocker.patch("set_plan.json.load")
    mock_update_time_data = mocker.patch("set_plan._update_time_data")
    mock_json_dump = mocker.patch("set_plan.json.dump")

    set_plan._save_to_json("monkey_meadowMediumMilitary", ["1,0:01\n", "0:01"])

    mock_update_time_data.assert_called_once()
    mock_load.assert_called_once()
    assert mock_open.call_count == 3
    assert mock_json_dump.call_count == 2

@pytest.mark.parametrize("plan_info, hero_str", [
    (["'''"
    "[Plan Name] monkey_meadowEasyPrimary",  
    "[Game Version] 45",    
    "[Hero] Quincy",
    "[Monkey Knowledge] Yes",
    "-------------------------------------------------------------",
    "_______________________________________",
    "",
    "Testing...",
    "",
    "'''"], "Quincy"),
    (["'''",
    "[Plan Name] dark_castleHardChimps",
    "[Game Version] 46",
    "[Hero]test hero string",
    "[Monkey Knowledge] -",
    "-------------------------------------------------------------",
    "_______________________________________",
    "Test",
    "",
    "'''"], "test hero string"),
    (["'''",  
    "[Plan Name] dark_castleMediumMilitary",
    "[Game Version]  ",
    "[Hero]    -  ",
    "[Monkey Knowledge]    ",
    "-------------------------------------------------------------",
    "==Monkeys==",
    "ace 2-0-3 ",
    "alch 4-2-0",
    "village 2-2-0",
    "_______________________________________",
    "'''"], '-'),
    (['"""',
    "[Plan Name] map",
    "[Game Version] version",
    "[Heeeeero] Quincy",
    "[Monkey Knowledge] mk",
    "-------------------------------------------------------------",
    '"""'], '-')
])
def test_get_hero_name_from_plan_mock(plan_info, hero_str):
    assert set_plan.get_hero_name_from_plan(plan_info) == hero_str

@pytest.mark.parametrize("strat, expected_rounds", [
    (('EASY', 'STANDARD'), (1, 40)),
    (('EASY', 'PRIMARY'), (1, 40)),
    (('EASY', 'DEFLATION'), (31, 60)),

    (('MEDIUM', 'STANDARD'), (1, 60)),
    (('MEDIUM', 'REVERSE'), (1, 60)),
    (('MEDIUM', 'MILITARY'), (1, 60)),
    (('MEDIUM', 'APOPALYPSE'), (1, 60)),

    (('HARD', 'STANDARD'), (3, 80)),
    (('HARD', 'MAGIC'), (3, 80)),
    (('HARD', 'DOUBLE_HP'), (3, 80)),
    (('HARD', 'HALF_CASH'), (3, 80)),
    (('HARD', 'ALTERNATE'), (3, 80)),
    (('HARD', 'IMPOPPABLE'), (6, 100)),
    (('HARD', 'CHIMPS'), (6, 100))
])
def test_get_rounds(strat, expected_rounds):
    assert set_plan.get_rounds(*strat) == expected_rounds

def test_get_rounds_raise_BotError():
    with pytest.raises(SetPlanError):
        set_plan.get_rounds('EASY', 'Test')
    with pytest.raises(SetPlanError):
        set_plan.get_rounds('', 'EASY')

@pytest.mark.parametrize("plan_str, map_info", [
    ("cubismHardMagic", ('cubism', 'HARD', 'MAGIC', 3, 80)),
    ("one_two_treeMediumStandard", ('one two tree', 'MEDIUM', 'STANDARD', 1, 60)),
    ('test_mapEasyStandard', ('test map', 'EASY', 'STANDARD', 1, 40)),
    ('testmapHardChimps', ('testmap', 'HARD', 'CHIMPS', 6, 100))
])
def test_get_plan_info(plan_str, map_info):
    assert set_plan.get_plan_info(plan_str) == map_info

@pytest.mark.parametrize("map_name, error_msg", [
    ('test_map', "Current plan file has invalid syntax: Correct syntax is map_nameDifficultyMode."),
    ('test_mapDiff', "Current plan file has invalid syntax: Correct syntax is map_nameDifficultyMode."),
    ('test_map_number_twoeasyDeflation', 
     "Current plan file has invalid syntax: Correct syntax is map_nameDifficultyMode."),
    ('test_map_number_threeTooeasyStandard', "Current plan file has invalid difficulty."),
    ('test_map_number_fourHardMode', "Current plan file has invalid game mode for selected difficulty.")

])
def test_get_plan_info_SetPlanError(map_name, error_msg):
    with pytest.raises(SetPlanError, match=error_msg):
        assert set_plan.get_plan_info(map_name)

def test_plan_run(mocker):
    # set_plan.importlib.import_module must be patched last or otherwise it will, as expected, interfere with all 
    # imports done after.

    mock_temp_valid = mocker.patch("set_plan._check_if_temp_valid")
    mock_temp_valid.return_value = True

    mock_savetojson = mocker.patch("set_plan._save_to_json") # override _save_to_json call; no need to test it here.

    mock_name = "test_planEasyStandard"
    mock_module= mocker.patch("set_plan.importlib.import_module") # this must be patched last!
    moc_info = ("test_plan", "Easy", "Standard", 1, 40, 'Quincy', False)

    set_plan.plan_run(mock_name, mock_module, moc_info)

    mock_savetojson.assert_called()

def test_plan_setup(mocker):
    mock_open_in_hero_select = mocker.patch("set_plan.open", mocker.mock_open())
    mocker.patch("set_plan.plan_run", lambda a, b, c: 1) # override plan_run; no need to test it here.
    mock_module = mocker.patch("set_plan.importlib.import_module")
    set_plan.plan_setup("dark_castleEasyStandard")

    mock_module.assert_called_once()
    mock_open_in_hero_select.assert_called_once()