"""Unit tests for btd6bot/set_plan.py"""

import pytest

import set_plan
from utils.exceptions import SetPlanError

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