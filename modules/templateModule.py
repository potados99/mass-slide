#-*- coding: utf-8 -*-

import re

TEMPLATE_PATH='/home/pi/Projects/massSlide/templates'

def read_template(template):
	f = open(TEMPLATE_PATH + '/' + template + '.txt', 'r')
	rawText = f.read()
	f.close
	return rawText

# Split raw text by chapters(#) and split each chapters by lines(\n)
def make_chapterList(raw):
        chapterList = [x.split('\n') for x in raw.split('#')]
	chapterList.pop(0)
	return chapterList

def delete_space(List):
	for chapter in List:
		while chapter[1] == '': # until not empty space
			chapter.pop(1)
	return List

def write_template(new):
	return nul



