#!python3
#Map: Monkey Meadow

from time import sleep

'''Don't mind interpreter warning about unresolved imports.
Maps are located in a separate folder (= not project root Btd6Bot) so they cannot be accessed from this file's location.'''
import functions
from monkey import Monkey, Hero


#Plays map on specified settings
def play(info):

    map = info[0]
    diff = info[1]
    mode = info[2]
    begin = info[3]
    end = info[4]
    current_round = begin

##### EASY #####
#--------------------------------------------------------------------------------------
    '''STANDARD'''

    if (diff, mode) == ('EASY', 'STANDARD'): 
        hero_name = 'Sauda'
        functions.load(hero_name, map, diff, mode)
            
        while True:
            while functions.check_round(current_round):
                sleep(0.5)
            '''''''''''''''''''''''Rounds start here'''''''''''''''''''''''
            #------ First round ------#
            if current_round == begin:
                ninja1 = Monkey('Ninja', 0.33229, 0.48333)
                hero = Hero(hero_name, 0.05, 0.35)
                hero.change_target('Strong')
                dart1 = Monkey('Dart', 0.4651, 0.44167)
                dart1.change_target('Close')
            ###### START
                functions.start_round()
            ######
            elif current_round == 3:
                Monkey.use_ability('a1')           
                dart1.upgrade(['1-0-0'])
            elif current_round == 6: 
                ninja1.upgrade(['1-0-0'])
            elif current_round == 8:
                ninja1.upgrade(['2-0-0'])
                alch1 = Monkey('Alch', 0.25677, 0.47593)
            elif current_round == 10:
                ninja1.upgrade(['2-0-1'])
            elif current_round == 17:
                alch1.upgrade(['1-0-0', '2-0-0'])
            elif current_round == 20:
                ninja1.upgrade(['3-0-1'])
            elif current_round == 25:
                alch1.upgrade(['3-0-0'])
            elif current_round == 30:
                ninja1.upgrade(['4-0-1'])
            elif current_round == 35:
                alch1.upgrade(['3-1-0', '3-2-0'])
            elif current_round == 38:
                sniper1 = Monkey('Sniper', 0.76094, 0.30463)
                sniper1.change_target('Strong')
                sniper1.upgrade(['1-0-0', '2-0-0', '2-0-1', '2-0-2', '2-0-3'])
            #------ Final round ------#
            elif current_round == end:
                Monkey.use_ability('a1')
                sniper1.upgrade(['2-0-4'])

            ###### EXIT
                functions.return_menu()
                return
            ######
            '''''''''''''''''''''''Rounds end here'''''''''''''''''''''''
            ###### ROUND COUNTER
            sleep(1)
            current_round += 1
            ######


#--------------------------------------------------------------------------------------
    '''PRIMARY'''

    
#--------------------------------------------------------------------------------------
    '''DEFLATION'''

    if (diff, mode) == ('EASY', 'DEFLATION'): 
        hero_name = 'Quincy'
        functions.load(hero_name, map, diff, mode)
            
        while True:
            while functions.check_round(current_round):
                sleep(0.5)
            '''''''''''''''''''''''Rounds start here'''''''''''''''''''''''
            if current_round == begin:
                dart = Monkey('Dart', 0.4651, 0.44167)
                dart.upgrade(['0-0-1', '0-0-2', '0-0-3', '0-0-4', '0-0-5', '0-1-5', '0-2-5'])
            ###### START
                functions.start_round()
            ######

            #------ Final round ------#
            elif current_round == end:
 

            ###### EXIT
                functions.return_menu()
                return
            ######
            '''''''''''''''''''''''Rounds end here'''''''''''''''''''''''
            ###### ROUND COUNTER
            sleep(1)
            current_round += 1
            ######



####### MEDIUM ######
#--------------------------------------------------------------------------------------
    '''STANDARD'''

#--------------------------------------------------------------------------------------
    ''''MILITARY'''

#--------------------------------------------------------------------------------------
    '''REVERSE'''

#--------------------------------------------------------------------------------------
    '''APOPALYPSE'''




###### HARD ######
#--------------------------------------------------------------------------------------
    '''STANDARD'''

#--------------------------------------------------------------------------------------
    '''MAGIC'''

#--------------------------------------------------------------------------------------
    '''HALF_CASH'''

#--------------------------------------------------------------------------------------
    '''DOUBLE_HP'''

#--------------------------------------------------------------------------------------
    '''ALTERNATE'''

#--------------------------------------------------------------------------------------
    '''IMPOPPABLE'''

#--------------------------------------------------------------------------------------
    '''CHIMPS'''

    if (diff, mode) == ('HARD', 'CHIMPS'): 
        hero_name = 'Sauda'
        functions.load(hero_name, map, diff, mode)
            
        while True:
            while functions.check_round(current_round):
                sleep(0.5)
            '''''''''''''''''''''''Rounds start here'''''''''''''''''''''''
            if current_round == begin:
                hero = Hero(hero_name, 0.33229, 0.48333)
            ###### START
                functions.start_round()
            ######
            if current_round == 8:
                dart1 = Monkey('Dart', 0.4651, 0.44167)
        
            #------ Final round ------#
            elif current_round == end:
 

            ###### EXIT
                functions.return_menu()
                return
            ######
            '''''''''''''''''''''''Rounds end here'''''''''''''''''''''''
            ###### ROUND COUNTER
            sleep(1)
            current_round += 1
            ######
