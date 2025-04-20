"""Contains Rounds class."""

import time

from bot import kb_mouse, times
from bot.bot_data import BotData
from bot.commands.flow import AutoStart, change_autostart, begin
from bot.bot_vars import BotVars
import bot.menu_return
from bot.ocr.ocr import weak_substring_check, strong_substring_check, strong_delta_check, get_pixelcolor
from bot.ocr.ocr_reader import OCR_READER
from utils import timing
from utils.exceptions import BotError

class Rounds:
    """Handles game start, round checks and returning to main menu.

    Begin and end round (constant) values are imported from current plan file, or else they would need to be passed to
    round_check repeatedly. Also, current round begin time is class variable, as it's needed to print round end times.

    Attributes:
        CURRENT_ROUND (tuple[float, float, float, float], class attribute): Text location of current in-game round, 
            located in the upper-right of screen.
        UPGRADE_TEXT (tuple[float, float, float, float], class attribute): Used in starting the first round.
        NEXT_TEXT (tuple[float, float, float, float], class attribute): Exiting map.
        LEVEL_UP (tuple[float, float, float, float], class attribute): Level up text location --CURRENTLY UNUSED--
        DEFEAT (tuple[float, float, float, float], class attribute): Defeat screen 'bloons leaked' text location.
        BUTTONS (dict[str, tuple[float, float]], class attribute): All required button locations to operate in-game 
            rounds and exiting game.
        DEFEAT_CHECK_FREQUENCY (int, class attribute): Controls the frequency of defeat checks under Rounds.¨
            round_check, Monkey._check_upgrade, and Monkey._place. Increasing the value makes defeat screen detection 
            slower, but improves speed (and thus accuracy) of ocr in listed methods.

        begin (int, class attribute): Current plan first round. Should only change its value through a plan file when 
            initialize() is called.
        end (int, class attribute): Current plan last round. Should only change its value through a plan file when 
            initialize() is called.
        current_round_begin_time (float, class attribute): Stores starting time of current round. Should only change 
            its value after round_check verifies current round.
        defeat_status (bool, class attribute): Whether bot has been unable to place/upgrade a tower for a set period of 
            time: this time is determined under BotVars.checking_time_limit.
        escsettings_checked (bool, class attribute): Whether automatic game settings check has been performed once.
    """

    CURRENT_ROUND: tuple[float, float, float, float] = (0.7181666666667, 0.027001, 0.8119791666667, 0.0685185185185)
    UPGRADE_TEXT: tuple[float, float, float, float] = (0.875, 0.0175925925926, 0.9682291666667, 0.0638888888889) 
    NEXT_TEXT: tuple[float, float, float, float] = (0.4364583333333, 0.8046296296296, 0.5526041666667, 0.8740740740741)
    LEVEL_UP: tuple[float, float, float, float] = (0.4270833333333, 0.4907407407407, 0.5708333333333, 0.5648148148148)
    DEFEAT: tuple[float, float, float, float] = (0.446875, 0.5361111111111, 0.5635416666667, 0.5712962962963)
    BUTTONS: dict[str, tuple[float, float]] = {
        'next_button': (0.5, 0.85),
        'home_button': (0.37, 0.78),
        'home_button2': (0.44, 0.78),
        'defeat_home_button': (0.33, 0.75),
        'defeat_home_button_first_round': (0.38, 0.75)
        }
    
    DEFEAT_CHECK_FREQUENCY = 9

    begin_round: int = 0
    end_round: int = 0
    current_round_begin_time: float = 0

    defeat_status: bool = False
    escsettings_checked: bool = False

    @staticmethod
    def _check_gamesettings() -> None:
        if not Rounds.escsettings_checked:
            kb_mouse.press_esc()
            time.sleep(0.5)
            dragdrop = get_pixelcolor(0.4427083333333, 0.2777777777778)
            nugde = get_pixelcolor(0.4458333333333, 0.412962962963)
            autostart = get_pixelcolor(0.6697916666667, 0.2796296296296)
            if dragdrop[0] != 0:
                kb_mouse.click((0.4427083333333, 0.2777777777778))
                print("Enabled 'drag & drop'")
                time.sleep(0.5)
            if nugde[2] != 0:
                kb_mouse.click((0.4458333333333, 0.412962962963))
                print("Disabled nugde mode'")
                time.sleep(0.5)
            if autostart[2] != 0:
                kb_mouse.click((0.6697916666667, 0.2796296296296))
                print("Enabled 'auto start'")
                time.sleep(0.5)
            kb_mouse.press_esc()
            Rounds.escsettings_checked = True

    @staticmethod
    def defeat_check(current_time: float, cycle: int, frequency: int) -> bool:
        """Checks and updates current defeat status.
        
        Checks if current time hasn't exceeded BotVars.checking_time_limit, then checks if current cycle matches the 
        given frequency. If both true, searches once for defeat screen and either finds it, sets defeat_status to True
        and returns True, or return False if no defeat detected. If checking time limit is exceeded instead, does the 
        same as with finding defeat screen.

        How to use: insert this inside a loop where you wish to check defeat conditions every Nth cycle by passing
        frequency = N. Then implement a counter which starts from 1, gets incremented after each loop, and caps out at 
        frequency value, then resets back to 1; check Rounds.round_check for an example.

        If cycle = frequency, defeat check is performed every loop which means no incrementing is needed.

        Args:
            current_time: A time.time() float value.
            cycle: Current loop iteration cycle, must be less or equal to frequency value.
            frequency: Amount of cycles it takes between defeat checks.
        """
        if isinstance(cycle, int) and cycle >= 1 and isinstance(frequency, int) and frequency >= cycle:
            if times.current_time() - current_time < BotVars.checking_time_limit:
                if cycle == frequency:   # frequency of defeat checks: 2 = every second loop, N = every Nth loop.
                    if weak_substring_check('bloons leaked', Rounds.DEFEAT, OCR_READER):
                        print("\n**Defeat screen detected, game status set to defeat.**")
                        Rounds.defeat_status = True
                        return True
                    else:
                        return False
                return False
            else:
                print("Checking time limit reached! Game status set to defeat.")
                Rounds.defeat_status = True
                return True
        else:
            print("Bad cycle and/or frequency values.")
            return False

    @staticmethod
    def return_menu(final_round_start: float, total_start: float, final_round: int) -> None:
        """Return to main menu after game completion.
        
        After game ends, a victory screen pops up. Then ocr is performed to find 'Next' text and click it + click the
        home button opening after it.

        Takes arguments of start and end time of final round, map start time and final round number to print
        final round and map durations. Then clicks 'Next' and 'Home' button to return to main menu.

        Args:
            final_round_start: Start time of final round.
            total_start: Start time from round 1 placements.
            final_round: Final round number.
        """
        while not strong_delta_check('Next', Rounds.NEXT_TEXT, OCR_READER):
            kb_mouse.click((0.999, 0.01))    # click away if round 100 insta pop-up.
            time.sleep(1)
        BotData.set_data(current_round=Rounds.end_round+1)
        final_round_end = times.current_time()
        times.time_print(final_round_start, final_round_end, f'Round {final_round}')
        time.sleep(0.5)
        times.time_print(total_start, final_round_end, 'Total')

        print('Exiting map in...', end=' ')
        timing.counter(3)
        kb_mouse.click(Rounds.BUTTONS['next_button'])
        time.sleep(0.5)
        kb_mouse.click(Rounds.BUTTONS['home_button'])
        time.sleep(0.5)
        # for some reason, in apopalypse, the home button is placed slighty more to the right than usual.
        kb_mouse.click(Rounds.BUTTONS['home_button2'])
        bot.menu_return.returned()

    @staticmethod
    def start() -> None:
        """Starts the game after seeing the 'Upgrades' message box top-right.

        Checks also current autostart status and will change it to True if not already, as True is the default value 
        (you start the bot with Autostart setting enabled in-game).
        """
        start_time = times.current_time()
        while not weak_substring_check('Upgrades', Rounds.UPGRADE_TEXT, OCR_READER): 
            if times.current_time() - start_time > 15:
                for _ in range(3):
                    kb_mouse.press_esc()
                raise BotError("Failed to enter game: wrong map name in plan file, or map/game mode not unlocked.", 1)
            kb_mouse.click((0.5, 0.69)) #if game mode is 'Apopalypse', click the button.
            time.sleep(1)
        time.sleep(0.5)
        print('--> Running...')
        kb_mouse.click((0.999, 0.01))  # closes any difficulty info pop-up window after entering a game.
        time.sleep(1)
        if BotVars.check_gamesettings:
            Rounds._check_gamesettings()
        if not AutoStart.autostart_status:
            change_autostart()

    @staticmethod
    def round_check(prev_round: int, map_start: float, mode: str = '') -> int:
        """Handles round text checking, round time printing, updating current round and the end round check.
        
        Takes in the previous round value (which initially starts from begin-1) so that round updating can be done
        inside this function. Otherwise, current round updating would be performed at the end of each plan file.

        Has also checks for defeat screen detection.

        Args:
            prev_round: Previous round number.
            map_start: Starting time of entire plan.
            mode: Only used in forcing end round if game mode if 'Apopalypse'.
            
        Returns:
            Current round number.
        """
        current_round: int
        if Rounds.defeat_status:
            BotData.set_data(current_round=Rounds.end_round+1)
            wait_start = times.current_time()
            while not weak_substring_check('bloons leaked', Rounds.DEFEAT, OCR_READER):
                if times.current_time()-wait_start > 5:
                    print("Defeat: no defeat screen found, returning via espace menu.")
                    kb_mouse.press_esc()
                    time.sleep(1)
                    kb_mouse.click(Rounds.BUTTONS['home_button2'])
                    time.sleep(0.25)
                    kb_mouse.click(Rounds.BUTTONS['defeat_home_button'])
                    time.sleep(0.25)
                    kb_mouse.click(Rounds.BUTTONS['defeat_home_button_first_round'])
                    bot.menu_return.returned()
                    print('Plan completed.\n')
                    return Rounds.end_round + 1
                time.sleep(0.3)
            print('Defeat: returning to menu in...', end=' ')
            Rounds.defeat_status = False
            timing.counter(3)
            kb_mouse.click(Rounds.BUTTONS['defeat_home_button'])
            time.sleep(0.5)
            kb_mouse.click(Rounds.BUTTONS['defeat_home_button_first_round'])
            print('\nPlan completed.\n')
            return Rounds.end_round + 1
        
        current_round = prev_round + 1
        if current_round == Rounds.begin_round:
            Rounds.start()
        elif current_round == Rounds.end_round+1:
            Rounds.return_menu(Rounds.current_round_begin_time, map_start, Rounds.end_round)
            print('\nPlan completed.\n')
            return current_round
        elif mode.lower() == 'apopalypse':
            return Rounds.end_round
        else:
            if not AutoStart.called_begin:
                begin()
            total_time = times.current_time()
            defeat_check = 1
            while not strong_substring_check(str(current_round)+'/'+str(Rounds.end_round), Rounds.CURRENT_ROUND, 
                                             OCR_READER):
                times.pause_bot()
                if defeat_check > Rounds.DEFEAT_CHECK_FREQUENCY:
                    defeat_check = 1
                if Rounds.defeat_check(total_time, defeat_check, Rounds.DEFEAT_CHECK_FREQUENCY):
                    timing.counter(3)
                    kb_mouse.click(Rounds.BUTTONS['defeat_home_button'])
                    time.sleep(0.5)
                    kb_mouse.click(Rounds.BUTTONS['defeat_home_button_first_round'])
                    print("\nPlan completed.\n")
                    return Rounds.end_round+1
                defeat_check += 1
            times.time_print(Rounds.current_round_begin_time, times.current_time(), f'Round {current_round-1}')
            print('===Current round:', current_round, '===')
        times.pause_bot()
        Rounds.current_round_begin_time = times.current_time()
        BotData.set_data(round_time=Rounds.current_round_begin_time,
                            current_round=Rounds.begin_round,
                            begin_round=Rounds.begin_round,
                            end_round=Rounds.end_round)
        return current_round