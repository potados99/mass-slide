#-*- coding: utf-8 -*-

import re

DRAFTS = '/home/pi/Projects/massSlide/drafts'
RAW = DRAFTS + '/raw'
PROCESSED = DRAFTS + '/processed'
DONE = DRAFTS + '/done'

def read_file(file):
	f = open(file, 'r')
	rawText = f.read().decode("utf8")
	f.close
	return rawText

def parse():
	return nul

def convert_title(title, eng):
	titleList = [
		['표지', 'cover'],
		['입당송', 'pardon'],
		['본기도', 'collect'],
		['제1독서', 'first_reading'],
		['제2독서', 'second_reading'],
		['복음환호송', 'acclamation'],
		['복음', 'gospel'],
		['영성체송', 'antiphon'],
		['성가', 'chants'],
		['보편지향기도', 'prayers'],
		['강론', 'quiz']
	]

	if eng: lang = 1
	else: lang = 0

	for line in titleList:
		if title in line:
			return line[lang]


def write_raw():
	return nul

def get_raw_list():
	rawFileList = [
		RAW + '/automated/cover.txt', 
		RAW + '/automated/pardon.txt', 
		RAW + '/automated/collect.txt', 
		RAW + '/automated/first_reading.txt', 
		RAW + '/automated/second_reading.txt', 
		RAW + '/automated/acclamation.txt', 
		RAW + '/automated/gospel.txt', 
		RAW + '/automated/antiphon.txt', 
		RAW + '/chants.txt',
		RAW + '/prayers.txt',
		RAW + '/quiz.txt'
	]

	rawDict = {}

	r = re.compile('.+/(.+)\.txt')

	for rawFile in rawFileList:
		rawText = read_file(rawFile)

		chapterList = rawText.split('\n')
		match = r.search(rawFile)
		title = convert_title(title=match.group(1), eng=False)

		rawDict[title] = chapterList

	return rawDict


def write_processed(new):
	return nul

def get_processed_list(new):
 	return nul




def write_done(new):
	return nul

def get_done_list(filename):
	rawText = read_file(DONE + '/' + filename + '.txt', 'r')

        chapterList = [x.split('\n') for x in rawText.split('#')]
	chapterList.pop(0)

	for chapter in chapterList:
		while chapter[1] == '':
			chapter.pop(1)

	return chapterList



"""
Dict = get_raw_list()

for title in Dict:
	print (title)
	for lines in Dict[title]:
		print lines

"""
