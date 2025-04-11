"""
[Plan Name] dark_CastleHardChimps
[Game Version] 48
[Hero] Obyn
[Monkey Knowledge] -
-------------------------------------------------------------
===Monkeys required===
dart 0-0-0
sub 0-0-0
druid 0-1-5
alch 4-2-1
village 2-3-0
spike 2-0-5
_______________________________________
Strategy: https://www.youtube.com/watch?v=JXWhHHX9vdk

Made slight adjustments to run:
1. bought a 1-0-3 spike before r40 to avoid Obyn's brambles & totem rng
2. upgraded all druid to 1-0-3 before getting alch/village for better dps
"""

from._plan_imports import *

def play(rounds: tuple[str, str, str, int, int, str]) -> None:
	BEGIN, END = menu_start.load(*rounds)
	current_round = BEGIN-1
	map_start = time()
	while current_round < END+1:
		current_round = Rounds.round_check(current_round, map_start)
		if current_round == BEGIN:
			sub1 = Monkey('sub', 0.5640625, 0.4009259259259)
			dart1 = Monkey('dart', 0.4526041666667, 0.6083333333333)
			dart1.target('last')
		elif current_round == 7:
			dart2 = Monkey('dart', 0.3057291666667, 0.4490740740741)
		elif current_round == 10:
			hero = Hero(0.4244791666667, 0.4138888888889)
		elif current_round == 12:
			druid1 = Monkey('druid', 0.3848958333333, 0.4101851851852)
		elif current_round == 14:
			druid2 = Monkey('druid', 0.3557291666667, 0.3694444444444)
		elif current_round == 15:
			druid3 = Monkey('druid', 0.4640625, 0.4138888888889)
		elif current_round == 18:
			druid4 = Monkey('druid', 0.4057291666667, 0.3583333333333)
		elif current_round == 19:
			druid5 = Monkey('druid', 0.4473958333333, 0.3583333333333)
		elif current_round == 21:
			druid6 = Monkey('druid', 0.5036458333333, 0.412037037037)
		elif current_round == 22:
			dart2.upgrade(['0-0-1','0-0-2'])
		elif current_round == 23:
			druid1.upgrade(['0-1-0','0-1-1'])
		elif current_round == 24:
			druid2.upgrade(['0-1-0','0-1-1'])
		elif current_round == 26:
			druid3.upgrade(['0-1-0','0-1-1'])
		elif current_round == 27:
			druid4.upgrade(['0-1-0','0-1-1'])
		elif current_round == 28:
			druid5.upgrade(['0-1-0','0-1-1'])
		elif current_round == 29:
			druid6.upgrade(['0-1-0','0-1-1'])
		elif current_round == 31:
			spike = Monkey('spike', 0.790625, 0.5101851851852)
		elif current_round == 33:
			spike.upgrade(['1-0-0'])
		elif current_round == 35:
			spike.upgrade(['1-0-1', '1-0-2', '1-0-3'])
			spike.target('close')
		elif current_round == 36:
			druid1.upgrade(['0-1-2', '0-1-3'])
		elif current_round == 37:
			druid2.upgrade(['0-1-2','0-1-3'])
		elif current_round == 38:
			druid3.upgrade(['0-1-2','0-1-3'])
		elif current_round == 39:
			druid4.upgrade(['0-1-2','0-1-3'])
			druid5.upgrade(['0-1-2','0-1-3'])
		elif current_round == 41:
			druid6.upgrade(['0-1-2','0-1-3'])
		elif current_round == 42:
			village = Monkey('village', 0.4473958333333, 0.2787037037037)
		elif current_round == 43:
			village.upgrade(['1-0-0','2-0-0'])
		elif current_round == 44:
			alch1 = Monkey('alch', 0.4067708333333, 0.2305555555556)
		elif current_round == 45:
			alch1.upgrade(['1-0-0','2-0-0','3-0-0','3-0-1'])
		elif current_round == 47:
			druid3.upgrade(['0-1-4'])
		elif current_round == 48:
			druid2.upgrade(['0-1-4'])
		elif current_round == 49:
			druid4.upgrade(['0-1-4'])
			druid1.upgrade(['0-1-4'])
		elif current_round == 51:
			druid5.upgrade(['0-1-4'])
		elif current_round == 52:
			druid6.upgrade(['0-1-4'])
		elif current_round == 54:
			alch1.upgrade(['4-0-1'])
		elif current_round == 55:
			spike.upgrade(['1-0-4','2-0-4'])
		elif current_round == 79:
			druid1.upgrade(['0-1-5'])
			alch2 = Monkey('alch', 0.3734375, 0.2240740740741)
		elif current_round == 80:
			alch2.upgrade(['1-0-0','2-0-0','3-0-0'])
		elif current_round == 81:
			alch2.upgrade(['4-0-0','4-0-1'])
		elif current_round == 83:
			village.upgrade(['2-1-0','2-2-0','2-3-0'])
		elif current_round == 94:
			spike.upgrade(['2-0-5'])
		elif current_round == 95:
			alch3 = Monkey('alch', 0.7869791666667, 0.5851851851852)
			alch3.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-1-0','4-2-0'])
		elif current_round == 96:
			alch4 = Monkey('alch', 0.4859375, 0.3277777777778)
			alch4.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-0-1'])