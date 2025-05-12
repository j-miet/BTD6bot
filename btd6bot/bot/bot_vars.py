"""Contains BotVars class."""

class BotVars:
    """Variables which are used to control some of bot's behaviour.

    These values are only modified by gui functions. However, all variables have default initialization values, so Gui 
    is not required as long the bot has access to this class.

    Attributes:
        custom_resolution (list[str], class attribute): Custom resolution if this setting is enabled in gui.
        windowed (bool, class attribute): Whether windowed mode is enabled in gui.
        current_event_status (str, class attribute): Whether collection event checks are enabled or not. In api.menu, 
            bot needs to know current collection event status. To make passing of this value from gui to all the way 
            there, it's stored here and imported instead. Has values 'On' or 'Off', with default being 'Off'.
        time_recording_status (bool, class attribute): Whether the bot will record current map times for plotting 
            purposes, or not. Bot will always display time values during runtime, but with this setting as True, it 
            will also save their values in a txt file. Then, after a plan finishes, time data is stored and can be seen
            under 'Show plot' button in gui. Default value is True: bot will always update time values after succesful
            completion of a plan.
        checking_time_limit (int, class attribute): A time limit for monkey placing and upgrading until they give up 
            trying. Utilized under monkey placing and upgrading methods in bot.monkey module. Default value is 300.
        check_gamesettings (bool, class attribute): Whether bot checks the in-game esc settings and auto-updated them.
            Default is True: when bot is run first time, setting are always checked. Afterwards, they are only checked
            after bot detects defeat and makes sure defeat was not caused by wrong settings.
        print_delta_ocrtext (bool, class attribute): Print delta ocr texts e.g. monkey upgrade texts.
        print_substring_ocrtext (bool, class attribute): Print substring texts e.g. round numbers.
        paused (bool, class attribute): Is bot paused or not. Default is False, should only be modified internally by
            bot.
    """
    custom_resolution: list[int] = [0, 0]
    windowed: bool = False
    current_event_status: str = 'Off'
    time_recording_status: bool = True
    checking_time_limit: int = 300
    check_gamesettings: bool = True
    print_delta_ocrtext: bool = False
    print_substring_ocrtext: bool = False

    paused: bool = False