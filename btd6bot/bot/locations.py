import json
import pathlib
from typing import Any

from bot.bot_vars import BotVars

_DEFAULT_LOCATIONS: dict[str, Any] = {
    "CLICK": {
        "heroes": {
            "quincy": (0.0552083333333, 0.2018518518519),
            "gwen": (0.1338541666667, 0.2111111111111),
            "striker": (0.2192708333333, 0.2064814814815),
            "obyn": (0.0567708333333, 0.3777777777778),
            "silas": (0.134375, 0.387962962963),
            "benjamin": (0.2171875, 0.3916666666667),
            "pat": (0.0572916666667, 0.5648148148148),
            "churchill": (0.1401041666667, 0.5731481481481),
            "ezili": (0.2130208333333, 0.5787037037037),
            "rosalia": (0.0567708333333, 0.7546296296296),
            "etienne": (0.1354166666667, 0.75),
            "sauda": (0.2161458333333, 0.7453703703704),
            "adora": (0.0526041666667, 0.9157407407407),
            "brickell": (0.1307291666667, 0.9203703703704),
            "psi": (0.2104166666667, 0.9148148148148)
        },
        "heroes2": {
            "geraldo": (0.0541666666667, 0.835185185185266667),
            "corvus": (0.1507291666667, 0.8403703703704),
        },
        "menu": {
            "hero_window": (0.275, 0.8888888888889),
            "heroscreen_scroll": (0.1401041666667, 0.5731481481481),
            "hero_select": (0.5734375, 0.5592592592593),
            "menu_play": (0.5, 0.8657407407407),
            "search_map": (0.0395833333333, 0.1518518518519),
            "search_map_bar": (0.4338541666667, 0.0462962962963),
            "choose_map": (0.2817708333333, 0.3055555555556),
            "save_overwrite": (0.5984375, 0.6842592592593),
            "collection_event": (0.5, 0.63),
            "collection_continue": (0.4953125, 0.9240740740741),
            "collection_two_left": (0.4244791666667, 0.5074074074074),
            "collection_two_right": (0.5807291666667, 0.5092592592593),
            "collection_three_left": (0.3130208333333, 0.5027777777778),
            "collection_three_middle": (0.5015625, 0.5009259259259),
            "collection_three_right": (0.6911458333333, 0.4935185185185)
        },
        "difficulty": {
            "EASY": (0.3255208333333, 0.3814814814815),
            "MEDIUM": (0.5026041666667, 0.3833333333333),
            "HARD": (0.6744791666667, 0.3861111111111)
        },
        "modes": {
            "standard": (0.3276041666667, 0.5564814814815),
            "top_left": (0.5036458333333, 0.4259259259259),
            "top_middle": (0.6651041666667, 0.4425925925926),
            "top_right": (0.8348958333333, 0.4296296296296),
            "bottom_left": (0.503125, 0.7027777777778),
            "bottom_middle": (0.6682291666667, 0.6981481481481),
            "bottom_right": (0.8411458333333, 0.6990740740741)
        },
        "ingame": {
            "dragdrop": (0.4427083333333, 0.2777777777778),
            "nudge": (0.4458333333333, 0.412962962963),
            "autostart": (0.6697916666667, 0.2796296296296),
            "next_button": (0.5, 0.85),
            "home_button": (0.37, 0.78),
            "home_button2": (0.44, 0.78),
            "defeat_home_button": (0.33, 0.75),
            "defeat_home_button_first_round": (0.38, 0.75),
            "apopalypse_start": (0.5, 0.69),
            "target_leftpanel_leftarrow": (0.044, 0.294),
            "target_leftpanel_rightarrow": (0.185, 0.292),
            "target_rightpanel_leftarrow": (0.680, 0.292),
            "target_rightpanel_rightarrow": (0.822, 0.292)
        },
        "hero_left_menu": {
            "1": (0.0453125, 0.1712962962963),
            "2": (0.0932291666667, 0.1712962962963),
            "3": (0.1432291666667, 0.1712962962963),
            "4": (0.1901041666667, 0.1712962962963),
            "5": (0.0453125, 0.3268518518519),
            "6": (0.0932291666667, 0.3268518518519),
            "7": (0.1432291666667, 0.3268518518519),
            "8": (0.1901041666667, 0.3268518518519),
            "9": (0.0453125, 0.4638888888889),
            "10": (0.0932291666667, 0.4638888888889),
            "11": (0.1432291666667, 0.4638888888889),
            "12": (0.1901041666667, 0.4638888888889),
            "13": (0.0453125, 0.6101851851852),
            "14": (0.0932291666667, 0.6101851851852),
            "15": (0.1432291666667, 0.6101851851852),
            "16": (0.1901041666667, 0.6101851851852)
        },
        "hero_right_menu": {
            "1": (0.6817708333333, 0.175),
            "2": (0.7307291666667, 0.175),
            "3": (0.7786458333333, 0.175),
            "4": (0.8255208333333, 0.175),
            "5": (0.6817708333333, 0.325),
            "6": (0.7307291666667, 0.325),
            "7": (0.7786458333333, 0.325),
            "8": (0.8255208333333, 0.325),
            "9": (0.6817708333333, 0.4657407407407),
            "10": (0.7307291666667, 0.4657407407407),
            "11": (0.7786458333333, 0.4657407407407),
            "12": (0.8255208333333, 0.4657407407407),
            "13": (0.6817708333333, 0.6083333333333),
            "14": (0.7307291666667, 0.6083333333333),
            "15": (0.7786458333333, 0.6083333333333),
            "16": (0.8255208333333, 0.6083333333333)
        }
    },
    "TEXT": {
        "menu": {
            "menu_playtext": (0.4560416666667, 0.932962962963, 0.55875, 0.9914814814815),
            "map_searchtext": (0.4140625, 0.0203703703704, 0.4651041666667, 0.0537037037037),
            "collection_collect": (0.43, 0.59, 0.534375, 0.6453703703704)
        },    
        "ingame": {
            "current_round": (0.7181666666667, 0.027001, 0.8119791666667, 0.0685185185185),
            "upgrade_text": (0.875, 0.0175925925926, 0.9682291666667, 0.0638888888889),
            "next_text": (0.4364583333333, 0.8046296296296, 0.5526041666667, 0.8740740740741),
            "level_up": (0.4270833333333, 0.4907407407407, 0.5708333333333, 0.5648148148148),
            "defeat": (0.446875, 0.5361111111111, 0.5635416666667, 0.5712962962963),
            "right_panel_sell_location": (0.7808333333333, 0.8148148148148, 0.8380208333333, 0.8703703703704),
            "left_panel_sell_location": (0.141083333333, 0.808148148148, 0.1984375, 0.8638888888889),
            "top_upg_current_leftwindow": (0.0333333333333, 0.3696296296296, 0.121875, 0.462037037037),
            "top_upg_current_rightwindow": (0.6777083333333, 0.3696296296296, 0.7661458333333, 0.462037037037),
            "mid_upg_current_leftwindow": (0.0333333333333, 0.5122222222222, 0.121875, 0.5861111111111),
            "mid_upg_current_rightwindow": (0.6777083333333, 0.5122222222222, 0.7661458333333, 0.5861111111111),
            "bot_upg_current_leftwindow": (0.0333333333333, 0.6492592592593, 0.121875, 0.7231481481481),
            "bot_upg_current_rightwindow": (0.6777083333333, 0.6492592592593, 0.7661458333333, 0.7231481481481)
        }
    }
}
"""All default locations for 16:9 aspect ratio resolutions.

Locations are either 
- 2-tuples if position is a clickable, or
- 4-tuples if position refers to a text box where bot searches for a pre-specified text value. First two coordinates
point to top-left corner, next two to bottom-right corner.

*Do not modify these values*. Instead, modify corresponding values in _CUSTOM_LOCATIONS dictionary which will be used
when resolution shifting is enabled.

CLICK (2-tuple):
    heroes: All heroes which icons can be clicked immediately after entering hero panel.

    heroes2: Heroes which require scrolling down to access their icons.

    menu (Main menu):
        hero_window:
            Hero panel access.
        heroscreen_scroll:
            Mouse location where hero screen can be scrolled down to access more heroes.
        hero_select:
            Herp select button.
        menu_play:
            Menu play button.
        search_map:
            Map screen search button i.e. the looking glass icon. 
        search_map_bar:
            Map screen search bar.
        choose_map:
            Upper left map location. After searching any map, it appears at this same location.
        save_override:
            After selecting difficulty
        collection_event:
            Collection event collect button.
        collection_continue:
            Continue button to exit collection event screen.
        collection_two_left/collection_two_right/collection_three_left/collection_three_middle/collection_three_right:
            Collection event clickable insta monkey icons. 

    difficulty (Map difficulty menu buttons)

    modes (Map game mode menu buttons)       

    ingame (In-game click locations except hero menu panels):
        dragdrop:
            Drag & drop setting.
        nudge:
            Nudge mode setting.
        autostart:
            Autostart setting.
        next_button:
            Next button after a map is finished successfully.
        home_button:
            Default home button after a map is finished or defeat screen appears after first round.
        home_button2:
            Home button location if esc menu is opened, or during apopalypse mode win screen.
        defeat_home_button:
            Defeat screen home button.
        defeat_home_button_first_round:
            Defeat screen home button if it appears during first round.
        apopalypse_start:
            Apopalypse start button.
        target_leftpanel_leftarrow:
            After clicking an monkey and opening its info panel on the left (because monkey position on the right),
            targeting can be changed via arrows. This is the left arrow click location.
        target_leftpanel_rightarrow: 
            Same as above, but right arrow location.
        target_rightpanel_leftarrow:
            Same as left panel"s left arrow, but when panel opens on right.
        target_rightpanel_rightarrow:
            Panel on the right and right arrow.
        
    hero_left_menu (Hero utility panel button locations for Geraldo shop, Corvus spellbook etc., if panel opens on the  
        left => hero is placed on the right side of gameplay screen middle point).

    hero_right_menu (Same as above except if panel opens on right => hero placed on the left).      

TEXT (4-tuple):
    menu (Menu text boxes): 
        menu_playtext: 
            Start menu "Play" text.
        map_searchtext:
            Location of text "search" inside map search bar.
        collection_collect:
            Collect event "collect" button text.

    ingame (Text boxes during gameplay): 
        current_round:
            Current round text location with start and end round e.g. 6/100. 
        upgrade_text:
            In-game "Upgrade" text location; used for checking entering a map was successful.
        next_text:
            Next button text location.
        level_up:
            Level-up pop up message.
        defeat:
            Defeat screen.
        right_panel_sell_location:
            Sell button text location if monkey panel opens on right side. Used for checking successful placements.
        left_panel_sell_location:
            Sell button text location if monkey panel opens on left side. Used for checking successful placements.
        top_upg_current_leftwindow:
            Top upgrade path name if monkey upgrade window opens on the right (= monkey places on the left side of
            gameplay screen middle point).
        top_upg_current_rightwindow:
            Top upgrade path name if upgrade panel on right side.
        mid_upg_current_leftwindow:
            Middle upgrade path name if upgrade panel on left side.
        mid_upg_current_rightwindow:
            Middle upgrade path name if upgrade panel on right side.
        bot_upg_current_leftwindow:
            Bottom upgrade path name if upgrade panel on left side.
        bot_upg_current_rightwindow:
            Bottom upgrade path name if upgrade panel on right side.
"""

_custom_locations: dict[str, Any] = {}
"""Custom location values. These will be used instead of default values if in-game resolution shift is enabled.

Values should be recorded in the resolution you"re planning to use. In-game shift setting will disable
coordinate scaling for all TEXT values and only shifts CLICK positions.
"""

def update_customlocations(default_file: dict[str, Any] = _custom_locations) -> None:
    with open(pathlib.Path(__file__).parent.parent/'Files'/'custom_locations.json') as loc_file:
        locations: dict[str, Any] = json.load(loc_file)
    default_file.update(locations)

def get_click(category: str, value: str) -> Any:
    """Return a click location (2-tuple) from selected category dictionary.
    
    Args:
        category (str): A dictionary key
        value (str): Value of dictionary, a 2-tuple
    
    Returns:
        A 2-tuple value
    """
    if BotVars.ingame_res_enabled:
        return _custom_locations["CLICK"][category][value]
    else:
        return _DEFAULT_LOCATIONS["CLICK"][category][value]

def get_text(category: str, value: str) -> Any:
    """Return a text box location (4-tuple) from selected category dictionary.
    
    Args:
        category (str): A dictionary key
        value (str): Value of dictionary, a 4-tuple
    
    Returns:
        A 2-tuple value
    """
    if BotVars.ingame_res_enabled:
        return _custom_locations["TEXT"][category][value]
    else:
        return _DEFAULT_LOCATIONS["TEXT"][category][value]
    
def get_locationdict() -> dict[str, Any]:
    """Return entire dictionary of all click and text positions.
    
    If in-game resolution shift is enabled, a custom location dictionary is returned instead.

    Returns:
        Location dictionary
    """
    if BotVars.ingame_res_enabled:
        return _custom_locations
    else:
        return _DEFAULT_LOCATIONS

