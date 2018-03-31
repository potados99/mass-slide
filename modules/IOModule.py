#-*- coding: utf-8 -*-

import re
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

DRAFTS = '/home/pi/Projects/massSlide/drafts'
RAW = DRAFTS + '/raw'
PROCESSED = DRAFTS + '/processed'
DONE = DRAFTS + '/done'
TEMPLATE = '/home/pi/Projects/massSlide/templates'

def read_file(file):
	f = open(file, 'r')
	rawText = f.read()
	f.close
	return rawText

def write_file(file, chapterList):
	f = open(file, 'w')
	for chapter in chapterList:
		for line in chapter:   
 			f.write(line + '\n')
	f.close()

def get_chapter_list(rawText, original):
        chapterList = [x.split('\n') for x in rawText.split('# ')]
	chapterList.pop(0)

	if original:
		for chapter in chapterList:
			chapter[0] = '# ' + chapter[0]
	else:
		for chapter in chapterList:
			while (chapter[1] == '') and (len(chapter) >= 3):
				chapter.pop(1)
	
	for chapter in chapterList:
		chapter.pop(-1)

	return chapterList

def convert_title(title, eng):
	titleList = [
		['표지', 'cover'],
		['입당송', 'pardon'],
		['본기도', 'collect'],
		['제1독서', 'first_reading'],
		['제2독서', 'second_reading'],
		['복음환호송', 'acclamation'],
		['부속가', 'sequence'],
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

def get_raw_chapter_dict(template):
	rawFileList = [
		RAW + '/chants.txt',
		RAW + '/prayers.txt',
		RAW + '/quiz.txt'
	]
	
	filenameSet = read_file(TEMPLATE + '/' + template + '_updates.txt').split('\n')

	for filename in filenameSet:
		if not filename is '':
			rawFileList.append(RAW + '/automated/' + filename)

	rawDict = {}

	r = re.compile('.+/(.+)\.txt')

	for rawFile in rawFileList:
		rawText = read_file(rawFile)

		chapterList = rawText.split('\n')
		match = r.search(rawFile)
		title = convert_title(title=match.group(1), eng=False)

		rawDict[title] = chapterList

	return rawDict

def write_processed(fileName, chapterList):
	write_file(file=PROCESSED + '/' + fileName + '.txt', chapterList=chapterList)

def get_processed_chapter_list(fileName):
	rawText = read_file(file=PROCESSED + '/' + fileName + '.txt')
	return get_chapter_list(rawText=rawText, original=True)

def write_done(fileName, chapterList):
	write_file(file=DONE + '/' + fileName + '.txt', chapterList=chapterList)

def get_done_chapter_list(fileName):
	rawText = read_file(DONE + '/' + fileName + '.txt')
	return get_chapter_list(rawText=rawText, original=False)
