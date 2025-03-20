#!python3
#Implements the Monkey class to allow placing and upgrading of towers

import time

import functions
from hotkeys import hotkeys


#Monkey class: creates all placeable towers and implements their functions & methods
class Monkey:
    ###Class, has to be accompanied with Monkey prefix

    """Functions"""
    #uses a specified ability hotkey
    def use_ability(a):
        functions.kb_input(hotkeys[a])

    #defines basic targetting behaviour of monkey
    #with Robo monkey, no hotkey for second hand so currently can't change its focus
    def basic_monkey_target(monkey):
        match monkey:
            case 'Tack':
                return None
            case 'Heli':
                return 'Follow'
            case 'Ace':
                return 'Circle'
            case 'Mortar':
                return None
            case 'Sub':
                return 'First'
            case 'Dartling':
                return 'Normal'
            case 'Spike':
                return 'Normal'
            case 'Farm':
                None
            case _:
                return 'First'

    #defines basic targetting behaviours of hero
    def basic_hero_target(hero):
        match hero:
            case 'Etienne':
                return 'D&Q'
            case 'Benjamin':
                return None
            case _:
                return 'First'

    ###Instance

    #initiates a monkey object
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.target = Monkey.basic_monkey_target(name)
        self.upg = '0-0-0'
        self.place()

    '''get'''
    #return monkey name; Hero, Dart, Sniper etc.
    def get_name(self):
        return self.name
    
    # return monkey location
    def get_pos_x(self):
        return self.pos_x
    def get_pos_y(self):
        return self.pos_y
    
    # returns current focus of monkey, for most towers this refers to First, Strong, Last or Close.
    def get_target(self):
        return self.target
    
    # returns current upgrade path
    def get_upg(self):
        return self.upg

    #return keyboard hotkey of given monkey type that can be used in pynput module
    def get_hotkey(self):
        match self.name:
            #Hero
            case 'Hero': return hotkeys['hero']
            #Primary
            case 'Dart': return hotkeys['dart_monkey']
            case 'Boomer': return hotkeys['boomerang']
            case 'Bomb': return hotkeys['bomb_shooter']
            case 'Tack': return hotkeys['tack_shooter']
            case 'Ice': return hotkeys['ice_monkey']
            case 'Glue': return hotkeys['glue_gunner']
            #Military
            case 'Sniper': return hotkeys['sniper_monkey']
            case 'Sub': return hotkeys['monkey_sub']
            case 'Boat': return hotkeys['monkey_buccaneer']
            case 'Ace': return hotkeys['monkey_ace']
            case 'Heli': return hotkeys['heli_pilot']
            case 'Mortar': return hotkeys['mortar_monkey']
            case 'Dartling': return hotkeys['dartling_gunner']
            #Magic
            case 'Wizard': return hotkeys['wizard_monkey']
            case 'Super': return hotkeys['super_monkey']
            case 'Ninja': return hotkeys['ninja_monkey']
            case 'Alch': return hotkeys['alchemist']
            case 'Druid': return hotkeys['druid']
            case 'Mermonkey': return hotkeys['mermonkey']
            #Support
            case 'Farm': return hotkeys['banana_farm']
            case 'Spike': return hotkeys['spike_factory']
            case 'Village': return hotkeys['monkey_village']
            case 'Engi': return hotkeys['engineer_monkey']
            case 'Beast': return hotkeys['beast_handler']
    
    '''set'''
    #sets monkey's target value
    def set_target(self, value):
        self.target = value

    #uses special target 1 button of current monkey and sets possible target location, if supported.
    #Examples: Almost all targetable/behaviour changing abilities:
    #heroes: ezili totem, geraldo shop
    #dartling, mortar, ace direction, heli lock-in, mermonkey mid path, at least 0-1-4 engi, beast handler* (read comments above special2)
    def special1(self, x=None, y=None):
        functions.click_away()
        functions.click(self.get_pos_x(), self.get_pos_y)
        functions.kb_input(hotkeys['special_1'])
        functions.click(x,y)

    #uses special button 2 of current monkey and sets possible target location, if supported.
    #Examples: beast handler* 
    # *BE VERY CAREFUL with beast handler inputs and pay attention which path is special1 and which special2)
    def special2(self, x=None, y=None):
        functions.click_away()
        functions.click(self.get_pos_x(), self.get_pos_y)
        functions.kb_input(hotkeys['special_2'])
        functions.click(x,y)

    #changes monkey's (non-hero) targetting
    #standard (First, Last, Close, Strong) and non-standard cases have been accounted for, even those unlocking after specific upgrades
    def change_target(self, target, pos_X=None, pos_Y=None):
        current = self.get_target()
        if current == target:
            if self.get_name() == 'Mortar':
                print(f'{self.name} is already \'Locked\', use {self.name}.special1(x,y) instead where x,y are your target coordinates')
            print(f'Already set to {target}')
            return
        functions.click(self.get_pos_x(), self.get_pos_y())   #choose correct monkey
        match self.name:
            case 'Tack':
                print(f'Not possible to change targetting of {self.name}')
            case 'Heli':    #follow is used as base value, otherwise follow or patrol points are unavailevable
                if target == 'Lock':
                    if current == 'Follow':
                        functions.kb_input(hotkeys['target_change'], 2)
                        self.special1(pos_X, pos_Y)
                    elif current == 'Pursuit':
                        functions.kb_input(hotkeys['target_change'], 2)
                        self.special1(pos_X, pos_Y)
                elif target == 'Pursuit':
                    if current == 'Follow':
                        functions.kb_input(hotkeys['target_change'], 1)
                    elif current == 'Lock':
                        functions.kb_input(hotkeys['target_reverse'], 2)
                else:
                    print(f'Target input for {self.name} is invalid.')
            case 'Ace':     #CENTERED PATH HAS NO HOTKEY (special1 changes flight direction) SO CHANGING IT'S LOCATION IS CURRENTLY UNAVAILEVABLE
                if target == 'Circle':
                    if current == 'Infinite':
                        functions.kb_input(hotkeys['target_change'], 1)
                    elif current == 'Eight':
                        functions.kb_input(hotkeys['target_reverse'], 2)
                    elif current == 'Wingmonkey':
                        functions.kb_input(hotkeys['target_change'], 1)
                    elif current == 'Centered':
                        functions.kb_input(hotkeys['target_reverse'], 3)
                elif target == 'Infinite':
                    if current == 'Circle':
                        functions.kb_input(hotkeys['target_change'], 1)
                    elif current == 'Eight':
                        functions.kb_input(hotkeys['target_reverse'], 1)
                    elif current == 'Wingmonkey':
                        functions.kb_input(hotkeys['target_change'], 2)
                    elif current == 'Centered':
                        functions.kb_input(hotkeys['target_reverse'], 2)   
                elif target == 'Eight':
                    if current == 'Circle':
                        functions.kb_input(hotkeys['target_change'], 2)
                    elif current == 'Infinite':
                        functions.kb_input(hotkeys['target_change'], 1)
                    elif current == 'Wingmonkey':
                        functions.kb_input(hotkeys['target_change'], 3)
                    elif current == 'Centered':
                        functions.kb_input(hotkeys['target_reverse'], 1)
                elif target == 'Wingmonkey':
                    if current == 'Circle':
                        functions.kb_input(hotkeys['target_reverse'], 1)
                    elif current == 'Infinite':
                        functions.kb_input(hotkeys['target_reverse'], 2)
                    elif current == 'Eight':
                        functions.kb_input(hotkeys['target_reverse'], 3)
                    elif current == 'Centered':
                        functions.kb_input(hotkeys['target_change'], 1)
                elif target == 'Centered':
                    if current == 'Circle':
                        functions.kb_input(hotkeys['target_change'], 3)
                    elif current == 'Eight':
                        functions.kb_input(hotkeys['target_change'], 1)
                    elif current == 'Infinite':
                        functions.kb_input(hotkeys['target_change'], 1)
                    elif current == 'Wingmonkey':
                        functions.kb_input(hotkeys['target_reverse'], 1)
                else: 
                    print(f'Target input for {self.name} is invalid.')
            case 'Mortar':  #You can keep using change_target or alternatively the special1 method.
                if target == 'Set':
                    functions.kb_input(hotkeys['target_change'], 1)
                    functions.click(pos_X, pos_Y)
                    return      #keeps target value of Mortar as None
                else:
                    print(f'Target input for {self.name} is invalid.')
            case 'Spike':
                if target == 'Normal':
                    if current == 'Close':
                        functions.kb_input(hotkeys['target_reverse'], 1)
                    elif current == 'Far':
                        functions.kb_input(hotkeys['target_reverse'], 2)
                    elif current == 'Smart':
                        functions.kb_input(hotkeys['target_change'], 1)
                elif target == 'Close':
                    if current == 'Normal':
                        functions.kb_input(hotkeys['target_change'], 1)
                    elif current == 'Far':
                        functions.kb_input(hotkeys['target_reverse'], 1)
                    elif current == 'Smart':
                        functions.kb_input(hotkeys['target_change'], 2)
                elif target == 'Far':
                    if current == 'Close':
                        functions.kb_input(hotkeys['target_change'], 1)
                    elif current == 'Normal':
                        functions.kb_input(hotkeys['target_change'], 2)
                    elif current == 'Smart':
                        functions.kb_input(hotkeys['target_reverse'], 1)
                elif target == 'Smart':
                    if current == 'Close':
                        functions.kb_input(hotkeys['target_change'], 2)
                    elif current == 'Far':
                        functions.kb_input(hotkeys['target_change'], 1)
                    elif current == 'Normal':
                        functions.kb_input(hotkeys['target_reverse'], 1)
            case 'Dartling':    #you have to set dartling to 'Locked' initially. After you NEED TO use special1 instead e.g. Dartling.special1(x,y)
                if target == 'Locked':
                    functions.kb_input(hotkeys['target_change'], 1)
                    self.special1(pos_X, pos_Y)
                else:
                    print(f'Target input for {self.name} is invalid.')
            case 'Village':
                print(f'Not possible to change targetting of {self.name}')
            case _:
                self.normal_targetting(current, target)
        self.set_target(target)
        functions.click_away()      #closes upgrade window

    #updates monkey's upgrade path 
    def set_upg(self, value):
        self.upg = value 

    """General methods"""
    #wait till upgrade image is matched, then upgrade tower and send confirmation. Also updates monkey's upgrade path.
    def press_upgrade(self, upg, button):
        while functions.check_image(upg+'.png'):
            functions.kb_input(hotkeys[button])
            time.sleep(0.3)         #if problems with image recognition, increase this
        print('upgraded!')
        self.set_upg(upg)

    #most towers have the basic 4 targetting choises: First, Last, Close, and Strong. 
    #This method handles targetting change for such monkeys
    def normal_targetting(self, current, target):
        if target == 'First':
            if current == 'Last':
                functions.kb_input(hotkeys['target_reverse'], 1)
            elif current == 'Strong':
                functions.kb_input(hotkeys['target_change'], 1)
            elif current == 'Close':
                functions.kb_input(hotkeys['target_change'], 2)
        elif target == 'Last':
            if current == 'First':
                functions.kb_input(hotkeys['target_change'], 1)
            elif current == 'Strong':
                functions.kb_input(hotkeys['target_change'], 2)
            elif current == 'Close':
                functions.kb_input(hotkeys['target_reverse'], 1)
        elif target == 'Close':
            if current == 'First':
                functions.kb_input(hotkeys['target_reverse'], 2)
            elif current == 'Strong':
                functions.kb_input(hotkeys['target_reverse'], 1)
            elif current == 'Last':
                functions.kb_input(hotkeys['target_change'], 1)
        elif target == 'Strong':
            if current == 'First':
                functions.kb_input(hotkeys['target_reverse'], 1)
            elif current == 'Last':
                functions.kb_input(hotkeys['target_change'], 2)
            elif current == 'Close':
                functions.kb_input(hotkeys['target_change'], 1)
        else:
            print(f'Target input for {self.name} is invalid.')
            return
        print(f'Changed {self.get_name()} targetting to {target}')
                
    #places created monkey object. Checks if any tower has been placed at that location and keeps trying until it succesfully places tower
    #this helps a lot with placements as we no longer need to time tower placement
    def place(self):
        functions.kb_input(self.get_hotkey())
        functions.click(self.get_pos_x(), self.get_pos_y())
        functions.click(self.get_pos_x(), self.get_pos_y())
        time.sleep(0.3)
        while functions.check_image('sell_button.png'):
            functions.click_away()
            print(f'trying to place {self.get_name()}')
            functions.kb_input(self.get_hotkey())
            functions.click(self.get_pos_x(), self.get_pos_y())
            functions.click(self.get_pos_x(), self.get_pos_y())
            time.sleep(1)
        functions.click_away()        #clicks away after succesful placement
        print(f'{self.get_name()} succesfully placed')

    #upgrades monkey by first checking current upgrade path then matching it to next upgrade and choosing right hotkey to press
    #upgrades are passed as a list of strings which allows multiple upgrades with one method call
    #will also check if tower is heli and path leads to 'Pursuit' (2-x-x) or if it's ace and path leads to 'Centered' (x-x-2) as these will change targettin automatically
    def upgrade(self, upgrade_list : list):
        time.sleep(0.3)
        functions.click(self.get_pos_x(), self.get_pos_y())
        for upg in upgrade_list:
                u = self.get_upg()
                print(f'upgrading {self.name} {u} to {upg}...')              
                if upg == '0-0-1':
                    self.press_upgrade(upg, 'b')   
                elif upg == '0-0-2':
                    self.press_upgrade(upg, 'b')
                    if self.name == 'Ace':
                        self.set_target('Centered')
                elif upg == '0-0-3':
                    self.press_upgrade(upg, 'b')
                elif upg == '0-0-4':
                    self.press_upgrade(upg, 'b')   
                elif upg == '0-0-5':    
                    self.press_upgrade(upg, 'b')      
                elif upg == '0-1-0':
                    self.press_upgrade(upg, 'm')
                elif upg == '0-1-1':
                    if u == '0-1-0':
                        self.press_upgrade(upg, 'b')
                    elif u == '0-0-1':
                        self.press_upgrade(upg, 'm')
                elif upg == '0-1-2':
                    if u == '0-0-2':
                        self.press_upgrade(upg, 'm')
                    elif u == '0-1-1':
                        self.press_upgrade(upg, 'b')
                        if self.name == 'Ace':
                            self.set_target('Centered')
                elif upg == '0-1-3':
                    if u == '0-0-3':
                        self.press_upgrade(upg, 'm')
                    elif u == '0-1-2':
                        self.press_upgrade(upg, 'b')
                elif upg == '0-1-4':
                    if u == '0-0-4':
                        self.press_upgrade(upg, 'm')
                    elif u == '0-1-3':
                        self.press_upgrade(upg, 'b')   
                elif upg == '0-1-5':
                    if u == '0-1-4':
                        self.press_upgrade(upg, 'b')
                    elif u == '0-0-5':
                        self.press_upgrade(upg, 'm')
                elif upg == '0-2-0':
                    self.press_upgrade(upg, 'm')
                elif upg == '0-2-1':
                    if u == '0-1-1':
                        self.press_upgrade(upg, 'm')
                    elif u == '0-2-0':
                        self.press_upgrade(upg, 'b')
                elif upg == '0-2-2':
                    if u == '0-1-2':
                        self.press_upgrade(upg, 'm')
                    elif u == '0-2-1':
                        self.press_upgrade(upg, 'b')
                        if self.name == 'Ace':
                            self.set_target('Centered')
                elif upg == '0-2-3':
                    if u == '0-2-2':
                        self.press_upgrade(upg, 'b')
                    elif u == '0-1-3':
                        self.press_upgrade(upg, 'm')
                elif upg == '0-2-4':
                    if u == '0-1-4':
                        self.press_upgrade(upg, 'm')
                    elif u == '0-2-3':
                        self.press_upgrade(upg, 'b')
                elif upg == '0-2-5':
                    if u == '0-1-5':
                        self.press_upgrade(upg, 'm')
                    elif u == '0-2-4':
                        self.press_upgrade(upg, 'b')
                elif upg == '0-3-0':
                    self.press_upgrade(upg, 'm')
                elif upg == '0-3-1':
                    if u == '0-2-1':
                        self.press_upgrade(upg, 'm')
                    elif u == '0-3-0':
                        self.press_upgrade(upg, 'b')
                elif upg == '0-3-2':
                    if u == '0-3-1':
                        self.press_upgrade(upg, 'b')
                        if self.name == 'Ace':
                            self.set_target('Centered')
                    elif u == '0-2-2':
                        self.press_upgrade(upg, 'm')
                elif upg == '0-4-0':
                    self.press_upgrade(upg, 'm')
                elif upg == '0-4-1':
                    if u == '0-3-1':
                        self.press_upgrade(upg, 'm')
                    elif u == '0-4-0':
                        self.press_upgrade(upg, 'b')
                elif upg == '0-4-2':
                    if u == '0-4-1':
                        self.press_upgrade(upg, 'b')
                        if self.name == 'Ace':
                            self.set_target('Centered')
                    elif u == '0-3-2':
                        self.press_upgrade(upg, 'm')
                elif upg == '0-5-0':
                    self.press_upgrade(upg, 'm')
                elif upg == '0-5-1':
                    if u == '0-5-0':
                        self.press_upgrade(upg, 'b')
                    elif u == '0-4-1':
                        self.press_upgrade(upg, 'm')
                elif upg == '0-5-2':
                    if u == '0-4-2':
                        self.press_upgrade(upg, 'm')
                    elif u == '0-5-1':
                        self.press_upgrade(upg, 'b')
                        if self.name == 'Ace':
                            self.set_target('Centered')
                elif upg == '1-0-0':
                    self.press_upgrade(upg, 't')                   
                elif upg == '1-0-1':
                    if u == '1-0-0':
                        self.press_upgrade(upg, 'b')
                    elif u == '0-0-1':
                        self.press_upgrade(upg, 't')
                elif upg == '1-0-2':
                    if u == '0-0-2':
                        self.press_upgrade(upg, 't')
                    elif u == '1-0-1':
                        self.press_upgrade(upg, 'b')
                        if self.name == 'Ace':
                            self.set_target('Centered')
                elif upg == '1-0-3':
                    if u == '0-0-3':
                        self.press_upgrade(upg, 't')
                    elif u == '1-0-2':
                        self.press_upgrade(upg, 'b')
                elif upg == '1-0-4':
                    if u == '0-0-4':
                        self.press_upgrade(upg, 't')
                    elif u == '1-0-3':
                        self.press_upgrade(upg, 'b')
                elif upg == '1-0-5':
                    if u == '0-0-5':
                        self.press_upgrade(upg, 't')
                    elif u == '1-0-4':
                        self.press_upgrade(upg, 'b')
                elif upg == '1-1-0':
                    if u == '1-0-0':
                        self.press_upgrade(upg, 'm')
                    elif u == '0-1-0':
                        self.press_upgrade(upg, 't')
                elif upg == '1-2-0':
                    if u == '0-2-0':
                        self.press_upgrade(upg, 't')
                    elif u == '1-1-0':
                        self.press_upgrade(upg, 'm')
                elif upg == '1-3-0':
                    if u == '0-3-0':
                        self.press_upgrade(upg, 't')
                    elif u == '1-2-0':
                        self.press_upgrade(upg, 'm')
                elif upg == '1-4-0':
                    if u == '0-4-0':
                        self.press_upgrade(upg, 't')
                    elif u == '1-3-0':
                        self.press_upgrade(upg, 'm')
                elif upg == '1-5-0':
                    if u == '0-5-0':
                        self.press_upgrade(upg, 't')
                    elif u == '1-4-0':
                        self.press_upgrade(upg, 'm')
                elif upg == '2-0-0':
                    self.press_upgrade(upg, 't') 
                    if self.name == 'Heli':
                        self.set_target('Pursuit')
                elif upg == '2-0-1':
                    if u == '1-0-1': 
                        self.press_upgrade(upg, 't')   
                        if self.name == 'Heli':
                            self.set_target('Pursuit')                
                    elif u == '2-0-0': 
                        self.press_upgrade(upg, 'b')
                elif upg == '2-0-2':
                    if u == '2-0-1':
                        self.press_upgrade(upg, 'b')
                        if self.name == 'Ace':
                            self.set_target('Centered')
                    elif u == '1-0-2':
                        self.press_upgrade(upg, 't')
                        if self.name == 'Heli':
                            self.set_target('Pursuit')
                elif upg == '2-0-3':
                    if u == '2-0-2':
                        self.press_upgrade(upg, 'b')
                    elif u == '1-0-3':
                        self.press_upgrade(upg, 't')
                        if self.name == 'Heli':
                            self.set_target('Pursuit') 
                elif upg == '2-0-4':
                    if u == '1-0-4':
                        self.press_upgrade(upg, 't')
                        if self.name == 'Heli':
                            self.set_target('Pursuit')                
                    elif u == '2-0-3':
                        self.press_upgrade(upg, 'b')                  
                elif upg == '2-0-5':
                    if u == '1-0-5':
                        self.press_upgrade(upg, 't')
                        if self.name == 'Heli':
                            self.set_target('Pursuit') 
                elif upg == '2-1-0':
                    if u == '2-0-0':
                        self.press_upgrade(upg, 'm')
                    elif u == '1-1-0':
                        self.press_upgrade(upg, 't')
                        if self.name == 'Heli':
                            self.set_target('Pursuit') 
                elif upg == '2-2-0':
                    if u == '2-1-0':
                        self.press_upgrade(upg, 'm')
                    elif u == '1-2-0':
                        self.press_upgrade(upg, 't')
                        if self.name == 'Heli':
                            self.set_target('Pursuit') 
                elif upg == '2-3-0':
                    if u == '2-2-0':
                        self.press_upgrade(upg, 'm')
                    elif u == '1-3-0':
                        self.press_upgrade(upg, 't')
                        if self.name == 'Heli':
                            self.set_target('Pursuit') 
                elif upg == '2-4-0':
                    if u == '2-3-0':
                        self.press_upgrade(upg, 'm')
                    elif u == '1-4-0':
                        self.press_upgrade(upg, 't')
                        if self.name == 'Heli':
                            self.set_target('Pursuit') 
                elif upg == '2-5-0':
                    if u == '2-4-0':
                        self.press_upgrade(upg, 'm')
                    elif u == '1-5-0':
                        self.press_upgrade(upg, 't')
                        if self.name == 'Heli':
                            self.set_target('Pursuit') 
                elif upg == '3-0-0':
                    self.press_upgrade(upg, 't')
                elif upg == '3-0-1':
                    if u == '2-0-1': 
                        self.press_upgrade(upg, 't')
                    elif u == '3-0-0': 
                        self.press_upgrade(upg, 'b')
                elif upg == '3-0-2':
                    if u == '2-0-2':
                        self.press_upgrade(upg, 't')
                    elif u == '3-0-1':
                        self.press_upgrade(upg, 'b')
                        if self.name == 'Ace':
                            self.set_target('Centered')
                elif upg == '3-1-0':
                    if u == '3-0-0':
                        self.press_upgrade(upg, 'm')
                    elif u == '2-1-0':
                        self.press_upgrade(upg, 't')
                elif upg == '3-2-0':
                    if u == '3-1-0':
                        self.press_upgrade(upg, 'm')
                    elif u == '2-2-0':
                        self.press_upgrade(upg, 't')
                elif upg == '4-0-0':
                    self.press_upgrade(upg, 't') 
                elif upg == '4-0-1':
                    if u == '4-0-0':
                        self.press_upgrade(upg, 'b')
                    elif u == '3-0-1':
                        self.press_upgrade(upg, 't')
                elif upg == '4-0-2':
                    if u == '4-0-1':
                        self.press_upgrade(upg, 'b')
                        if self.name == 'Ace':
                            self.set_target('Centered')
                    elif u == '3-0-2':
                        self.press_upgrade(upg, 't')
                elif upg == '4-1-0':
                    if u == '4-0-0':
                        self.press_upgrade(upg, 'm')
                    elif u == '3-1-0':
                        self.press_upgrade(upg, 't')
                elif upg == '4-2-0':
                    if u == '4-1-0':
                        self.press_upgrade(upg, 'm')
                    elif u == '3-2-0':
                        self.press_upgrade(upg, 't')
                elif upg == '5-0-0':
                    self.press_upgrade(upg, 't')  
                elif upg == '5-0-1':
                    if u == '4-0-1':
                        self.press_upgrade(upg, 't')
                    elif u == '5-0-0':
                        self.press_upgrade(upg, 'b')
                elif upg == '5-0-2':
                    if u == '4-0-2':
                        self.press_upgrade(upg, 't')
                    elif u == '5-0-1':
                        self.press_upgrade(upg, 'b')
                        if self.name == 'Ace':
                            self.set_target('Centered')
                elif upg == '5-1-0':
                    if u == '5-0-0':
                        self.press_upgrade(upg, 'm')
                    elif u == '4-1-0':
                        self.press_upgrade(upg, 't')
                elif upg == '5-2-0':
                    if u == '4-1-0':
                        self.press_upgrade(upg, 'm')
                    elif u == '4-2-0':
                        self.press_upgrade(upg, 't')  
        ###
        time.sleep(0.3)                     #Sleep is used at the end so program has time to input upgrades
        functions.click_away()              #click away sso overlay doesn't block anything


#Hero class that is used in placing hero and contain hero-specific methods. Inherits the Monkey class.
class Hero(Monkey):

    #initiates a hero object
    def __init__(self, hero_name, pos_x, pos_y):
        self.name = 'Hero'
        self.hero_name = hero_name
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.target = Monkey.basic_hero_target(hero_name)
        self.upg = None
        self.place()

    '''set'''
    #changes hero's targetting
    def change_target(self, target):
        current = self.get_target()
        if target == current:
            print(f'Target already set to {target}')
            return
        functions.click(self.get_pos_x(), self.get_pos_y())   #choose correct monkey
        match self.hero_name:
            case 'Benjamin':
                print('Can\'t change targetting on Benjamin')
            case 'Etienne':         #Etienne switches to 'Zone' at lvl 12 - YOU NEED TO MANUALLY SET hero.set_target('Zone') at the round start
                if target == 'D&Q':
                    if current == 'First':
                        functions.kb_input(hotkeys['target_change'])
                    elif current == 'Zone':
                        functions.kb_input(hotkeys['target_reverse'])
                elif target == 'First':
                    if current == 'D&Q':
                        functions.kb_input(hotkeys['target_reverse'])
                    elif current == 'Zone':
                        functions.kb_input(hotkeys['target_change'])
                elif target == 'Zone':
                    if current == 'First':
                        functions.kb_input(hotkeys['target_reverse'])
                    elif current == 'D&Q':
                        functions.kb_input(hotkeys['target_change'])
            case _:
                self.normal_targetting(current, target)
        self.set_target(target)

    """General methods"""
    #TODO: Geraldo's ability to use shop. Give item and coordinates where to use item
    def shop(self, item, pos_x, pos_y):
        if self.hero_name == 'Geraldo':
            None

    #TODO: Corvus' spell usage. Takes a list of spells and casts them
    def spell(self, spells):
        if self.hero_name == 'Corvus':
            None
