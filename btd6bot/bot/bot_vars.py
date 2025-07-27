"""Contains BotVars class."""

class BotVars:
    """Variables for controlling key aspects of bot's behaviour.

    All variables should have default initialization values in case that gui_vars.json file cannot be accessed/read.

    Attributes:
        custom_resolution (tuple[int, int], class attribute): Custom resolution if this setting is enabled in gui.
        windowed (bool, class attribute): Enable windowed mode and use custom_resolution value as screen resolution.
        ingame_res_enabled (bool, class attribute): Enable a separate in-game resolution via shifting coordinates.
        ingame_res_shift (tuple[int, int], class attribute): Width and height shift values for in-game resolution. Bot
            will shift all coordinates given amount of pixels, allowing user to possibly use other than 16:9 aspect 
            ratios. Shifting moves coordinates towards or away of the middle point: positive values shift inward, 
            negative values outward.
        checking_time_limit (int, class attribute): A time limit for monkey placing and upgrading until they give up 
            trying. Utilized under monkey placing and upgrading methods in bot.monkey module. Default value is 300.
        upg_verify_limit (int, class attribute): How many upgrades text checks are performed between upgrade key 
            presses. Prevents bot from getting stuck on upgrade loop (only halted by checking_time_limit) if ocr fails 
            to register text in a single attempt.
        use_gpu (bool, class attribute): Enable CUDA support for ocr is supported.
        logging (bool, class attribute): Enable logging of all cprint messages into Logs.txt file.
        print_delta_ocrtext (bool, class attribute): Print delta ocr texts e.g. monkey upgrade texts.
        print_substring_ocrtext (bool, class attribute): Print substring texts e.g. round numbers.

        current_event_status (str, class attribute): Whether collection event checks are enabled or not. In api.
            menu, bot needs to know current collection event status. To make passing of this value from gui to all the 
            way there, it's stored here and imported instead. Has values 'On' or 'Off', with default being 'Off'.

        time_recording_status (bool, class attribute): Whether the bot will record current map times for plotting 
            purposes, or not. Bot will always display time values during runtime, but with this setting as True, it 
            will also save their values in a txt file. Then, after a plan finishes, time data is stored and can be seen
            under 'Show plot' button in gui. Default value is True: bot will always update time values after succesful
            completion of a plan.
        check_gamesettings (bool, class attribute): Whether bot checks the in-game esc settings and auto-updated them.
            Default is True: when bot is run first time, setting are always checked. Afterwards, they are only checked
            after bot detects defeat and makes sure defeat was not caused by wrong settings.
        paused (bool, class attribute): Is bot paused or not. Default is False, should only be modified internally by
            bot.
        defeat_status (bool, class attribute): If bot detected an issue and cannot continue, it sets this value to True.
            Then every command will be skipped so that bot may exit to main menu as quickly as possible.
    """
    custom_resolution: tuple[int, int] = (1920, 1080)
    windowed: bool = False
    ingame_res_enabled: bool = False
    ingame_res_shift: tuple[int, int] = (0, 0)
    checking_time_limit: int = 300
    upg_verify_limit: int = 3
    use_gpu: bool = False
    logging: bool = False
    print_delta_ocrtext: bool = False
    print_substring_ocrtext: bool = False

    current_event_status: str = 'Off'

    # internal parameters; do not change their initial values manually
    time_recording_status: bool = True
    check_gamesettings: bool = True
    paused: bool = False
    defeat_status: bool = False