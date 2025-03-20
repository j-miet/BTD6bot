#!python3
#update your hotkeys here; they are on the right side of colons (:). Left ones are the names and should be left untouched unless you know what you're doing
#normal character keys like letters, numbers and symbols can be inserted just by pressing that key and putting '' around them.
#for special keys, DON'T USE single quotations '' around them and write them in format Key.X where X is the key.
#X can be for example: esc, tab, ctrl, alt, space, backspace, page_up, page_down, F1, F2 etc.
#to see all of them, you can use documentation https://pynput.readthedocs.io/en/latest/keyboard.html#pynput.keyboard.Key

from pynput.keyboard import Key

hotkeys = {
    #monkeys + hero
    'dart_monkey' : 'q',
    'boomerang' : 'w',
    'bomb_shooter' : 'e',
    'tack_shooter' : 'r',
    'ice_monkey' : 't',
    'glue_gunner' : 'y',
    'sniper_monkey' : 'z',
    'monkey_sub' : 'x',
    'monkey_buccaneer' : 'c',
    'monkey_ace' : 'v',
    'heli_pilot' : 'b',
    'mortar_monkey' : 'n',
    'dartling_gunner' : 'm',
    'wizard_monkey' : 'a',
    'super_monkey' : 's',
    'ninja_monkey' : 'd',
    'alchemist' : 'f',
    'druid' : 'g',
    'mermonkey' : 'o',
    'banana_farm' : 'h',
    'spike_factory' :'j',
    'monkey_village' : 'k',
    'engineer_monkey' : 'l',
    'beast_handler' : 'i',
    'hero' : 'u',
    #upgrades; top, middle and bottom paths
    't' : ',',      #top
    'm' : '.',      #mid
    'b' : '-',      #bot
    #targetting
    'target_change' : Key.tab,
    'target_reverse' : '§',
    'special_1' : Key.page_down,
    'special_2' : Key.page_up,
    #other; not in use currently so you can leave them be
    'sell' : Key.backspace,
    'play' : Key.space,
    'send_round' : '+',
    #abilities
    'a1' : '1',
    'a2' : '2',
    'a3' : '3',
    'a4' : '4',
    'a5' : '5',
    'a6' : '6',
    'a7' : '7',
    'a8' : '8',
    'a9' : '9',
    'a10' : '0'
    }