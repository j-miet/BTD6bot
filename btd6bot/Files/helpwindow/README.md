# BTD6bot

![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/monitoring/monitoring_finish.PNG)


``BTD6bot`` is a program for automating **Bloons Tower Defense 6** game.  
It includes a simple graphical user interface (**gui**): not impressive visually, but easy to use.

**Supports only <u>single player game modes</u> accessed under the main menu &#39;Play&#39; button.**  
Support for multiplayer/competitive modes such as races, bosses, contested territory, boss rush, etc. will not be 
added.

Bot should be run on resolutions with **16:9** aspect ratio, with **fullscreen enabled**. 
However, it does support *windowed mode* and you can probably run it on any resolution where in-game actions are 
centered in a 16:9 area with some tricks which are explained later.
For example, with ``3440x1440``, the actual game screen area is ``2560x1440`` which has exactly 16:9 ratio.  

**If you have any questions or problems you can&39;t figure out, feel free to create a new issue on github.** 

---
**[Update status]  
Updated for Bloons TD 6 version ``48``**

**[OS support]  
Tested only on Windows operating systems**

**-- Warning --**  
***Be aware that automation/botting is againts Ninja Kiwi&#39;s [Terms of Service](https://ninjakiwi.com/terms) and
imposes the risk of flagging your account for cheating, or worst case, getting it banned.  
I&#39;m not certain how they could enforce this in single player environment, though. But if you&#39;re concerned,
you can always run the bot offline. <u>You have been warned</u>.***


## Table of contents

- [<u>Features</u>](#features)
- [<u>Installation</u>](#installation)
- [<u>First-time setup</u>](#first-time-setup)
    - [Quick tutorial](#quick-tutorial)
    - [Full tutorial](#full-tutorial)
        - [Update bot hotkeys](#update-bot-hotkeys)
        - [Settings: update resolution and enable ocr auto-adjust](#settings-update-resolution-and-enable-ocr-auto-adjust)
        - [Run the ocr adjusting process](#run-the-ocr-adjusting-process)
- [<u>GUI windows</u>](#gui-windows)
    - [Main](#main)
    - [Help](#help)
    - [Queue](#queue)
    - [Hotkeys](#hotkeys)
    - [Settings](#settings)
    - [Monitoring](#monitoring)
- [<u>Creating a new plan</u>](#creating-a-new-plan)
    - [Create a plan file](#create-a-plan-file)
    - [Commands](#commands)
        - [Monkeys](#monkeys)
        - [Heroes](#heroes)
        - [General](#general)
    - [Table: Monkeys, heroes and targeting options](#table-monkeys-heroes-and-targeting-options)
- [<u>Updating the bot</u>](#updating-the-bot)

# <u>Features</u>

- [Tested on update ``48``, ``1920x1080`` , ``fullscreen``]  
Plans for **all expert maps on chimps difficulty are included, making black medals obtainable.** Note that some maps
can include rng and you might need to retry them a few times.

- Graphical user interface, made with Python&#39;s build-in Tkinter library. Very simplified when it comes to visuals,
but easy to use. Here are some of the properties:

    - set bot hotkeys
    - change various settings: display resolution, windowed mode, auto-update in-game esc settings, and several more
    - run a single plan or customize a queue of plans
    - see info for currently selected plan if available
    - record round times and afterwards, check the time graph with &#39;Show plot&#39; button
    - see all the printed text bot produces during runtime inside the monitoring window, etc.
 
    For gui images and in-depth look on all features, see [GUI windows](#gui-windows) section.
 
- Support for creating custom plans files. Plans include all the commands bot performs on each round until a map 
finishes. 

    - Note that commands are Python code, so plan files are fully written in Python
 (= they are .py files).  
 In particular, monkeys and heroes are class objects because this makes implementing new 
 features for them much easier.  
 Commands are not very hard to write, but using them effortlessly can take time.
    - A plan template is provided which can then be copied and modified. Furthermore, the *command_tracker* tool is 
    specifically designed for plan creation.

    See [Creating a new plan file](#Creating_a_new_plan_file) section for more info.

- Extensive bot library with build-in gui support, which can also operate independently. Uses optical character reading
(ocr) and kb+mouse to update bot state.  
While library code is thoroughly documented, it still benefits from a short
guide. [Update the bot](#update-the-bot) section is devoted to this topic and provides the baseline for
adding new content.

# <u>Installation</u>
First you need to install [Python](https://www.python.org/downloads/).  
Most of bot was programmed in Python versions 3.12 and 3.13 so **Python 3.12+** is recommended.  
It is likely to work on earlier versions of Python 3, but this has not been tested.

Now, download *BTD6bot*:

Click the green [<> Code] button at the top of github page.

![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/github_codebutton.PNG)

Then either

- clone this repo to your local repository, or
- click &#39;Download ZIP&#39; and extract the contents

Next, the external dependencies. Install the following third party packages:

    easyocr==1.7.2
    markdown==3.8
    matplotlib==3.10.1
    numpy==2.2.3
    pillow==11.1.0
    pyautogui==0.9.54
    pynput==1.7.8
    pyperclip==1.9.0
    tkinterweb==4.3.1

Install them by going to your BTD6bot folder, then run ``reqs.bat``. 

If this isn&#39;t working: run cmd, change your current directory to ``<your path>/btd6bot`` where you installed
BTD6bot, then type
``
pip install -r requirements.txt
``

[Note] Exact version as listed above might not be required, but are always recommended. For pynput however, versions
above 1.7.8 cause a fatal error when any gui hotkeys are used.

And that&#39;s it! You&#39;re good to go and should be able to start BTD6bot. To test this, try one of the following:

- Open your BTD6bot folder, then run the ``run.bat`` file
- Open cmd, set current directory to ``<your path>/btd6bot`` then type ``py btd6bot ``


# <u>First-time setup</u>
| ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/main/main.PNG) |
|:--:|
| *Main window default view*|

If you managed to run BTD6bot, then the window similar to above should have opened.
There&#39;s plenty of stuff in here, but for now focus is on getting the bot to work properly.  
<u>Following steps must be done in order to make bot work properly for each user</u>:  

    1. Update bot hotkeys
    2. Settings: update resolution and enable ocr auto-adjust
    3. Run the ocr adjusting process

**Below is a quick tutorial of first-time setup. After it begins the full tutorial, which is detailed and quite long.**

[**Quick vs Full tutorial**]  
**If quick summary seems difficult to understand, or you think you got something wrong, just switch into full tutorial:   
<u>It&#39;s highly recommended you read through it at least once</u>.**

**Getting the bot to run properly is the hard part (which is not that hard).  
Afterwards, you&#39;re free to experiment with all the gui settings and if needed, can repeat first-time setup steps
should something break irrevocably.**


## Quick tutorial:

*1920x1080 monitor is used below; your values can look different*  
*1600x900 is used as custom resolution example* 

1. Set hotkeys in **Set hotkeys** window; gui hotkeys are not mandatory, but very much recommended. After you&#39;re
done, close hotkeys window.
2. Open **Settings** window and set resolution. 

    **Select a resolution with aspect ratio of 16:9 AND prefer fullscreen**.

    *However, it might be possible to use larger aspect ratios if you use fullscreen in-game, but set bot to use custom resolution and windowed mode in order to limit the area the bot sees; check [this](#using-windowed-mode-for-resolutions-with-varying-aspect-ratios) for more info*. 

    - If you use fullscreen/windowed fullscreen, **don&#39;t** enable custom resolution, or use windowed mode. Just leave it untoggled.

        ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/settings/disable_custom.PNG)

    - If you use custom resolution, set width & height values, then update values.
        - Toggle windowed mode on if you wish to use it. **It&#39;s recommended to always use fullscreen**, and use
        windowed mode only for *aspect ratios differing from 16:9*, as mentioned before.

        ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/settings/custom_windowed.PNG)

        **If windowed mode is enabled, you must run Btd6 with ``-popupwindow`` launch argument.** E.g. if you use Steam
        version:  
        library -> bloons td 6 -> right-click -> properties, then set the following

        ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/settings/launchoption.PNG)


3. Enable ocr auto-adjusting, make sure it has correct res and win values. Res is your current resolution, win stands
for fullscreen (``win=0``) or windowed (``win=1``).  
Finally, ``monkeys=all`` and ``delta=4`` values should be automatically set.  
Easiest way is to just press ``Reset args`` button once, then press ``Set args`` button after.

    ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/settings/auto_adjust.PNG)

    Now, close settings window. In main window, press **Initialize bot**, wait a bit for initialization, then press
    **Open bot window** to open monitoring window.
    
    Have your Btd6 game opened on main
    monitor, placed in main menu screen with ``Play`` button visible. Now, run the bot and let it finish auto-adjusting.
    This process can take a while.  
    After adjusting process is finished, bot should be able to detect in-game upgrade texts properly based on your
    current resolution settings.


    **<u>Know that any time you change resolution or windowed mode, you need to toggle the adjust setting on in settings
    and run this process again!</u>**.

    Finally, test if bot work by running a simple plan: close current monitoring window instance, then select either
    *dark_castleEasyStandard* or *monkey_meadowEasyStandard*.

    Then press ``Open bot window`` again to open fresh monitoring window and press ``Run``. Don&#39;t use keyboard or
    mouse while bot is running.  
    If bot can finish a plan and returns to main menu with "*Plan completed*" message, everything&#39;s working!

---
## Full tutorial


### Update bot hotkeys 

Open a game instance of bloons td 6.
Click the gear symbol and open hotkeys menu.

Now, update your game hotkeys for bot. Press &#39;Set hotkeys&#39; button in gui. Following window opens:

| ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/hotkeys/hotkeys.PNG) |
|:--:|
| *Hotkey window*|

Under &#39;Hotkeys&#39; label, there are two windows: top one is for game hotkeys, bottom for gui hotkeys. Game hotkeys
you simply copy from btd6, gui hotkeys you select freely.

You should quickly read the &#39;Instructions&#39; but here&#39;s the important parts:

- Not stated, but should be obvious: Do not use same hotkey for two actions
- You can scroll hotkey panel down (for example, there are abi)
- supported keys:
    - letters a-z, digits 0-9, other symbols like +, -, *, § etc.
    - numpad keys 0-9; these show up as <96> to <105>
    - modifier keys; these are displayed as Key.keyname e.g. Key.ctrl
- Some keys like § might get displayed weirdly but should still work
- Custom gui hotkeys:
    - &#39;pause&#39; queues up a pause flag. When bot hits it, it will press esc to pause game and also pauses bot. To
    unpause, press this button again.  
    Do not close the esc menu manually! Pausing only works in maps and does nothing when bot navigates menu screens
    - &#39;start-stop&#39; this start/stops the current bot loop. Stop will also reset the loop which means you need to
    start bot from main menu again.  
    And if you decide to run multiple plans in row, it will also reset this queue back to first plan.
    - &#39;exit&#39; stops BTD6bot entirely: it terminates current bot loop and closes all existing gui windows. Set
    this on a keybind that you don&#39;t press accidentally.

**To update a hotkey**

- click on any line so it becomes highlighted
- press &#39;Set hotkey&#39; button at the bottom
- &#39;Set hotkey&#39; button is now greyed out: press any supported keyboard key to update value
- you should now see the right side of &#39;=&#39; get updated

After you&#39;ve updated all the keys, close the hotkey window.

### Settings: update resolution and enable ocr auto-adjust

Next, open settings window by pressing &#39;Settings&#39; button.

| ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/settings/settings.PNG) |
|:--:|
| *Settings window*|

For now, only 3 settings are needed:

 - resolution (native or custom resolution)
 - windowed mode
 - auto-adjust ocr upgrade data the next time a plan is run

First the important part: **the base layout of Bloons is made for resolutions with aspect ratio of 16:9 or very close 
to it**.
For this reason, bot is also programmed around this requirement.  
Resolutions clearly differing from this are unlikely 
to work. The reason is that game will extend existing borders or even change the general ui layout 
(like text locations) for some aspect ratios.
  
Now, despite this, **it might be possible to run different resolutions, for example ultrawide resolutions, as long as
they don&#39;t change the relative positions of ui**.   
For such cases, you will probably need to do some tricks with
windowed mode enabled, even if you plan to play in fullscreen. 
Check [this part](#using-windowed-mode-for-resolutions-with-varying-aspect-ratios) for more detailed explanation.

Assuming you&#39;ve decided which resolution to use, you have two choices:

- *fullscreen/windowed fullscreen with native screen resolution*: if you toggle the &#39;Enable custom resolution&#39;
option off, you should see your current resolution next to &#39;Current resolution&#39; text.

    For example, if your monitor is ``1920x1080``, you see following 

    ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/settings/disable_custom.PNG)

    [**Note**] For bot, fullscreen and windowed fullscreen mean the same thing so always use this option if you wish to
    use maximum supported resolution.

- *custom resolution*: type width and height in their respective entry boxes, then click the &#39;Update resolution&#39;
button.  
Custom value is stored in a file and will be loaded back if you disable and re-enable this setting. 

    Example: if you have ``1920x1080`` as native res and set a custom res ``1600x900``, then toggling setting on and off
    would display following resolutions:

    ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/settings/difference.PNG)

    With custom resolutions, you can enable *windowed mode*.
    
    ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/settings/windowed.PNG)
    
    If you use windowed mode in btd6 normally, it adds the bar on top of game window. Bot, however, assumes this bar
    doesn&#39;t exist and requires game to be opened with ``-popupwindow`` option.  
    If you have Btd6 steam version, go to steam library, right click on Bloons TD 6, then simply add the argument like
    shown below

    ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/settings/launchoption.PNG)

    Using windowed mode can decrease the text quality for ocr, though. If you use significantly smaller resolution with
    windowed mode, bot could have issues with verifying text inputs.  
    If windowed causes issues, just use fullscreen instead.

Lastly, enable the &#39;Auto-adjust ocr upgrade data the next time a plan is run&#39; option. 
For 1920x1080 with fullscreen enabled, it looks like this:

![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/settings/auto_adjust.PNG)


It should include following parts, each separated by space:

 - ``res='width'x'height'``; where &#39;width&#39;, &#39;height&#39; are based on your own resolution,
 - ``win=0`` for fullscreen, ``win=1`` for windowed
 - ``monkeys=all``
 - ``delta=4``
 
You can press &#39;Reset args&#39; button once, if res and win values are not immediately updated. 

Then just press &#39;Set args&#39; and you&#39;re done! You may now close the settings window.


### Run the ocr adjusting process 


For last part, you need to enter the monitoring window. Click the &#39;Initialize bot&#39; button, located at bottom
right of main window:

![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/main/init_button.PNG)

Following load message appears

![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/main/load_msg.PNG)

Program needs to load the ocr model into your temporary memory (RAM) each time you initialize bot and is therefor only
required once per runtime loop. If you close the entire program and reopen it, the model must be loaded again.

After the message disappears, model has been loaded and initialize button should now display &#39;Open bot window&#39;
instead.

![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/main/openbotwin_button.PNG)

Click the button to open monitoring window.

| ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/monitoring/monitoring.PNG) |
|:--:|
| *Monitoring window*|

Monitoring window handles the running of bot and importantly, includes the big text window. All text prints get 
redirected into this window during bot runtime so you can have it on second monitor while main monitor is occupied by 
game itself.

Before we begin the adjusting, it&#39; would be a good time to explain why it&#39;s needed in first place. I would 
recommend to read it through once, but if you don&#39;t care, skip the following wall of text.

---

[**How does the upgrading system work**]


Most ocr strings the bot will see are static i.e. have always same text value, and are quite easy to detect. They are
used updating bot state and allowing it to make decision/execute commands. For certain commands, however, more 
complicated system are required to verify the input. 

The most complicated of these is the monkey upgrade system. In order to make upgrading to work properly, bot needs to
wait until upgrading becomes possible. The easy way to program this would be just say "when command is run, upgrade
monkey, don't check if it was succesful". But then user would need to time the upgrading exactly and this becomes
obviously annoying over time.

So better but more complicated way to implement this is to allow user to queue upgrade checks. Bot will just wait until
the upgrade flag is hit, then upgrade. But even then, there's a chance bot makes a mistake and upgrades too early or
might not upgrade at all. For this reason, upgrading process must

 - queue upgrades
 - perform upgrading process when asked to
 - verify the upgrade process was succesful

If it fails, it can either throw an error or keep trying again. The latter is how this bot works:

 - takes upgrade command
 - attemps to upgrade bot simply by pressing the right upgrade path hotkey
 - reads the current upgrade name, matches it with actual upgrade name, then   
   compares the difference of these strings and outputs a delta parameter.

    - if delta is over the threshold, upgrade was succesful
    - if delta was below the threshold, run the cycle again until above is true

This system is effective, but faces one problem: it uses same delta for ALL UPGRADES! Some upgrades might match easily,
others being more difficult (require high delta). And not only this (require low delta), if two concecutive upgrade 
paths are similarly named, like 'sharp shots' and 'razor sharp shots', they could be confused as same if delta is not
high enough. To solve this problem, current system uses <u>individual deltas for each monkey and upgrade path</u>. 

Process is now as follows: upgrade checks monkey name and desired upgrade path, say dart 5-x-x. It then gets the actual
string value for this path, 'ultra juggernaut' and corresponding delta, lets say 0.8. If the upgrade input text is
'ulta jugernaut', bot checks the following

 - actual string has 16 letters (spaces includes)
 - input string has 14/16 similar letters, in same order*
    *I don't know the exact implementation; it's a Python build-in system, but  
     it does something like this
 - 14/16 = 0.875 > 0.8, upgrade passes
 - however, exact delta value is avoided because some reading error could  
   change a few letters and then this becomes 12/16 = 0.75 < 0.8 = no match
 - to give room for some error, a delta value is substracted to lower this 
   exact value. From testing, substracting 0.04 from all deltas keeps good 
   accuracy. In settings, this value is written as delta=4: it lowers all 
   deltas by 4 units, where unit is 0.01. Valid deltas are 0-9 (which translate 
   to 0-0.09)

Above process is then repeated for all monkeys and all upgrade paths. It very loosely speaking 'trains' the bot to
detect valid upgrade thresholds. Then, when you run any plan file, it should have no issues with upgrading and mixing
inputs, thus working as intended.

Another thing you might be thinking of: Why not just use the cash value instead of upgrade names? Bot could just read
cash value, wait until cash is there, then upgrade a monkey. Well, this would actually be just fine to do, but for this
project:

 - cash values proved to be often inaccurate, especially on maps where 
   background had other elements like snow. With upgrade texts, background is 
   always the same.
 - upgrade costs would need to be updated in a separate file after each update. 
   This is not really a big deal, but adds one extra layer of active maintenance.

---

| ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/monitoring/monitoring_adjustbegin.PNG) |
|:--:|
| *After 'Run' button is pressed and menu play button is detected on main monitor, bot sets a countdown from 5 to 0, then begins the auto-adjusting process*|

Now, to complete the final step, you need to have your BTD6 game instance opened on your main monitor, placed at the
main menu screen. Then, press the &#39;Run&#39; button or use &#39;start-stop&#39; hotkey you set previously.

Text window gets updated: the text &#39;Ocr adjust mode enabled&#39; pops up and signals that bot will perform the
adjusting process. Bot is now active and is searching for the menu &#39;Play&#39; button text. After it finds it, ocr
adjusting may begin.

**During adjusting, do not use keyboard or mouse! Just wait until it&#39;s done.**

<u>What is delta adjusting:</u>

 1. bot automatically navigates to &#39;Spa pits&#39; map and enters it in sandbox mode
 2. goes over all the upgrades of listed monkeys, read their upgrade texts, check how closely they match to actual
    texts and save the obtained delta value. Because monkeys=all, it checks all monkeys.
 3. after it checks all listed monkeys once, it will check them again! This time it places them on opposite side of map.
    Why? Well, if you&#39;re never noticed, depending on which side of middle section you place a monkey 
    (left or right), the monkey panel opens on the opposite side of screen. Different sides can produce slighly
    different inputs so bot will analyze both sides and save all the deltas.
 4. After both sides are checked, both compares deltas of left and right side, selects the smaller value and save it as
    final delta.
 5. To finish things, all delta values are adjusted with equal amount. Default value is 4 i.e. delta=4: this adjust
    them by 4 units. An unit is 0.01 so with 4, bot substracts 0.04 from all values. This process is done to allow room
    for error. If delta=0, exact values are used, but then even a slightest error breaks the ocr process, and
    eventually, the bot.
 6. Process is now done and your upgrades_current.json file inside btd6bot/Files folder has been updated. Bot will also
    automatically disable the auto-adjust option from setting so if need to do this process again, enable it again
    manually.


| ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/monitoring/monitoring_adjustend.PNG) |
|:--:|
| *Adjusting process complete*|

And if everything worked, you should now have updated all delta values for your current monitor resolution. This means
your bot is ready to run!

To run your first plan, it&#39;s recommended to pick something simple. Close the monitoring window and select either
``[monkey meadow, easy-standard]`` or ``[dark castle, easy-standard]`` in main window:

![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/main/monkeymeadow.PNG)

or

![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/main/darkcastle.PNG)

Make sure you have the required hero, all monkeys and their upgrade paths unlocked. For upgrade paths:

- they follow the normal order of top-mid-bot e.g. ``sniper 2-0-4`` uses 2. top path and 4. bottom path upgrades
- they state **highest crosspaths required**. Therefore you sometimes see stuff like ``2-5-5 sniper`` listed which
simply means plan requires 2. top, 5. middle and 5. bottom paths. For example, such plan could use both ``2-0-5`` and
``0-5-2`` snipers, maybe even include a few ``0-3-2``&#39;s, too.  

Remember to scroll the info panel down to see all requirements!

Now reopen the monitoring window, have Btd6 menu screen opened, press run and just wait for bot to do its thing.
If you&#39;re able to finish a plan and bot can return to main menu automatically, everything&#39;s working!

**----- Full tutorial ends here -----**
-


# <u>GUI windows</u>
This section goes over all the gui windows and gives detailed explanations on each.

- Each window has fixed size and cannot be adjusted (dynamic window scaling might be implemented at some point, but no
promises)
- Gui interracts with ``Files`` folder. Don't change data values of these files by hand unless you know what you&#39;re
doing

    - only exception is the ``Files/map images``. Check sections for [Main](#main) or [Queue](#queue) for more info.


## Main

| ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/main/main_modified.PNG) |
|:--:|
| *Main window, with ocr already initialized. Currently selected plan is bloody_puddlesHardChimps, collection event and replay modes enabled.*|

- Responsible for running the program: if closed, entire program closes.
- Includes buttons for other windows (Help, Settings, Hotkeys, Queue, Monitoring)
- Includes drop-down lists of all maps and their respective available strategies. Displays info text for current plan
i.e. selected map + strategy combination. Info is stored in each plan file and can be freely customized.
- Has toggle buttons for
    - collection event mode: this will check if pop-up window appears after a plan is finished and collects the rewards
    - queue mode: loads all listed plans from queue mode maplist and plays them one after another
    - replay mode: replays current plan or queue of plans until bot is manually stopped. If used with queue of plans,
     plays all plans once, then start over again from first one.
    >All of these modes work with one another so you can have all disabled/enabled, or mix them. 
- 'Show plot' button opens a new process window which displays saved time and round data for currently selected plan.
- **(Optional)** You can add map images to replace the ascii art. To do this, have map images saved in
 'Files/map images' folder and make sure they follow correct format: 

    To do this, have map images saved in 'Files/map images' folder and make sure they follow correct format: 
    
    1. only letters and spaces allowed

    2. only lowercase letters, speicla characters are allowed (like ``#`` in ``#ouch``, ``'`` in ``adora's temple``)

    3. image resolution is 320x195

        - you can use tools/image_scaler for this

    4. file format is ``png``
    
    For example, if you wanted monkey meadow, x factor and #ouch map images, files should be named  

    - ``monkey meadow.PNG``

    - ``x factor.PNG``
    
    - ``#ouch.PNG``

    Map images can be downloaded from https://www.bloonswiki.com/List_of_maps_in_BTD6
    

## Help

| ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/help/help.PNG) |
|:--:|
| *Help window, expanded to fullscreen. It displays the same README.md contents, but links don&#39;t work*|

- Help window displays the document you&#39;re currenly reading (either in web browser or inside gui help window). 
It&#39;s meant for offline mode in case you don&#39;t have access to web
version. However, it should have exact same contents as web version so you can use it as replacement, too.

- It has dark mode always enabled.

- Comes with one major issue: **none of the links work**. Reference links simply point nowhere in document, web links
display some random mess so don&#39;t try to use them either.

Also something worth to mention: the offline readme is actually an html document translated from the README markdown
file. Annoyingly, the Python library used for this conversion requires absolutely file paths in order to display all
images. This means that resulting README.html file has to save **full file paths of your BTD6bot install folder**.

- To avoid storing paths in this file for extended periods, each time a Help window is closed or program is rebooted,
BTD6bot will automatically delete this README.html file.
- Of course, a new one needs to be also generated each time you open a new Help window. But again, after closing Help
or reopening the Main window, this file gets deleted again!


## Queue

| ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/queue/queue.PNG) |
|:--:|
| *Queue window with dark_dungeonsHardChimps plan inserted in queue. When a plan is selected, its info panel is displayed.*|

- Shows all existing plans and currently selected plan queue. When a plan is selected, its info panel is also displayed.
Info texts are exactly the same you see on main window page.
- You can use the 'Add' and 'Remove' buttons to add new/remove existing plan in queue. These also have supported
hotkeys: 'a' for add, 'r' for remove.
- When queue mode is toggled on, bot will use this plan queue instead of currently selected plan in main window.


## Hotkeys

| ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/hotkeys/hotkeys.PNG) |
|:--:|
| *Hotkey window.*|

- Is used for updating bot hotkeys.
- Includes instructions window. Not very long so you should read through it once.
- Hotkey panel is divided into two parts: 
  - upper part is for in-game hotkeys, which must match with Btd6 in-game hotkeys
  - lower part is for gui hotkeys. These work either always (exit) or when a monitoring window exist (pause, start-stop)
- To update a key, 

    1. simply press any line on hotkeys panel,
    2. press 'Set hotkey' button, then press any supported keyboard key
    3. value for that line should now display the updated value on the right of '=' sign.

    >Note that some symbols might show up weirdly, but the hotkey should still work.


## Settings

| ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/settings/settings.PNG) |
|:--:|
| *Settings window*|

- Includes basic and advanced settings. Advanced settings are mostly for internal testing, except the auto-adjust option
which was already used in [First-time setup](#first-time-setup).

<u>Explanations</u>  
**(Basic)**

- **Enable custom resolution**: 
    Change resolution the bot uses to determine relative mouse clicking/ocr text locations. Must match with used in-game
    resolution which should approximately have 16:9 aspect ratio.
- **Windowed mode**: 
    If Btd6 is run in windowed mode. Btd6 must be launced with ``-popupwindow`` launch option and window cannot be moved
    from its initial position. 
    
    Windowed mode can face issues with ocr accuracy, though. If resolution is considerably smaller, text reading errors
    become more common and can hinder upgrading of monkeys.

    Therefore, **it&#39;s always recommended you use fullscreen if possible.**

    #### <u>*Using windowed mode for resolutions with varying aspect ratios*</u>
    As stated under &#39;Enable custom resolution&#39;, resolutions should have aspect ratio of 16:9. But, it is possible to leave in-game resolution to your native resolution, but still use custom resolution + windowed mode to reduce the actual screen area.

    Because windowed mode normally leaves empty space around, you could limit the readable area to the middle of screen.
    A good example would be ``3440x1440`` resolution: it adds extra borders during maps which is 440 pixels each side. This
    means the actual screen area is 3440-440*2=2560 which has aspect ratio of 16:9 with height of 1440!  
    In fact, this should also work for menu screens because play and hero select button are in correct position relative
    to everything else. Only actually problematic case would be the map search button which falls outside the middle
    area, but there&#39;s a built-in checking system which should be able to locate this button no matter the resolution
    setting.  
    So if you have a 3440x1440 monitor and wish to play on this resolution, go to gui settings:

    - enable custom resolution and set it as ``2560x1440``
    - enable windowed mode
    - And of course, remember to readjust ocr deltas for new resolution, as always!

    Here's a beautiful visual explanation:

    ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/settings/3440x1440example.png)
    
    
    In general, for any resolution, check the following:

    - run BTD6 and open any map on your desired resolution
    - find out how much space do the unused areas on left and right side take. These should have equal size: in above
    example, it was 440 on each side so 880 combined.
    - then substract this total unused space from your x-resolution e.g. in above example this was 3440-880.
    - now check if the resulting resolution has close to identical aspect ratio 16:9. Again, in above example,
    3440-880=2560 -> 2560/1440 = 16/9 which is exactly right.
    - (optional) if required, you could repeat this for y-resolution as well, but I believe it&#39;s very rare you&#39;d
    need this. One example would be 1280x800 - test this in-game and see how it adds a wider bar on top and bottom of
    the screen.
    - Then readjust ocr values like usual and you should be good to go.


- **Game version**: 
    Current major game patch version. If version is 48, 48.1, 48.2 etc. just use 48. This value is used to update plan
    info for any plan and verify it works on current version.

- **Retries**: 
    How many times the bot will retry current plan before moving on to next one. However, if bot finishes before
    reaching this limit, it behaves as usual: if a single plan, bot finished; if queue mode enabled, moves onto next
    plan. It&#39;s recommended to keep these value somewhere around 5 as some expert maps in particular have rng and
    can fail once or twice before getting over the problematic round(s).

- **Update** esc menu settings automatically**:
    When bot enters a map first time in current session, it will automatically verify all required in-game menu settings
    are enabled. These are: drag & drop, disable nudge mode, auto start.

- **Record round times and update plan version**: 
    Record all round times during plan execution and updates them in time_data.json. Current version value is also
    stored. Data is only saved if plan finishes and bot returns to menu normally by finding the victory screen. Time
    data is used under 'Show Plot' whereas version is used in plan info panel as a confirmation that this plan can be
    finished on current game version.

**(Advanced)**

- **Ocr time limit**: How long will bot attempt to search for various text flags before it gives up and attempts to
return to main menu. Typically, this should never occur so a high value of 300 seconds or more is recommended: this 
is especially important for apopalypse plans, as in those you can have long periods of downtime where bot attemps to 
place/upgrade a monkey.

- **Ocr frequency**: Pause interval between most ocr operations, in seconds. Naturally, every operation has base cost
 which depends on cpu speed on which this value is then added. Raising this value will greatly decrease cpu load, but
makes ocr more inaccurate/slow. For normal use, keep this value around 0.01-0.1. For extended, repeating but simple
processes, like farming xp/monkey money with simple strategies such dark castle easy/deflation - for hours - you 
could set this value to even high as 0.5-1.

- **Print ocr (delta | substring) text values in monitoring window**: Enables text printing for ocr processes which use
delta matching | substring matching. For example, monkey placements and upgrades use delta matching whereas finding 
current round number uses substring matching.

- **Auto-adjust ocr upgrade data the next time a plan is run**: <u>this was already introduced under
[first-time setup](#update-resolution-and-enable-ocr-auto-adjust)</u>. Updates all upgrade ocr values based on current
resolution settings. As bot uses upgrade labels to determine whether is has succesfully upgraded a monkey or has to keep
on trying, these texts must be as precisely readable as possible. For upgrades, bot has three cases:

     1. not mixing and accepting similar strings like 'sharp shots' & 'razor sharp shots',
     2. not accept too weak a string
     3. accept strings that are good enough.

    To ensure these all work in harmony, bot uses three identifiers: 

     1. monkey name with upgrade path e.g. dart x-2-x
     2. static string it matches to e.g. 'very quick shots'
     3. a delta value of how much the output needs to match with static string. 
    So 0.8 means 80% of static string's symbols must be found in ocr output string, in similar order. Now, each upgrade
    path has *individual* delta value which should be high enough to ignore false strings, but still 
    accept string that is close enough, even if some further error is included. For this reason, this operation performs
    check for all upgrades, updates the delta value and then subtracts a external delta value to make room for error.
    The value is passed as integer 0-9 and it means it will simply subtract 0.01-0.09 from ALL DELTAS.

    ->one more thing: when bot performs the adjusting process, it will do it twice, first for monkeys placed on the
    left side (which opens upgrade panel on right), then on right (which opens panel on left). Then, it will use 
    the lower value of the two and after this, does the previously mentioned subtraction process. This is important 
    as upgrade panels of different sides can give quite different results so lower one is used as baseline.


## Monitoring

| ![](file:/c:/Hobbies/IT/Programming/Python/Projects/btd6bot/btd6bot/Files/helpwindow/images/monitoring/monitoring.PNG) |
|:--:|
| *Monitoring window, with plan dark_castleEasyStandard selected, no extra modes enabled.*|

- Loads all settings set in other windows and initializes the bot. User can then run the bot by simply pressing
 &#39;Run&#39; button or the start-stop hotkey (which can be customized under gui hotkeys), and bot starts to search for
Btd6 main menu screen. After menu screen is found, bot then begins it&#39;s current loop. 

    >Most settings (like resolution) and hotkey values, are updated immediately to current monitoring window. But any
    toggleable modes and current map+strat/queue maplist, will only get updated after you close and reopen this window.
    If you want to be 100% certain your setting are up to date after any changes, just close and reopen monitoring
    window after each time you have change settings.

- Has a output window where all printed text is redirected during bot runtime. This way, it&#39;s easy to follow what
the bot is currently doing. Not all text is displayed because it would clutter the print window. To enable extra text 
for ocr outputs, check Settings window on advanced section and toggle delta/substring text checks on.

- Displays current plan, and if queue mode is on, next plan in queue. Also displays any toggled modes from main window
as On/Off.

- Displays round timer for current round; not 100% accurate, but still quite good and very useful for adjusting ability
timings when new plans are created.

- **(Optional)** Similar to main screen, you can add map images to replace the ascii art. 
**If you did this step for main window, no need to do it again, as same images are used here**. 

    To do this, have map images saved in 'Files/map images' folder and make sure they follow correct format: 
    
    1. only letters and spaces allowed

    2. only lowercase letters, speicla characters are allowed (like ``#`` in ``#ouch``, ``'`` in ``adora's temple``)

    3. image resolution is 320x195

        - you can use tools/image_scaler for this

    4. file format is ``png``
    
    For example, if you wanted monkey meadow, x factor and #ouch map images, files should be named  

    - ``monkey meadow.PNG``

    - ``x factor.PNG``
    
    - ``#ouch.PNG``

    Map images can be downloaded from https://www.bloonswiki.com/List_of_maps_in_BTD6

    

# <u>Creating a new plan</u>

Plan files are located in ``btd6bot/plans``.

For creating and writing plans, it helps a lot if you understand basics of syntax and object-oriented programming in
Python. This is not required, but except some things to be harder to understand.

## Create a plan file

First, you need a plan template. One can be found in 'plan template' folder, located in project root folder. Then,
simply copy this plan_template.py to yours plan folder.


**<u>Plan file: naming</u>**

File names follow specific standard. This was originally implemented to make working with plan files simple for gui and
it has stayed the same to this day.

1. <u>Map name</u>:

    - spaces are replaced by underscores ``_``. Then ``end of the road`` becomes ``end_of_the_road``
    - special characters are allowed. So ``#ouch`` and ``adora's_temple`` are fine.

2. <u>Difficulty</u>:

    - only 3 choices here: ``Easy``, ``Medium`` or ``Hard``.
    - it&#39;s important the difficulty is exactly as stated above: starts with capital letter and rest are lowercase.

3. <u>Game mode</u>

    - same as with difficulty: first letter is capitalized, rest lowercase.
    - only special syntax is Double HP moabs, which includes underscore.

    Game modes for each difficulty:
    |Easy  | Medium | Hard |
    |-|-|-|
    |Standard | Standard | Standard|
    |Primary | Military | Magic |
    |Deflation | Apopalypse | Double_hp |
    | | Reverse   | Halfcash |
    | | | Alternate|
    | | | Impoppable|
    | | | Chimps |

<u>Examples for each game mode:</u>

    monkey_meadowEasyStandard.py
    middle_of_the_roadEasyPrimary.py
    winter_parkEasyDeflation.py

    sulfur_springsMediumStandard.py
    adora's_templeMediumMilitary.py
    kartsndartsMediumApopalypse.py
    rakeMediumReverse.py

    last_resortHardStandard.py
    sunken_columnsHardMagic.py
    pat's_pondHardDouble_hp.py
    cornfieldHardHalfcash.py
    ravineHardAlternate.py
    workshopHardImpoppable.py
    #ouchHardChimps.py


**<u>Plan files: info panel and round block structure</u>**

Now, open your plan file. It looks like this:


    """  
    [Hero]  
    [Monkey Knowledge] -
    -------------------------------------------------------------
    ===Monkeys & upgrades required===
    *list all monkeys + their highest crosspaths here*
    Example: sniper 5-3-1 means plan uses tier 5 top path, tier 3 middle path, and tier 1 bottom path for snipers.
    _______________________________________
    *put description/any additional comments here*
    """

    # copy this file into btd6bot/plans, then uncomment all the code below this line
    '''
    from._plan_imports import *

    def play(rounds: tuple[str, str, str, int, int, str]) -> None:
        BEGIN, END = menu_start.load(*rounds)
        current_round = BEGIN-1
        map_start = time()
        while current_round < END+1:
            current_round = Rounds.round_check(current_round, map_start)
            if current_round == BEGIN:     
                ...
>

First, remove the comments as stated + remove the comment line itself (begins with #). You can also remove the 
placeholder text from info section. Now contents should look like similar to this:

    """  
    [Hero]  
    [Monkey Knowledge] -
    -------------------------------------------------------------
    ===Monkeys & upgrades required===
    _______________________________________
    """

    from._plan_imports import *

    def play(rounds: tuple[str, str, str, int, int, str]) -> None:
        BEGIN, END = menu_start.load(*rounds)
        current_round = BEGIN-1
        map_start = time()
        while current_round < END+1:
            current_round = Rounds.round_check(current_round, map_start)
            if current_round == BEGIN:     
                ...
>

This is about the minimal code needed to run a plan file. To quickly summarize what&#39;s in here:

- Plan files start with a block of text wrapped in triple quotes ``"""``. Everything inside quotes is treated as info
for current plan: it will be displayed both under main and queue windows. It consists of 4 entries:

    1. [Hero] which is the hero used for this plan. For example, if you wanted to use Quincy, you simply leave one empty
    space, then type Quincy:

            ``[Hero] Quincy``.

        Names are not case sensitive so ``[Hero] quincy`` would also work. For all available heroes, have a look at
    [this](#heroes-1). If your plan does not need a hero, you can leave at default or add a dash i.e. ``[Hero] -``
    2. [Monkey knowledge] states if plan requires monkey knowledge. Use ``[Monkey knowledge] Yes`` or 
    ``[Monkey knowledge] -``. To give information on required mk, see 4.
    3. List of required monkeys and <u>highest</u> crosspaths.  

        Examples: 

        - if plan uses 2-0-5 sniper and 0-5-2 sniper, then you would type ``sniper 2-5-5``.
        - uses darts at start but doesn&#39;t upgrade them -> dart 0-0-0
        - uses multiple 0-0-4 beast handlers to merge and create a 0-0-5 beast-> beast 0-0-5

        All examples combined, info sections would look like this:

            ===Monkeys & upgrades required===
            dart 0-0-0

            sniper 2-5-5

            beast 0-0-5
        You can write all the requirements without separating categories, but in above example, primary/military/support
        are separated by empty line each.
    4. General info: here you can write anything you&#39;d like the user to know about e.g. monkey knowledge
    requirements or just comment something.
    Example:

            ``
            _______________________________________
            this is a test plan and this is a comment
            ``
    
    With all sections 1.-4. combined, here&#39;s a simple info text:
  
        [Hero] Quincy
        [Monkey Knowledge] -
        -------------------------------------------------------------
        ===Monkeys & upgrades required===
        dart 0-0-0

        sniper 2-5-5

        beast 0-0-5
        _______________________________________
        this is a test plan and this is a comment

    *For better examples, you should check other existing plans in plans folder*.

    Info will also display current plan file name without the .py suffix, and current game version value if it exists.
    To set a version value, you need to open Settings and 

    - Enable &#39;Record round times and update plan version&#39;
    - Set &#39;Game version&#39; to current bloons td 6 version. Only the major version number is accepted as integer:
    if version would be 50.2, just insert 50 and press &#39;Update version&#39;.
    - Then, let bot run and finish the plan to verify it can be completed, and it will auto-update version number for 
    that plan.

Now that you know what the info panel is, let us have a look at the main body:

    from._plan_imports import *

    def play(rounds: tuple[str, str, str, int, int, str]) -> None:
        BEGIN, END = menu_start.load(*rounds)
        current_round = BEGIN-1
        map_start = time()
        while current_round < END+1:
            current_round = Rounds.round_check(current_round, map_start)
            if current_round == BEGIN:     
                ...

This block is Python code. It includes

- all required imports: these are mostly the commands you will use to write bot actions
- play function which is called for each plan
- initialization through menu_start.load; select hero, map, difficulty and game mode
- set a starting point to track total time
- and finally, the main round loop: this begins from round BEGIN (value depens of difficulty and game mode) and
continues until you finish final round (reach END+1). After it does checks and updates current_round value, it matches
this to corresponding if/elif block to perform command for that round.

Thus, you only need to interract with the part starting from
    
        if current_round == BEGIN:
            ...

Note that BEGIN is a variable: <u>YOU DON&#39;T NEED TO CHANGE THIS VALUE</u>, it will always stand for first round.

Usually, you have multiple rounds which means rounds look like this:

        if current_round == BEGIN:
            ...
        elif current_round == 7:
            ...
        elif current_round == 10:
        .
        .
        .
        elif current_round == 99:
            ...

Previous block could serve as chimps mode plan template: here BEGIN stands for 6. Note that if nothing happens during a
round, you can exclude it from if/elif: here rounds 8 and 9 are skipped over. For final round you can just use the round
number or variable END:
        
        elif current_round == 100:
            ...
        # or 
        elif current_round == END:
            ...
Again, no need to include final round block if it has no commands.

On two special cases, you can just use the first if-block

        if current_round == BEGIN:
            ...
to include all commands. These are deflation and apopalypse. In fact, for apopalypse, you 
**have to use only the first round block!**. After first round ends, bot sets internal flag for end round and stops
processing other rounds.
    
For examples, see *dark_castleEasyDeflation.py* and *infernalMediumApopalypse.py* plan files.


## **Commands**

With commands, you can make bot to do stuff during rounds.

    
For now, you can ignore cpos_x and cpos_y arguments; they are only needed for maps with changing positions e.g. Geared
and Sanctuary. There are also other important topics you should be aware of; all of them are explained later in 
[Advanced](#advanced) section.

For practical examples, check any plan file in ``btd6bot/plans`` folder.

**Monkeys**
-

| Command (with arguments)      | Description | Examples |
|-|-|-|
| Monkey(name, pos_x, pos_y) | Places a monkey ``name`` at location (``x``,``y``). **To access commands, store it in a variable with recognizable name**. <br>All supported monkeys can be found [here](#monkey-names). | <pre>dart = Monkey('dart', 0.5, 0.5) <br>heli1 = Monkey('heli', 0.1, 0)</pre>
| target(set_target, x, y, cpos_x, cpos_y) | Change monkey targeting to ``set_target``. For non-targetable monkeys, simply enter the target string. <br>For target options with target coordinate (x, y), pass ``x`` and ``y`` values.<br>All possible targeting options are listed [here](#targeting). | <pre>dart.target('strong')<br>heli1.target('lock', 0.1, 0.15)</pre>
| upgrade(set_upg, cpos_x, cpos_y) | Upgrade a monkey. Upgrades are given as a list of strings ``set_upg`` of form 't-m-b' where t=top, m=middle, b=bottom<br> path i.e. they follow the usual path standard. Multiple upgrade can thus be queued in one call. <br>Make sure path is valid: cannot do ``['0-0-1','0-0-3']``. | <pre>dart.upgrade(['1-0-0']) <br>dart.upgrade(['2-0-0-','2-1-0','3-1-0']) </pre>
| special(s, x, y, cpos_x, cpos_y) | Use special ability 1 or 2. Thus, ``s`` is either ``1`` or ``2``. If targetable special, give also ``x`` and ``y`` for target location. <br>Is required for moving mortar and dartling location. Special 2 is rarer: some uses would be beast handler second <br>crosspath beast location and (for heroes) Rosalia replace location. | <pre>heli.special(1, 0.1, 0.1) <br>mortar.special(1, 0.1, 0.1) <br>dartling.special(1, 0.5, 0.785) <br>sniper.special(1) <br>beast.special(2)</pre>
| sell(cpos_x, cpos_y) | Sells current monkey. On code level, object still exists so please don&#39;t refer to it afterwards, unless you&#39;ve inserted<br> another non-sold monkey in same variable. | <pre>dart.sell()</pre>
| target_robo(direction, clicks, cpos_x, cpos_y) | Change second arm targeting of a robo monkey. Current targeting value must be tracked manually: then, you simply <br>pass ``direction`` as ``'left'`` or ``'right'`` to click either left or right arrow direction and give amount of ``clicks`` to <br>this direction. For example, after placing a robo monkey, if first hand is on &#39;first&#39; then second is set on &#39;last&#39;. Clicking <br>left arrow once<br> changes it to &#39;close&#39;. And clicking right once would change it back to &#39;last&#39;. | <pre>super.target_robo('left', 2)</pre>
| merge(x, y, cpos_x, cpos_y) | Merge this beast with another at location (``x``, ``y``) i.e. target beast gets the benefit of merging, this one becomes idle. | <pre>beast.merge(0.5, 0.5)</pre>
| center(x, y, cpos_x, cpos_y) | Change x-x-2 ace center path location to (``x``, ``y``). | <pre>ace.center(0.45, 0.35)</pre>

**Heroes**
-

| Command (with arguments) | Description | Examples |
|-|-|-|
| Hero(pos_x, pos_y) | Places a hero at location (``x``,``y``). **To access commands, store it in a variable with recognizable name**. <br>All available heroes are listed [here](#heroes-1). | <pre>hero = Hero(0.5, 0.5)</pre>
| target<br> special<br>sell | Works exactly the same as with Monkey, see the table above. | <pre>hero.target('last')<br>hero.special(2, 0.1, 0.1)<br>hero.sell()</pre>
| force_target() | Currently, only use is to update internal targeting flag for bot when ``Etienne`` hits level ``11``: because bot is unable to <br>track hero xp, it cannot auto-update divide & conquer to zone control.If you use ``Etienne`` and plan to change his <br>targeting after lvl 11, you must call this command at the beginning of the round he reaches this milestone; otherwise <br>bot and game have different targeting value which could cause issues. | <pre>hero.force_target() </pre>
| shop(item, target_x, target_y, cpos_x, cpos_y) | Use Geraldo&#39;s shop ``item`` at location (``target_x``, ``target_y``). Item is given as an integer 1-16: first item being top left, <br>last being bottom right, order of items is left to right, top to bottom. This means first row is items 1-4, second 5-8, <br>third 9-12, fourth 13-16 | <pre>hero.shop(10, 0.5, 0.5)</pre>
| spellbook(spells, cpos_x, cpos_y) | Use Corvus&#39;s spellbook. Similar to Geraldo&#39;s shop, but ``spells`` takes a **list** of integers 1-16; order still the same <br>(left to right, top to bottom). You can pass multiple integers to chain spells. | <pre>hero.spellbook([1])<br>hero.spellbook([20, 6, 2, 3])</pre>

**General**
-

| Command (with arguments) | Description | Examples |
|-|-|-|
| ability(key, timer, xy, delay) | Press ability hotkey 1-10, after ``timer`` seconds has passed, at tuple location``xy``, with optional ``delay`` value.<br> Abilities order depend on the order they get unlocked; keep this in mind!Timer value is counted as seconds and is a float number. <br>It defaults to 0 and uses ability instantly the moment bot reads the command. If timer value N > 0, bot wait N seconds from <br>round start before using the ability. <br>However, if time since round start has already exceeded the N, ability is obviosly used instantly when command is read <br>e.g. ``ability(1,10)`` uses ability 1 instantly if, say 15 seconds have passed. If ability requires a target (e.g. engineer overclock),<br> pass it **as a tuple value ``xy``, NOT as separate x and y**. <br>Finally, ``delay`` uses ability, waits for delay amount (measured in seconds), then moves cursor over to location xy. Its only reasonable<br> use is to refresh Obyn&#39;s trees, wait the delay amount to let bananas finish their moving animation, then move cursor to tree location<br> to collect them. You can just also achieve this by setting a wait timer, then use ``move_cursor`` command at tree location.<br>**Importantly**, ``delay`` has default value of ``0``, which actually disables the cursor moving: any value greated than 0 enables it!  | <pre>ability(1)<br>ability(3,10)<br>ability(2,xy=(0.25, 0.25))<br>ability(1, 5, (0.1, 0.1), 1)</pre>
| wait(timer) | Pauses any bot commands for ``timer`` amount of seconds, then resumes after. | <pre>wait(10)</pre>
| click(x, y, N) | Left mouse click at target location (``x``, ``y``), ``N`` times. Useful for interracting with map elements. Default for N is 1, usually this suffices.<br> Exception would be Ravine where sword needs to clicked 23 out of total 24 to prepare it. |<pre>click(0.3, 0.4)<br>click(0.05, 0.12, 15)</pre>
| move_cursor(x, y) | Move mouse cursor to target location (``x``, ``y``). Rarely useful. Similarly to ``ability``, you could use it to collect bananas from Obyn's<br> tree. | <pre>move_cursor(0.75, 0.44)</pre>
| forward(clicks) | Click the forward button on bottom right ``clicks`` times, which gets value ``1`` or ``2`` times. Default is 2, which sets the game on fast<br> forward. <br>If you play on apopalypse, game already start on basic speed so forward(1) sets it on fast.<br><u>**Important**</u> You don&#39;t need to insert this command inside first round block, as bot will automatically call it if it has not<br> been called yet. On some harder maps however, you might need to do initial placements, then buy another <br>monkey/change targeting midround. For this, write the initial commands, then add forward call, then add rest of the commands | <pre>forward(1)<br>forward(2)</pre>
| change_autostart() | Changes current autostart status: if you have autostart enabled, this will disable it, and vice versa. <br>Used mostly for advanced/expert chimps. Using this effectively can make your advanced/expert plans much safer (=less rng)<br> and some plans just require it and cannot be completed otherwise. | <pre>change_autostart()</pre>
| end_round(timer) | Pressed the start/forward button a single time after ``timer`` amount of seconds has passed; supports float values. If no timer value is<br> given, defaults to 0 seconds. Only used when autostart is disabled with change_autostart(). You can see this used often under expert<br> chimps plans, because with autostart disabled rounds need to be ended manually.|<pre>end_round(20)</pre>

**Advanced**
-

These topics are more difficult to grasp, but are necessary for creating more complex plans.

- [**cpos**] ``cpos_x`` and ``cpos_y`` update current x and y positions. If map such as Geared moves your monkey
 location from previous and you need to call a command on this monkey, cpos must be used. Otherwise bot thinks the
monkey is still at previous location which of course will break it. To use cpos, simply add ``cpos_x=..., cpos_y=...`` 
arguments at the end and insert the new location coordinate. 
    - Note that cpos will also update this as current coordinate, so if monkey has not changes it&#39;s position since 
    last cpos command, you don&#39;t need to add them again. 
    
        An example could be Geared map: you place a monkey at location (x,y) then 8 rounds pass and gear has done full 
        rotation and landed on same coordinate. Then, updating cpos is not needed because bot already points at this 
        location.
        
        But, for safety/good practise measures, you should still always add them on Geared/Sanctuary plans: makes easier
        to go back and check for possible errors.

    To see how ``cpos`` is used in practise, check *sanctuaryHardChimps.py* or *gearedHardChimps.py* plan files.

- [**placement_check**] When you create a Monkey object, there&#39;s another parameter called ``placement_check``. It 
defaults to boolean value True which means bot will perform the usual check as intended. But, on some occasions, you 
might want to avoid this: if you place towers close to upper hud i.e. under hp, cash or round display, changes are you 
cannot click the monkey at same location you initially placed it at. This is because those hud values can change and 
block the access. If access is blocked, bot cannot verify the placed monkey and this is likely to break the plan 
execution.

    To avoid this, you can pass ``placement_check=False`` which ignores the checking process e.g. 
    ``dart1 = Monkey('dart', 0.1, 0.1, placement_check=False)``. Then, you use ``cpos`` to update the location where 
    this monkey is accessed from: you click slightly off the center and it should still count as clicking on this 
    monkey. Then just set this new position as cpos when you next need to command said monkey.

    While this process is often an overkill and can be avoided by changing placements further away from hud, one actual
    use case is found in *bloody_puddlesHardChimps* plan: here, a sniper is placed at the top left position, next to 
    left outermost track, to provide best coverage for early game. The position is just under the cash display: sniper
    can be placed normally, but cannot be clicked and accesed again at same location. Thus following commands are 
    performed:

        sniper3 = Monkey('sniper', 0.1619791666667, 0.0268518518519, placement_check=False)
        sniper3.target('strong', cpos_x=0.1291666666667, cpos_y=0.0601851851852)
    
    Here, as you can see, sniper ignores the placement check, and next target command updates the (x,y) position of 
    sniper by moving slightly left and up from initial x and y coordinates.

- [**Order of arguments**] In command examples, commands often exclude the argument names. For example

        dart = Monkey('dart', 0.5, 0.5)

    is the same as

        dart = Monkey(name='dart', pos_x=0.5, pos_y=0.5)
    
    Reason is, **if you use arguments in order**, ``arg_name=`` syntax is not needed: Python knows that, in above 
    example, ``'dart'`` refers to argument ``name``, the first ``0.5`` value refers to ``pos_x`` and second to 
    ``pos_y``.

    However, if you ever need to access latter arguments without using all the previous ones, you have to use actual 
    argument keyword. For example, in map Geared, you placed a dart monkey, just like in code above. Now, you want to 
    change its &#39;first&#39; to &#39;strong&#39;, but to do this, you need to update its current position because gear
    has moved since it&#39;s initial placement. So maybe the new position is (0.45, 0.3). To update dart position, the
    cpos_x, cpos_y arguments are needed. Now, target command has syntax ``target(set_target, x, y, cpos_x, cpos_y)`` 
    which means if you write

        dart.target('strong', 0.45, 0.3)
    
    this will actually just click dart&#39;s current internal location (0.5, 0.5) and try to set monkey at that location
    on &#39;strong&#39;. Well there could be a monkey, or not. Nontheless, it&#39;s not the intended outcome! After 
    this, it will attempt to &#39;target&#39; dart location (0.45, 0.3); again, this doesn&#39;t mean anything for
    current 0-0-0 dart!

    The problem? Just as stated at the first example, this argument means

        dart.target('strong', x=0.45, y=0.3)

    Because x and y values are not needed for dart, command needs to be provided with argument names:

        dart.target('strong', cpos_x=0.45, cpos_y=0.3)

    This would do what we originally wanted. Of course, something like

        dart.target('strong', 0.2, 0.3, 0.45, 0.3)

    would also work in sense, because it does the same as

        dart.target('strong', x=0.2, y=0.3, cpos_x=0.45, cpos_y=0.3)
    
    but again, bot would set the target location of 0-0-0 dart at (0.2, 0.3). Luckily, it would cause no harm, but is 
    not what was intended.

    <u>To summarize:</u> if you use all arguments up to a point, no need to add argument names. But if you skip over 
    even one, rest of the arguments must use argument names. This might be difficult to understand at first, but with 
    practise and using existing plans as examples, it becomes easy to remember.

- [**Possible round detection issues**] If you have lot of things happening under the round label top right, bot might 
sometimes have issues with detecting rounds: this can either result into delayed round start OR it can even skip over 
rounds because bot will falsely detect it has falled behind in rounds and tries to catch up. 
**This rarely becomes a problem**, but if it happens, it could cause serious issues, as bot uses abilities before their
intended rounds/timings. 

    A good example of this would be *<u>Erosion</u>* map: here, lot of end game defense is likely concentrated in the 
    remaining ground located top right. Not only this, all bloons move around this area during final rounds as well. 
    Combined, bloons and lot of projectiles flying around round text might create detection issues. 
    
    **So just be aware that this issue can exist, but majority of time you don&#39;t need to concern yourself with it!**

## Table: Monkeys, heroes and targeting options

**Monkey names**
-

Use these values when placing a new monkey with ``Monkey(name, pos_x, pos_y)`` command

|Primary    | Military      | Magic         | Support
|-|-|-|-|
| dart      | sniper        | wizard        | farm
| boomer    | sub           | super         | spike
| bomb      | boat          | ninja         | village
| tack      | ace (**1**)   | alch          | engineer
| ice       | heli          | druid         | beast
| glue      | mortar        | mermonkey     |
|           | dartling      |               |


**1**: If you plan to use ``wingmonkey`` monkey knowledge, see [Targeting](#targeting) (**2**).

**Heroes**
-

 Hero for current plan is selected based on ``[Hero]`` value inside the plan file info panel.  
*In the following table, Heroes are categorized by their xp multiplier.*

| x1            | x1.425        | x1.5          | x1.71
|-|-|-|-|
| Etienne       | Brickell      | Benjamin      | Adora
| Geraldo       | Corvus        | Psi           | Churchill
| Gwen          | Ezili
| Obyn          | Pat
| Quincy        | Rosalia
| Striker       | Sauda

**Targeting**
-

Use ``target(set_target, x, y, cpos_x, cpos_y)`` to change targeting.


| Basic (**1**)     | heli          | ace                   | sniper            | mortar (**4**)| dartling          | spike (**6**)
|-|-|-|-|-|-|-|
| 'first'           | 'lock' (**5**)| 'circle'              | 'elite' (**3**)   |               | 'locked' (**5**)  | 'normal'
| 'close'           | 'pursuit'     | 'infinite'            |                   |               |                   | 'far'
| 'last'            |               | 'eight'               |                   |               |                   | 'close'
| 'strong'          |               | 'centered'            |                   |               |                   | 'smart'
|                   |               | 'wingmonkey' (**2**)

**1**: Valid for most monkeys/heroes. Also, ``x-x-3+ ice`` and ``5-x-x village`` can use these.
- For ``x-3+-x super``, use ``target_robo`` command to control second arm targeting.

**2**: To enable ``wingmonkey`` mk, first ace must be named ``ace_wing`` instead of ``ace``. This enables a global flag
to take wingmonkey into account with targeting changes; without the flag enabled, actual target value and bot value are
going to be desynced.
Afterwards, you normally place aces using ``ace``. 

**3**: When a ``x-5-x sniper`` is bought, a global flag tracking ``elite`` targeting is set to ``1``. Bot can then 
automatically adjust targeting system around elite targeting. And, when ``x-5-x sniper`` is sold with ``sell()``, this
status is reverted back to ``0``.

**4**: Mortars cannot be targeted using ``target`` command. Use ``special(1, x, y)`` instead.

**5**: Dartling guns behave a bit differently and require both ``target`` and ``special`` commands for (re)targeting. 
Some other monkeys, like ``heli`` can benefit from this as well.
- For ``dartling``, use ``target('locked', x, y)`` the first time to set direction. 
- For ``heli``, use ``target('lock', x, y)`` the first time to set hover position.

To retarget either of monkeys, you must use ``special(1, x, y)`` instead. This is because bot has been programmed to 
require new targeting value to be different from current e.g. you can&#39;t set a monkey on ``first`` if it already has
this value. Therefore, when trying set dartling/heli to ``locked``/``lock`` respectively, same rule applies.

**6**: Requires ``x-x-2+ spike``.



# <u>Updating the bot</u>

This section covers how to add new content for ``BTD6bot``. 

Some Python knowledge is required. 
You should also use a code editor like VS Code for optimal experience.

---

btd6bot source folder looks like this:

    _ocr_tests
    bot
    Files
    gui
    plans
    utils
    __init__.py
    __main__.py
    _no_gui.py
    set_plan.py

For in-game updates, only ``bot`` and ``Files`` necessary, as only somewhat frequent additions would be new monkeys and
heroes. 

- Maps don&#39;t require any changes because bot selects a map using the plan file: if a new map called ``bloons map`` 
was added and you wanted to create a plan for it on *hard, standard* then simply name the plan file 
``bloons_mapHardStandard.py``.

- For major changes, like new additions to ui, some big changes in bot code could be required. However, because changes
 like these are too vague to be descripted under set rules, they are not covered here and each case must be handled 
 individually.

Bot and files directory can be summed shortly:

- ``bot`` contains the entire bot library which is responsible of all in-game bot actions. It includes the logic for
 menu navigation, round and defeat checks, time flow, kb and mouse controls. Also includes commands and all the ocr
  functions.

- ``Files`` includes all the non-Python files and store various pieces of data. Only upgrade ocr template and hotkeys
 need to be updated.

So, only files you likely need to modify are

- ``bot``
    - ``menu_start.py``
    - ``commands/monkey.py``
    - ``commands/hero.py``
- ``Files``
    - ``text files/hotkeys.txt``
    - ``_ocr_upgradedata.json``


## New monkeys

1. **Monkey name**

    - open ``bot/commands/monkeys.py``

    - under ``_MonkeyConstants`` class, find ``_MONKEY_NAMES`` constant.

    - add monkey name here. Each category is on its own line; ``hero`` is just a identifier for hero-type monkeys.
    **Make sure name is short, written as lowercase string (add ' ' around it) and related to actual monkey.** <u>It 
    will be used in multiple places, in particular each time a monkey of this type is created.</u>

    Example: if your monkey is called ``'test_monkey'`` and it belongs to military category, then code becomes

        _MONKEY_NAMES = (
            'dart', 'boomer', 'bomb', 'tack', 'ice', 'glue',
            'sniper', 'sub', 'boat', 'ace', 'heli', 'mortar', 'dartling', 'test_monkey',
            'wizard', 'super', 'ninja', 'alch', 'druid', 'mermonkey',
            'farm', 'spike', 'village', 'engineer', 'beast',
            'hero'
    )

    **Don&#39;t forget to add comma ``,`` at the end!**

2. **Set hotkey**

    - open ``Files/text files/hotkeys.txt`` and add a new row:

        - first, name of the monkey e.g. ``test monkey``
        - then, one space, followed by ``=`` then another space
        - then, set an initial hotkey value; user sees this in gui. Some existing symbols can display weirdly when you
         edit this file manually: make sure to update these through gui.
        
        Lets say you used just ``q`` as hotkey. Then simply write ``test monkey = q``.

    - in ``bot/commands/monkeys.py``, search ``_get_hotkey`` and support for new hotkey:

            case 'test_monkey':
                return hotkeys['test monkey']

    Here, 
    
    - use the code-level name you added in ``_MONKEY_NAMES`` inside ``case`` e.g. ``case 'test_monkey'``
    - hotkey string you wrote in ``hotkeys.txt`` inside ``hotkeys[...]``; remember to add ``' '`` to use string type
    e.g. ``hotkeys['test monkey']``.


3. **Add targeting settings**

    - in ``monkeys.py``, search ``_change_target``
    - add a ``case`` for your monkey
    - add **all possible** targeting outcomes: ``target`` value is the one you are switching to, ``current`` is current
     value before switching to ``target``.

    Some monkeys like ``sniper`` and ``ace`` have more complex systems, because the amount of key presses to move from
    ``current`` to ``target`` depends on what targeting options are currently available. For snipers, x-5-x unlocks
    ``elite``; for aces, x-x-2+ unlocks ``centered`` and possible monkey knowledge unlocks ``wingmonkey``.

4. **Add possible automatic update of target values**

    For most monkeys, this one is not required. Only for monkeys which auto-switch to a targeting option after 
    upgrading. Examples: ``heli 2-x-x-``, ``ace x-x-2``, ``sniper x-5-x``. To add a new value:

    - in ``monkeys.py``, search ``_update_auto_target_paths``
    - then simply add a new line like this:

            if self._name == 'test_monkey' and i == 0 and int(u[2*i]) == 4:
                self._targeting = 'strong'
    
    Here, 
    
    - ``i == ...`` stands for the upgrade path: ``0`` for top, ``1`` for middle, ``2`` for bottom.
    - ``int(u[2*i])`` points to upgrade path position value i.e. the crosspath value ``0-5``. In example above, 
    ``i == 0 and int(u[2*i]) == 4`` means top path 4. upgrade, or ``4-x-x`` path.

    Together, code above states: if ``'test_monkey'`` is upgraded to ``4-x-x``, change targeting to ``strong``.

5. **Set basic targeting value**

    - in ``monkeys.py``, search ``_basic_monkey_targeting``
    - again, add a new case for your monkey and its default targeting when its initially placed. If targeting value is 
    ``first``, ``close``, ``last`` or ``strong``, **don&#39;t add anything, ``case _`` covers this.**


6. **Add any command methods**

    Again, **optional for most monkeys**. But if your monkey requires some custom command, add method for it. Add these 
    at the bottom of ``monkeys.py``. Examples for current monkeys:

    - ``robo_target``: for ``super`` monkeys only, in particular robo monkeys. Change second arm targeting.
    - ``merge``: merge this ``beast`` handler with another located in target location.
    - ``center``: change a ``x-x-2+ ace`` center path location.

7. **Update upgrade ocr base values (VERY IMPORTANT)**

    In order to include the new monkey in ocr adjusting, you need to add **<u>all</u>** its upgrade paths, upgrade names 
    and placeholder deltas to ``Files/_ocr_upgradedata.json``. This data must be similar to existing entries: 
    for example, ``dart`` monkey has its data listed something like this:

        "dart 1-x-x": [
          "sharp shots",
          0.5
        ],
        "dart 2-x-x": [
          "razor sharp shots",
          0.5
        ],
        .
        .
        .
        "dart x-x-4": [
          "sharp shooter",
          0.5
        ],
        "dart x-x-5": [
          "crossbow master",
          0.5
        ]

    To summarize:

    1. type monkey name and upgrade crosspath: each such string forms a key
    2. under each key is a value: this value is a list object with 2 entries.
        - first is <u>upgrade path name</u>; copy the names from in-game upgrades and **try to avoid typos**: one wrong 
        letter is mostly fine, but multiple can cause problems with ocr.
        - second is <u>delta value</u>: because this file is just a template, these are just default placeholder values. 
        The actual file which is created during ocr adjusting process copies these to initialize fields, then updates 
        them immediately after with real data. Just insert a valid value like ``0.5``, then copy-paste it under other 
        upgrades as well.

---

## New heroes

1. **Hero click location in selection screen**

    - open ``bot/menu_start.py``
    - under ``MouseLocations`` class, there are constants ``HEROES`` and ``HEROES2``: these contain click locations for 
    selecting each hero when in selection screen. Then,

        - If hero can be accessed without needing to scroll the selection screen down, it should be added in ``HEROES``. 
        Currently, the last row of heroes accessably in this way are: ``Brickell``, ``Psi``, ``Geraldo``
        - Otherwise, hero is initially hidden and screen must be scrolled down to reveal it. Currently, only ``Corvus`` 
        requires this.
    
    - then, get the hero portrait location with coordinate tool (``tools/show_coordinates``) and add a new entry to one 
    of the lists: it needs to include
    
        1. hero name, **all lowercase**, and
        2. **click location as a tuple**.  
        Note that hero locations **can change between updates so you might need to change location of other heroes as 
        well.**

This in in fact the only mandatory step for adding heroes. However, if hero uses custom targeting options 
(other than **first**, **close**, **last**, **strong**) or requires custom commands 
(**Geraldo&#39;s shop**, **Corvus&#39;s spellbook**) then read the following sections.

2. **Custom targeting options**

    - open ``bot/commands/hero.py``

    - search for method ``_change_hero_target`` and find following part under it:

            match self._hero_name:
                case 'benjamin':
                    print('???')
                case 'etienne':
                    if target == 'd&q':
                        if current == 'first':
                            kb_mouse.kb_input(hotkeys['target change'])
                        elif current == 'zone':
                            kb_mouse.kb_input(hotkeys['target reverse'])
                    elif target == 'first':
                        if current == 'd&q':
                            kb_mouse.kb_input(hotkeys['target reverse'])
                        elif current == 'zone':
                            kb_mouse.kb_input(hotkeys['target change'])
                    elif target == 'zone':
                        if current == 'first':
                            kb_mouse.kb_input(hotkeys['target reverse'])
                        elif current == 'd&q':
                            kb_mouse.kb_input(hotkeys['target change'])
                    else:
                        return self._name, target
                case _:
                    return self._normal_targeting(current, target) 

        Here the special cases: all other heroes operate under basic system. 
        
        - For **benjamin**, no case would be required: all it does currently is to print text ``???`` if user tries to 
        change targeting. 
        
        - For **Etienne** however, system matches to new target value ``target``, then jumps into if-elif block to see 
        ``current`` targeting setting and presses target change/reverse keys desired amount of times: in this particular
        case, only a single key press is required which is already the default value.

        **IMPORTANT** Bot cannot track hero xp and thus is unable to know current level of hero. If hero unlocks a new 
        targeting setting on some level, like Etienne does, following happens:

        - in-game, when Etienne reaches lvl 11, targeting is automatically set to *zone control*. For bot, it should 
        also become ``zone``, but this cannot happen automatically for the reason stated. Thus, to sync targeting 
        between game and bot, user must call ``force_target`` method in any plan that includes Etienne reaching lvl 11. 
        All this method does is it sets ``self._targeting = zone`` which means bot is now in sync game targeting. 
        Afterwards, targeting works as expected.

        So, if any hero behaves similarly, add an internal flag by editing ``force_target`` method and notify the user 
        which heroes require this under by adding a comment in [Heroes](#heroes) 

3. **Custom commands for a hero**

    If you need to add custom command(s) for any hero, simply

    - add a new method, name it in a way that describes it well, but is relatively short 
    (e.g. ``shop`` for Geraldo, ``spellbook`` for Corvus)
    - implement any other requires internal methods (e.g. ``prepare_hero_menu`` for Gerald and Corvus)
    - **(Optional)** Add pause flag, cpos checks so method can be used in maps with changing locations; see other 
    existing methods for examples.