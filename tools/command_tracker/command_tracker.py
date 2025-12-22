"""Saves inserted data into a text file.

Can easily save create valid commands which can be copy-pasted into actual plans files.

---Works only with fullscreen 16:9 aspect ratio resolutions with game on main monitor---

>How to use:
-pressing right mouse allows adding commands to commands.txt:
 >current mouse location is saved with right click
 >then you need to input a command and possible args
 >then press enter to save a nicely formatted command string, assuming you gave correct arguments
 --type nothing and press enter in case you pressed right mouse accidentally
-pressing '+' will add a starting row for next rounds inputs. Round number follows ct_round_counter so you can change
 its starting value
-pressing 'f8' will exit program; adds vertical ellipsis (triple vertical dots) to text file after exiting to separate
 previous runtime commands.

Note: coordinates increase right on x-axis and down on y-axis.
-So main monitor's upper left corner is (0,0) and down right corner is (x_res-1, y_res-1). Then 1920x1080 would have
(1919, 1079) as max coordinate.
-If you have multiple monitors, coordinates extend below/above of your max res if you move them outside main monitor
-So it's easy to identify if you saved valid coordinates: they will have a non-negative x-coordinate within your 
 resolution e.g. with 1920x1080, x < 0 is invalid and so is x > 1919.
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

ACCURACY = 13
WIDTH, HEIGHT = pyautogui.size()

def scalar_position(real_x: int, real_y: int) -> tuple[float, float]:
    """Float numbers have quite a lot of decimals so we round them up a bit.

    Args:
        real_x: Pixel x-coordinate.
        real_y: Pixel y-coordinate.
        
    Returns:
        scalar_x, scalar_y: Coordinates in scalar form.
    """
    ACCURACY = 13
    scalar_x, scalar_y = round(real_x / WIDTH, ACCURACY), round(real_y / HEIGHT, ACCURACY)
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

    Declares ct_round_counter variable as global so it can be actually be updated instead of resetting back to original
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
            TrackerVals.coordinates_file.write(
                'elif current_round == '+ str(TrackerVals.ct_round_counter)+':\n')
            print('Current round is ' + str(TrackerVals.ct_round_counter))
    elif key_pressed == Key.pause:
        with open(pathlib.Path(__file__).parent/'commands.txt', 'w') as TrackerVals.coordinates_file:
            print("commands.txt contents flushed!")
    elif key_pressed == Key.f8:
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
    while True:
        try:
            start = input("Please input starting round (1-100).\n" \
                          "Other commands: 'delete' = delete commands.txt contents, 'exit' = exit script.\n"
                          "-> ")
            if start == 'exit':
                os.kill(os.getpid(), signal.SIGTERM)
            elif start == 'delete':
                with open(pathlib.Path(__file__).parent/'commands.txt', 'w') as _:
                    print("commands.txt contents deleted.")
            elif int(start) in range(1, 101):
                return int(start)
            else:
                print("Not a valid input")
        except ValueError:
            print("Not a valid input")

def add_command(comment_str: str) -> None:
    """Add command text to commands.txt."""
    cmd = comment_str.split()
    if len(cmd) == 0:
        print("Empty input")
        return
    x, y = str(TrackerVals.ct_x0), str(TrackerVals.ct_y0)
    match cmd[0]:
        case 'help':
            print("<Commands>\n"
                    "	-m: place a monkey\n"
                    "		args:\n" 
                    "		\tvar_name, name\n"
                    "   	\texample:\n"
                    "		 \t-p dart_name dart 0.1 0.5 => dart_name = Monkey('dart', 0.1, 0.5)\n\n"
                    "	-h: place a hero\n"
                    "    	\targs:\n"
                    "		\tvar_name\n"
                    "    	\texample:\n"
                    "        \t\t-h hero 0.1 0.5 => hero = Hero(0.1, 0.5)\n\n"
                    "	-u: upgrade a monkey\n"
                    "    	\targs:\n"
                    "  		\tvar_name, upgs_list\n"
                    "    	\texample:\n"  
                    "        \t\t-u dart_name ['1-0-0','2-0-0'] => dart_name.upgrade(['1-0-0','2-0-0'])\n"  
                    "       \t[Note] upgrade list must not contain spaces!\n\n"
                    "	-t: change targeting on monkey/hero\n"
                    "    	\targs:\n"
                    "	  	\tvar_name, target_str. Optional pos argument 'p' to add mouse location as target x,y\n"
                    "    	\texample:\n"
                    "    	 \t\t-t dart_name strong => dart_name.target('strong')\n"
                    "    	 \t\t-t dart_name strong p => dart_name.target('strong', x=0.1, y=0.1)\n\n"
                    "	-trobo: change targeting on robo monkey's second arm\n"
                    "    	\targs:\n"
                    "	  	\tvar_name, direction, clicks\n"
                    "    	\texample:\n"
                    "    	 \t\t-trobo super left 2 => super.target_robo('left', 2)\n"
                    "       \t[Note] will automatically add cpos_x, cpos_y; remember to remove those afterwards if they"
                    "               \t\t are not needed.\n\n"
                    "	-s: use special ability of monkey/hero\n"
                    "    	\targs:\n"
                    "		\tvar_name, special, x, y\n"
                    "    	\texample:\n"
                    "       \t\t\t-s dart_name 1, 0.1, 0.5 => dart_name.special(1, 0.1, 0.5)\n\n"
                    "	-ucp: upgrade a monkey by first updating its current position\n"
                    "    	\targs:\n"
                    "  		\tvar_name, upgs_list, cpos_x, cpos_y\n"
                    "   	\texample:\n"
                    "        \t\t-ucp dart_name ['1-0-0','2-0-0'] 0.5, 0.6\n"
					"			=> dart_name.upgrade(['1-0-0','2-0-0'], cpos_x=0.5, cpos_y=0.6)\n"
                    "       \t[Note] upgrade list must not contain spaces!\n\n"
                    "	-tcp: change targeting on monkey/hero by first updating its current position\n"
                    "    	\targs:\n"
                    "	 	\tvar_name, target_str, x, y.\n"
                    "    	\texample:\n"
                    "        \t\t-tcp dart_name first 0.5 0.6 (assuming mouse location is (0.1, 0.1))\n"
                    "			=> dart_name.target('first', x=0.5, y=0.6, cpos_x=0.1, cpos_y=0.1)\n\n"
                    "	-scp: use special ability of monkey/hero by first updating its current position\n"
                    "    	\targs:\n"
                    "  		\tvar_name, x, y, cpos_x, cpos_y\n"
                    "    	\texample:\n"
                    "        \t\t-scp dart_name 1 0.1 0.2 0.5 0.6\n"
                    "       	\t\t=> dart_name.upgrade(1, x=0.1, y=0.2, cpos_x=0.5, cpos_y=0.6)\n\n"
                    "	-c: general commands (not monkey/hero specific)\n"
                    "    	\t-this just writes the text you type. Used for general commands such as\n"
                    "        \tbegin()/begin('normal')\n" 
                    "        \tchange_autostart()\n" 
                    "        \tend_round(20)\n" 
                    "        \tability(1,5)\n"
                    "        \twait(3)\n"
                    "	-l: coordinate location (x,y)\n"
                    "    	\t-can be used with 'click' command, for example.\n"
					"\n"
                    "--typing anything else as first argument does nothing.\n")
            return
        case '-m':
            if len(cmd[1:]) < 2:
                print("Need 2 args: var_name, name")
                return
            TrackerVals.coordinates_file.write('    '+cmd[1]+" = Monkey('"+cmd[2]+"', "+x+", "+y+")\n")
            print("-> "+cmd[1]+" = Monkey('"+cmd[2]+"', "+x+", "+y+")", end='')
        case '-h':
            if len(cmd[1:]) < 1:
                print("Need 1 arg: var_name")
                return
            TrackerVals.coordinates_file.write('    '+cmd[1]+" = Hero("+x+", "+y+")\n")
            print("-> "+cmd[1]+" = Hero("+x+", "+y+")", end='')
        case '-u':
            if len(cmd[1:]) < 2:
                print("Need 2 args: var_name, upgrades_list")
                return
            TrackerVals.coordinates_file.write('    '+cmd[1]+".upgrade("+cmd[2]+")\n")
            print("-> "+cmd[1]+".upgrade("+cmd[2]+")", end='')
        case '-t':
            if len(cmd[1:]) < 2:
                print("Need 2: var_name, target_str")
                return
            if len(cmd[1:]) == 3 and cmd[3] == 'p':
                TrackerVals.coordinates_file.write('    '+cmd[1]+".target('"+cmd[2]+"', x="+x+", y="+y+")\n")
                print("-> "+cmd[1]+".target('"+cmd[2]+"', x="+x+", y="+y+")", end='')
            else:
                TrackerVals.coordinates_file.write('    '+cmd[1]+".target('"+cmd[2]+"')\n")
                print("-> "+cmd[1]+".target('"+cmd[2]+"')", end='')
        case '-trobo':
            if len(cmd[1:]) < 2:
                print("Need 3 args: var_name, direction, clicks")
                return
            TrackerVals.coordinates_file.write(
                '    '+cmd[1]+".target_robo('"+cmd[2]+"', "+cmd[3]+", cpos_x="+x+", cpos_y="+y+")\n")
            print(
                "-> "+cmd[1]+".target_robo('"+cmd[2]+"', "+cmd[3]+", cpos_x="+x+", cpos_y="+y+")", end='')
        case '-s':
            if len(cmd[1:]) < 2:
                print("Need 2 args: var_name, special")
                return
            TrackerVals.coordinates_file.write('    '+cmd[1]+".special("+cmd[2]+", "+x+", "+y+")\n")
            print("-> "+cmd[1]+".special("+cmd[2]+", "+x+", "+y+")", end='')
        case '-ucp':
            if len(cmd[1:]) < 2:
                print("Need 2 args: var_name, upgrades_list")
                return
            TrackerVals.coordinates_file.write('    '+cmd[1]+".upgrade("+cmd[2]+", cpos_x="+x+", cpos_y="+y+")\n")
            print("-> "+cmd[1]+".upgrade("+cmd[2]+", cpos_x="+x+", cpos_y="+y+")", end='')
        case '-tcp':
            if len(cmd[1:]) < 4:
                print("Need 4 args: var_name, target_str, x, y")
                return
            TrackerVals.coordinates_file.write(
                '    '+cmd[1]+".target('"+cmd[2]+"', x="+cmd[3]+", y="+cmd[4]+", cpos_x="+x+", cpos_y="+y+")\n")
            print(
                "-> "+cmd[1]+".target('"+cmd[2]+"', x="+cmd[3]+", y="+cmd[4]+", cpos_x="+x+", cpos_y="+y+")", end='')
        case '-scp':
            if len(cmd[1:]) < 4:
                print("Need 4 args: var_name, special, x, y")
                return
            TrackerVals.coordinates_file.write(
                '    '+cmd[1]+".special("+cmd[2]+", x="+cmd[3]+", y="+cmd[4]+", cpos_x="+x+", cpos_y="+y+")\n")
            print(
                "-> "+cmd[1]+".special("+cmd[2]+", x="+cmd[3]+", y="+cmd[4]+", cpos_x="+x+", cpos_y="+y+")", end='')
        case '-c':
            if len(cmd[1:]) < 1:
                print("Need 1 arg: text_str")
                return
            TrackerVals.coordinates_file.write('    '+''.join(cmd[1:])+"\n")
            print("-> "+''.join(cmd[1:]), end='')
        case '-l':
            TrackerVals.coordinates_file.write(f'    ({x}, {y})\n')
            print(f"-> ({x}, {y})", end='')
        case _:
            print("--Nothing was added--")
            return
    print(" added to commands.txt")

def run_tracker() -> None:
    TrackerVals.ct_round_counter = begin_round()
    # creates two Listener thread objects. First listens to mouse clicks and second to keyboard inputs
    m_listener = pynput.mouse.Listener(on_click = mouse_tracker)
    m_listener.start()

    kb_listener = pynput.keyboard.Listener(on_press = keyboard_tracker)
    kb_listener.start()

    # prints first round message layout
    print('-------------------------')
    print('Press right mouse to add commands text, "+" to change round, and f8 (or CTRL+C) to ' 
        'quit.')
    print("[All right-click commands]: help, -m, -h, -u, -t, -s, -ucp, -tcp, -scp, -c, -l")        
    with open(pathlib.Path(__file__).parent/'commands.txt', 'a') as TrackerVals.coordinates_file:
        TrackerVals.coordinates_file.write('if current_round == BEGIN:\n')
    print('Current round is ' + str(TrackerVals.ct_round_counter))

    # updates file during program runtime by opening it in append mode. 
    # Also writes down coordinates + optional user # comments in file commands.txt
    while True:
        time.sleep(0.2)
        TrackerVals.coordinates_file = open(pathlib.Path(__file__).parent/'commands.txt', 'a')
        if TrackerVals.ct_user_input == '<>':   # right mouse button identifier
            flush_input()
            comment_input = input('Insert command text --->')     # this input() is now part of main thread so it won't cause lag like it would if it were inside mouse_tracker
            add_command(comment_input)
            TrackerVals.ct_user_input = ''