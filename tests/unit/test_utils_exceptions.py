"""Unit tests for btd6bot/utils/exceptions.py"""

import pytest

from utils.exceptions import SetPlanError, BotError

def test_setplanerror_args():
    err = SetPlanError("SyntaxError")
    assert err.code == "SyntaxError"

@pytest.mark.parametrize("error, message", [
    (SetPlanError("SyntaxError"), "Current plan file has invalid syntax: Correct syntax is map_nameDifficultyMode."),
    (SetPlanError("DifficultyError"), "Current plan file has invalid difficulty."),
    (SetPlanError("GamemodeError"), "Current plan file has invalid game mode for selected difficulty."),
    (SetPlanError(""), "Undefined error.")
])
def test_setplanerror_msg(error: SetPlanError, message: str):
    assert error.__str__() == message

def test_boterror_args():
    err = BotError("test message", 10)
    assert err.msg == "test message"
    assert err.code == 10

def test_boterror_msg():
    boterror1 = BotError("test message", "Error code")
    boterror2 = BotError("Failed to enter a game", "FailedToEnter")
    boterror3 = BotError("error", 1)
    assert boterror1.__str__() == "BotError: Error code -> test message"
    assert boterror2.__str__() == "BotError: FailedToEnter -> Failed to enter a game"
    assert boterror3.__str__() == "BotError: 1 -> error"