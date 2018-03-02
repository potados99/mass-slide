#-*- coding: utf-8 -*-

SMALL_FONT_LIST = [
	'성호경',
	'신앙고백'
]

MEDIUM_FONT_LIST = [
	'입당송'
	'입당성가'
]

BIG_FONT_LIST = [
]

def fontSize(x):
	return {'big': 115, 'medium': 88, 'small': 75}.get(x, '88')

def setFontSize(t):
	if t in SMALL_FONT_LIST:
		return fontSize('small')

	elif t in MEDIUM_FONT_LIST:
		return fontSize('medium')

	elif t in BIG_FONT_LIST:
		return fontSize('big')

	else:
		return fontSize('medium')
