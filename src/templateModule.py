#-*- coding: utf-8 -*-
import re

TEMPLATE_PATH='/home/pi/Projects/massSlide/templates'

def readTemplate(template):
	print('opening template.txt')
	f = open(TEMPLATE_PATH + '/' + template + '.txt', 'r')
#	rawText = unicode(f.read(), 'utf-8')
	rawText = f.read()
	f.close
	return rawText

# Split raw text by chapters(#) and split each chapters by lines(\n)
def makeChapterList(raw):
        chapterList = [x.split('\n') for x in raw.split('#')]
	chapterList.pop(0)
	return chapterList

def writeTemplate(new):
	return nul



