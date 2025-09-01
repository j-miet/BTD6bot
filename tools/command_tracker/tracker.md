# How to use:

1. open 'run.bat' or use .py file: this opens a command line interface
2. in the interface,
    - first, if your commands.txt file has previous contents and you'd wish to remove them, type delete and press enter
    - type the starting round of current plan:
	    - easy: 1
	    - deflation: 31
	    - medium: 1
	    - hard: 3
	    - impoppable & chimps: 6

    Press enter to confirm value
3. For general commands:
	- ``F8`` to quit. If for some reason this breaks, close the window manually/highlight it and press ctrl+c
    - ``+`` to increment round counter by 1. So if your current round is 10, after '+' it becomes 11

4. For round commands:
	1. first, you hover mouse at any location, then press right-click. This will store the location coordinate for possible use.
	2. then you type any of the commands:

		``help`` = to display help text

 		``-m`` = place a monkey at right click location.

		- Arguments: ``variable_name``, ``monkey_type``
		- Example => output:

		        -m dart1 dart => dart1 = Monkey('dart', x_pos, y_pos)
		        -m super_monkey super => super_monkey = Monkey('super', x_pos, y_pos)

		``-h`` = place hero at right click location. 

		- Arguments: ``variable_name``  
		- Example => output:

		        -h hero => hero = Hero(x_pos, y_pos)
		        -h quincy => quincy = Hero(x_pos, y_pos)

		``-u`` = upgrades a monkey

		- Arguments: ``variable_name``, ``upgrade_list``
		- Example => output:

				-u dart1 ['1-0-0'] => dart1.upgrade(['1-0-0'])
				-u sniper ['0-0-1','0-0-2','0-0-3','1-0-3'] => sniper.upgrade(['0-0-1','0-0-2','0-0-3','1-0-3'])

		``-t`` = change targeting of monkey/hero.

		- Arguments: ``variable_name``, ``targeting_value``. Optional argument ``p`` can be added to add target coordinates of your right click position

		- Example => output:

				-t dart1 close => dart1.target('close')
				-t heli lock p => heli.target('lock', x=x_pos, y=y_pos)
				-t spike smart => spike.target('smart')
				-t hero strong => hero.target('strong')

        ``-trobo``: change targeting of robo monkey 2. hand. Unlike default target command, robo monkey targeting must be handled "manually" e.g. by clicking the arrows left/right to select correct setting. In arguments, ``direction`` is left/right, ``clicks`` is how many times the left/right arrow is clicked. Args cpos_x, cpos_y are automatically added so **remember to remove those afterwards if they are not needed.**
        
        - Arguments: ``var_name``, ``direction``, ``clicks``
        - Example => output:

           	    -trobo super left 2 => super.target_robo('left', 2, cpos_x=x, cpos_y=y)


		``-s`` = use monkey's special ability. Ability target location is your right click location. **If the special doesn't require target location, remember to remove it manually afterwards!!!**
			
        - Arguments: ``variable_name``, ``special_number`` (either ``1`` or ``2``)
		- Example => output:

				-s hero 1 => hero.special(1, x_pos, y_pos)
				-s beast 2 => beast.special(2, x_pos, y_pos)

		``-c`` = save arbitrary text. Useful for writing ability uses and other general commands not tied to monkeys or heroes.

		- Arguments: ``text_string`` *without spaces*
		- Examples (outputs are exactly the same)

				ability(1)
				ability(2,5)
				click(0.5,0.5)
				forward(1)

		``-l`` = save right click coordinate location as a tuple. Useful if you need to add clicking location to interact with map elements.

		### Following commands are for maps with moving locations i.e. Geared/Sanctuary, but could also be useful in static maps.
		You could actually just use above commands, then save any locations with ``-l`` command and add these location as cpos_x, cpos_y
		- cpos_x, cpos_y will update monkey/hero location to cpos_x, cpos_y, then perform upgrade/target/special command at this location

		``-ucp`` = upgrade a monkey at right click location

		- Arguments: ``variable_name``, ``upgrade_list``
			Example => output:

				    -u dart1 ['5-0-0','5-1-0','5-2-0'] => dart1.upgrade(['5-0-0','5-1-0','5-2-0'], cpos_x=x_pos, cpos_y=y_pos)

		``-tcp`` = change targeting of monkey/hero at right click location. Unlike ``-t``, requires target x and y positions: **if you don't need these, just add arbitrary values like 0 0 and remember to remove them afterwards!!!**

		- Arguments: ``variable_name``, ``targeting_value``, ``target_x``, ``target_y``
		- Example => output:
        
				    -t dart1 first 0 0 => dart1.target('first', x=0, y=0, cpos_x=x_pos, cpos_y=y_pos)

		``-scp`` = use monkey's special ability; monkey location is updated to right click location. Target coordinates need to be added: **just like with targeting, add 0 0 as placeholder if not needed and remove afterwards!!!**

		- Arguments: variable_name, special_number, x, y
		- Example => output:

				    -s hero 1 0.5 0.25 => hero.special(1, x=0.5, y=0.25, cpos_x=x_pos, cpos_y=y_pos)

### General advice
- AVOID USING SPACES!	
    - For command arguments, don't use spaces inside an argument: spaces signal end of argument!
	 Examples:
	- For variable naming: don't use 

		    super monkey

	    use 

	 	    super_monkey 
        
	    instead. 

    - For upgrades, don't use 

		    ['1-0-0', '2-0-0']

 	    use 

		    ['1-0-0','2-0-0']

	    instead.

	- For arbitrary text with -c command like ability use, don't use

		    ability(1, 5)

	    use

		    ability(1,5)

	    instead

- Note that you can actually open ``commands.txt`` (the file where commands get saved) in a editor and edit stuff after commands.

  This way you can add/fix stuff live and not do it all after finishing the plan writing process.
  
  However, 
	*avoid writing to file manually when ``Insert command text --->`` is displayed*.
  This means file is in append mode and any added text will interfere with existing source because you are writing from 2 different sources. 
  So always make sure above text is not displayed, then edit the commands.txt, save changes to this file, then right click to add new command text.
