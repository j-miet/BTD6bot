"""
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
"""

from._plan_imports import *

def play(data):
	BEGIN, END = menu_start.load(*data)
	round = BEGIN-1
	map_start = time()
	while round < END+1:
		round = Rounds.round_check(round, map_start, data[2])
		if round == BEGIN:
			sub1 = Monkey('sub', 0.5640625, 0.4009259259259)
			dart1 = Monkey('dart', 0.4526041666667, 0.6083333333333)
			dart1.target('last')
		elif round == 7:
			dart2 = Monkey('dart', 0.3057291666667, 0.4490740740741)
		elif round == 10:
			hero = Hero(0.4244791666667, 0.4138888888889)
		elif round == 12:
			druid1 = Monkey('druid', 0.3848958333333, 0.4101851851852)
		elif round == 14:
			druid2 = Monkey('druid', 0.3557291666667, 0.3694444444444)
		elif round == 15:
			druid3 = Monkey('druid', 0.4640625, 0.4138888888889)
		elif round == 18:
			druid4 = Monkey('druid', 0.4057291666667, 0.3583333333333)
		elif round == 19:
			druid5 = Monkey('druid', 0.4473958333333, 0.3583333333333)
		elif round == 21:
			druid6 = Monkey('druid', 0.5036458333333, 0.412037037037)
		elif round == 22:
			dart2.upgrade(['0-0-1','0-0-2'])
		elif round == 23:
			druid1.upgrade(['0-1-0','0-1-1'])
		elif round == 24:
			druid2.upgrade(['0-1-0','0-1-1'])
		elif round == 26:
			druid3.upgrade(['0-1-0','0-1-1'])
		elif round == 27:
			druid4.upgrade(['0-1-0','0-1-1'])
		elif round == 28:
			druid5.upgrade(['0-1-0','0-1-1'])
		elif round == 29:
			druid6.upgrade(['0-1-0','0-1-1'])
		elif round == 31:
			spike = Monkey('spike', 0.790625, 0.5101851851852)
		elif round == 33:
			spike.upgrade(['1-0-0'])
		elif round == 35:
			spike.upgrade(['1-0-1', '1-0-2', '1-0-3'])
			spike.target('close')
		elif round == 36:
			druid1.upgrade(['0-1-2', '0-1-3'])
		elif round == 37:
			druid2.upgrade(['0-1-2','0-1-3'])
		elif round == 38:
			druid3.upgrade(['0-1-2','0-1-3'])
		elif round == 39:
			druid4.upgrade(['0-1-2','0-1-3'])
			druid5.upgrade(['0-1-2','0-1-3'])
		elif round == 41:
			druid6.upgrade(['0-1-2','0-1-3'])
		elif round == 42:
			village = Monkey('village', 0.4473958333333, 0.2787037037037)
		elif round == 43:
			village.upgrade(['1-0-0','2-0-0'])
		elif round == 44:
			alch1 = Monkey('alch', 0.4067708333333, 0.2305555555556)
		elif round == 45:
			alch1.upgrade(['1-0-0','2-0-0','3-0-0','3-0-1'])
		elif round == 47:
			druid3.upgrade(['0-1-4'])
		elif round == 48:
			druid2.upgrade(['0-1-4'])
		elif round == 49:
			druid4.upgrade(['0-1-4'])
			druid1.upgrade(['0-1-4'])
		elif round == 51:
			druid5.upgrade(['0-1-4'])
		elif round == 52:
			druid6.upgrade(['0-1-4'])
		elif round == 54:
			alch1.upgrade(['4-0-1'])
		elif round == 55:
			spike.upgrade(['1-0-4','2-0-4'])
		elif round == 79:
			druid1.upgrade(['0-1-5'])
			alch2 = Monkey('alch', 0.3734375, 0.2240740740741)
		elif round == 80:
			alch2.upgrade(['1-0-0','2-0-0','3-0-0'])
		elif round == 81:
			alch2.upgrade(['4-0-0','4-0-1'])
		elif round == 83:
			village.upgrade(['2-1-0','2-2-0','2-3-0'])
		elif round == 94:
			spike.upgrade(['2-0-5'])
		elif round == 95:
			alch3 = Monkey('alch', 0.7869791666667, 0.5851851851852)
			alch3.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-0-1'])
		elif round == 96:
			alch4 = Monkey('alch', 0.4859375, 0.3277777777778)
			alch4.upgrade(['1-0-0','2-0-0','3-0-0','4-0-0','4-0-1'])