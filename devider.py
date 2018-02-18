#-*- coding: utf-8 -*-
import re

TEMPLATE = './template.txt'

def readTemplate():
	print('opening template.txt')
	f = open(TEMPLATE, 'r')
#	rawText = unicode(f.read(), 'utf-8')
	rawText = f.read()
	f.close
	return rawText

# Split raw text by chapters(#) and split each chapters by lines(\n)
def makeChapterList(raw):
        chapterList = [x.split('\n') for x in raw.split('#')]
        return chapterList


out = makeChapterList(readTemplate())
	
print (out)
