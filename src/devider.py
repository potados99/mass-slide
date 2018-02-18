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
	chapterList.pop(0)
#	chapterList = [x[:-2] for x in chapterList if x[-2] == ""]
	print (chapterList)
	return chapterList


out = makeChapterList(readTemplate())
	
#print (out)

for i in out:
	linebreakCount = 0

	for j in i:
		# Bold string
		m = re.match('\*\*.+\*\*', j)
		if (m):
			boldStr = "BOLD: " + m.group().replace("*", "")
			print(boldStr)

		# Title
		elif (i.index(j) == 0):
			print ("		new chapter")
			print ("TITLE: " + j)

		# Linebreak
		elif (j == ""):
			linebreakCount += 1
		else:
			if (linebreakCount >= 1):
				print ("	new page")
				linebreakCount = 0
			print (j)

