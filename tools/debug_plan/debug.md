# How to use:

- use the run.bat/run.sh to open script CLI
- for general commands, simply follow introduction.
- for debugging i.e. using the command

    `debug {plan_name} {debug_mode} [start_round] [hero_lvl]`

    1. `plan_name` is any of the plan file names without .py suffix
    2. `debug_mode` is either `static` or `start`:
        - 'static' tests static tower positions for any plan. Static means tower position don't move between rounds 
        because of map. Therefore this doesn't work on maps such as Geared and Sanctuary
        - 'start' sets up any plan with static positioning to begin on a specific round. Requires use of challenge 
        editor
    3. `start_round` is <u>optional argument</u> and should only be used with `start` to specify start round.
    4. `hero_lvl` is <u>optional argument</u> and should only be used with `start` to specify hero level. Challenge
    editor doesn't have a setting to auto-level hero to match actual leveling. For this user must
        - check hero level and pass this value e.g. use [this xp calculator](https://svrng.github.io/BTD6-Hero-XP-Calculator/)
        - and because hero is leveled in-game, you must add the total cost **on top of start round income**
    
    Example:
    - challenge editor: select map, difficulty and start round. Also set starting income for that round e.g. 
    using [this round income chart](https://topper64.co.uk/nk/btd6/income/chimps)
    
         => so let's assume Dark Castle, Hard difficulty on Chimps. Start round is 90. Based on that link you would 
         set income at the end of 89 which would be **131120** (rounded down). Let's assume hero is Psi: using the xp 
         calculator, on Expert map on Chimps round 90 would be lvl 16 and costs **210855**. Unfortunately exact xp 
         cannot be entered so this is the best bot has to do with. Now combining income and hero cash yields **341975**
         as required start income.
        
    - then start the challenge and game start at round 90/100
    - run the script and type command `debug dark_castleHardChimps start 90 16`. As stated this runs dark castle on 
    chimps with 90 as starting round and hero level 16.
    - now bot will simply setup game state to round 89 end. It will then continue normally from 90 and onward.
    - when it hits 100 and finishes successfully, it will simply stop here.
        