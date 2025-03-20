#!python3

import sys

import btd6_bot

sys.path.append('Maps')  #this is used to find map folder and its map modules. Otherwise interpreter can't find maps.py

# main program. In Python, not actually necessary.
def main():
    btd6_bot.run_btd6bot()

# Every time a program is executed, it sets a name variable __name__ equal to the starting module's name. So if a program is started from 'foo.py' then __name__ = 'foo'.
# This essentially means that code below will only run if it's executed from this file. And thus no program that imports this module can run it.
if __name__ == '__main__':
    main()