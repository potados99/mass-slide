#-*- coding: utf-8 -*-
import re

CHANTS = '/home/pi/Projects/massSlide/chants'

def read_file(file):
        f = open(file, 'r')
        rawText = f.read().decode('utf8')
        f.close
        return rawText

def cut_text(text, maxLength):
	lineList = []

	print("Removing patterns")

	temp1 = re.sub('\d{1,2},\d{1,2}', '', text) 
	temp2 = re.sub('\d{1,2} ', '', temp1) 
	text = re.sub('\n', ' ', temp2)

	location = 0
	lineCount = 0
	while location < len(text): # until current character reaches the last character of texts
		length = maxLength # recommanded length of each single line
	
		# when to add a new line, if it overs the length of total texts
		if location + length >= len(text): #last line
			print("Appending last line to list, " + str(length) + "characters")
			lineList.append(text[location:len(text)-1]) # make new line from current character to last character
			break # break while statement
   
		while text[location + length - 1] != " ":
			length -= 1

		lineList.append(text[location:location+length])
		lineList.append("")
		print("Appeding lines to list, " + str(length) + "characters")
		location += length
		lineCount += 1

	return lineList


def process_cover(rawList):
	mainTextList = ["**" + x + "**" for x in rawList if not x == ""]

	coverList = ["#표지", ""]
	coverList.extend(mainTextList)
	coverList.extend(["", "", ""])

	return coverList

def process_pardon(rawList):
	mainTextList = cut_text(text=" ".join(rawList), maxLength=60)

	pardonList = [
		"#입당송", 
		"", 
		"**입당송**", 
		""
	]
	pardonList.extend(mainTextList)
	pardonList.extend(["", "", ""])

	return pardonList

def process_collect(rawList):
	mainTextList = cut_text(text=" ".join(rawList), maxLength=60)

	collectList = [
		"#본기도", 
		"", 
	]
	collectList.extend(mainTextList)
	collectList.extend(["", "", ""])

	return collectList

def process_first_reading(rawList):
	title = rawList.pop(0)

	first_readingList = [
		"#제1독서", 
		"",
		"**제2 독서**",
		"\'" + title + "\'"
	]
	first_readingList.extend(["", "", ""])

	return first_readingList

def process_second_reading(rawList):
	title = rawList.pop(0)

	second_readingList = [
		"#제2독서", 
		"",
		"**제2 독서**",
		"\'" + title + "\'"
	]
	second_readingList.extend(["", "", ""])

	return second_readingList

def process_acclamation(rawList):
	acclamationList = [
		"#복음환호송",
		"",
		"**복음환호송**",
		""
	]
	mainTextList = []
	tempList = [cut_text(text=x, maxLength=40) for x in rawList]

	for page in tempList:
		for line in page:
			mainTextList.append(line.replace("(", "").replace(")", ""))
		if (page != tempList[-1]):
			mainTextList.append("")

	acclamationList.extend(mainTextList)
	acclamationList.extend(["", ""])

	return acclamationList

def process_gospel(rawList):
	title = rawList.pop(0)
	mainTextList = cut_text(text=" ".join(rawList), maxLength=60)

	gospelList = [
		"#복음",
		"",
		"**복음**",
		"\'" + title + "\'",
		"",
		"†주님께서 여러분과 함께",
		"**◎또한 사제의 영과 함께**",
		"†요한이 전한 거룩한 복음입니다.",
		"**◎주님 영광 받으소서.**",
		""
	]
	gospelList.extend(mainTextList)
	gospelList.extend(["", "", ""])

	return gospelList

def process_antiphon(rawList):
	mainTextList = cut_text(text=" ".join(rawList), maxLength=60)

	antiphonList = [
		"#영성체송", 
		"", 
		"**영성체송**", 
		""
	]
	antiphonList.extend(mainTextList)
	antiphonList.extend(["", "", ""])

	return antiphonList

def process_chants(rawList):
	chantsList = []

	entrance = ["#입당성가", "", "**입당성가**"]
	offertory = ["#봉헌성가", "", "**봉헌성가**"]
	eucharistic1 = ["#성체성가1", "", "**성체성가**"]
	eucharistic2 = ["#성체성가2", "", "**성체성가**"]
	dispatch = ["#파견성가", "", "**파견성가**"]
	empty = ["", ""]

	for line in rawList:
		ent_match = re.match(u'입당성가=(.+)', line)
		off_match = re.match(u'봉헌성가=(.+)', line)
		euc1_match = re.match(u'성체성가1=(.+)', line)
		euc2_match = re.match(u'성체성가2=(.+)', line)
		dis_match = re.match(u'파견성가=(.+)', line)

		if ent_match:
			 entrance.extend(read_file(CHANTS + '/' + ent_match.group(1) + '.txt').split('\n'))
		elif off_match:
			offertory.extend(read_file(CHANTS + '/' + off_match.group(1) + '.txt').split('\n'))
		elif euc1_match:
			 eucharistic1.extend(read_file(CHANTS + '/' + euc1_match.group(1) + '.txt').split('\n'))
		elif euc2_match:
			 eucharistic2.extend(read_file(CHANTS + '/' + euc2_match.group(1) + '.txt').split('\n'))
		elif dis_match:
			 dispatch.extend(read_file(CHANTS + '/' + dis_match.group(1) + '.txt').split('\n'))

	chantsList = entrance + empty + offertory + empty + eucharistic1 + empty + eucharistic2 + empty + dispatch + empty

	return chantsList

def process_prayers(rawList):
	return ['test']

def process_quiz(rawList):
	return ['test']



