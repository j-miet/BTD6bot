"""Contains Rounds class."""

import time

from bot import kb_mouse, times
from bot.bot_data import BotData
from bot.commands.flow import AutoStart, change_autostart, forward
from bot.bot_vars import BotVars
from bot.kb_mouse import ScreenRes
from bot.locations import get_click, get_text
import bot.menu_return
from bot.ocr.ocr import weak_substring_check, strong_substring_check, strong_delta_check, get_pixelcolor
from bot.ocr.ocr_reader import OCR_READER
from bot.times import PauseControl
from customprint import cprint
from utils import timing
from utils.exceptions import BotError

class Rounds:
    """Handles game start, round checks and returning to main menu.

    Begin and end round (constant) values are imported from current plan file, or else they would need to be passed to
    round_check repeatedly. Also, current round begin time is class variable, as it's needed to print round end times.

    Attributes:
        DEFEAT_CHECK_FREQUENCY (int, class attribute): Controls the frequency of defeat checks under Rounds.¨
            round_check, Monkey._check_upgrade, and Monkey._place. Increasing the value makes defeat screen detection 
            slower, but improves speed (and thus accuracy) of ocr in listed methods.
        LEVELUP_CHECK_FREQUENCY (int, class attribute): Frequency of clicking top right of the screen to push away any
            level up popups.

        begin (int, class attribute): Current plan first round. Should only change its value through a plan file when 
            initialize() is called.
        end (int, class attribute): Current plan last round. Should only change its value through a plan file when 
            initialize() is called.
        current_round_begin_time (float, class attribute): Stores starting time of current round. Should only change 
            its value after round_check verifies current round.
        exit_type (str, class attribute): Identifier for bot to select how to properly exit back to main menu. Default
            value is 'defeat', which means bot return to menu via defeat screen. Another possibility is 'manual' which
            means bot will open esc menu and exit manually.
        escsettings_checked (bool, class attribute): Whether automatic game settings check has been performed once.
    """    
    DEFEAT_CHECK_FREQUENCY = 12
    LEVEL_UP_CHECK_FREQUENCY = 30

    begin_round: int = 0
    end_round: int = 0
    current_round_begin_time: float = 0

    exit_type: str = 'defeat'
    escsettings_checked: bool = False

    @staticmethod
    def _check_gamesettings() -> None:
        if not Rounds.escsettings_checked:
            kb_mouse.press_esc()
            time.sleep(0.5)
            dragdrop = get_pixelcolor(*get_click('ingame', 'dragdrop'))
            nugde = get_pixelcolor(*get_click('ingame', 'nudge'))
            autostart = get_pixelcolor(*get_click('ingame', 'autostart'))
            if dragdrop[0] != 0:
                kb_mouse.click(get_click('ingame', 'dragdrop'))
                cprint("Enabled 'drag & drop'")
                time.sleep(0.5)
            if nugde[2] != 0:
                kb_mouse.click(get_click('ingame', 'nudge'))
                cprint("Disabled nugde mode'")
                time.sleep(0.5)
            if autostart[2] != 0:
                kb_mouse.click(get_click('ingame', 'autostart'))
                AutoStart.autostart_status = True
                cprint("Enabled 'auto start'")
                time.sleep(0.5)
            kb_mouse.press_esc()
            Rounds.escsettings_checked = True

    @staticmethod
    def _defeat_return(exit_str: str) -> None:
        BotData.set_data(current_round=Rounds.end_round+1)
        cprint('Defeat: returning to menu in...', end=' ')
        timing.counter(3)
        if exit_str == 'manual':
            kb_mouse.click(get_click('ingame', 'home_button2'))
        elif exit_str == 'defeat':
            kb_mouse.click(get_click('ingame','defeat_home_button'))
            time.sleep(0.5)
            kb_mouse.click(get_click('ingame','defeat_home_button_first_round'))
        bot.menu_return.returned(False)
        Rounds.escsettings_checked = False
        cprint('\nPlan failed.\n')

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
                    if weak_substring_check('bloons leaked', get_text('ingame', 'defeat'), OCR_READER):
                        cprint("\n**Defeat screen detected, game status set to defeat.**")
                        BotVars.defeat_status = True
                        return True
                    else:
                        return False
                return False
            else:
                cprint("\nChecking time limit reached! Game status set to defeat.")
                BotVars.defeat_status = True
                Rounds.exit_type = 'manual'
                return True
        else:
            cprint("Bad cycle and/or frequency values.")
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
        while not strong_delta_check('Next', get_text('ingame', 'next_text'), OCR_READER):
            if weak_substring_check('bloons leaked', get_text('ingame', 'defeat'), OCR_READER):
                BotData.set_data(current_round=Rounds.end_round+1)
                Rounds._defeat_return(Rounds.exit_type)
                return
            else:
                kb_mouse.click((0.999, 0.01))    # click away if round 100 insta pop-up.
                time.sleep(0.5)
        BotData.set_data(current_round=Rounds.end_round+1)
        final_round_end = times.current_time()
        times.time_print(final_round_start, final_round_end, f'Round {final_round}')
        time.sleep(0.5)
        times.time_print(total_start, final_round_end, 'Total')

        cprint('\nExiting map in...', end=' ')
        timing.counter(3)
        kb_mouse.click(get_click('ingame', 'next_button'))
        time.sleep(0.5)
        kb_mouse.click(get_click('ingame', 'home_button'))
        time.sleep(0.5)
        # for some reason, in apopalypse, the home button is placed slighty more to the right than usual.
        kb_mouse.click(get_click('ingame', 'home_button2'))
        bot.menu_return.returned()
        cprint('\nPlan completed.\n')

    @staticmethod
    def start() -> None:
        """Starts the game after seeing the 'Upgrades' message box top-right.

        Checks also current autostart status and will change it to True if not already, as True is the default value 
        (you start the bot with Autostart setting enabled in-game).
        """
        if ScreenRes.get_shift() != (0,0):
            BotVars.ingame_res_enabled = True
        start_time = times.current_time()
        loop: bool = True
        while loop:
            for letter in ('u','p','g','r','a','d','e'):
                kb_mouse.click(get_click('ingame', 'apopalypse_start')) # if mode is 'Apopalypse', click start
                if not weak_substring_check(letter, get_text('ingame','upgrade_text'), OCR_READER): 
                    if times.current_time() - start_time > 15:
                        for _ in range(3):
                            kb_mouse.press_esc()
                        raise BotError("Failed to enter game: wrong map name in plan file, or map/game mode not "
                                        "unlocked.", 1)
                else:
                    loop = False
                    break
                time.sleep(0.25)
        time.sleep(1)
        cprint('--> Running...')
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
        if prev_round == -1:
            cprint("\nHero/map selection failed.")
            kb_mouse.click((0.1911458333333, 0.0388888888889))
            time.sleep(1)
            kb_mouse.press_esc()
            return Rounds.end_round + 1
        current_round: int
        if BotVars.defeat_status:
            kb_mouse.press_esc()
            BotData.set_data(current_round=Rounds.end_round+1)
            wait_start = times.current_time()
            while not weak_substring_check('bloons leaked', get_text('ingame', 'defeat'), OCR_READER):
                if times.current_time()-wait_start > 3:
                    time.sleep(1)
                    Rounds._defeat_return('manual')
                    return Rounds.end_round + 1
                time.sleep(0.3)
            Rounds._defeat_return('defeat')
            return Rounds.end_round + 1
        
        current_round = prev_round + 1
        if current_round == Rounds.begin_round:
            Rounds.start()
        elif current_round == Rounds.end_round+1:
            Rounds.return_menu(Rounds.current_round_begin_time, map_start, Rounds.end_round)
            return current_round
        elif mode.lower() == 'apopalypse':
            return Rounds.end_round
        else:
            if not AutoStart.called_forward:
                forward()
            total_time = times.current_time()
            defeat_check = 1
            levelup_check = 1
            while True:
                round_value = strong_substring_check(str(current_round)+'/'+str(Rounds.end_round), 
                                                     get_text('ingame', 'current_round'), 
                                                     OCR_READER)
                if not round_value[0]:
                    PauseControl.pause_bot()
                    if levelup_check == Rounds.LEVEL_UP_CHECK_FREQUENCY:
                        kb_mouse.click((0.9994791666667, 0))
                        levelup_check = 0
                    levelup_check += 1
                    if defeat_check > Rounds.DEFEAT_CHECK_FREQUENCY:
                        defeat_check = 1
                    if Rounds.defeat_check(total_time, defeat_check, Rounds.DEFEAT_CHECK_FREQUENCY):
                        Rounds._defeat_return(Rounds.exit_type)
                        return Rounds.end_round+1
                    if '/' in round_value[1]:
                        try:
                            if int(round_value[1].split('/')[0]) > current_round:
                                break
                        except ValueError:
                            ...
                    defeat_check += 1
                else:
                    break
            times.time_print(Rounds.current_round_begin_time, times.current_time(), f'Round {current_round-1}')
            cprint('=== Current round:', current_round, '===')
        PauseControl.pause_bot()
        Rounds.current_round_begin_time = times.current_time()
        BotData.set_data(round_time=Rounds.current_round_begin_time,
                            current_round=Rounds.begin_round,
                            begin_round=Rounds.begin_round,
                            end_round=Rounds.end_round)
        return current_round