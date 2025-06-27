"""Implements Monkey class.

Monkey class creates a prototype of a monkey and is responsible for 
-placing (happens automatically after creating a monkey object) and upgrading them
-changing their targeting priority
-using possible special abilities
-selling them

It also implements 
-checking of succesful placements and upgrades, which allows queueing up these commands beforehand, for
 example if player can't currently afford a monkey, bot keeps repeating the command until it succeeds.
-checks for correct inputs in coordinate and targeting values. With upgrades, it only checks for non-empty
 inputs.

Special abilities and selling don't have any ocr-level checks like targetting and upgrading do.

Examples of this module can be found in 'plans' folder and picking any .py plan file OR checking the documentation of 
used method.

All constants required in Monkey are wrapped under _MonkeyConstants class, which Monkey then inherits.
"""

from __future__ import annotations
import re
import time

from pynput.keyboard import Key, KeyCode

from bot import kb_mouse, times
from bot.bot_vars import BotVars
from bot.hotkeys import hotkeys
import bot.ocr.ocr as ocr
from bot.ocr.ocr import OcrValues
from bot.ocr.ocr_reader import OCR_READER
from bot.rounds import Rounds
from customprint import cprint

class _MonkeyConstants:
    """Wrapper for constants of Monkey class.

    Type T[F] in attributes refers to tuple[float, float, float, float].

    Attributes:
        MONKEY_NAMES (tuple[str], class attribute): All monkey names.  

        TOP_UPG_CURRENT_LEFTWINDOW (T[F], class attribute): Location of current top path 
            upgrade if upgrade window opens on the left.
        TOP_UPG_CURRENT_RIGHTWINDOW (T[F]], class attribute): Current top path upgrade if 
            upgrade window opens on the right.

        MID_UPG_CURRENT_LEFTWINDOW (T[F], class attribute): Current middle path upgrade if 
            upgrade window opens on the left.
        MID_UPG_CURRENT_RIGHTWINDOW (T[F], class attribute): Current middle path upgrade 
            if upgrade  window opens on the right.

        BOT_UPG_CURRENT_LEFTWINDOW (T[F], class attribute): Current bottom path upgrade if 
            upgrade window opens on the left.
        BOT_UPG_CURRENT_RIGHTWINDOW (T[F], class attribute): Current path bottom upgrade 
            if upgrade  window opens on the right.

        RIGHT_PANEL_SELL_LOCATION (T[F], class attribute): Sell button location if upgrade 
            panel opens on the right.
        LEFT_PANEL_SELL_LOCATION (T[F], class attribute): Sell button location if upgrade 
            panel opens on the left.
    """
    _MONKEY_NAMES = (
        'dart', 'boomer', 'bomb', 'tack', 'ice', 'glue', 'desperado',
        'sniper', 'sub', 'boat', 'ace', 'heli', 'mortar', 'dartling',
        'wizard', 'super', 'ninja', 'alch', 'druid', 'mermonkey',
        'farm', 'spike', 'village', 'engineer', 'beast',
        'hero'
    )
    _MONKEY_SPECIAL_NAMES = (
        'ace_wing'
    )
    
    _TOP_UPG_CURRENT_LEFTWINDOW = (0.0333333333333, 0.3696296296296, 0.121875, 0.462037037037)
    _TOP_UPG_CURRENT_RIGHTWINDOW = (0.6777083333333, 0.3696296296296, 0.7661458333333, 0.462037037037)

    _MID_UPG_CURRENT_LEFTWINDOW = (0.0333333333333, 0.5122222222222, 0.121875, 0.5861111111111)
    _MID_UPG_CURRENT_RIGHTWINDOW = (0.6777083333333, 0.5122222222222, 0.7661458333333, 0.5861111111111)

    _BOT_UPG_CURRENT_LEFTWINDOW = (0.0333333333333, 0.6492592592593, 0.121875, 0.7231481481481)
    _BOT_UPG_CURRENT_RIGHTWINDOW = (0.6777083333333, 0.6492592592593, 0.7661458333333, 0.7231481481481)

    _RIGHT_PANEL_SELL_LOCATION = (0.7808333333333, 0.8148148148148, 0.8380208333333, 0.8703703703704)
    _LEFT_PANEL_SELL_LOCATION = (0.141083333333, 0.808148148148, 0.1984375, 0.8638888888889)


class Monkey(_MonkeyConstants):
    """Monkey class: creates all placeable monkeys and implements their common behaviour.

    Inherits _MonkeyConstants class which has monkey names and all required ocr locations.

    Attributes:
        name (str): Name of a Monkey. All available monkeys names:
            'dart', 'boomer', 'bomb', 'tack', 'ice', 'glue', 'desperado',
            'sniper', 'sub', 'boat', 'ace', 'heli', 'mortar', 'dartling',
            'wizard', 'super', 'ninja', 'alch', 'druid', 'mermonkey',
            'farm', 'spike', 'village', 'engineer', 'beast'.

            A special name 'ace_wing' is used for aces if 'wingmonkey' monkey knowledge is enabled!  
        pos_x (float | None): X-coordinate location. Value must be on interval [0, 1), or to be more precise, 
            [0.0141, 0.8567] because left frame and monkey panel on the right. But bot takes care of invalid values, so 
            this won't be repeated under other comments (except right below, because y has different values). Also, 
            monkey size matters so you can't place a super monkey right at x=0.0141, but dart works. 
        pos_y (float | None): Y-coordinate location. Value must be on interval [0, 1), or actually [0.02593, 0.9731].
            Just like with pos_x, bot will check correct values, but it won't check monkey size: while a sniper is slim 
            enough, trying to place a heli at y=0.02593 doesn't work.
        placement_check: If bot will verify the monkey was placed. Should always use the default value True unless you 
                know what you're doing. Use case: if placed monkey is under life/money/round hud, it can be placed 
                there but afterwards clicking on this location does nothing because of hud. To access monkey again, you 
                need to update its position slighly away from center and it should work again. To update monkey 
                location, use cpos_x, cpos_y arguments for next command. A concrete example of above would be bloody 
                puddles chimps plan, where sniper is placed on top of current cash display.
        panel_pos (str): Side where upgrade panel opens. This is always relative to middle x-coordinate of non-panel 
            screen i.e. somewhere around 0.42-0.44. Panel opens to the opposite side of this relative position e.g. 
            monkey to the left has panel on right. Values are 'left', 'right' and 'middle'. Last value is only needed 
            as a placeholder because different resolutions could change the panel opening side: actual side should be 
            checked via ocr and set as final value.
        targeting (str): Targeting priority, initial value is set via basic_monkey_targeting method automatically. 
            Change this value via 'target' method afterwards.
        upgrade_path (str): Current upgrade path of Monkey, initially '0-0-0'. Change value via 'upgrade' method 
            afterwards.

    Methods:
    --
        target: Change targeting priority of this monkey.  
        upgrade: Upgrade this monkey.  
        special: Use special of this monkey.  
        sell: Sell this monkey.  
        robo_target: Control targeting of robo monkey's second arm.
        merge: Merge beast handlers with another.
        center: Change monkey ace centered path location.

    See also:
    --
        ability.ability to use abilities (in plan files, just type ability() to see docs for more info).  
        btd6bot (project root) -> tools -> show_coordinates or coordinate_tracker, to find coordinates.

    Examples:
        Even if you never refer to a monkey after its placement, it's prefered to save it in a variable for clarity.

        >>> 
            Monkey('dart', 0.15, 0.2)
    
        If multiple monkeys of same type, use descriptive names for variables so it's easy to refer to correct monkey 
        later.

        >>> sniper = Monkey('sniper', 0.1, 0.35)
        Placing Sniper... Sniper placed.
        >>> sniper2 = Monkey('sniper', 0.1, 0.25)
        Placing Sniper... Sniper placed.
        >>> super_top = Monkey('super', 0.2, 0.35)
        Placing Super... Super placed.
        >>> super_bottom = Monkey('super', 0.2, 0.25)
        Placing Super... Super placed.
        >>> sniper.target('last')
        Sniper targeting set to 'last'.
        >>> super_bottom.upgrade(['1-0-0', '2-0-0'])
        Upgrading 0-0-0 Super to 1-0-0... Upgraded.
        Upgrading 1-0-0 Super to 2-0-0... Upgraded.
        >>> sniper2.sell()
        Sniper sold!
        >>> super_top.target('strong')
        Super targeting set to 'strong'.
        >>> heli = Monkey('heli', 0.3, 0.1)
        Placing Heli... Heli placed.
        >>> heli.target('lock') # usually, you'd give x=, y= to set where heli hovers, but it's not necessary
        Heli targeting set to 'lock'.
        >>> heli.special(1, x=0.15, y=0.2)
        Heli special 1 used.
        >>> super_bottom.upgrade(['3-0-0', '3-1-0', '3-2-0', '4-2-0', '5-2-0'])
        Upgrading 2-0-0 Super to 3-0-0... Upgraded.
        Upgrading 3-0-0 Super to 3-1-0... Upgraded.
        Upgrading 3-1-0 Super to 3-2-0... Upgraded.
        Upgrading 3-2-0 Super to 4-2-0... Upgraded.
        Upgrading 4-2-0 Super to 5-2-0... Upgraded.
    """
    _wingmonkey = 0
    _elite_sniper = 0

    def __init__(self, name: str, pos_x: float, pos_y: float, placement_check: bool = True) -> None:
        """Initializes a Monkey by passing it name and position coordinates.
        
        Args:
            name: Name string. See 'Monkey' class documentation for all valid names.
            pos_x: X-coordinate, must be on interval [0, 1).
            pos_y: Y-coordinate, must be on interval [0, 1).
            placement_check: Whether bot will verify the monkey was placed or not. Default is True.
        """
        self._name = name
        self._pos_x = pos_x
        self._pos_y = pos_y
        self._placement_check = placement_check
        self._panel_pos = self._init_panel_position()
        self._targeting = self._basic_monkey_targeting()
        self._upgrade_path = '0-0-0'
        self._check_init_values()
        self._place()

    def _error(self, type: str,
                error_object: str | list[str] | list[str | float], 
                other: str | list[str] | tuple[str,  str] = ''
                ) -> None:
        """Outputs an error message if monkey name/x-position/y-position/target/upgrade is invalid.

        Errors will stop the bot by first printing the message and setting bot to 'defeat' state, preventing further 
        commands in current plan.

        Args:
            type: Error type.
            error_object: String text or list of strings if object is empty upgrade list or init value checklist.
            other: Additional text string, string list or string tuple, not required. Default value is ''.
        """
        obj = error_object 
        if type == 'init':
            if obj[0] == '-1':
                cprint(f'\nNAME ERROR "{obj[0]}": monkey name not found.')
            if obj[1] == '-1':
                cprint(f'\nPOS_X ERROR {obj[1]}: x-coordinate must be within interval [0,1).')
            if obj[2] == '-1':
                cprint(f'\nPOS_Y ERROR {obj[2]}: y-coordinate must be within interval [0,1).')
        elif type == 'target':
            cprint(f'\nTARGET ERROR "{obj}": {obj} is not a valid targeting for {other}.')
        elif type == 'upgrade_list':
            cprint('\nUPGRADE LIST ERROR: upgrade list is empty.')
        elif type == 'upgrade':
            cprint(f'\nUPGRADE PATH ERROR: upgrade path {obj} in current upgrade list {other} is invalid.')
        time.sleep(1)
        BotVars.defeat_status = True
        cprint('\n**An Error has occured. Current game state treated as Defeat**')

    def _init_panel_position(self) -> str:
        """Get upgrade panel position of current monkey.
        
        Values 'left' and 'right' are always opposite of relative position of monkey from middle. The 'middle' value is 
        only required because different resolution could shift the small interval of middle values. Then for some 
        resolutions it could be left, for other right. However, 'middle' is a placeholder value anyway, as _place will 
        ovewrite it and set it as one of the directional values.

        Returns:
            "left" if monkey is on right, "right" if on left, "middle" if close to midpoint.
        """
        if self._pos_x > 0.439:
            return "left"
        elif self._pos_x < 0.428:
            return "right"
        else:
            return "middle"
        
    def _update_panel_position(self, new_x: float) -> bool:
        if new_x > 0.439:
            self._panel_pos = 'left'
            return True
        elif new_x < 0.428:
            self._panel_pos = 'right'
            return True
        else:
            if ocr.strong_delta_check('Sell', Monkey._RIGHT_PANEL_SELL_LOCATION, OCR_READER):
                self._panel_pos = 'right'
                return True
            elif ocr.strong_delta_check('Sell', Monkey._LEFT_PANEL_SELL_LOCATION, OCR_READER):
                self._panel_pos = 'left'
                return True
        return False

    def _check_init_values(self) -> None:
        """Checks the validity of name, pos_x and pos_y values during initialization.
        
        If at least one value is invalid, calls for _error method.
        """
        init_check: list[str | float] = ['-1', -1, -1]
        if self._name in Monkey._MONKEY_NAMES or self._name in Monkey._MONKEY_SPECIAL_NAMES:
            init_check[0] = self._name
        if 0.0141 <= self._pos_x <= 0.8567:
            init_check[1] = self._pos_x
        if 0.02593 <= self._pos_y <= 0.9731:
            init_check[2] = self._pos_y
        if '-1' in init_check:
            self._error('init', init_check)
            
    def _get_hotkey(self) -> Key | KeyCode | str:
        """Returns keyboard hotkey of current monkey.

        Returns:
            Corresponding pynput.keyboard Key, KeyCode, or a string value. If no key-like value can be returned, 
                returns False.
        """
        match self._name.lower():
            # Hero
            case 'hero':
                return hotkeys['hero']
            # Primary
            case 'dart':
                return hotkeys['dart monkey']
            case 'boomer':
                return hotkeys['boomerang']
            case 'bomb':
                return hotkeys['bomb shooter']
            case 'tack':
                return hotkeys['tack shooter']
            case 'ice':
                return hotkeys['ice monkey']
            case 'glue':
                return hotkeys['glue gunner']
            case 'desperado':
                return hotkeys['desperado']
            # Military
            case 'sniper':
                return hotkeys['sniper monkey']
            case 'sub':
                return hotkeys['monkey sub']
            case 'boat':
                return hotkeys['monkey buccaneer']
            case 'ace' | 'ace_wing':
                return hotkeys['monkey ace']
            case 'heli':
                return hotkeys['heli pilot']
            case 'mortar':
                return hotkeys['mortar monkey']
            case 'dartling':
                return hotkeys['dartling gunner']
            # Magic
            case 'wizard':
                return hotkeys['wizard monkey']
            case 'super':
                return hotkeys['super monkey']
            case 'ninja':
                return hotkeys['ninja monkey']
            case 'alch': 
                return hotkeys['alchemist']
            case 'druid': 
                return hotkeys['druid']
            case 'mermonkey':
                return hotkeys['mermonkey']
            # Support
            case 'farm':
                return hotkeys['banana farm']
            case 'spike':
                return hotkeys['spike factory']
            case 'village': 
                return hotkeys['monkey village']
            case 'engineer':
                return hotkeys['engineer monkey']
            case 'beast': 
                return hotkeys['beast handler']
        cprint("HOTKEY NOT FOUND")
        return "Error"
    
    def _basic_monkey_targeting(self) -> str | None:
        """Defines default targeting behaviour of monkey.

        Returns:
            Targeting option string or None if monkey has no targeting options.
        """
        match self._name:
            case 'heli':
                return 'follow'
            case 'ace' | 'ace_wing':
                return 'circle'
            case 'mortar':
                return None
            case 'dartling':
                return 'normal'
            case 'spike':
                return 'normal'
            case 'farm':
                return None
            case _:
                return 'first'
        return None
    
    def _normal_targeting(self, current: str | None, target: str) -> str | tuple[str, str]:
        """Set targeting for monkey under normal targeting rules.
        
        Most monkeys have the basic 4 targeting choises: first, last, close, and strong. 
        This method handles targeting change for such cases.
        
        Args:
            current: Current targeting priority as a string.
            target: New targeting priority.     
            
        Returns:
            'OK' string if targeting change was succesful.
            name, target: If problems were encountered, return monkey's name and target string.
        """
        if target == 'first':
            if current == 'last':
                kb_mouse.kb_input(hotkeys['target reverse'], 1)
            elif current == 'strong':
                kb_mouse.kb_input(hotkeys['target change'], 1)
            elif current == 'close':
                kb_mouse.kb_input(hotkeys['target change'], 2)
        elif target == 'last':
            if current == 'first':
                kb_mouse.kb_input(hotkeys['target change'], 1)
            elif current == 'strong':
                kb_mouse.kb_input(hotkeys['target change'], 2)
            elif current == 'close':
                kb_mouse.kb_input(hotkeys['target reverse'], 1)
        elif target == 'close':
            if current == 'first':
                kb_mouse.kb_input(hotkeys['target reverse'], 2)
            elif current == 'strong':
                kb_mouse.kb_input(hotkeys['target reverse'], 1)
            elif current == 'last':
                kb_mouse.kb_input(hotkeys['target change'], 1)
        elif target == 'strong':
            if current == 'first':
                kb_mouse.kb_input(hotkeys['target reverse'], 1)
            elif current == 'last':
                kb_mouse.kb_input(hotkeys['target change'], 2)
            elif current == 'close':
                kb_mouse.kb_input(hotkeys['target change'], 1)
        else:
            return self._name, target
        cprint(f"{self._name.capitalize()} targeting set to '{target}'.")
        return 'OK'
    
    def _change_target_special(self, s: str | int, x: float | None = None, y: float | None = None) -> None:
        """Similar to actual special method, but is only called in _change_target.

        Args:
            s: Special ability, either 1 (most common) or 2. Can also pass strings '1' or '2'.
            x: If targetable ability, its x-coordinate. Default value is None.
            y: If targetable ability, its y-coordinate. Default value is None.
        """
        if s not in [1, 2, '1', '2']:
            cprint("Wrong input value on special ability; use 1/'1' or 2/'2'")
            return
        kb_mouse.kb_input(hotkeys['special '+str(s)])
        if x is not None and y is not None:
            kb_mouse.click((x, y))

    def _change_target(self, target: str,
                      x: float | None = None,
                      y: float | None = None,
                      cpos_x: float | None = None,
                      cpos_y: float | None = None
                      ) -> str | tuple[str, str]:
        """Changes monkey's (not hero's) targeting.
        Standard (first, last, close, strong) and non-standard cases have been accounted for, even those unlocking
        after specific upgrades.

        If monkey position has changed after initial placement (Geared/Sanctuary), use cpos to update current position.

        Args:
            target: New targeting priority.
            x: If targeting priority needs coordinates (e.g. dartling/heli), its x-coordinate. Default value is None.
            y: If targeting priority needs coordinates (e.g. dartling/heli), its y-coordinate. Default value is None.
            cpos_x: If monkey's current x-coordinate position has changed, update it. Default value is None.
            cpos_y: If monkey's current y-coordinate position has changed, update it. Default value is None.

        Returns:
            normal_targeting(current, target) value if targeting falls under that category,
            'OK' string if any other targeting change was succesful.
            name, target: If problems were encountered, return monkey's name and target string as a tuple. 
        """ 
        current = self._targeting
        if current == target:
            cprint(f'Already set to {target.capitalize()}.')
            kb_mouse.press_esc()
            return 'OK'
        if cpos_x is not None:
            self._pos_x = cpos_x
        if cpos_y is not None:
            self._pos_y = cpos_y
        kb_mouse.click((self._pos_x, self._pos_y))
        if cpos_x is not None:
            self._update_panel_position(cpos_x)
        match self._name:
            case 'farm':
                return self._name, target
            case 'sniper':
                if Monkey._elite_sniper == 1:
                    if target == 'first':
                        if current == 'last':
                            kb_mouse.kb_input(hotkeys['target reverse'], 1)
                        elif current == 'strong':
                            kb_mouse.kb_input(hotkeys['target change'], 2)
                        elif current == 'close':
                            kb_mouse.kb_input(hotkeys['target reverse'], 2)
                        elif current == 'elite':
                            kb_mouse.kb_input(hotkeys['target change'], 1)
                    elif target == 'last':
                        if current == 'first':
                            kb_mouse.kb_input(hotkeys['target change'], 1)
                        elif current == 'strong':
                            kb_mouse.kb_input(hotkeys['target reverse'], 2)
                        elif current == 'close':
                            kb_mouse.kb_input(hotkeys['target reverse'], 1)
                        elif current == 'elite':
                            kb_mouse.kb_input(hotkeys['target change'], 2)
                    elif target == 'close':
                        if current == 'first':
                            kb_mouse.kb_input(hotkeys['target change'], 2)
                        elif current == 'strong':
                            kb_mouse.kb_input(hotkeys['target reverse'], 1)
                        elif current == 'last':
                            kb_mouse.kb_input(hotkeys['target change'], 1)
                        elif current == 'elite':
                            kb_mouse.kb_input(hotkeys['target reverse'], 2)
                    elif target == 'strong':
                        if current == 'first':
                            kb_mouse.kb_input(hotkeys['target reverse'], 2)
                        elif current == 'last':
                            kb_mouse.kb_input(hotkeys['target change'], 2)
                        elif current == 'close':
                            kb_mouse.kb_input(hotkeys['target change'], 1)
                        elif current == 'elite':
                            kb_mouse.kb_input(hotkeys['target reverse'], 1)
                    elif target == 'elite':
                        if current == 'first':
                            kb_mouse.kb_input(hotkeys['target reverse'], 1)
                        elif current == 'strong':
                            kb_mouse.kb_input(hotkeys['target change'], 1)
                        elif current == 'last':
                            kb_mouse.kb_input(hotkeys['target reverse'], 2)
                        elif current == 'close':
                            kb_mouse.kb_input(hotkeys['target change'], 2)
                    else:
                        return self._name, target
                else:
                    return self._normal_targeting(current, target)
            case 'heli':    # follow is used as base value. You can't switch to 'follow' or 'patrol points'.
                if target == 'lock':
                    if current == 'follow':
                        kb_mouse.kb_input(hotkeys['target change'], 1)
                        if x is not None and y is not None: # allows for locking in place without new coordinates.
                            self._change_target_special(1, x, y)
                    elif current == 'pursuit':
                        kb_mouse.kb_input(hotkeys['target change'], 2)
                        if x is not None and y is not None:
                            self._change_target_special(1, x, y)
                elif target == 'pursuit':
                    if current == 'follow':
                        kb_mouse.kb_input(hotkeys['target reverse'], 1)
                    elif current == 'lock':
                        kb_mouse.kb_input(hotkeys['target reverse'], 2)
                else:
                    return self._name, target
            case 'ace':
                if int(self._upgrade_path[4]) >= 2:
                    if Monkey._wingmonkey:
                        if target == 'circle':
                            if current == 'infinite':
                                kb_mouse.kb_input(hotkeys['target change'], 1)
                            elif current == 'eight':
                                kb_mouse.kb_input(hotkeys['target reverse'], 2)
                            elif current == 'wingmonkey':
                                kb_mouse.kb_input(hotkeys['target change'], 1)
                            elif current == 'centered':
                                kb_mouse.kb_input(hotkeys['target reverse'], 3)
                        elif target == 'infinite':
                            if current == 'circle':
                                kb_mouse.kb_input(hotkeys['target change'], 1)
                            elif current == 'eight':
                                kb_mouse.kb_input(hotkeys['target reverse'], 1)
                            elif current == 'wingmonkey':
                                kb_mouse.kb_input(hotkeys['target change'], 2)
                            elif current == 'centered':
                                kb_mouse.kb_input(hotkeys['target reverse'], 2)   
                        elif target == 'eight':
                            if current == 'circle':
                                kb_mouse.kb_input(hotkeys['target change'], 2)
                            elif current == 'infinite':
                                kb_mouse.kb_input(hotkeys['target change'], 1)
                            elif current == 'wingmonkey':
                                kb_mouse.kb_input(hotkeys['target change'], 3)
                            elif current == 'centered':
                                kb_mouse.kb_input(hotkeys['target reverse'], 1)
                        elif target == 'wingmonkey':
                            if current == 'circle':
                                kb_mouse.kb_input(hotkeys['target reverse'], 1)
                            elif current == 'infinite':
                                kb_mouse.kb_input(hotkeys['target reverse'], 2)
                            elif current == 'eight':
                                kb_mouse.kb_input(hotkeys['target reverse'], 3)
                            elif current == 'centered':
                                kb_mouse.kb_input(hotkeys['target change'], 1)
                        elif target == 'centered':
                            if current == 'circle':
                                kb_mouse.kb_input(hotkeys['target change'], 3)
                            elif current == 'eight':
                                kb_mouse.kb_input(hotkeys['target change'], 1)
                            elif current == 'infinite':
                                kb_mouse.kb_input(hotkeys['target change'], 1)
                            elif current == 'wingmonkey':
                                kb_mouse.kb_input(hotkeys['target reverse'], 1)
                        else:
                            return self._name, target
                    else:
                        if target == 'circle':
                            if current == 'infinite':
                                kb_mouse.kb_input(hotkeys['target reverse'], 1)
                            elif current == 'eight':
                                kb_mouse.kb_input(hotkeys['target reverse'], 2)
                            elif current == 'centered':
                                kb_mouse.kb_input(hotkeys['target change'], 1)
                        elif target == 'infinite':
                            if current == 'circle':
                                kb_mouse.kb_input(hotkeys['target change'], 1)
                            elif current == 'eight':
                                kb_mouse.kb_input(hotkeys['target reverse'], 1)
                            elif current == 'centered':
                                kb_mouse.kb_input(hotkeys['target reverse'], 2)   
                        elif target == 'eight':
                            if current == 'circle':
                                kb_mouse.kb_input(hotkeys['target change'], 2)
                            elif current == 'infinite':
                                kb_mouse.kb_input(hotkeys['target change'], 1)
                            elif current == 'centered':
                                kb_mouse.kb_input(hotkeys['target reverse'], 1)
                        elif target == 'centered':
                            if current == 'circle':
                                kb_mouse.kb_input(hotkeys['target change'], 1)
                            elif current == 'eight':
                                kb_mouse.kb_input(hotkeys['target reverse'], 1)
                            elif current == 'infinite':
                                kb_mouse.kb_input(hotkeys['target change'], 2)
                        else:
                            return self._name, target
                else:
                    if Monkey._wingmonkey:
                        if target == 'circle':
                            if current == 'infinite':
                                kb_mouse.kb_input(hotkeys['target reverse'], 1)
                            elif current == 'eight':
                                kb_mouse.kb_input(hotkeys['target reverse'], 2)
                            elif current == 'wingmonkey':
                                kb_mouse.kb_input(hotkeys['target change'], 1)
                        elif target == 'infinite':
                            if current == 'circle':
                                kb_mouse.kb_input(hotkeys['target change'], 1)
                            elif current == 'eight':
                                kb_mouse.kb_input(hotkeys['target reverse'], 1)
                            elif current == 'wingmonkey':
                                kb_mouse.kb_input(hotkeys['target reverse'], 2)   
                        elif target == 'eight':
                            if current == 'circle':
                                kb_mouse.kb_input(hotkeys['target change'], 2)
                            elif current == 'infinite':
                                kb_mouse.kb_input(hotkeys['target change'], 1)
                            elif current == 'wingmonkey':
                                kb_mouse.kb_input(hotkeys['target reverse'], 1)
                        elif target == 'wingmonkey':
                            if current == 'circle':
                                kb_mouse.kb_input(hotkeys['target reverse'], 1)
                            elif current == 'eight':
                                kb_mouse.kb_input(hotkeys['target change'], 1)
                            elif current == 'infinite':
                                kb_mouse.kb_input(hotkeys['target change'], 2)
                        else:
                            return self._name, target
                    else:
                        if target == 'circle':
                            if current == 'infinite':
                                kb_mouse.kb_input(hotkeys['target reverse'], 1)
                            elif current == 'eight':
                                kb_mouse.kb_input(hotkeys['target change'], 1)
                        elif target == 'infinite':
                            if current == 'circle':
                                kb_mouse.kb_input(hotkeys['target change'], 1)
                            elif current == 'eight':
                                kb_mouse.kb_input(hotkeys['target reverse'], 1)  
                        elif target == 'eight':
                            if current == 'circle':
                                kb_mouse.kb_input(hotkeys['target reverse'], 1)
                            elif current == 'infinite':
                                kb_mouse.kb_input(hotkeys['target change'], 1)
                        else:
                            return self._name, target
            case 'mortar':  
                # with mortar, you need to always use special(1, x, y) as mortars cannot use targeting.
                cprint("Use special(1, x, y) instead.")
                return 'OK'
            case 'dartling':
                # after changing to 'locked', you must use special(1, x, y) instead to change target. 
                if target == 'locked':
                    if current == 'normal':
                        kb_mouse.kb_input(hotkeys['target change'], 1)
                        self._change_target_special(1, x, y)
                    elif current == 'independent':
                        kb_mouse.kb_input(hotkeys['target reverse'], 1)
                        self._change_target_special(1, x, y)
                elif target == 'independent':
                    if current == 'normal':
                        kb_mouse.kb_input(hotkeys['target reverse'], 1)
                    elif current == 'locked':
                        kb_mouse.kb_input(hotkeys['target change'], 1)
                else:
                    return self._name, target
            case 'spike':
                if target == 'normal':
                    if current == 'close':
                        kb_mouse.kb_input(hotkeys['target reverse'], 1)
                    elif current == 'smart':
                        kb_mouse.kb_input(hotkeys['target reverse'], 2)
                    elif current == 'set':
                        kb_mouse.kb_input(hotkeys['target change'], 2)
                    elif current == 'automatic':
                        kb_mouse.kb_input(hotkeys['target change'], 1)
                elif target == 'close':
                    if current == 'normal':
                        kb_mouse.kb_input(hotkeys['target change'], 1)
                    elif current == 'smart':
                        kb_mouse.kb_input(hotkeys['target reverse'], 1)
                    elif current == 'set':
                        kb_mouse.kb_input(hotkeys['target reverse'], 2)
                    elif current == 'automatic':
                        kb_mouse.kb_input(hotkeys['target change'], 2)
                elif target == 'set':
                    if current == 'normal':
                        kb_mouse.kb_input(hotkeys['target reverse'], 2)
                        if x is not None and y is not None:
                            self._change_target_special(1, x, y)
                    elif current == 'close':
                        kb_mouse.kb_input(hotkeys['target change'], 2)
                        if x is not None and y is not None:
                            self._change_target_special(1, x, y)
                    elif current == 'smart':
                        kb_mouse.kb_input(hotkeys['target change'], 1)
                        if x is not None and y is not None:
                            self._change_target_special(1, x, y)
                    elif current == 'automatic':
                        kb_mouse.kb_input(hotkeys['target reverse'], 1)
                        if x is not None and y is not None:
                            self._change_target_special(1, x, y)
                elif target == 'smart':
                    if current == 'close':
                        kb_mouse.kb_input(hotkeys['target change'], 1)
                    elif current == 'set':
                        kb_mouse.kb_input(hotkeys['target reverse'], 1)
                    elif current == 'normal':
                        kb_mouse.kb_input(hotkeys['target change'], 2)
                    elif current == 'automatic':
                        kb_mouse.kb_input(hotkeys['target reverse'], 2)
                elif target == 'automatic':
                    if current == 'close':
                        kb_mouse.kb_input(hotkeys['target reverse'], 2)
                    elif current == 'set':
                        kb_mouse.kb_input(hotkeys['target change'], 1)
                    elif current == 'normal':
                        kb_mouse.kb_input(hotkeys['target reverse'], 1)
                    elif current == 'smart':
                        kb_mouse.kb_input(hotkeys['target change'], 2)
                else:
                    return self._name, target
            case _:
                return self._normal_targeting(current, target)
        cprint(f"{self._name.capitalize()} targeting set to '{target}'.")
        return 'OK'
    
    def _update_auto_target_paths(self, upg_path: str, path_index: int) -> None:
        """Checks if new crosspath updates the targeting priority automatically and if so, updates targeting value.
        
        For some monkeys, like ace, if you do upgrade x-x-1 -> x-x-2, it unlocks a new targeting priority (centered 
        path in this case) which is automatically set as current targetin priority. This method will check such cases 
        and handles the updating of current attributes for bot as well.

        This method is only called inside self._do_upgrades.

        Args:
            upg_path: Current update path after upgrading.
            path_index: Which path was updated: 0 for top, 1 for middle, 2 for bottom.
        """
        u: str = upg_path
        i: int = path_index
        if self._name == 'ace' and i == 2 and int(u[2*i]) == 2:
            self._targeting = 'centered'
        elif self._name == 'heli' and i == 0 and int(u[2*i]) == 2:
            self._targeting = 'pursuit'
        elif self._name == 'sniper' and i == 1 and int(u[2*i]) == 5:
            self._targeting = 'elite'
            Monkey._elite_sniper = 1

    def _do_upgrades(self, upgrade_list: list[str], cpos_x: float | None = None, cpos_y: float | None = None) -> None:
        """Handles the choosing of correct upgrade path and verifies the process.

        Upgrades monkey by first checking current upgrade path, then matching it to next upgrade and choosing correct
        upgrade by comparing differing values. Upgrades are passed as a list of strings which allows multiple upgrades
        with one target method call. Ater
        
        If monkey position has changed after initial placement (Geared/Sanctuary), use cpos to point current position.

        Args:
            upgrade_list: List of upgrade path strings.
            cpos_x: If monkey's current x-coordinate position has changed, update it. Default value is None.
            cpos_y: If monkey's current y-coordinate position has changed, update it. Default value is None.
        """
        times.pause_bot()
        paths = ['upgrade top', 'upgrade mid', 'upgrade bot'] 
        if cpos_x is not None:
            self._pos_x = cpos_x
        if cpos_y is not None:
            self._pos_y = cpos_y
        kb_mouse.click((self._pos_x, self._pos_y))
        if cpos_x is not None:
            self._update_panel_position(cpos_x)
        start = time.time()
        counter = 0
        if self._panel_pos == 'right':
            while not ocr.strong_delta_check('Sell', Monkey._RIGHT_PANEL_SELL_LOCATION, OCR_READER):
                if time.time()-start > 10:
                    BotVars.defeat_status = True
                    cprint("Failed to find the upgradeable monkey.")
                    return
                if counter == 3:
                    kb_mouse.click((self._pos_x, self._pos_y))
                    if cpos_x is not None:
                        self._update_panel_position(cpos_x)
                    counter = 0
                time.sleep(0.1)
                counter += 1
        elif self._panel_pos == 'left':
            while not ocr.strong_delta_check('Sell', Monkey._LEFT_PANEL_SELL_LOCATION, OCR_READER):
                if time.time()-start > 10:
                    BotVars.defeat_status = True
                    cprint("Failed to find the upgradeable monkey.")
                    return
                if counter == 3:
                    kb_mouse.click((self._pos_x, self._pos_y))
                    if cpos_x is not None:
                        self._update_panel_position(cpos_x)
                    counter = 0
                time.sleep(0.1)
                counter += 1
        for upg in upgrade_list:
            u = self._upgrade_path
            cprint(f'Upgrading {u} {self._name.capitalize()} to {upg}...', end=' ')
            for i in range(0, 3):
                if int(u[2*i]) != int(upg[2*i]):
                    self._select_upgrade(upg, paths[i])
                    if BotVars.defeat_status:
                        return
                    self._update_auto_target_paths(upg, i)
                    break
        kb_mouse.press_esc()

    def _select_upgrade(self, upg: str, button: str) -> None:
        """Calls upgrading method with correct coordinate and path inputs.

        After upgrade path is verified, _check_upgrade gets passed with coordinates that correspond to current upgrade 
        text boxes: one for left panel and one for right.

        Args:
            upg: Current upgrade path string/the upgrade we want to buy for our monkey.
            button: Upgrade button, either for top, mid or bottom path.
        """
        if button == 'upgrade top':
            self._check_upgrade(upg, button,
                                Monkey._TOP_UPG_CURRENT_LEFTWINDOW,
                                Monkey._TOP_UPG_CURRENT_RIGHTWINDOW,
                                0)
        elif button == 'upgrade mid':
            self._check_upgrade(upg, button,
                                Monkey._MID_UPG_CURRENT_LEFTWINDOW,
                                Monkey._MID_UPG_CURRENT_RIGHTWINDOW,
                                1)
        elif button == 'upgrade bot':
            self._check_upgrade(upg, button,
                                Monkey._BOT_UPG_CURRENT_LEFTWINDOW,
                                Monkey._BOT_UPG_CURRENT_RIGHTWINDOW,
                                2)

    def _check_upgrade(self, upg: str,
                      button: str,
                      current_l: tuple[float, float, float, float],
                      current_r: tuple[float, float, float, float], 
                      upg_path: int
                      ) -> None:
        """Keeps trying to upgrade a monkey, then sends confirmation message after a succesful attempt.

        Also updates _upgrade_path attribute.

        Implemented with ocr: first finds the current upgrade string, presses upgrade and passes result onto ocr 
        function. Ocr will handle the actual matching with corresponding result string that gets read from a json file; 
        see ocr.strong_delta_check for more info.

        If monkey is placed on the right side of map, it opens upgrade panel on left. Similarly, if monkey is placed
        on the left side of map, it opens upgrade panel on right. For these reasons, both left and
        right coordinates have to be included for current upgrade.

        Args:
            upg: Next upgrade path for this monkey.
            button: Crosspath button - top, middle or bottom.
            current_l: Current upgrade image location on screen, if the panel opens on the left.
            current_r: Current upgrade image location on screen, if the panel opens on the right.
            upg_path: Integer for upgrade path: 0 = top, 1 = middle, 2 = bot. Is necessary for some special monkey 
                upgrade paths which ocr needs to identify and handle separately.
        """
        c_path = self._upgrade_path
        if upg_path == 0:
            upg_match = self._name+' '+str(int(c_path[0])+1)+'-x-x'
        elif upg_path == 1:
            upg_match = self._name+' x-'+str(int(c_path[2])+1)+'-x'
        elif upg_path == 2:
            upg_match = self._name+' x-x-'+str(int(c_path[4])+1)

        total_time = times.current_time()
        upgraded = 0
        defeat_check = 1
        levelup_check = 1
        while not upgraded:
            if levelup_check == Rounds.LEVEL_UP_CHECK_FREQUENCY:
                kb_mouse.click((0.9994791666667, 0))
                levelup_check = 0
            levelup_check += 1
            if defeat_check > Rounds.DEFEAT_CHECK_FREQUENCY:
                defeat_check = 1
            if Rounds.defeat_check(total_time, defeat_check, Rounds.DEFEAT_CHECK_FREQUENCY):
                cprint(f'**Failed to upgrade {self._name.capitalize()}**')
                kb_mouse.press_esc()    # close the upgrade panel if still open
                return
            defeat_check += 1
            kb_mouse.kb_input(hotkeys[button])
            if self._name == 'super' and re.search("^4-[0-2]-0$|^4-0-[0-2]$|^5-[0-2]-0$|^5-0-[0-2]$", upg) is not None:
                kb_mouse.kb_input(Key.enter)    # if upgrade is Sun Temple/True Sun God, press Enter to confirm it
            if self._panel_pos == 'right':
                if ocr.strong_delta_check(
                    '_upgrade_', 
                    (current_r[0], current_r[1], current_r[2], current_r[3]),
                    OCR_READER,
                    upg_match):
                    upgraded = 1
            elif self._panel_pos == 'left':
                if ocr.strong_delta_check(
                    '_upgrade_', 
                    (current_l[0], current_l[1], current_l[2], current_l[3]),
                    OCR_READER, 
                    upg_match):
                    upgraded = 1
            if upgraded:
                if not OcrValues._log_ocr_deltas:
                    cprint('Upgraded.')
                self._upgrade_path = upg
                return

    def _place(self) -> None:
        """Places a monkey to an in-game location.
         
        Checks if it's been placed at that location and if not, keeps trying until it succeeds: this helps a lot with 
        placements as user no longer needs to time monkey placement and can instead queue them in advance.

        However, user should not attempt to create a new Monkey too early in advance, as this method will naturally 
        ignore any other calls until it succeeds. This could potentially skip over a round or multiple, and ruin 
        your current plan execution. Rather, you should create a Monkey if you know you it can be affored soon, 
        preferably during the same round you call it, or in some cases, the next round - but not any further!

        This method also updates upgrade panel position to 'left' or 'right' if it was 'middle', to remove any 
        ambiguity and need to handle this value separately under other methods.
        """
        if BotVars.defeat_status:
            return
        cprint(f'Placing {self._name.capitalize()}...', end=' ')
        total_time = times.current_time()
        placed = 0
        defeat_check = 1
        levelup_check = 1
        while not placed:
            if OcrValues._log_ocr_deltas or not self._placement_check:
                kb_mouse.click((0.5, 0))
                kb_mouse.kb_input(self._get_hotkey())
                kb_mouse.click((self._pos_x, self._pos_y), 1)
                cprint(f'{self._name.capitalize()} placed.')
                return
            times.pause_bot()
            if levelup_check == Rounds.LEVEL_UP_CHECK_FREQUENCY:
                kb_mouse.click((0.9994791666667, 0))
                levelup_check = 0
            levelup_check += 1
            if defeat_check > Rounds.DEFEAT_CHECK_FREQUENCY:
                defeat_check = 1
            if Rounds.defeat_check(total_time, defeat_check, Rounds.DEFEAT_CHECK_FREQUENCY):
                cprint(f'**Failed to place {self._name.capitalize()}**')
                return
            defeat_check += 1
            kb_mouse.kb_input(self._get_hotkey())
            kb_mouse.click((self._pos_x, self._pos_y), 2)
            time.sleep(0.2)
            if self._panel_pos == 'right':
                if ocr.strong_delta_check('Sell', Monkey._RIGHT_PANEL_SELL_LOCATION, OCR_READER):
                    placed = 1
            elif self._panel_pos == 'left':
                if ocr.strong_delta_check('Sell', Monkey._LEFT_PANEL_SELL_LOCATION, OCR_READER):
                    placed = 1
            else:
                if self._update_panel_position(self._pos_x):
                    placed = 1
            if placed:
                kb_mouse.press_esc()
                if Monkey._wingmonkey == 0 and self._name == 'ace_wing':
                    Monkey._wingmonkey = 1  # detect and account for 'wingmonkey' mk if name 'ace_wing' is used.
                cprint(f'{self._name.capitalize()} placed.')
                return
    
    def special(self, s: str | int = 1,
                x: float | None = None,
                y: float | None = None,
                cpos_x: float | None = None,
                cpos_y: float | None = None
                ) -> None:
        """Uses special target button of current monkey and sets possible target location, if necessary.

        Examples: Almost all targetable/behaviour changing abilities:
            heroes: ezili totem, geraldo shop
            monkeys: dartling, mortar, ace direction, heli lock-in, mermonkey mid path, at least 
                0-1-4 engineer, beast handler.
        Note that some monkeys have 2 specials. For beast handler in particular, their order depends on which paths you
        ultimately end up choosing.

        If monkey position has changed after initial placement (Geared/Sanctuary), use cpos to update current position.

        Args:
            s: Special ability, either 1 (most common) or 2. Strings '1' or '2' are also valid. Default value is 1.
            x: If targetable ability, its x-coordinate. Default value is None.
            y: If targetable ability, its y-coordinate. Default value is None.
            cpos_x: If monkey's current x-coordinate position has changed, update it. Default value is None.
            cpos_y: If monkey's current y-coordinate position has changed, update it. Default value is None.

        Examples:

            Mortars are very good example of using 'special' as they cannot use 'target' method.
            >>> mortar = Monkey('mortar', 0.05, 0.52)
            Placing Mortar... Mortar placed.
            >>> mortar.target('any_value', x=0.05, y=0.5)  # points user to 'special' instead
            Use special(1, x, y) instead.
            >>> mortar.special(1, x=0.05, y=0.5) # set mortar to shoot on top of itself
            Mortar special 1 used.

            As default value for special is 1, you can leave it out unless you need 2. special. However, if you include 
            the special type, you don't need to mention x and y explicitly, just make sure they are in right positions.
            >>> mortar.special(1, x=0.2, y=0.25)
            Mortar special 1 used.
            >>> mortar.special(x=0.2, y=0.25) # identical to above one in functionality
            Mortar special 1 used.
            >>> mortar.special(1, 0.2, 0.25) # still the same, but x= and y= are not used.
            Mortar special 1 used.

            Some monkeys such as beast handler, have a second special. For beast handler, the special order depends on 
            unlocked paths so pay attention to them.
            >>> beast = Monkey('beast', 0.1, 0.5)
            Placing Beast... Beast placed.
            >>> beast.upgrade(['0-0-1'])
            Upgrading 0-0-0 Beast to 0-0-1... Upgraded.
            >>> mermonkey = Monkey('mermonkey', 0.2, 0.5) # create a 5-x-x mermonkey to place handler bottom path
            Placing Mermonkey... Mermonkey placed.
            >>> mermonkey.upgrade(['1-0-0', '2-0-0', '3-0-0', '4-0-0', '5-0-0'])
            Upgrading 0-0-0 Mermonkey to 1-0-0... Upgraded.
            Upgrading 1-0-0 Mermonkey to 2-0-0... Upgraded.
            Upgrading 2-0-0 Mermonkey to 3-0-0... Upgraded.
            Upgrading 3-0-0 Mermonkey to 4-0-0... Upgraded.
            Upgrading 4-0-0 Mermonkey to 5-0-0... Upgraded.
            >>> beast.upgrade(['1-0-1'])
            Upgrading 0-0-1 Beast to 1-0-1... Upgraded.
            >>> beast.special(1, x=0.19, y=0.41)  # this refers to bottom path handler
            Beast special 1 used.
            >>> beast.special(2, x=0.2, y=0.63)  # this refers to top path handler
            Beast special 2 used.

                ...but...

            >>> beast2 = Monkey('beast', 0.15, 0.5)
            Placing Beast... Beast placed.
            >>> beast2.upgrade(['0-1-0'])
            Upgrading 0-0-0 Beast to 0-1-0... Upgraded.
            >>> beast2.special(2, x=0.25, y=0.6)  # 2 refers to middle path, for now...
            Beast special 2 used.
            >>> beast2.upgrade(['1-1-0'])
            Upgrading 0-1-0 Beast to 1-1-0... Upgraded.
            >>> beast2.special(1, x=0.25, y=0.65) # but now 1 refers to middle path!
            Beast special 1 used.
            >>> beast2.special(2, x=0.25, y=0.7)  # and 2 to top path!
            Beast special 2 used.
            
            For some monkeys, like dartling or heli, you need to first change targeting to something where location can 
            be used. The good things is, you can pass 'target' a location value.
            >>> dartling = Monkey('dartling', 0.1, 0.65) # base targeting is 'normal'
            Placing Dartling... Dartling placed.
            >>> dartling.target('locked', x=0.1, y=0.0) # set dartling to 'locked' and to point straight up
            Dartling targeting set to 'locked'.

            And now you can change dartling targeting by calling calling special.       
            >>> dartling.special(1, x=0.0, y=0.5)   # set dartling to point left; must have set target to 'locked'!
            Dartling special 1 used.
            >>> dartling.special(1, x=0.15, y=1.0) # set dartling to point straight down
            Dartling special 1 used.

            Different monkeys have (obviously) different functions when 'special' is called: for heli, it can 
            relocate heli with status 'lock', for ace it will reverse flying direction, for 0-1-4+ engineer it can be 
            used to relocate bloon/XXXL trap, etc.

            Finally, if your monkey has changed its position from original (maybe you're playing Geared or Sanctuary 
            maps), you can add additional cpos_x and cpos_y arguments to update position. Remember that cpos updates 
            the monkey location, not the target location!
            >>> mortar2 = Monkey('mortar', 0.05, 0.75)
            Placing Mortar... Mortar placed.
            >>> mortar2.special(1, x=0.25, y=0.25)    # this refers to previous monkey location (0.05, 0.75)
            Mortar special 1 used.
            >>> mortar2.special(1, x=0.4, y=0.25)  # mortar target set to (0.4, 0.25), monkey location still (0.5, 0.5)
            Mortar special 1 used.

            The following would update both monkey location (to (0.3, 0.85)) and mortar target location (to (0.3, 0.3))
            But it points to no monkey: avoid empty monkey pointers as bot is likely to get stuck in situations like 
            these. Unlike 'target' or 'upgrade', special doesn't verify that actual monkey exists at cpos, or that 
            ability can be even used.
            __
            >>> 
                mortar2.special(1, x=0.3, y=0.3, cpos_x=0.3, cpos_y=0.85) # points to nothing at (0.3, 0.85)
            >>> mortar2.special(1, x=0.4, y=0.4,  cpos_x=0.05, cpos_y=0.75) # back to original location
            Mortar special 1 used.
        """
        times.pause_bot()
        if BotVars.defeat_status:
            return
        elif s not in [1, 2, '1', '2']:
            cprint('Wrong input value on special ability; use 1 or 2')
            return
        # current position click; used on monkey-moving maps like Geared/Sanctuary. Updates new coordinates to monkey.
        if cpos_x is not None:
            self._pos_x = cpos_x
        if cpos_y is not None:
            self._pos_y = cpos_y
        kb_mouse.click((self._pos_x, self._pos_y))
        if cpos_x is not None:
            self._update_panel_position(cpos_x)
        kb_mouse.kb_input(hotkeys['special '+str(s)])
        if x is not None and y is not None:
            kb_mouse.click((x, y))
        kb_mouse.press_esc()
        #time.sleep(0.3)
        cprint(f'{self._name.capitalize()} special {s} used.')

    def sell(self, cpos_x: float | None = None, cpos_y: float | None = None) -> None:
        """Sells this monkey.

        Doesn't actually delete the bot monkey object so please don't refer to it afterwards - unless you've created a 
        new monkey and stored it in same variable.
        
        Args:
            cpos_x: If monkey's current x-coordinate position has changed, update it. Default value is None.
            cpos_y: If monkey's current y-coordinate position has changed, update it. Default value is None.

        Examples
        --
        >>> wizard = Monkey('wizard', 0.1, 0.85)
        Placing Wizard... Wizard placed.
        >>> mermonkey = Monkey('mermonkey', 0.2, 0.85)
        Placing Mermonkey... Mermonkey placed.
        >>> wizard.sell()
        Wizard sold!
        >>> mermonkey.sell()
        Mermonkey sold!

        You can store a new monkey in the same variable and even place it in the same location as previous one - just 
        ensure it has been sold
        >>> boomerang = Monkey('boomer', 0.1, 0.85)  
        Placing Boomer... Boomer placed.
        >>> boomerang.sell()
        Boomer sold!
        >>> boomerang = Monkey('boomer', 0.1, 0.85)
        Placing Boomer... Boomer placed.
        >>> boomerang.sell()
        Boomer sold!
        """
        times.pause_bot()
        if BotVars.defeat_status:
            return
        if cpos_x is not None:
            self._pos_x = cpos_x
        if cpos_y is not None:
            self._pos_y = cpos_y
        kb_mouse.click((self._pos_x, self._pos_y))
        time.sleep(0.3)
        kb_mouse.kb_input(hotkeys['sell'])
        if self._name == 'sniper' and self._upgrade_path[2] == 5:
            Monkey._elite_sniper = 0
        if not OcrValues._log_ocr_deltas:
            cprint(f'{self._name.capitalize()} sold!')

    def target(self, set_target: str,
               x: float | None = None,
               y: float | None = None,
               cpos_x: float | None = None,
               cpos_y: float | None = None
               ) -> None:
        """Changes targeting priority of a monkey.

        If monkey is 'mortar', use special(1, x, y) instead: mortars don't support 'target' command.

        All possible targeting priorities for each monkey are listed under "Targeting options" section below.

        Remember that some priority options become available only after certain upgrades (e.g. 'pursuit' on heli); 
        there are no checks in place for doing this behaviour, so pay attention to these rare cases.

        If monkey needs coordinate position for its targeting e.g. dartling gun direction, heli position etc., use x 
        and y values.

        If monkey position has changed after initial placement (Geared/Sanctuary), use cpos_x and cpos_y to update 
        current position.

        Args:
            set_target: New targeting priority.
            x: If targeting priority needs coordinates, its x-coordinate. Default value is None.
            y: If targeting priority needs coordinates, its y-coordinate. Default value is None.
            cpos_x: If monkey's current x-coordinate position has changed, update it. Default value is None.
            cpos_y: If monkey's current y-coordinate position has changed, update it. Default value is None.

        Targeting options
        --
        >>> #
            'heli' {default: 'follow'}  
                'lock' = Lock In Place  
                'pursuit'   # use only for 2+-x-x  
        >>>     
            'ace' {default: 'circle'}
                'circle'
                'infinite' = Figure Infinite
                'eight' = Figure Eight
                'wingmonkey'    # use only if Monkey knowledge enabled
                'centered' = Centered Path  # use only for x-x-3+
        >>>
            'mortar' {default: None} # always use special(1, x= , y=) for targeting
        >>>     
            'dartling' {default: 'normal'}
                'locked'    # use special(1, x= , y=) to retarget while locked
                'independent' = Target Independent # use only for x-x-4+ 
        >>>
            'spike' {default: 'normal'} # use only for x-x-2+
                'normal'
                'set'
                'close'
                'smart'
                'automatic'
        >>>
            Others {default: 'first'}
                'first'
                'close'
                'last'
                'strong'

        Special cases:
        __
        >>>
        'village' has initial value 'first'; change targeting only for 5-x-x paths  
        'ice' has initial value 'first'; change targeting only for x-x-3+ paths  
        'tack' has initial value 'first'; change targeting only for 5-x-x paths
        'farm' has value None; but you have no need to target these anyway

        Examples:
            Dart monkey has default targeting value 'first' so calling it again does nothing.
            >>> dart = Monkey('dart', 0.5, 0.1)  
            Placing Dart... Dart placed.
            >>> dart.target('first')  # this does nothing.
            Already set to First.
            >>> dart.target('strong') 
            Dart targeting set to 'strong'.

            While most monkeys have the basic targeting options (first, last, close, strong), some have their custom 
            ones and some have none. For example, heli has initial targeting mode 'lock', but tack has None. For 
            monkeys like tack, calling tack.target('first') causes an error and sets current game state as 'defeat' to 
            prevent problems - similar happens with banana farms, so don't try these.
            >>> heli = Monkey('heli', 0.6, 0.1)
            Placing Heli... Heli placed.
            >>> heli.target('lock')  
            Heli targeting set to 'lock'.
            >>> tack = Monkey('tack', 0.6, 0.2)
            Placing Tack... Tack placed.

            Some monkeys get targeting priority unlocked after certain upgrade.

            5-x-x Village
            >>> village = Monkey('village', 0.48, 0.2)
            Placing Village... Village placed.
            >>> village.upgrade(['1-0-0', '2-0-0', '3-0-0', '4-0-0', '5-0-0'])
            Upgrading 0-0-0 Village to 1-0-0... Upgraded.
            Upgrading 1-0-0 Village to 2-0-0... Upgraded.
            Upgrading 2-0-0 Village to 3-0-0... Upgraded.
            Upgrading 3-0-0 Village to 4-0-0... Upgraded.
            Upgrading 4-0-0 Village to 5-0-0... Upgraded.
            >>> village.target('strong')
            Village targeting set to 'strong'.

            x-x-2+ Spike factory
            >>> spike = Monkey('spike', 0.48, 0.3)
            Placing Spike... Spike placed.
            >>> spike.upgrade(['0-0-1', '0-0-2'])
            Upgrading 0-0-0 Spike to 0-0-1... Upgraded.
            Upgrading 0-0-1 Spike to 0-0-2... Upgraded.
            >>> spike.target('smart')
            Spike targeting set to 'smart'.

            x-x-3+ Ice monkey
            >>> ice = Monkey('ice', 0.48, 0.4)
            Placing Ice... Ice placed.
            >>> ice.upgrade(['0-0-1', '0-0-2', '0-0-3'])
            Upgrading 0-0-0 Ice to 0-0-1... Upgraded.
            Upgrading 0-0-1 Ice to 0-0-2... Upgraded.
            Upgrading 0-0-2 Ice to 0-0-3... Upgraded.
            >>> ice.target('close')
            Ice targeting set to 'close'.

            Some monkeys have targeting priorities that also need a position to be set: you can use x and y arguments 
            to pinpoint the position.
            >>> dartling = Monkey('dartling', 0.7, 0.2)
            Placing Dartling... Dartling placed.
            >>> dartling.target('locked', x=0.5, y=0.0) # set targeting to 'locked' and set location to (0.5, 0.0)
            Dartling targeting set to 'locked'.

            In particular for mortar, you don't use 'target' at all, instead always use 'special' - check its 
            documentation or read the readme text in gui.
            >>> mortar = Monkey('mortar', 0.75, 0.3)
            Placing Mortar... Mortar placed.
            >>> mortar.target('type_something_here', x=0.25, y=0.25) # this will just remind you to call special().
            Use special(1, x, y) instead.
            >>> mortar.special(1, x=0.25, y=0.25)
            Mortar special 1 used.

            The 'special' command has also other uses: to move 'lock' heli position, change locked dartling direction, 
            target other monkey abilities etc. You should use 'target' and 'special' in sync, as most targetable 
            abilities can only be accessed with 'special' - and some only with 'special' as we saw with mortar.

            Use cpos_x and cpos_y to update monkey location if it has changed from previous (e.g. map is 
            Geared or Sanctuary). Unlike with upgrade command, special uses no ocr and thus can't verify where cpos
            in pointing to.
            >>> mortar2 = Monkey('mortar', 0.8, 0.2)
            Placing Mortar... Mortar placed.
            >>> glue = Monkey('glue', 0.8, 0.4)
            Placing Glue... Glue placed.
            >>> mortar2.special(1, x=0.5, y=0.5) # this would refer to location (0.8, 0.2)
            Mortar special 1 used.
            >>> mortar2.special(1, x=0.5, y=0.5, cpos_x=0.8, cpos_y=0.4) # refers to location of glue monkey.
            Mortar special 1 used.
            >>> mortar2.special(1, x=0.5, y=0.5) # cpos updates location so still refers to glue at (0.8, 0.4)
            Mortar special 1 used.
            >>> mortar2.special(1, x=0.1, y=0.8, cpos_x=0.8, cpos_y=0.2) # finally refers back to mortar2
            Mortar special 1 used.
        """
        times.pause_bot()
        if BotVars.defeat_status:
            return
        val = self._change_target(set_target.lower(), x , y, cpos_x, cpos_y)
        if val != 'OK':
            self._error('target', set_target, val)
        kb_mouse.press_esc()      # closes currently opened targeting window   
        self._targeting = set_target.lower()

    def upgrade(self, set_upg: list[str], cpos_x: float | None = None, cpos_y: float | None = None) -> None:
        """Upgrades current monkey.

        Upgrades are passed a list, which allows to queue multiple upgrades in one call. But even if you need just one 
        upgrade, you still need to wrap it in a list; see Examples below.

        You need to track the upgrades yourself and do them in order: upgrading a monkey from 0-0-0 to 2-0-0 must be 
        done in order 0-0-0 -> 1-0-0 -> 2-0-0. And if you have multiple choices, like with 0-3-2, then you can 
        obviously have many different paths to get there; just remember to do upgrades in logical order.

        If monkey position has changed after initial placement (Geared/Sanctuary), use cpos_x and cpos_y to update 
        current position.

        Args:
            set_upg: List of upgrade path strings. Each string is of form 'x-y-z' where 

                >at least one of x,y,z is 0 (can do only 1 crosspath),

                >at most one of x,y,z is 5 and one of remaining paths can be at most 2
                (max path is 5, crosspath max is 2).          
            cpos_x: If monkey's current x-coordinate position has changed, update it. Default value is None.
            cpos_y: If monkey's current y-coordinate position has changed, update it. Default value is None.

        Examples:
            For a single upgrade, you still need the list brackets []
            >>> dart = Monkey('dart', 0.6, 0.9) 
            Placing Dart... Dart placed.
            >>> dart.upgrade(['1-0-0'])
            Upgrading 0-0-0 Dart to 1-0-0... Upgraded.
            >>> dart.upgrade(['1-1-0', '2-1-0', '2-2-0', '3-2-0'])
            Upgrading 1-0-0 Dart to 1-1-0... Upgraded.
            Upgrading 1-1-0 Dart to 2-1-0... Upgraded.
            Upgrading 2-1-0 Dart to 2-2-0... Upgraded.
            Upgrading 2-2-0 Dart to 3-2-0... Upgraded.

            You can use both ' or " in upgrade strings
            >>> bomb = Monkey('bomb', 0.5, 0.9) 
            Placing Bomb... Bomb placed.
            >>> bomb.upgrade(['1-0-0', "1-1-0"])  
            Upgrading 0-0-0 Bomb to 1-0-0... Upgraded.
            Upgrading 1-0-0 Bomb to 1-1-0... Upgraded.

            Could also do the first example in one go or spread it under multiple lines: this of course depends on 
            whether you need to do other commands in-between upgrades.
            >>> dart2 = Monkey('dart', 0.7, 0.9)
            Placing Dart... Dart placed.
            >>> dart2.upgrade(['1-0-0', '1-1-0', '2-1-0', '2-2-0', '3-2-0'])
            Upgrading 0-0-0 Dart to 1-0-0... Upgraded.
            Upgrading 1-0-0 Dart to 1-1-0... Upgraded.
            Upgrading 1-1-0 Dart to 2-1-0... Upgraded.
            Upgrading 2-1-0 Dart to 2-2-0... Upgraded.
            Upgrading 2-2-0 Dart to 3-2-0... Upgraded.
            
            *or*

            >>> dart3 = Monkey('dart', 0.75, 0.85)
            Placing Dart... Dart placed.
            >>> dart3.upgrade(['1-0-0', '1-1-0']) 
            Upgrading 0-0-0 Dart to 1-0-0... Upgraded.
            Upgrading 1-0-0 Dart to 1-1-0... Upgraded.
            >>> dart3.upgrade(['2-1-0'])
            Upgrading 1-1-0 Dart to 2-1-0... Upgraded.
            >>> dart3.upgrade(['2-2-0', '3-2-0'])
            Upgrading 2-1-0 Dart to 2-2-0... Upgraded.
            Upgrading 2-2-0 Dart to 3-2-0... Upgraded.

            Same as before, but in different order:
            >>> dart4 = Monkey('dart', 0.75, 0.75)
            Placing Dart... Dart placed.
            >>> dart4.upgrade(['0-1-0', '1-1-0'])
            Upgrading 0-0-0 Dart to 0-1-0... Upgraded.
            Upgrading 0-1-0 Dart to 1-1-0... Upgraded.
            >>> dart4.upgrade(['2-1-0', '3-1-0', '3-2-0'])
            Upgrading 1-1-0 Dart to 2-1-0... Upgraded.
            Upgrading 2-1-0 Dart to 3-1-0... Upgraded.
            Upgrading 3-1-0 Dart to 3-2-0... Upgraded.

            Following is *not possible*; you need to include all intermediary paths!

            >>>
                dart.upgrade(['1-0-0', '3-2-0'])

            Fully upgrade an ice monkey in one go to 2-5-0.
            >>> ice = Monkey('ice', 0.5, 0.8)
            Placing Ice... Ice placed.
            >>> ice.upgrade(['1-0-0', '2-0-0', '2-1-0', '2-2-0', '2-3-0', '2-4-0', '2-5-0'])
            Upgrading 0-0-0 Ice to 1-0-0... Upgraded.
            Upgrading 1-0-0 Ice to 2-0-0... Upgraded.
            Upgrading 2-0-0 Ice to 2-1-0... Upgraded.
            Upgrading 2-1-0 Ice to 2-2-0... Upgraded.
            Upgrading 2-2-0 Ice to 2-3-0... Upgraded.
            Upgrading 2-3-0 Ice to 2-4-0... Upgraded.
            Upgrading 2-4-0 Ice to 2-5-0... Upgraded.

            On some specific maps, like Geared or Sanctuary, monkey positions change over time. Bot only knows the 
            original/previous location, so you must update this by passing cpos_x and cpos_y (=current position)
            arguments. After you enter new coordinates with cpos_x, cpos_y, these values are also set as current pos_x 
            and pos_y values. Just be careful where you update cpos, as it could point to wrong location and break the
            upgrading process as ocr can't find the correct upgrade string.
            >>> engi = Monkey('engineer', 0.45, 0.9)
            Placing Engineer... Engineer placed.
            >>> 
                engi.upgrade(['1-0-0'], cpos_x=0.5, cpos_y=0.9) # this actually points to previous 1-0-1 bomb
            
            >>> engi.upgrade(['1-0-0'], cpos_x=0.45, cpos_y=0.9) # this works as point to right location
            Upgrading 0-0-0 Engineer to 1-0-0... Upgraded.

            >...a round later, engineer monkey has somehow moved to location (0.75, 0.9)...

            >>> 
            engi.upgrade(['1-1-0']) # still refers to location (0.5, 0.9) i.e. the bomb monkey

            >>> engi.upgrade(['1-1-0', '2-1-0'], cpos_x=0.45, cpos_y=0.9)
            Upgrading 1-0-0 Engineer to 1-1-0... Upgraded.
            Upgrading 1-1-0 Engineer to 2-1-0... Upgraded.

            If location hasn't changed since last upgrade, you can leave the cpos arguments out. Or you could add them 
            anyway even if position has not yet changed, but would like to now current locations clearly after each 
            step. You can check the sanctuaryHardChimps.py plan in plans folder for an actual use case of cpos args.
           
            Now if map was Geared, for example, then after 8 rounds, a monkey returns to its original position.

            >>> dart.upgrade(['4-2-0'], cpos_x=0.75, cpos_y=0.9)
            Upgrading 3-2-0 Dart to 4-2-0... Upgraded.

            >...dart is in position (0.75, 0.9) and 8 rounds pass...

            >>> dart.upgrade(['5-2-0']) # this would work as position is the same as it was 8 rounds back.
            Upgrading 4-2-0 Dart to 5-2-0... Upgraded.
        """
        times.pause_bot()
        if BotVars.defeat_status:
            return
        elif self._name == 'hero':
            cprint("Heroes cannot be upgraded.")
            return
        elif set_upg != []:
            for upg in set_upg:
                if re.search("^[0-5]-[0-2]-0$|^[0-5]-0-[0-2]$|"
                            "^[0-2]-[0-5]-0$|^0-[0-5]-[0-2]$|"
                            "^[0-2]-0-[0-5]$|^0-[0-2]-[0-5]$", upg) is None:
                    self._error('upgrade', upg, set_upg)
                    return
            self._do_upgrades(set_upg, cpos_x, cpos_y)
        else:
            self._error('upgrade_list', set_upg)

    def target_robo(self, 
                    direction: str, 
                    clicks: int, 
                    cpos_x: float | None = None,
                    cpos_y: float | None = None
                    ) -> None:
        """Changes robo monkey second arm targeting.
        
        Unlike 'target' method, this one lacks complex internal systems. Instead, it does just the following:  
        -clicks on current super monkey location  
        -clicks either left or right arrow to change targeting, set amount of times  
        -then closes the panel

        Cannot set same targeting option for both arms.

        Args:
            direction (str): Either 'left' or 'right' depending which targeting direction you'd wish to click.
            clicks (int): Total amout of clicks.
            cpos_x (float | None. Default = None): Updated current x-position.
            cpos_y (float | None. Default = None): Updated current y-position.
        """
        times.pause_bot()
        if BotVars.defeat_status:
            return
        if self._name != 'super':
            cprint('This monkey is not a super monkey.')
            return
        if cpos_x is not None:
            self._pos_x = cpos_x
        if cpos_y is not None:
            self._pos_y = cpos_y
        kb_mouse.click((self._pos_x, self._pos_y))
        if cpos_x is not None:
            self._update_panel_position(cpos_x)
        if self._panel_pos == 'left':
            if direction == 'left':
                kb_mouse.click((0.044, 0.294), clicks)
            elif direction == 'right':
                kb_mouse.click((0.185, 0.292), clicks)
            else:
                cprint("Could not change targeting.")
        else:
            if direction == 'left':
                kb_mouse.click((0.680, 0.292), clicks)
            elif direction == 'right':
                kb_mouse.click((0.822, 0.292), clicks)
            else:
                cprint("Could not change targeting.")
        kb_mouse.press_esc()
        cprint("Changed robo monkey second arm targeting.")

    def merge(self, x: float, y: float, cpos_x: float | None = None, cpos_y: float | None = None) -> None:
        """Merges this beast handler into another.

        Args:
            x (float): X-position of beast handler you merge into.
            y (float): Y-position of beast handler you merge into.
            cpos_x (float | None. Default = None): Updated current x-position.
            cpos_y (float | None. Default = None): Updated current y-position.
        """
        times.pause_bot()
        if BotVars.defeat_status:
            return
        if self._name != 'beast':
            cprint("This monkey is not a beast handler.")
            return
        if cpos_x is not None:
            self._pos_x = cpos_x
        if cpos_y is not None:
            self._pos_y = cpos_y
        kb_mouse.click((self._pos_x, self._pos_y))
        if cpos_x is not None:
            self._update_panel_position(cpos_x)
        kb_mouse.kb_input(hotkeys["merge beast"])
        kb_mouse.click((x,y))
        time.sleep(0.5)
        kb_mouse.press_esc()
        time.sleep(0.1)
        cprint("Beast merged.") 

    def center(self, x: float, y: float, cpos_x: float | None = None, cpos_y: float | None = None) -> None:
        """Change monkey ace centered path location.

        Args:
            x (float): X-coordinate.
            y (float): Y-coordinate.
            cpos_x (float | None. Default = None): Updated current x-position.
            cpos_y (float | None. Default = None): Updated current y-position.
        """
        times.pause_bot()
        if BotVars.defeat_status:
            return
        if self._name != 'ace':
            cprint("Can only be used on ace.")
            return
        if cpos_x is not None:
            self._pos_x = cpos_x
        if cpos_y is not None:
            self._pos_y = cpos_y
        kb_mouse.click((self._pos_x, self._pos_y))
        if cpos_x is not None:
            self._update_panel_position(cpos_x)
        kb_mouse.kb_input(hotkeys["centered path"])
        kb_mouse.click((x,y))
        kb_mouse.press_esc()
        cprint("Ace center location updated.") 