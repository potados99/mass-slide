#-*- coding: utf-8 -*-

import re

DRAFTS = 'home/pi/Projects/massSlide/drafts'

RAW = DRAFTS + '/raw'
PROCESSED = DRAFTS + '/processed'
DONE = DRAFTS + '/done'

def write_raw():
	return nul

def read_raw(new):
	rawList = [
		RAW + 'automated/cover.txt', 
		RAW + 'automated/pardon.txt', 
		RAW + 'automated/collect.txt', 
		RAW + 'automated/first_reading', 
		RAW + 'automated/second_reading', 
		RAW + 'automated/acclamation.txt', 
		RAW + 'automated/gospel.txt', 
		RAW + 'automated/antiphon.txt', 
		RAW + 'chants',
		RAW + 'prayers',
		RAW + 'quiz'
	]

	return nul




def write_processed(new):
	return nul

def read_processed(new):
 	return nul




def write_done(new):
	return nul

def read_done(filename):
	f = open(DONE + '/' + filename + '.txt', 'r')
	rawText = f.read()
	f.close

        chapterList = [x.split('\n') for x in rawText.split('#')]
	chapterList.pop(0)

	for chapter in chapterList:
		while chapter[1] == '':
			chapter.pop(1)

	return chapterList

