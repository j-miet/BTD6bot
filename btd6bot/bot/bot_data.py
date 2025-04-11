"""BotData class for passing information to gui."""

class BotData:
    """Stores various pieces of data into variables which can be utilized by gui.

    For example, monitoring window round timer requires this data.

    Data is only stored if bot_vars.BotVars class attribute get_botdata is set as True.

    Attributes:
        round_time (float, class attribute): Current round begin time.
        current_round (int, class attribute): Current round.
        begin_r (int, class attribute): Begin round of current plan.
        end_r (int, class attribute): End round of current plan.
    """
    round_time: float = 0
    current_round: int = 0
    begin_r: int = 0
    end_r: int = 0

    @staticmethod
    def set_data(round_time: float = 0,
                 current_round: int = 0,
                 begin_round: int = 0,
                 end_round: int = 0) -> None:
        """Set new values for BotData variables.  

        Default values are initial values: if you need to reset all settings, just call BotData.set_data().

        Args:
            round_time (float): Current round begin time.
            current_round (int): Current round.
            begin_round (int): Begin round of current plan.
            end_round (int): End round of current plan.
        """
        BotData.round_time = round_time
        BotData.current_round = current_round
        BotData.begin_r = begin_round
        BotData.end_r = end_round