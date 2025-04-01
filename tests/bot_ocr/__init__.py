"""Tests for ocr interractions.

All tests located under this folder require a BT6 game instance. Do not run these if you don't have the game opened in 
main menu screen!

You should run each test in this folder separately, as they are quite long. After a test/tests begin, refrain from 
doing anything with mouse and keyboard, as any movement/input could  break current test environment.
---

Bot library handles all ocr: gui and other non-bot modules are completely independent from this.
These are very important for verifying plans can be run from start to finish as bot only communicate with game through 
ocr texts.

Use cases:  
-starting bot from main menu
-menu navigation  
-monkey/hero placements and upgrades  
-starting and leaving maps
-current round number  
-detecting specific messages: defeat screen, collection events

Most of above cases are easily tested by setting the bot to run any existing plan. However, upgrades in particular can
be a nuisance as matching to simpler name strings require often the highest amount of testing and tweaking.

To run ocr tests, you must have an instance of BTD6 running on main monitor and set in main menu screen. Each tests 
starts with detecting the menu play button text. Each test will also return back to this state before finishing so next 
one can start right after.  
"""