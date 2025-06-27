"""
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
"""

from._plan_imports import *

def play(rounds: tuple[str, str, str, int, int, str]) -> None:
    BEGIN, END = menu_start.load(*rounds)
    current_round = BEGIN-1
    map_start = time()
    while current_round < END+1:
        current_round = Rounds.round_check(current_round, map_start)
        if current_round == BEGIN:     
            dart_left = Monkey('dart', 0.2088541666667, 0.5185185185185)
            dart_right = Monkey('dart', 0.6677083333333, 0.5259259259259)
            dart_top = Monkey('dart', 0.4072916666667, 0.237037037037)
        elif current_round == 7:
            dart_right.target('strong')
        elif current_round == 8:
            dart_right.target('first')
            dart_bot = Monkey('dart', 0.4354166666667, 0.7787037037037)
        elif current_round == 9:
            dart_left.target('strong')
            sniper_tl = Monkey('sniper', 0.2885416666667, 0.2796296296296)
            sniper_tl.target('strong')
            dart_left.target('first')
        elif current_round == 12:
            hero = Hero(0.4614583333333, 0.2351851851852)
        elif current_round == 14:
            engi = Monkey('engineer', 0.2260416666667, 0.5703703703704)
        elif current_round == 15:
            sniper_br = Monkey('sniper', 0.5989583333333, 0.7305555555556)
            sniper_br.target('strong')
        elif current_round == 17:
            engi.upgrade(['1-0-0'])
        elif current_round == 19:
            sniper_tl.upgrade(['1-0-0'])
        elif current_round == 20:
            sniper_br.upgrade(['1-0-0'])
        elif current_round == 23:
            spike_bl = Monkey('spike', 0.1921875, 0.7601851851852)
        elif current_round == 27:
            engi.upgrade(['2-0-0', '3-0-0'])
        elif current_round == 28:
            engi.upgrade(['3-0-1', '3-0-2'])
        elif current_round == 32:
            village_tr = Monkey('village', 0.5234375, 0.162037037037)
        elif current_round == 34:
            village_tr.upgrade(['0-0-1', '0-0-2'])
            wizard_tr = Monkey('wizard', 0.4880208333333, 0.2805555555556)
            wizard_tr.upgrade(['0-1-0'])
        elif current_round == 35:
            sniper_br.target('first')
        elif current_round == 36:
            wizard_tr.upgrade(['0-2-0', '0-2-1'])
            wizard_tr.upgrade(['0-2-2'])
            sniper_br.target('strong')
        elif current_round == 37:
            village_tr.upgrade(['1-0-2', '2-0-2'])
        elif current_round == 38:
            ability(1, 5)
        elif current_round == 39:
            wizard_tr.upgrade(['0-3-2'])
        elif current_round == 40:
            ability(1, 2.25)
        elif current_round == 41:
            sniper_tl.upgrade(['1-1-0'])
            sniper_tl.special()
            spike_bl.upgrade(['1-0-0', '1-0-1', '1-0-2'])
            spike_bl.target('smart')
        elif current_round == 43:
            village_bl = Monkey('village', 0.2578125, 0.7314814814815)
            village_bl.upgrade(['0-0-1', '0-0-2'])
            wizard_bl = Monkey('wizard', 0.3296875, 0.6824074074074)
            wizard_bl.upgrade(['0-1-0'])
        elif current_round == 44:
            wizard_bl.upgrade(['0-2-0'])
        elif current_round == 46:
            wizard_bl.upgrade(['0-3-0', '0-3-1', '0-3-2'])
        elif current_round == 48:
            village_bl.upgrade(['1-0-0', '2-0-0'])
            alch_bl = Monkey('alch', 0.1816666666667, 0.8212962962963)
            alch_bl.upgrade(['1-0-0', '2-0-0', '3-0-0'])
            spike_bl.target('close')
        elif current_round == 49:
            spike_tr = Monkey('spike', 0.5536458333333, 0.2314814814815)
            spike_tr.upgrade(['1-0-0', '2-0-0', '3-0-0', '3-0-1', '3-0-2'])
            spike_tr.target('smart')
        elif current_round == 50:
            alch_tr = Monkey('alch', 0.5713541666667, 0.1722222222222)
            alch_tr.upgrade(['1-0-0', '2-0-0', '3-0-0'])
        elif current_round == 51:
            spike_bl.upgrade(['2-0-2'])
        elif current_round == 52:
            spike_bl.upgrade(['3-0-2'])
        elif current_round == 54:
            click(0.4328125, 0.0388888888889)
            click(0.4932291666667, 0.2953703703704)
            tack_top = Monkey('tack', 0.4380208333333, 0.1898148148148)
            tack_top.upgrade(['0-0-1', '0-0-2', '0-0-3'])
        elif current_round == 55:
            tack_top.upgrade(['0-0-4', '1-0-4', '2-0-4'])
        elif current_round == 60:
            ability(1, 8)
        elif current_round == 62:
            spike_bl.upgrade(['4-0-2'])
        elif current_round == 64:
            hero.target('close')
            wizard_tr.target('close')
        elif current_round == 68:
            spike_tr.upgrade(['4-0-2'])
        elif current_round == 69:
            tack_b1 = Monkey('tack', 0.3526041666667, 0.8527777777778)
            tack_b1.upgrade(['0-0-1', '0-0-2', '0-0-3'])
        elif current_round == 71:
            tack_b1.upgrade(['0-0-4', '1-0-4', '2-0-4'])
            tack_b2 = Monkey('tack', 0.3296875, 0.8138888888889)
        elif current_round == 73:
            tack_b2.upgrade(['0-0-1', '0-0-2', '0-0-3'])
        elif current_round == 74:
            tack_b2.upgrade(['0-0-4', '1-0-4', '2-0-4'])
        elif current_round == 75:
            alch_b1 = Monkey('alch', 0.3276041666667, 0.9064814814815)
            alch_b1.upgrade(['1-0-0', '2-0-0', '3-0-0', '3-1-0', '3-2-0'])
            alch_b2 = Monkey('alch', 0.3067708333333, 0.8527777777778)
        elif current_round == 77:
            alch_b2.upgrade(['1-0-0', '2-0-0', '3-0-0', '3-1-0', '3-2-0'])
        elif current_round == 78:
            glue_top = Monkey('glue', 0.4911458333333, 0.1064814814815)
            glue_top.upgrade(['0-0-1', '0-0-2', '0-0-3', '0-1-3', '0-2-3'])
            glue_top.target('strong')
        elif current_round == 79:
            glue_top.upgrade(['0-2-4'])
            village_bl.upgrade(['3-0-2'])
            village_tr.upgrade(['3-0-2'])
        elif current_round == 80:
            click(0.4364583333333, 0.8861111111111)
            click(0.4916666666667, 0.8611111111111)
            ice_bot = Monkey('ice', 0.3895833333333, 0.7712962962963)
        elif current_round == 81:
            ice_bot.upgrade(['1-0-0', '2-0-0', '3-0-0', '4-0-0', '4-1-0'])
        elif current_round == 82:
            glue_bot = Monkey('glue', 0.36875, 0.7305555555556)
            glue_bot.upgrade(['0-0-1', '0-0-2', '0-0-3', '0-0-4'])
            glue_bot.target('strong')
        elif current_round == 83:
            glue_bot.upgrade(['0-1-4', '0-2-4'])
        elif current_round == 84:
            boomer_top = Monkey('boomer', 0.5229166666667, 0.0787037037037)
            boomer_top.upgrade(['0-0-1', '0-0-2', '0-0-3', '0-0-4', '0-1-4', '0-2-4'])
            boomer_top.target('strong')
            boomer_bot = Monkey('boomer', 0.2546875, 0.937962962963)
            boomer_bot.upgrade(['0-0-1', '0-0-2', '0-0-3', '0-0-4', '0-1-4', '0-2-4'])
            boomer_bot.target('strong')
        elif current_round == 85:
            boomer_bot2 = Monkey('boomer', 0.2505208333333, 0.8768518518519)
            boomer_bot2.upgrade(['0-0-1', '0-0-2', '0-0-3'])
            boomer_bot2.target('strong')
        elif current_round == 86:
            boomer_bot2.upgrade(['0-0-4', '0-1-4', '0-2-4'])
        elif current_round == 87:
            engi2 = Monkey('engineer', 0.3869791666667, 0.6787037037037)
            engi2.upgrade(['0-1-0', '0-2-0', '0-3-0', '0-3-1'])
            engi2.special(1, 0.4359375, 0.9527777777778)
        elif current_round == 88:
            engi3 = Monkey('engineer', 0.5578125, 0.0314814814815)
            engi3.upgrade(['0-1-0', '0-2-0', '0-3-0', '0-3-1'])
            engi3.special(1, 0.3765625, 0.0453703703704)
        elif current_round == 89:
            sauda_alch = Monkey('alch', 0.4390625, 0.2805555555556)
            sauda_alch.upgrade(['1-0-0', '2-0-0', '3-0-0', '3-1-0', '3-2-0'])
        elif current_round == 91:
            alch_top = Monkey('alch', 0.38125, 0.1138888888889)
            alch_top.upgrade(['1-0-0', '2-0-0', '3-0-0', '3-1-0', '3-2-0'])
        elif current_round == 92:
            boomer_top2 = Monkey('boomer', 0.5864583333333, 0.2833333333333)
            boomer_top2.upgrade(['0-0-1', '0-0-2', '0-0-3', '0-0-4', '0-1-4', '0-2-4'])
            boomer_top2.target('strong')
        elif current_round == 96:
            tack_top.upgrade(['2-0-5'])
        elif current_round == 97:
            heli = Monkey('heli', 0.2885416666667, 0.5824074074074)
            heli.target('lock', 0.3083333333333, 0.7111111111111)
            ice_top = Monkey('ice', 0.4723958333333, 0.3342592592593)
        elif current_round == 98:
            ability(1, 8)
            ability(2, 10)
            heli.upgrade(['0-0-1', '0-0-2', '0-0-3', '0-1-3', '0-2-3'])
            ice_top.upgrade(['1-0-0', '2-0-0', '3-0-0', '4-0-0', '4-0-1'])
            alch_top.upgrade(['4-2-0'])
        elif current_round == 99:
            bomb = Monkey('bomb', 0.5151041666667, 0.3703703703704)
            bomb.upgrade(['0-1-0', '0-2-0', '0-3-0'])
            bomb.target('strong')
        elif current_round == 100:
            druid = Monkey('druid', 0.3807291666667, 0.2796296296296)
            druid.upgrade(['0-0-1','0-0-2','0-1-2'])
            heli.special(1, 0.6057291666667, 0.3527777777778)
            ability(1, 6)
            ability(2, 7.5)