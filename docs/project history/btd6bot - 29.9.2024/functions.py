#!python3
# put all functions here that will be utilised in every map module (and possibly others as well), located inside Maps folder

import os
import time
import msvcrt

import pyautogui
import pynput
from pynput.keyboard import Key

from hotkeys import hotkeys

pyautogui.FAILSAFE = False #prevents build-in fail-safe of moving mouse to a corner of the screen
abspath = os.path.abspath(__file__)
path = os.path.dirname(abspath)
os.chdir(path)

width, height = pyautogui.size()    # screen resolution.
resolution = str(width)+'x'+str(height)
#constant list of all round images from 1 to 100, uses list comprehension to create list of strings 'rN.png' where N is round number
ROUND_NAMES = ['r'+str(i)+'.png' for i in range(1, 101)]

# fixed time interval used to allow inputs to register depending how fast PC you have or how fast game loads. Used in choose-functions within this module
def pause():
    time.sleep(0.2)

# flushes input flow so that key inputs from pynput-module don't stack in front of next input() call
def flush_input():
    while msvcrt.kbhit():
        msvcrt.getch()

# used to click to desired coordinate. Converts scalar coordinates to real coordinates to find position
def click(posX, posY):
    newX, newY = real_position(posX, posY)               # revert scalar coordinates to real coordinates
    pyautogui.moveTo(newX, newY)
    pyautogui.click(newX, newY)

#used to move cursor out of the way (bottom left) + closing any extra windows during gameplay.
def click_away():
    kb_input(Key.esc)
    click(0.01875, 0.9902777777778)

# simulates pressing a single keyboard input
def kb_input(input):
    keyboard = pynput.keyboard.Controller()
    keyboard.press(input)
    keyboard.release(input)

#repeats simulating a keypress multiple time, with small break in-between to allow them register
def kb_input(key, times):
    for t in range(times):
        kb_input(key)
        time.sleep(0.1)

# scales coordinate scalars back to actual coordinates of user's display resolution.
def real_position(x0, y0):
     x,y = round(width*x0), round(height*y0)
     return x,y

# double-clicks the start button for fast speed.
def start_round():
    click(0.95, 0.95)
    click(0.95, 0.95)

# return to main menu after game completion is variable 'Yes' is passed. Otherwise returns false which is ideal for multimapping
def return_menu():
    while check_image('Victory.png'):
        None
    print('Exiting map in...', end=' ')         #if multiple maps implemented, gives enough time to load menu screen.
    for t in range(3, 0, -1):
        print(str(t), end=' ', flush=True)
        time.sleep(1)  
    click(0.5, 0.85)         #exit to main menu
    time.sleep(1)
    click(0.37, 0.78)
    print('\nMap completed!')

# shecks if the image of given round number is recognised from screen. If no image is found, this means current round is still going and thus return False
def check_round(round_number):
    os.chdir('Images'+"//"+resolution)
    try:
        if pyautogui.locateOnScreen(ROUND_NAMES[round_number-1], confidence=0.85) != None:         # lower confidence well below 1 so that locateScreen finds the image
            os.chdir(path)
            return False
    except pyautogui.ImageNotFoundException:
        os.chdir(path)
        return True

#used in while loops to keep searching for image until it's found, only then break the loop, returning False
#checks if a png-image can be found on screen with a marginal of error (confidence). Image must be placed inside Images-folder
#image name is in string format e.g. 'testImage.png'
def check_image(image):
    os.chdir('Images'+"//"+resolution)
    try:
        if pyautogui.locateOnScreen(image, confidence=0.85) != None:
            os.chdir(path)
            return False
    except pyautogui.ImageNotFoundException:
        os.chdir(path)
        return True
   
#from menu screen, chooses a correct hero. Current implementation uses just mouse clicks. 
#Can also choose None so hero won't change - useful in modes like deflation where hero might not be necessary
def choose_hero(hero_name):
    click(0.309375, 0.8888888888889)
    pause()
    match hero_name:
        case None: print('No specific hero chosen for this map')
        case 'Quincy': click(0.0552083333333, 0.2018518518519)
        case 'Gwen': click(0.1338541666667, 0.2111111111111)
        case 'Striker': click(0.2192708333333, 0.2064814814815)
        case 'Obyn': click(0.0567708333333, 0.3777777777778)
        case 'Rosalia': click(0.134375, 0.387962962963)
        case 'Churchill': click(0.2171875, 0.3916666666667)
        case 'Benjamin': click(0.0572916666667, 0.5648148148148)
        case 'Pat': click(0.1401041666667, 0.5731481481481)
        case 'Ezili': click(0.2130208333333, 0.5787037037037)
        case 'Adora': click(0.0567708333333, 0.7546296296296)
        case 'Etienne': click(0.1354166666667, 0.75)
        case 'Sauda': click(0.2161458333333, 0.7453703703704)
        case 'Brickell': click(0.0526041666667, 0.9157407407407)
        case 'Psi': click(0.1307291666667, 0.9203703703704)
        case 'Geraldo': click(0.2104166666667, 0.9148148148148)
        case 'Corvus':
            m = pynput.mouse.Controller()
            pyautogui.moveTo(real_position(0.1401041666667, 0.5731481481481))   #moves cursor over hero selection screen
            for _ in range(0,4):      #scroll down to see Corvus portair. As more new heroes are released, need to extend this
                m.scroll(0, -1)
                time.sleep(0.1)
            click(0.0541666666667, 0.835185185185266667)
    pause()
    click(0.5734375, 0.5592592592593)
    pause()
    click(0.0411458333333, 0.0518518518519)

#from menu screen, presses play button and enters the map passed as variable
def choose_map(map_name):
    type_map = pynput.keyboard.Controller()
    map = map_name.replace('_', ' ')
    click(0.4359375, 0.8657407407407)   #press menu play button
    pause()
    click(0.0395833333333, 0.1518518518519) #press map search button
    pause()
    click(0.4338541666667, 0.0462962962963) #press map search bar
    pause()
    type_map.type(map)  #types map name in CAPS which doesn't matter
    pause()
    click(0.2817708333333, 0.3055555555556) #chooses the map
    pause()

#chooses right difficulty
def choose_diff(d):
    if d == 'EASY':
        click(0.3255208333333, 0.3814814814815)     #selects easy difficulty     
    elif d == 'MEDIUM':
        click(0.5026041666667, 0.3833333333333)     #selects medium difficulty
    elif d == 'HARD':
        click(0.6744791666667, 0.3861111111111)     #selects hard difficulty
    pause()

#chooses right game mode after difficulty is set
def choose_mode(m):
    if m == 'STANDARD':
        click(0.3276041666667, 0.5564814814815)
    elif m == 'PRIMARY' or m == 'MILITARY' or m == 'MAGIC':
        click(0.5036458333333, 0.4259259259259)
    elif m == 'DEFLATION' or m == 'APOPALYPSE' or m == 'DOUBLE_HP':
        click(0.6651041666667, 0.4425925925926)
    elif m == 'REVERSE' or m == 'ALTERNATE':
        click(0.503125, 0.7027777777778)
    elif m == 'HALF_CASH':
        click(0.8348958333333, 0.4296296296296)
    elif m == 'IMPOPPABLE':
        click(0.6682291666667, 0.6981481481481)
    elif m == 'CHIMPS':                                          
        click (0.8411458333333, 0.6990740740741)
    #if already existing save, overwrite it
    pause()
    click(0.5984375, 0.6842592592593)  

#sets up the map with correct hero and game mode settings
def load(hero, map, diff, mode):
    choose_hero(hero)      #this chooses both hero and saves name to a variable which needs to passed as variable when hero-object is created
    choose_map(map)
    choose_diff(diff)
    choose_mode(mode)
    #time.sleep(5)
    while check_image('GoButton.png'):  #checks if round start icon is found. If yes, click at middle to put it away
        time.sleep(0.5)
    time.sleep(0.5)
    click(0.5, 0.5)
    print('Starting in...', end=' ')
    for t in range(3, 0, -1):
        print(str(t), end=' ', flush=True)
        time.sleep(1)                                      #letting map to load, then clicks the OK button, click 'Ok'
    print('--> Bot running...')
    click(0.5015625, 0.7092592592593)       