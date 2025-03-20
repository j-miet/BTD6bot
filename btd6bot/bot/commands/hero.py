"""Implements Hero class, a superclass of Monkey.

Hero class creates a hero prototype similar to Monkey. As it inherits the Monkey class, it has same or similar methods.
It has also some custom methods for specific heroes like Geraldo and Corvus (these are not implemented yet!!!)

Examples of this module can be found in 'plans' folder and picking any .py plan file that uses a hero.
"""

from bot import kb_mouse
from bot.commands.monkey import Monkey
from bot.hotkeys import hotkeys
from bot.rounds import Rounds

class Hero(Monkey):
    """Hero class that is used for placing a hero and implementing its hero-specific methods. 

    Inherits the Monkey class, which allows using methods like placing, targeting etc. on heroes.
    Hero names are already checked inside bot.menu_start module so no further verification is required here.

    To select a hero for current plan, you must edit the docstring of your plan file: at the very beginning, there 
    should be plan information wrapped in comments and in particular, the [Hero] line where you add the name. If the 
    plan doesn't use a hero, you should write '-'. Hero names are not case-sensitive so you can write quincy, Quincy, 
    QUINCY or anything similar. As always, if you're unsure then open any existing plan .py file and check how it's 
    done there.

    All supported hero names (these must be found under menu_start.py):
        quincy
        gwen
        striker
        obyn
        rosalia
        churchill
        benjamin
        pat
        ezili
        adora
        etienne
        sauda
        brickell
        psi
        geraldo (Can't use shop yet! This will be added soon)
        corvus (Can't use spellbook yet! This will be added soon)

    Attributes:
        current_plan_hero_name (str, class attribute): Hero name in current plan. If you use hero outside a plan file, 
            you must set a value of this variable with Hero.current_plan_hero_name = ...
        
        name (str): For heroes, this is always 'hero', to differentiate them from monkeys. Initialized with super().
        pos_x (float | None): X-coordinate location. Initialized with super().
        pos_y (float | None): Y-coordinate location. Initialized with super().
        targeting (str): Targeting priority, initial value is returned via basic_monkey_target method after
            calling super() in initialize, but overridden by basic_hero_target() right after.
        upgrade_path (str): Current upgrade path of Monkey, initially always '0-0-0'. Heroes don't use this.
            Initialized with super().
        hero_name (str): Name of Hero.

    Methods:
    --
        target: Change targeting priority of this hero.  
        special: Use special of this monkey (inherited from Monkey).  
        sell: Sell this monkey (inherited from Monkey).

        See also:
          ability.ability for ability usage.

    Examples:
        If you never refer to a hero after its placement, you don't have to store a reference.

        >>> 
            Hero(0.5, 0.35)
        
        Otherwise, use descriptive name for variable. Could be simple as 'hero':

        >>> Hero.current_plan_hero_name = 'quincy'
        >>> hero = Hero(0.4, 0.5)
        Placing Hero... Hero placed.
        >>> hero.target('strong')
        Hero targeting set to 'strong'.
        >>> hero.target('first')
        Hero targeting set to 'first'.
        >>> hero.sell()
        Hero sold!
    """
    current_plan_hero_name: str | None = None # if you need Hero class without existing plan, modify this variable.

    def __init__(self, pos_x: float, pos_y: float) -> None:
        """Initializes a Hero by passing it its name and placement position.
        
        Inherits Monkey class to get access to all base attributes. Doesn't utilize upgrade path, though, as heroes 
        don't have those. 
        
        Also, hero name has value None, but gets updated via info documentation '[Hero]' line of current plan file.

        Args:
            pos_x: X-coordinate, float type.
            pos_y: Y-coordinate, float type.
        """
        super().__init__('hero', pos_x, pos_y)
        self._hero_name = self._hero_name_lowercase(Hero.current_plan_hero_name)
        self._targeting = self._basic_hero_target()

    def _hero_name_lowercase(self, hero: str | None) -> str | None:
        """Normalizes hero name to lowercase.
        
        Args:
            hero: Name of the current hero.

        Returns:
            Hero name in lowercase, or None.
        """
        if hero is not None:
            return hero.lower() 
        else:
            return None

    def _basic_hero_target(self) -> str | None:
        """Defines default hero targeting behaviour.

        Returns:
            Targeting option string or None if hero has no targeting options.
        """
        match self._hero_name:
            case 'etienne':
                return 'd&q'
            case 'benjamin':
                return None
            case _:
                return 'first'

    def _change_hero_target(self, target: str,
                           x: float | None = None,  # currently no hero has a targeting mode requiring coordinates.
                           y: float | None = None,
                           cpos_x: float | None = None,
                           cpos_y: float | None = None
                           ) -> str | tuple[str, str]:
        """Changes hero's current targeting.

        Args:
            set_target: New targeting priority.
            x: If targeting priority needs coordinates, its x-coordinate. Default value is None.
            y: If targeting priority needs coordinates, its y-coordinate. Default value is None.
            cpos_x: If hero's current x-coordinate position has changed, update it. Default value is None.
            cpos_y: If hero's current y-coordinate position has changed, update it. Default value is None.
        """
        current = self._targeting
        if target == current:
            print(f'Target already set to {current.capitalize()}.')
            return 'OK'
        if cpos_x is not None and cpos_y is not None:
            kb_mouse.click((cpos_x, cpos_y))
            self._pos_x = cpos_x
            self._pos_y = cpos_y
        else:
            kb_mouse.click((self._pos_x, self._pos_y))
        match self._hero_name:
            case 'benjamin':
                print('???')
            case 'etienne':
                if target == 'd&q':
                    if current == 'first':
                        kb_mouse.kb_input(hotkeys['target change'])
                    elif current == 'zone':
                        kb_mouse.kb_input(hotkeys['target reverse'])
                elif target == 'first':
                    if current == 'd&q':
                        kb_mouse.kb_input(hotkeys['target reverse'])
                    elif current == 'zone':
                        kb_mouse.kb_input(hotkeys['target change'])
                elif target == 'zone':
                    if current == 'first':
                        kb_mouse.kb_input(hotkeys['target reverse'])
                    elif current == 'd&q':
                        kb_mouse.kb_input(hotkeys['target change'])
                else:
                    return self._name, target
            case _:
                return self._normal_targeting(current, target)   
        print(f"{self._name.capitalize()} targeting set to '{target}'.")
        return 'OK'

    def upgrade(self, upg_list: list[str], cpos_x: float | None = None, cpos_y: float | None = None) -> None:
        """Overrides method to prevent causing errors - you can't upgrade heroes!
        
        Overrides upgrade method of Monkey to prevent calling 'upgrade' of superclass Monkey. As upgrading heroes is 
        not possible, all this method does is print a message "Can't upgrade heroes".
        """
        print("Can't upgrade heroes.")

    def force_target(self) -> None:
        """Force targeting priority of a hero without checks.
        
        Currently, its only use is to set Etienne's Zone Control status for bot: bot doesn't know when Etienne 
        hits lvl 12 and won't update targeting priority to match in-game value. So user must call this command 
        inside the round block where Etienne reaches lvl 12 - otherwise some unintended behaviour could occur
        should user want to change targeting later.
        """
        if self._hero_name == 'etienne':
            self._targeting = 'zone'
            print('Etienne targeting prio set to \'zone\' to match in-game prio.')
        else:
            print("Nothing was changed.")
        
    def target(self, set_target: str,
              x: float | None = None,
              y: float | None = None,
              cpos_x: float | None = None,
              cpos_y: float | None = None
              ) -> None:
        """Change targetting priority of a hero.
        
        All possible targeting options for each monkey are listed under "Targeting options" section below.

        Args:
            set_target: New targeting priority.
            x: If targeting priority needs coordinates, its x-coordinate. Default value is None.
            y: If targeting priority needs coordinates, its y-coordinate. Default value is None.
            cpos_x: If hero's current x-coordinate position has changed, update it. Default value is None. 
            cpos_y: If hero's current y-coordinate position has changed, update it. Default value is None.

        Targeting options
        --
        >>> 
            'Ben' {default: None}  
        >>> 
            'Etienne' {default: 'd&q'}
                'd&q' = Divide & Conquer
                'zone' = Zone Control   # only after lvl 12; see IMPORTANT section below
                'first'
        >>> 
            Others {default: 'first'}
                'first'
                'last'
                'close'
                'strong'

        Examples:
            >>> Hero.current_plan_hero_name = 'quincy'
            >>> hero = Hero(0.4, 0.5)
            Placing Hero... Hero placed.
            >>> hero.target('close')
            Hero targeting set to 'close'.
            >>> hero.sell()
            Hero sold!

            >>> Hero.current_plan_hero_name = 'etienne'
            >>> hero = Hero(0.4, 0.5)
            Placing Hero... Hero placed.
            >>> hero.target('first')
            Hero targeting set to 'first'.
            >>> hero.target('d&q')
            Hero targeting set to 'd&q'.
            >>> hero.sell()
            Hero sold!

            If you play a map like Geared or Sanctuary, hero location may change over time. To point to its new 
            location, use cpos_x, cpos_y:
            >>> 
                hero = Hero(0.25, 0.75)
                hero.target('strong')    # this refers to location (0.25, 0.75)
                hero.target('first', cpos_x=0.5, cpos_y=0.25) # this would refer to hero at (0.5, 0.25s)

            *IMPORTANT* if you use 'ETIENNE' as hero:
            You need to *manually* update targeting status of 'zone' (i.e. Zone Control) after Etienne hits level 12. 
            Currently, bot has no way to track hero xp, and when etienne hits lvl 12, he will automatically change
            in-game targeting to Zone Control. But bot has no idea this has happened so it has either 'first' or 'd&q' 
            set as targeting priority. Now, if you never intend to change targeting, it doesn't really matter, but say 
            you wanted to change 'zone' back to 'first', but bot has currently status 'first': well, bot "does nothing" 
            because it sees it has already 'first' as priority. Or actually, bot will send an error, set current game 
            status as 'defeat' and return to main menu as soon as possible.

            So how to change targeting? You can't use 'target' as it would perform checks and takes the previous value 
            in account and uses it as a reference to get to new one. Instead, you type force_target():
            >>> Hero.current_plan_hero_name = 'quincy'
            >>> hero = Hero(0.4, 0.5)
            Placing Hero... Hero placed.
            >>> hero.force_target()
            Nothing was changed.
            >>> hero.sell()
            Hero sold!

            >>> Hero.current_plan_hero_name = 'etienne'
            >>> hero = Hero(0.4, 0.5)
            Placing Hero... Hero placed.
            >>> hero.force_target()
            Etienne targeting prio set to 'zone' to match in-game prio.
            >>> hero.sell()
            Hero sold!

            Do not use this force_target in any other situation.            
        """
        if Rounds.defeat_status:
            return
        val = self._change_hero_target(set_target.lower(), x, y, cpos_x, cpos_y)
        if val != 'OK':
            self._error('target', set_target, val)
        kb_mouse.press_esc()
        self._targeting = set_target.lower()

    '''
    def geraldo_shop(self, item, pos_x: float | None, pos_y: float | None) -> None:
        """UNFINISHED -- Implements Geraldo's shop item placement.
        

        """
        if Rounds.defeat_status:
            return
        elif self._hero_name == 'geraldo':
            None

    def corvus_spell(self, spells) -> None:
        """UNFINISHED -- Implements Corvus's spells.
        

        """
        if Rounds.defeat_status:
            return
        elif self._hero_name == 'corvus':
            None
    '''