#-*- coding: utf-8 -*-

SMALL_FONT_LIST = [

	'성호경',
	'고백기도',
	'축복',
	'영성체',
	'강복',
	'평화의인사'
]

MEDIUM_FONT_LIST = [

	'표지',
	'입당송',
	'입당성가',
	'자비송',
	'본기도',
	'제1독서',
	'제2독서',
	'복음환호송',
	'복음',
	'강론',
	'보편지향기도',
	'봉헌성가',
	'거룩하시도다',
	'영성체송',
	'성체성가1',
	'성체성가2',
	'성체성가3',
	'파견성가'
]

BIG_FONT_LIST = [
]

def font_size(x):
	return {'big': 115, 'medium': 88, 'small': 72, 'tiny': 65}.get(x, '88')

def set_font_size(title):
	if title in SMALL_FONT_LIST:
		return font_size('small')

	elif title in MEDIUM_FONT_LIST:
		return font_size('medium')

	elif title in BIG_FONT_LIST:
		return font_size('big')

	else:
		return font_size('medium')
