"""Unit tests for btd6bot/utils/exceptions.py"""

import pytest

from utils.exceptions import SetPlanError, BotError

def test_setplanerror_args():
    err = SetPlanError(1)
    assert err.code == 1

@pytest.mark.parametrize("error, message", [
    (SetPlanError(1), "Current plan file has invalid syntax: Correct syntax is map_nameDifficultyMode."),
    (SetPlanError(2), "Current plan file has invalid difficulty."),
    (SetPlanError(3), "Current plan file has invalid game mode for selected difficulty.")
])
def test_setplanerror_msg(error, message):
    assert error.__str__() == message

def test_boterror_args():
    err = BotError("test message", 10)
    assert err.msg == "test message"
    assert err.code == 10

def test_boterror_msg():
    boterror1 = BotError("test message", "Error code")  # works, but numbers are used instead
    boterror2 = BotError("Failed to enter a game", 1)
    assert boterror1.__str__() == "(BotError Error code) test message."
    assert boterror2.__str__() == "(BotError 1) Failed to enter a game."