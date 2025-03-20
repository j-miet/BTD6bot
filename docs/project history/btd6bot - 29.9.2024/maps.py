#!python3
#module that chooses rounds based on difficulty and game mode, and then chooses correct to start
#List all map modules here

from Maps import monkey_meadow
from Maps import dark_castle


# returns sbegin and end rounds of given difficulty+game mode combination
def get_rounds(difficulty, gamemode):
    if difficulty == 'EASY':
        match gamemode:
            case 'STANDARD' | 'PRIMARY':
                return 1, 40
            case 'DEFLATION':
                return 31, 60
    elif difficulty == 'MEDIUM':
                return 1, 60
    elif difficulty == 'HARD':
        match gamemode:
            case 'STANDARD' | 'MAGIC' | 'DOUBLE_HP' | 'HALF_CASH' | 'ALTERNATE':
                return 3, 80
            case 'IMPOPPABLE' | 'CHIMPS':
                return 6, 100

#print map info before starting
def map_print(map, diff, mode):
    print('-'*(6 + len(map)) +'\n' 
          f'>Map: {map[0] + map[1:].replace('_', ' ').lower()}\n'
          f'>Difficulty: {diff[0] + diff[1:].lower()}\n'
          f'>Mode: {mode[0] + mode[1:].lower()}\n')

#fetches begin and end rounds for given difficulty & game mode, then matches to correct map module and executes this
def playmap(map, diff, mode):
    begin, end = get_rounds(diff, mode)
    map_print(map, diff, mode)
    info = (map, diff, mode, begin, end)
    match map:
        case 'MONKEY_MEADOW':
            monkey_meadow.play(info)
        case 'DARK_CASTLE':
            dark_castle.play(info)