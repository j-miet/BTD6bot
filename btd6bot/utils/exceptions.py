"Custom exception classes for BTD6bot."

class SetPlanError(Exception):
    """Exception for tracking invalid syntax and/or invalid substring values in plan file string.
    
    Attributes:
        code: Error identification code.

    Error codes:
    __
        1: Plan file syntax error: cannot differentiate map, difficulty and game mode values.  
        2: Invalid difficulty in plan file.  
        3: Invalid game mode in plan file: either invalid game mode value, or it's under wrong difficulty e.g. 
            logsEasyChimps.
    """
    def __init__(self, code) -> None:
        """Invalid syntax and/or invalid substring values in plan file string."""
        self.code = code
        super().__init__(f"Current plan file has invalid difficulty and/or game mode.")

    def __str__(self):
        if self.code == 1:
            return "Current plan file has invalid syntax: Correct syntax is map_nameDifficultyMode."
        elif self.code == 2:
            return "Current plan file has invalid difficulty."
        elif self.code == 3:
            return "Current plan file has invalid game mode for selected difficulty."
    

class BotError(Exception):
    """BotError class for handling all errors occuring under 'bot' package.

    This errors should only be raised withing bot package modules.
    
    Attributes:
        msg (str): Message string. Important because if error is not handled, this text is displayed.
        code (int): Code to identify the exact problem.
    
    Error codes:
    __
        1: Bot failed to enter a game and got stuck in map/game mode selection. Reason: either current plan file 
            has invalid map name, or user has not unlocked said map and/or game mode on their account. 
    """
    def __init__(self, msg, code) -> None:
        """Error under 'bot' package."""
        self.msg = msg
        self.code = code
        super().__init__(self.msg)

    def __str__(self):
        return f"(BotError {self.code}) {self.msg}."