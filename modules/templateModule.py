#-*- coding: utf-8 -*-

import re

PR_PATH = 'home/pi/Projects/massSlide'

RAW_PATH = PR_PATH + '/raw'
PRE_READY_PATH = PR_PATH + '/pre-ready'
PPTX_READY_PATH = PR_PATH + '/ready'

def read_pptx_ready(filename):
	f = open(PPTX_READY_PATH + '/' + filename + '.txt', 'r')
	rawText = f.read()
	f.close

        chapterList = [x.split('\n') for x in rawText.split('#')]
	chapterList.pop(0)

	for chapter in chapterList:
		while chapter[1] == '':
			chapter.pop(1)

	return chapterList

def read_raw(new):
	rawList = [
		RAW_PATH + 'automated/cover.txt', 
		RAW_PATH + 'automated/pardon.txt', 
		RAW_PATH + 'automated/collect.txt', 
		RAW_PATH + 'automated/first_reading', 
		RAW_PATH + 'automated/second_reading', 
		RAW_PATH + 'automated/acclamation.txt', 
		RAW_PATH + 'automated/gospel.txt', 
		RAW_PATH + 'automated/antiphon.txt', 
		RAW_PATH + 'chants',
		RAW_PATH + 'prayers',
		RAW_PATH + 'quiz'
	]

	return nul

def write_pre_ready(new):
	return nul

def write_pptx_ready(new):
	return nul

