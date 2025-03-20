#!python3
#bot for Bloons TD 6
#reads from an user-inputed file where to play automatically through a map with a specific strat and difficulty + game mode

#Imports are sorted in 3 groups: internal/build-in, installed/third-party, and local/custom
#They will always be separated with a single empty line like below. Order will always be from top to bottom: build-ins, installed, local

import time
import os
import signal

import pynput

import maps
import functions


#global variable, is used within choose_mode to select either single-map or multi-map configuration of program
typed_input = None

#checks mapping mode input and runs the correct one
def run_mode():
    if typed_input == 's':
        single_map()
    else:
        multi_map()

# implements the single-map mode i.e. the normal single map experience
def single_map():
    print('Choose map, difficulty and gamemode, separated with spaces. Possible inputs:\n')
    print(open('maplist.txt').read() + '\n-------------------------------------')
    while True:
        try:
            read_list = open('maplist.txt').readlines()     #creates a list of each row in maps.txt
            map_list = []
            for map in read_list:        #remove whitespace characters from each row
                map_list.append(map.strip())
            time.sleep(1)
            functions.flush_input()      #flushes existing input so input() doesn't contain previous key presses
            user = input('=>')               #asks user input
            input_list = map_list[map_list.index(user)].split()             #reads user input and finds matching index in maplist.txt, then splits each word into another list.
            #TODO: implement replay function: asks user to type 'r'/'R' for True, anything else for False. Have to add extra argument to playmap. For multi-map, just set it to 0 always 
            replay_input = input('Keep replaying same map? Type REPLAY if yes, otherwise press Enter\n'
                                 'Note that you have to terminate program manually (F10) to end this loop\n=>')
            functions.flush_input()
            if replay_input == 'REPLAY':
                while True:
                    maps.playmap(input_list[0], input_list[1] , input_list[2])
            else:
                time.sleep(8)
                maps.playmap(input_list[0], input_list[1] , input_list[2])
                print('==============================================================================\n'
                      'Back to choosing map. Remember that you can quit at any point by pressing F10\n'
                      '.\n.\n.\n'
                      'Choose map, difficulty and gamemode, separated with spaces. Possible inputs:\n')
                continue
        except ValueError:
            print('Invalid input')          #if no user input can be matches to maps.txt, try again

# implements the multi-map mode which runs sequence of maps stated inside custom_maplist.txt. Checks valid input from list of maps in maplist.txt
def multi_map():
    while True:
        try:
            all_maps = open('maplist.txt').readlines()
            allmap_list = []
            for map in all_maps:                                    #format list of all maps
                allmap_list.append(map.strip()) 

            read_list = open('custom_maplist.txt').readlines()
            map_list = []
            for map in read_list:                                   #format list of maps chosen by user
                map_list.append(map.strip())  

            for maps in map_list:                                   #loops over all maps in map_list.py from top to bottom
                input_list = allmap_list[allmap_list.index(maps)].split()
                start = time.time()
                maps.playmap(input_list[0], input_list[1], input_list[2])
                end = time.time()
                print('')
            return
        except ValueError:
            print('ERROR: map_list.txt has invalid input(s). Program will now close.')
            return

#refers to global variable typed_input and updates its value depending of chosen mode. Because choose_mode is set as Listener-object, it cannot be passed variables
#therefore the use of global variable is a reasonable choise here, especially since we don't change its values after this function call has finished
def choose_mode(key_pressed):
    global typed_input
    try:      
        if key_pressed.char == 's' or key_pressed.char == 'S':
            typed_input = 's'
            return False
        elif key_pressed.char == 'm' or key_pressed.char == 'M':
            typed_input = 'm'
            return False
        else:
            print('Invalid input')

    #handles input that don't equate to a symbol, such as Enter, Shift, Esc etc.
    except AttributeError:
        None

#halts program after all the keys defined under exit_hotkey are pressed at least once during runtime
#os.kill(pid, sig) sends a signal, specified in signal module, to a process pid where pid is the process id
#terminates the process unconditionally if sig has any other value than signal.CTRL_C_EVENT or signal.CTRL_BREAK_EVENT
#thus, code below sends a kill command to current program using its process id from os.getpid(), terminating all of it
def exit():
    print('Program closing...')
    os.kill(os.getpid(), signal.SIGTERM)

#starts the btd6Bot
def run_btd6bot():

    #Introduction message
    print('### Welcome to Btd6Bot!\n' +
          'Press \'S\' to run \'single map mode\' where you can play any *supported* map + difficulty + game mode combination\n' +
          'Press \'M\' for \'multi map mode\' where maps are read from the \'map_list.py\' file. You need to edit this file yourself!\n'+
          'TO EXIT AT ANY POINT --> press \'F10\' <--')

    # modifier keys are those that temporarily modify action of another key when both are pressed simultaneosly, like Shift, Ctrl, Alt etc.
    # will clear any pre-existing modifier key state and normalise modifiers with more than one keyboard button, say Ctrl
    # this is necessary for Hotkey-object implementation if one wants to utilize it throughout a Listener-object's lifetime, in this case allowing exiting program at any point
    def for_canonical(func):
        return lambda key: func(listener.canonical(key))

    # first creates a Hotkey-object that executes function exit after user presses all the required button at least once (and not necessarily at the same time) during its lifetime
    # then creates a Listener-object via threading which listens to key pressed during entire program runtime. Then Hotkey-object is passed to it through a modifier function
    # finally, listener will now 'listen' to exit() after its started
    exit_hotkey = pynput.keyboard.HotKey(pynput.keyboard.HotKey.parse('<f10>'), exit)
    listener = pynput.keyboard.Listener(on_press =  for_canonical(exit_hotkey.press))
    listener.start()

    # creates a blocking Listener-object: this will collect events and needs to be released before program can move out of function choose_mode
    # it's used solely to get user's mode choise - either 's'/'S' for basic single map running, or 'm'/'M' for multimap implementation
    with pynput.keyboard.Listener(on_press = choose_mode) as kb_listener:
        kb_listener.join()

    # this checks if value set to the global variable typed_input during choose_mode. Doesn't actually require the if-condition as keyBo 
    if typed_input != None:
        run_mode()