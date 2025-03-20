#!python3
#Map: Dark Castle

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

#--------------------------------------------------------------------------------------
    '''PRIMARY'''

    
#--------------------------------------------------------------------------------------
    '''DEFLATION'''

    if (diff, mode) == ('EASY', 'DEFLATION'): 
        hero_name =  None
        functions.load(hero_name, map, diff, mode)
            
        while True:
            while functions.check_round(current_round):
                sleep(0.5)
            '''''''''''''''''''''''Rounds start here'''''''''''''''''''''''
            #------ First round ------#
            if current_round == begin:
                dart = Monkey('Dart', 0.7536458333333, 0.512962962963)
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