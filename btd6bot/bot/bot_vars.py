"""Contains BotVars class."""

class BotVars:
    """Variables which are used to control some of bot's behaviour, such as placing/upgrading time limits.

    These values are only modified by gui functions. However, all variables have default initialization values, so Gui 
    is not required as long the bot has access to this file.

    Attributes:
        current_event_status: Whether collection event checks are enabled or not. In api.menu, bot needs to know 
            current collection event status. To make passing of this value from gui to all the way there, it's stored 
            here and imported instead. Has values 'On' or 'Off', with default being 'Off'.
        time_recording_status: Whether the bot will record current map times for plotting purposes, or not. Bot will 
            always display time values during runtime, but with this setting as True, it will also save their values in 
            a txt file. Then, after a plan finishes, shared_api.save_bot_times will read this text, parse it, and save 
            all rounds and their time data in a json file, which gui_roundplot utilizes. Default value is False.
        checking_time_limit: A time limit for monkey placing and upgrading until they give up trying. Utilized under 
            monkey placing and upgrading methods in bot.monkeys module. Default value is 120.
    """
    current_event_status: str = 'Off'
    time_recording_status: bool = False

    checking_time_limit: int = 120

    #To be added:
    #screen_resolution = ...
    #logging = ...
    #display_ocr_text = ...