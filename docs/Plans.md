# Supported game plans (Last updated 2025-08-20)

- this list is auto-updated using ``scripts/update_plans.py``
- all implemented plans are listed. Each game mode includes
    - link to corresponding .py plan file located in ``plans`` directory
    - the documentation of corresponding .py plan file which is read from the same file

    Some plan names can have invalid symbols which causes their links not to work. One such example is #Ouch with its \# symbol

---

- [#Ouch](##ouch)
- [Ancient Portal](#ancient-portal)
- [Another Brick](#another-brick)
- [Bloody Puddles](#bloody-puddles)
- [Candy Falls](#candy-falls)
- [Cargo](#cargo)
- [Castle Revenge](#castle-revenge)
- [Cornfield](#cornfield)
- [Dark Castle](#dark-castle)
- [Dark Dungeons](#dark-dungeons)
- [Dark Path](#dark-path)
- [Enchanted Glade](#enchanted-glade)
- [Erosion](#erosion)
- [Flooded Valley](#flooded-valley)
- [Geared](#geared)
- [Glacial Trail](#glacial-trail)
- [High Finance](#high-finance)
- [In The Loop](#in-the-loop)
- [Infernal](#infernal)
- [Last Resort](#last-resort)
- [Mesa](#mesa)
- [Middle Of The Road](#middle-of-the-road)
- [Midnight Mansion](#midnight-mansion)
- [Monkey Meadow](#monkey-meadow)
- [Muddy Puddles](#muddy-puddles)
- [Off The Coast](#off-the-coast)
- [Pat's Pond](#pat's-pond)
- [Peninsula](#peninsula)
- [Quad](#quad)
- [Ravine](#ravine)
- [Sanctuary](#sanctuary)
- [Spa Pits](#spa-pits)
- [Spillway](#spillway)
- [Sunken Columns](#sunken-columns)
- [Sunset Gulch](#sunset-gulch)
- [Tinkerton](#tinkerton)
- [Underground](#underground)
- [Workshop](#workshop)
- [X Factor](#x-factor)

### #Ouch
- Hard
	- [Chimps](../btd6bot/plans/#ouchHardChimps.py)

			[Hero] Obyn
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-2
			ice 4-1-0
			glue 0-2-4
			
			sniper 4-2-0
			
			wizard 3-0-2
			ninja 0-4-0
			alch 4-2-0
			druid 3-1-5
			mermonkey 2-0-4
			
			village 2-3-2
			engi 0-4-0
			_______________________________________
			
### Ancient Portal
- Hard
	- [Chimps](../btd6bot/plans/ancient_portalHardChimps.py)

			[Hero] Quincy
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			
			ice 0-1-4
			glue 0-2-3
			
			sub 0-5-2
			dartling 2-0-5
			
			wizard 0-3-1
			alch 3-0-0
			
			village 2-3-0
			_______________________________________
			
### Another Brick
- Hard
	- [Chimps](../btd6bot/plans/another_brickHardChimps.py)

			[Hero] Psi
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-3-2
			glue 0-5-2
			
			sub 2-5-0
			heli 5-0-2
			
			alch 4-2-0
			
			village 2-3-0
			_______________________________________
			
### Bloody Puddles
- Hard
	- [Chimps](../btd6bot/plans/bloody_puddlesHardChimps.py)

			[Hero] Gwen
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-2
			boomer 2-0-4
			tack 2-0-4
			glue 0-2-4
			ice 4-1-0
			
			sniper 4-5-5
			sub 2-0-3
			
			wizard 3-0-2
			ninja 1-0-4
			alch 4-2-1
			
			village 3-2-2
			_______________________________________
			Minimal rng involved: round 23 is the most common to fail although still relatively rare.
			
### Candy Falls
- Hard
	- [Chimps](../btd6bot/plans/candy_fallsHardChimps.py)

			[Hero] Sauda
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			glue 0-2-4
			
			sniper 0-0-0
			heli 5-0-5
			
			village 2-3-0
			_______________________________________
			If price change to heli where 3-0-0 not available for round 28, please update to pop lead bloons.
			Copy of tinkertonHardChimps (tower position changed).
			
### Cargo
- Hard
	- [Chimps](../btd6bot/plans/cargoHardChimps.py)

			[Hero] Sauda
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-3-0
			
			sniper 2-2-5
			
			super 3-0-2
			alch 5-2-0
			
			village 2-0-2
			_______________________________________
			
### Castle Revenge
- Hard
	- [Chimps](../btd6bot/plans/castle_revengeHardChimps.py)

			[Hero] Gwen
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 3-2-0
			tack 2-0-3
			
			sniper 5-5-5
			sub 0-0-0
			
			alch 5-2-0
			
			village 2-0-2
			_______________________________________
			On round 83 hero is manually leveled up to in order to increase consistency.
			Some late rounds like 87, 89, 90 and 95 might also cause issues if gwen's heat up timing is off.
			
### Cornfield
- Hard
	- [Chimps](../btd6bot/plans/cornfieldHardChimps.py)

			[Hero] Sauda
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 5-0-2
			
			wizard 5-2-0
			alch 5-2-1
			
			spike 2-0-5
			village 2-0-2
			_______________________________________
			'No Harvest' achievement can be obtained as no corn is removed
			
### Dark Castle
- Easy
	- [Deflation](../btd6bot/plans/dark_castleEasyDeflation.py)

			[Hero] Gwen
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			ace 2-0-3
			
			alch 4-2-0
			
			village 2-2-0
			_______________________________________
			
	- [Standard](../btd6bot/plans/dark_castleEasyStandard.py)

			[Hero] Obyn
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			sub 2-0-4
			
			ninja 4-0-2
			alch 3-0-0
			_______________________________________
			
- Hard
	- [Chimps](../btd6bot/plans/dark_castleHardChimps.py)

			[Hero] Obyn
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys required===
			dart 0-0-0
			
			sub 0-0-0
			
			alch 4-2-1
			druid 0-1-5
			
			spike 2-0-5
			village 2-3-0
			_______________________________________
			
### Dark Dungeons
- Hard
	- [Chimps](../btd6bot/plans/dark_dungeonsHardChimps.py)

			[Hero] Sauda
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 5-2-2
			boomer 0-2-4
			tack 2-0-4
			glue 2-2-4
			ice 5-2-0
			
			wizard 0-3-2
			alch 3-2-1
			
			spike 4-2-2
			village 3-2-2
			engineer 1-3-2
			_______________________________________
			
### Dark Path
- Hard
	- [Chimps](../btd6bot/plans/dark_pathHardChimps.py)

			[Hero] Striker
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-0
			bomb 0-5-1
			glue 0-2-3
			
			sniper 0-1-0
			mortar 4-5-5
			
			druid 1-3-0
			
			village 2-2-0
			_______________________________________
			
### Enchanted Glade
- Hard
	- [Chimps](../btd6bot/plans/enchanted_gladeHardChimps.py)

			[Hero] Etienne
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-0
			
			ninja 0-4-0
			alch 5-0-0
			druid 1-3-0
			
			sub 0-0-0
			ace 2-0-4
			
			spike 1-3-0
			village 2-0-2
			engineer 0-0-0
			_______________________________________
			
### Erosion
- Hard
	- [Chimps](../btd6bot/plans/erosionHardChimps.py)

			[Hero] Psi
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-1
			bomb 5-2-0
			glue 0-1-3
			
			sniper 1-2-5
			sub 2-0-2
			
			ninja 0-0-0
			alch 4-2-0
			druid 3-0-2
			
			spike 0-4-2
			village 2-4-2
			_______________________________________
			Gameplay-wise, should be viable for black bordering.
			
			For late game rounds (90+), bot might skip ahead and begin executing commands for upcoming rounds.
			Reason is there's lot of projectiles/bloons moving around round label, which can cause false positives.
			This should not matter, as long as 99 => 100 is detected normally; 100 requires abilities and if bot uses them earlier than intended, you will 100% lose.
			Another harmless effect is incorrectly saved round times: some display too short and other too long round durations.
			
			Should issues rise with 99 => 100 transition, solution is to use manual round ending with end_round() command. With it enabled, bot won't begin to search for the next round until countdown ends.
			
### Flooded Valley
- Hard
	- [Chimps](../btd6bot/plans/flooded_valleyHardChimps.py)

			[Hero] Pat
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			ice 0-4-1
			
			sniper 1-2-0
			sub 0-2-1
			boat 5-0-2
			
			ninja 1-0-5
			alch 4-2-0
			mermonkey 5-0-4
			
			village 2-3-0
			engineer 0-3-2
			_______________________________________
			
### Geared
- Hard
	- [Chimps](../btd6bot/plans/gearedHardChimps.py)

			[Hero] Rosalia
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-0
			
			sniper 1-3-2
			heli 5-0-5
			
			ninja 0-4-0
			alch 3-2-0
			
			village 2-4-2
			_______________________________________
			
### Glacial Trail
- Easy
	- [Standard](../btd6bot/plans/glacial_trailEasyStandard.py)

			[Hero] Sauda
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-0
			
			mortar 0-0-0
			
			druid 1-3-0
			
			spike 2-0-3
			engineer 4-2-0
			_______________________________________
			Derived from glacial_trailHardChimps.
			
- Hard
	- [Chimps](../btd6bot/plans/glacial_trailHardChimps.py)

			[Hero] Sauda
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 5-2-0
			ice 5-2-0
			glue 0-2-4
			
			sub 0-4-0
			mortar 0-2-3
			
			alch 4-2-0
			druid 1-3-0
			
			spike 2-0-5
			engineer 5-2-0
			_______________________________________
			
	- [Standard](../btd6bot/plans/glacial_trailHardStandard.py)

			[Hero] Sauda
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 5-2-0
			
			mortar 0-2-3
			
			alch 3-0-0
			druid 1-3-0
			
			spike 2-0-5
			engineer 4-2-0
			_______________________________________
			Derived from glacial_trailHardChimps.
			
- Medium
	- [Standard](../btd6bot/plans/glacial_trailMediumStandard.py)

			[Hero] Sauda
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 5-2-0
			
			mortar 0-2-3
			
			alch 3-0-0
			druid 1-3-0
			
			spike 2-0-4
			engineer 4-2-0
			_______________________________________
			Derived from glacial_trailHardChimps.
			
### High Finance
- Hard
	- [Chimps](../btd6bot/plans/high_financeHardChimps.py)

			[Hero] Gwen
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-2
			
			sub 3-0-1
			boat 5-2-0
			ace 5-0-2
			
			alch 4-0-1
			druid 2-5-0
			mermonkey 4-0-2
			
			village 2-2-0
			_______________________________________
			
### In The Loop
- Hard
	- [Chimps](../btd6bot/plans/in_the_loopHardChimps.py)

			[Hero] Sauda
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			glue 0-2-4
			
			sniper 0-0-0
			heli 5-0-5
			
			village 2-3-0
			_______________________________________
			If price change to heli where 3-0-0 not available for round 28, please update to pop lead bloons.
			Copy of tinkertonHardChimps (tower position changed).
			
### Infernal
- Hard
	- [Chimps](../btd6bot/plans/infernalHardChimps.py)

			[Hero] Quincy
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-2
			
			sniper 0-1-0
			sub 2-5-0
			heli 2-0-5
			
			alch 4-0-1
			mermonkey 2-0-4
			
			village 2-3-0
			_______________________________________
			-Apache prime for dps  
			-Pre-Emptive Strike for ddts, late game moab damage, and round 100.
			
- Medium
	- [Apopalypse](../btd6bot/plans/infernalMediumApopalypse.py)

			[Hero] Psi
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-2
			bomb 2-0-4
			
			sniper 0-2-2
			sub 2-0-4
			
			alch 3-0-0
			druid 1-3-0
			
			village 0-2-0
			_______________________________________
			Apopalypse round rng might fail you. Should work after a few tries, though.
			
### Last Resort
- Hard
	- [Chimps](../btd6bot/plans/last_resortHardChimps.py)

			[Hero] Adora
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-0
			glue 0-2-4
			
			sniper 4-0-2
			
			alch 3-3-0
			druid 4-0-2
			
			village 2-0-2
			engi 5-2-0
			spike 4-0-5
			_______________________________________
			Some rounds can get skipped because bot incorrectly detects different value.
			This should mostly happen in early/mid game and thus not affecting later rounds where ability timings are necessary.
			
### Mesa
- Hard
	- [Chimps](../btd6bot/plans/mesaHardChimps.py)

			[Hero] Etienne
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-0
			tack 5-2-0
			glue 2-5-0
			
			sniper 1-0-0
			ace 2-0-3
			
			wizard 5-0-2
			ninja 0-4-0
			alch 3-2-0
			
			spike 3-2-0
			village 4-0-2
			_______________________________________
			
### Middle Of The Road
- Hard
	- [Chimps](../btd6bot/plans/middle_of_the_roadHardChimps.py)

			[Hero] Sauda
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			glue 0-2-4
			
			sniper 0-0-0
			heli 5-0-5
			
			village 2-3-0
			_______________________________________
			If price change to heli where 3-0-0 not available for round 28, please update to pop lead bloons.
			Copy of tinkertonHardChimps (tower position changed).
			
### Midnight Mansion
- Hard
	- [Chimps](../btd6bot/plans/midnight_mansionHardChimps.py)

			[Hero] Ezili
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-0
			ice 4-1-0
			glue 0-2-4
			
			sniper 1-3-2
			
			wizard 0-2-5
			ninja 1-4-5
			alch 3-0-0
			druid 1-5-0
			
			village 3-0-2
			_______________________________________
			
### Monkey Meadow
- Easy
	- [Standard](../btd6bot/plans/monkey_meadowEasyStandard.py)

			[Hero] Quincy
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			sniper 2-0-4
			
			ninja 4-0-1
			alch 3-2-0
			_______________________________________
			
### Muddy Puddles
- Hard
	- [Chimps](../btd6bot/plans/muddy_puddlesHardChimps.py)

			[Hero] Rosalia
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			boomer 0-0-0
			
			sniper 0-1-0
			sub 2-0-3
			boat 0-0-2
			ace 2-0-5
			
			alch 3-0-1
			village 2-2-2
			
			engineer 0-0-0
			_______________________________________
			
### Off The Coast
- Hard
	- [Chimps](../btd6bot/plans/off_the_coastHardChimps.py)

			[Hero] Psi
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-0
			glue 0-2-4
			desperado 5-2-0
			
			sniper 1-0-0
			boat 5-2-0
			ace 5-0-2
			
			alch 4-0-1
			mermonkey 4-0-0
			
			village 2-3-0
			_______________________________________
			
### Pat's Pond
- Hard
	- [Chimps](../btd6bot/plans/pat's_pondHardChimps.py)

			[Hero] Obyn
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-3-2
			tack 2-0-5
			
			sniper 0-2-5
			
			alch 5-0-0
			
			spike 2-3-0
			village 4-2-0
			_______________________________________
			
### Peninsula
- Hard
	- [Chimps](../btd6bot/plans/peninsulaHardChimps.py)

			[Hero] Psi
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-3-2
			glue 0-2-4
			
			sniper 1-0-0
			ace 2-0-4
			mortar 0-2-4
			
			alch 4-2-0
			mermonkey 4-0-0
			
			spike 2-5-0
			village 2-2-0
			engineer 0-3-3
			_______________________________________
			
### Quad
- Hard
	- [Chimps](../btd6bot/plans/quadHardChimps.py)

			[Hero] Sauda
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-0
			boomer 0-2-4
			bomb 0-3-0
			tack 2-0-5
			ice 4-1-1
			glue 0-2-4
			
			sniper 1-1-0
			heli 0-2-3
			
			wizard 0-3-2
			alch 4-2-0
			druid 0-1-2
			
			spike 4-0-2
			village 3-0-2
			engineer 3-3-2
			_______________________________________
			Depends on rng a bit, but should be quite consistent.
			Rounds 37-40, in particular 40, can leak randomly: the issue is with how quickly bot detects round change and times ability use correctly, and sometimes ability is not required at all if wizard firewall timing is just right.
			Round 100 has unfortunately some rng as well.
			
### Ravine
- Hard
	- [Chimps](../btd6bot/plans/ravineHardChimps.py)

			[Hero] Psi
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-3-0
			boomer 0-2-4
			bomb 4-2-0
			glue 2-2-4
			
			sub 0-4-0
			mortar 0-0-4
			
			wizard 5-2-0
			alch 4-2-1
			druid 1-3-0
			
			spike 3-0-3
			village 2-0-2
			engineer 0-3-2
			_______________________________________
			
### Sanctuary
- Easy
	- [Standard](../btd6bot/plans/sanctuaryEasyStandard.py)

			[Hero] Psi
			[Monkey Knowledge] -
			---------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-1
			boomer 4-0-2
			
			sniper 3-1-2
			_______________________________________
			Derived from sanctuary_HardChimps.
			
- Hard
	- [Chimps](../btd6bot/plans/sanctuaryHardChimps.py)

			[Hero] Psi
			[Monkey Knowledge] -
			---------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-1
			boomer 5-0-2
			glue 5-2-0
			
			sniper 4-2-2
			
			alch 4-0-1
			mermonkey 2-0-5
			
			village 3-2-0
			_______________________________________
			-Has some rng, but you should be able to succeed within a few attempts.
			
	- [Standard](../btd6bot/plans/sanctuaryHardStandard.py)

			[Hero] Psi
			[Monkey Knowledge] -
			---------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-1
			boomer 4-0-2
			glue 5-2-0
			
			sniper 4-1-2
			
			alch 4-0-1
			mermonkey 2-0-4
			
			village 3-2-0
			_______________________________________
			Derived from sanctuary_HardChimps. Some lives will be lost in early game.
			
- Medium
	- [Standard](../btd6bot/plans/sanctuaryMediumStandard.py)

			[Hero] Psi
			[Monkey Knowledge] -
			---------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-1
			boomer 4-0-2
			glue 4-2-0
			
			sniper 3-1-2
			
			alch 4-0-1
			mermonkey 2-0-4
			
			village 3-2-0
			_______________________________________
			Derived from sanctuary_HardChimps.
			
### Spa Pits
- Hard
	- [Chimps](../btd6bot/plans/spa_pitsHardChimps.py)

			[Hero] Sauda
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			glue 0-2-4
			
			sniper 0-0-0
			heli 5-0-5
			
			village 2-3-0
			_______________________________________
			If price change to heli where 3-0-0 not available for round 28, please update to pop lead bloons.
			Copy of tinkertonHardChimps (tower position changed).
			
### Spillway
- Hard
	- [Chimps](../btd6bot/plans/spillwayHardChimps.py)

			[Hero] Psi
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			ice 0-3-0
			
			sniper 0-0-0
			ace 2-0-4
			
			wizard 5-2-0
			ninja 2-0-4
			alch 3-2-0
			
			spike 2-5-0
			village 2-0-2
			engineer 0-3-1
			_______________________________________
			
### Sunken Columns
- Hard
	- [Chimps](../btd6bot/plans/sunken_columnsHardChimps.py)

			[Hero] Sauda
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-0
			glue 0-2-4
			
			sniper 2-5-5
			
			alch 5-2-0
			
			village 2-0-2
			engineer 0-3-0
			_______________________________________
			
### Sunset Gulch
- Hard
	- [Chimps](../btd6bot/plans/sunset_gulchHardChimps.py)

			[Hero] Churchill
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-2-5
			ice 0-1-4
			glue 0-2-4
			desperado 2-5-0
			
			sniper 1-0-0
			
			alch 3-2-1
			druid 3-0-2
			
			spike 4-4-2
			village 2-0-2
			engi 0-4-0
			_______________________________________
			
### Tinkerton
- Hard
	- [Chimps](../btd6bot/plans/tinkertonHardChimps.py)

			[Hero] Sauda
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			glue 0-2-4
			
			sniper 0-0-0
			heli 5-0-5
			
			village 2-3-0
			_______________________________________
			If price change to heli where 3-0-0 not available for round 28, please update to pop lead bloons.
			
### Underground
- Hard
	- [Chimps](../btd6bot/plans/undergroundHardChimps.py)

			[Hero] Geraldo
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-0
			boomer 0-2-4
			tack 5-0-2
			ice 4-2-0
			glue 0-2-3
			
			sniper 1-0-0
			
			ninja 4-0-2
			alch 4-2-1
			
			village 4-3-2
			_______________________________________
			Strat is build around testing Geraldo so it's bit scuffed and unoptimized.
			Still, should work quite consistently with minimal rng.
			
### Workshop
- Hard
	- [Chimps](../btd6bot/plans/workshopHardChimps.py)

			[Hero] Gwen
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-0
			boomer 2-0-4
			tack 2-0-5
			ice 4-1-0
			glue 0-2-5
			
			mortar 1-0-4
			
			alch 4-2-1
			druid 2-3-0
			
			spike 4-2-5
			village 3-0-2
			_______________________________________
			
### X Factor
- Hard
	- [Chimps](../btd6bot/plans/x_factorHardChimps.py)

			[Hero] Obyn
			[Monkey Knowledge] -
			-------------------------------------------------------------
			===Monkeys & upgrades required===
			dart 0-0-0
			
			sniper 2-2-5
			
			super 3-2-2
			ninja 2-2-0
			alch 5-2-0
			
			village 2-0-2
			_______________________________________
			Similar to maps like Erosion, sometimes bot can detect next round(s) too early because there are too many projectiles/bloons moving around round label, causing false positives. 
			Good thing is, this doesn't affect gameplay for this particular plan as ability timings are not needed late game.
			This only affects saved round times: some rounds could immediately skip over, causing other rounds falsely display extremely long durations.
			
