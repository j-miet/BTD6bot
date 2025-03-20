#!python3
#Map: EXAMPLE_MAP

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
        #pre-game settings like hero and auto-starting map with correct settings. User needs to be in menu screen.
        hero_name = 'Sauda'
        functions.load(hero_name, map, diff, mode)
            
        while True:
            while functions.check_round(current_round):   # Checks current round with image matching.
                sleep(0.5)
            '''''''''''''''''''''''Rounds start here'''''''''''''''''''''''
            #------ First round ------#
            if current_round == begin:


            ###### START (MUST BE INCLUDED AT END OF FIRST ROUND!)
                functions.start_round()
            ######
            #------ Final Round ------#
            elif current_round == end:


            ###### EXIT (THIS HAS TO BE INCLUDED AT THE END OF FINAL ROUND)   
                functions.return_menu()
                return
            ######
            '''''''''''''''''''''''Rounds end here'''''''''''''''''''''''
            ###### ROUND COUNTER (HAS TO BE INCLUDED HERE)
            sleep(1) #downtime after a round to ensure commands don't overlap
            current_round += 1
            ######


#--------------------------------------------------------------------------------------
    '''PRIMARY'''

    
#--------------------------------------------------------------------------------------
    '''DEFLATION'''

 
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