"""Saves coordinate locations to a list with optional commenting.

Program was first implemented using pyautogui which is much simpler than pynput. For example, pyautogui doesn't have any
input listening modules. All mouse and keyboard commands in this script could be implemented with just pynput instead.
Pyautogui does have size() method to return screen resolution which isn't found within pynput, so I decided to keep all
of pyautogui stuff instead of rewriting them again with pynput.

>How to use:
-you should have 2 monitors: one has game open and this script on the second one so you see what's going on all the time
-pressing right mouse adds current mouse coordinates and also asks for user input. If you don't want to add comments, 
 just press Enter
-pressing '+' will add a starting row for next rounds inputs. Round number follows ct_round_counter so you can change
 its starting value
-pressing 'f8' will exit program; adds vertical ellipsis (triple vertical dots) to text file after exiting to separate
 previous runtime commands

Note: coordinates increase right on x-axis and down on y-axis.
-So main monitor's upper left corner is (0,0) and down right corner is (x_res-1, y_res-1). Then 1920x1080 would have
(1919, 1079) as max coordinate.
-If you have multiple monitors, coordinates extend below/above of your max res if you move them outside main monitor
-So it's easy to identify if you saved valid coordinates: they will have a non-negative x-coordinate. Not 100% how this
 works if you have 3 or more monitors.
"""

from io import TextIOWrapper
import pathlib
import msvcrt
import os
import signal
import time

import pyautogui
import pynput
from pynput.keyboard import Key, KeyCode
from pynput.mouse import Button

class TrackerVals:
    coordinates_file: TextIOWrapper
    ct_round_counter = 0
    ct_user_input = ''
    ct_position_string = ''
    ct_x0 = -1.0    # need to be floats so mypy type testing won't complain after scalar_position inserts float values.
    ct_y0 = -1.0

WIDTH, HEIGHT = pyautogui.size()

def scalar_position(real_x: int, real_y: int) -> tuple[float, float]:
    """Float numbers have quite a lot of decimals so we round them up a bit.

    Args:
        real_x: Pixel x-coordinate.
        real_y: Pixel y-coordinate.
        
    Returns:
        scalar_x, scalar_y: Coordinates in scalar form.
    """
    accuracy = 13
    scalar_x, scalar_y = round(real_x / WIDTH, accuracy), round(real_y / HEIGHT, accuracy)
    return scalar_x, scalar_y

def flush_input() -> None:
    """Used in flushing previous inputs: when user presses '+', the comment line will be empty."""
    while msvcrt.kbhit():
        msvcrt.getch()

def mouse_tracker(x: int, y: int, button: Button, pressed: bool) -> None:
    """Saves mouse coordinates when right mouse button is pressed.

    Args:
        x: Coordinate x-position
        y: Coordinate y-position
        button: Mouse button.
        pressed: Boolean, whether mouse button is pressed or not.
    """
    if pressed and button == Button.right:
        TrackerVals.ct_x0, TrackerVals.ct_y0 = scalar_position(x, y)
        TrackerVals.ct_user_input = '<>'

def keyboard_tracker(key_pressed: Key | KeyCode | None) -> None:
    """Keyboard input tracker.

    Declares ct_round_counter variable as global so it can be actually be updated instead of reseting back to original
    value. 
    Declares ct_user_input as global so it can be used outside the listener-thread; using it inside listener
    will interfere it's input, slowing it down significantly.
    Finally, declares ct_user_input as global so we can inform the input() function outside this listener-thread for
    comment inputs. 

    Args:
        key_pressed: Latest keyboard key pressed.
    """
    if isinstance(key_pressed, KeyCode):
        TrackerVals.ct_position_string = str(TrackerVals.ct_x0) + ', ' + str(TrackerVals.ct_y0)
        if key_pressed.char == '+' and TrackerVals.ct_user_input == '':                                    
            TrackerVals.ct_round_counter += 1
            TrackerVals.coordinates_file.write('-'*15 + ' round: ' + str(TrackerVals.ct_round_counter) + '-'*15 + '\n')
            print('Current round is ' + str(TrackerVals.ct_round_counter))
    else:
        if key_pressed == Key.f8:
            TrackerVals.coordinates_file.write('\n.\n.\n.\n')
            TrackerVals.coordinates_file.close()
            print('Closing...')                                                                       
            flush_input()
            os.kill(os.getpid(), signal.SIGTERM)

def begin_round() -> int:
    """Sets starting round.

    Returns:
        Start round number, an integer in range 1-100.
    """
    print("Type 'exit' to quit.\n--------------------")
    while True:
        try:
            start = input("Please input starting round (1-100): ")
            if start == 'exit':
                os.kill(os.getpid(), signal.SIGTERM)
            elif int(start) in range(1, 101):
                return int(start)
            else:
                print("Not a valid input")
        except ValueError:
            print("Not a valid input")

def run_tracker() -> None:
    TrackerVals.ct_round_counter = begin_round()
    # creates two Listener thread objects. First listens to mouse clicks and second to keyboard inputs
    m_listener = pynput.mouse.Listener(on_click = mouse_tracker)
    m_listener.start()

    kb_listener = pynput.keyboard.Listener(on_press = keyboard_tracker)
    kb_listener.start()

    # prints first round message layout
    print('Press right mouse to update coordinates with optional comments, "+" to change round, and f8 (or CTRL+C) to ' 
        'quit.')
    with open(pathlib.Path(__file__).parent / 'BTD6coordinates.txt', 'a') as TrackerVals.coordinates_file:
        TrackerVals.coordinates_file.write('-'*15 + ' round: ' + str(TrackerVals.ct_round_counter) + '-'*15 + '\n')
    print('Current round is ' + str(TrackerVals.ct_round_counter))

    # updates file during program runtime by opening it in append mode. 
    # Also writes down coordinates + optional user # comments in file BTD6coordinates.txt
    # don't write to file manually during this script's runtime! But you can open it on side and see how it updates, though!
    while True:
        time.sleep(0.2)
        TrackerVals.coordinates_file = open(pathlib.Path(__file__).parent / 'BTD6coordinates.txt', 'a')
        if TrackerVals.ct_user_input == '<>':   # right mouse button identifier
            flush_input()
            comment_input = input('Insert comment --->   ')     # this input() is now part of main thread so it won't slow 
                                                                # down like it would if it were inside mouse_tracker
            TrackerVals.coordinates_file.write(TrackerVals.ct_position_string.ljust(35) + ' | ' + comment_input + '\n')
            print('>Row inserted<')
            TrackerVals.ct_user_input = ''