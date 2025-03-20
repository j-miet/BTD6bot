#!python3
# DEV TOOL: used in getting coordinates for BTD6bot-project
# Tracks mouse coordinates (pixels) and allows saving coordinates with a commenct into a text file.
# Uses external pyautogui, pynput modules to read/input keyboard and mouse commands. The latter offers simultaneous inputting listening via multithreading
# note: 
# program was first implemented using pyautogui which is much simpler than pynput. For example, pyautogui doesn't have any input listening modules
# all mouse and keyboard commands in this script could be implemented with just pynput instead. 
# pyautogui does have size() method to return screen resolution which isn't found within pynput, so I decided to keep it and rest of the previous code implemented through it

"""
How to use:

pressing '-' will add current mouse coordinates + comments; just remember to wipe the possible random text from input before writing your comment
 -this should only occur on the first round, afterwards the flush.input() should take care of it
pressing '+' will add a starting row for next rounds inputs
 -round number follows round_counter, initially printing automatically first value, then increments of 1
pressing 'Esc' will exit program
 -adds vertical ellipsis i.e. triple vertical dots after exiting to separate previous runtime text on BTD6coordinates.txt 
pressing anything else will notify the user of entering invalid inputs.

Note: coordinates increase right on x-axis and down on y-axis.
So main monitor's upper left corner is (0,0) and down right corner (x-res -1, y-res -1). So e.g. 1920x1080 would have (1919, 1079) as max coordinate
If you have multiple monitors, coordinates extend below/above of your max res if you move them outside main monitor
"""
import msvcrt
import os
import signal
import time

import pyautogui
import pynput

#global variables
ct_round_counter = 6        # first round, change this depending on which game mode you're planning the strategy for
ct_user_input = ''
ct_position_string = ''
ct_x0 = -1
ct_y0 = -1

#sets working directory to whatever location this script is run from
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

print('Press "Enter" to update coordinates. Press Ctrl-C OR *write* "Exit" to quit.')
coord = open('BTD6coordinates.txt', 'a')   # to save and read coordinates + comments. File is found in root folder of program.                        
coord.write('-'*15 + ' round: ' + str(ct_round_counter) + '-'*15 + '\n')
print('Current round is ' + str(ct_round_counter))

width, height = pyautogui.size()


# scales resolution for user. Coordinates will be now universally scaled from 0 to 1 instead of fixed resolution.
# float have quite a lot of decimals so we round them up a bit
def scalar_position(real_x, real_y):
    scalar_x, scalar_y = round(real_x / width, 13), round(real_y / height, 13)
    return scalar_x, scalar_y

# flush extra input symbol from key presses so when adding a comment by pressing '-', you can just write without needing always to delete extra inputs
def flush_input():
    while msvcrt.kbhit():
        msvcrt.getch()

# checks if user presses left mouse button. If True, updates global variables ct_x0, ct_y0 with mouse's clicking location coordinates
def mouse_tracker(x ,y, button, pressed):
    global ct_x0
    global ct_y0
    if pressed == True and button == pynput.mouse.Button.right:
        ct_x0, ct_y0 = scalar_position(int(x), int(y))

# prints and saves coordinates to a file, also updates the during runtime. 
# Press '+' to add text row indicating round change, '-' to add comment to current coordinate, and 'Esc' to exit program.
# declares ct_round_counter variable as global so it can be actually be updated instead of reseting back to original value
# declares ct_user_input as global so it can be used outside the listener-thread; using it inside listener will interfere it's input, slowing it down significantly
# finally, declares also ct_user_input as global so we can inform the input() function outside this listener-thread when wanting to input comments
def keyboard_tracker(key_pressed):
    global ct_round_counter
    global ct_position_string
    global ct_user_input
    
    try:
        ct_position_string = str(ct_x0) + ', ' + str(ct_y0)
        if key_pressed.char == '+' and ct_user_input == '':     #pressing '+' will add a round separator inside BT6coordinates.txt                                                   
            ct_round_counter += 1
            coord.write('-'*15 + ' round: ' + str(ct_round_counter) + '-'*15 + '\n')
            print('Current round is ' + str(ct_round_counter))
        elif key_pressed.char == '<':       #if you press left-mouse, it updates coordinates. Then pressing '<' will write down these coordinates
            ct_user_input = '<'
    except AttributeError:
        if key_pressed == pynput.keyboard.Key.f10:                                                                         
            print('Closing...')
            coord.write('\n.\n.\n.')                    #separates previous program inputs in text file
            flush_input()
            os.kill(os.getpid(), signal.SIGTERM)        #terminates program after pressing 'Esc'

# creates two Listener-objects. First listens to mouse clicks in mouse_tracker and second keyboard inputs in keyboard_tracker
m_listener = pynput.mouse.Listener(on_click = mouse_tracker)
m_listener.start()

kb_listener = pynput.keyboard.Listener(on_press = keyboard_tracker)
kb_listener.start()

#updates file during program runtime. Also writes down coordinates + optional user comments in file BTD6coordinates.txt
while True:
    time.sleep(0.1)
    coord = open('BTD6coordinates.txt', 'a')
    if ct_user_input == '<':       #if user presses '-', will ask for user comment and adds it to the file. Then empties user_input to allow repeated use
        flush_input()
        comment_input = input('Insert comment --->   ')     #this input() is now part of main thread so it won't slow down as it would if it were inside mouse_tracker
        coord.write(ct_position_string.ljust(35) + ' | ' + comment_input + '\n')
        print('>Row inserted<')
        ct_user_input = ''
