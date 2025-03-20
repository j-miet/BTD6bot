"""Unit tests for btd6bot/utils/plan_data.py"""

import pathlib

import pytest

from utils import plan_data

@pytest.mark.parametrize("mock_return, plan_list", [
    (["__pycache__",
        "some_folder",
        "__init__.py",
        "dark_castleEasyStandard.py",
        "dark_castleMediumApopalypse.py",
        "dark_castleHardDouble_hp.py",
        "quadHardMagic.py",
        "some_file.txt",
        "town_centerHardStandard.py"
      ],
      ["dark_castleEasyStandard",
        "dark_castleHardDouble_hp",
        "dark_castleMediumApopalypse",
        "quadHardMagic",
        "town_centerHardStandard"]),
    (["__init__.py"], []),
    ([], [])  
])
def test_read_plans(mocker, mock_return, plan_list):
    listdir_mock = mocker.patch("os.listdir")
    listdir_mock.return_value = mock_return

    assert plan_data.read_plans() == plan_list
    listdir_mock.assert_called_once_with(pathlib.Path(__file__).parent.parent.parent / 'btd6bot' / 'plans')

def test_return_map():
    assert plan_data.return_map('cubismEasyStandard') == 'cubism'
    assert plan_data.return_map('cubismeasystandard') == ''

@pytest.mark.parametrize("input_plan, expected_strat", [
    ('logsHardChimps', 'Hard-Chimps'),
    ('', ''),
    ('logshardChimps', ''),
    ('logsHardchimps', ''),
    ('logshardchimps', '')
])
def test_return_strategy(input_plan, expected_strat):
    assert plan_data.return_strategy(input_plan) == expected_strat

@pytest.mark.parametrize("file_list, data_dict", [
    (["balanceMediumMilitary",  
      "dark_castleEasyStandard",  
      "dark_castleMediumApopalypse",  
      "dark_castleHardDouble_hp",  
      "gearedEasyDeflation",  
      "quadEasyStandard",  
      "quadHardMagic",  
      "town_centerHardStandard"  
      ],
     {"balance": ["Medium-Military"],
      "dark castle": ["Easy-Standard", "Medium-Apopalypse", "Hard-Double_hp"],
      "geared": ["Easy-Deflation"],
      "quad": ["Easy-Standard", "Hard-Magic"],
      "town center": ["Hard-Standard"]
      }
    )  
])
def test_return_maps_and_strats(file_list, data_dict):
    assert plan_data.return_maps_and_strats(file_list) == data_dict

def test_info_display():
    assert plan_data.info_display('end_of_the_roadHardAlternate') == str(
    "------------\n"
    ">Map: end of the road\n"
    ">Difficulty: hard\n"
    ">Mode: alternate\n"
    )

def test_list_format():
    assert plan_data.list_format(["   string1", "string2   ", " string3\n\n", "\nstring4"]
                                 ) == ["string1", "string2", "string3", "string4"]
