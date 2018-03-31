#-*- coding: utf-8 -*-

import re
import sys
reload(sys)
import IOModule
sys.setdefaultencoding('utf-8')

CHANTS = '/home/pi/Projects/massSlide/chants'
LINE_LENGTH = 35

def raw_to_processed(rawDict):
	processedChapterList = []

	for title in rawDict:
        	processFunction = getattr(sys.modules[__name__], "process_" + IOModule.convert_title(title=title, eng=True))
        	processedChapterList.append(processFunction(rawDict[title]))

	return processedChapterList

def processed_to_done(chapterList, template):
        rawText = read_file(file=IOModule.TEMPLATE + '/' + template + '.txt')
        templateList = IOModule.get_chapter_list(rawText=rawText, original=True)

        for chapterOfList in chapterList:
                for chapterOfTemplate in templateList:
                        if chapterOfList[0] == chapterOfTemplate[0]:
                                templateList[templateList.index(chapterOfTemplate)] = chapterOfList

	return templateList

def read_file(file):
        f = open(file, 'r')
        rawText = f.read()
        f.close
        return rawText

def replace_text(text):
	temp1 = re.sub('\d{1,2},\d{1,2}', '', text) 
	temp2 = re.sub('\d{1,2} ', '', temp1)
#	temp3 = re.sub('● ', '', temp2) 
#	temp4 = re.sub('○ ', '', temp3) 
#	temp5 = re.sub('▣ ', '', temp4) 
#	temp6 = re.sub('\+ ', '', temp5) 
	temp3 = re.sub('\* ', '', temp2) 
	newText = re.sub('\n', ' ', temp3)

	return newText

def cut_text(text, maxLength):
	lineList = []

#	rep = {"\d{1,2},\d{1,2}": "", 
#		"\d{1,2} ": "",
#		"\* ": "",
#		"● ": "",
#		"○ ": "",
#		"▣ ": "",
#		"+ ": "",
#		"\n": ""
#	}
#
#	for i, j in rep.iteritems():
#		text = text.replace(i, j)
	
	#rep = dict((re.escape(k), v) for k, v in rep.iteritems())
	#pattern = re.compile("|".join(rep.keys()))
	#text = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)

	text = replace_text(text)

	location = 0
	lineCount = 0
	
	while location < len(text): # until current character reaches the last character of texts
		length = maxLength # recommanded length of each single line
	
		# when to add a new line, if it overs the length of total texts
		if location + length >= len(text): #last line
			lineList.append(text[location:len(text)]) # make new line from current character to last character
			break # break while statement
   
		while text[location + length - 1] != " ":
			length -= 1

		lineList.append(text[location:location+length])
		location += length
		lineCount += 1
		if (lineCount >= 5):
			lineList.append("")
			lineCount = 0

	return lineList

def by(name):
	beDict = {
		'요한': '이',
		'마르코': '가',
		'루카': '가',
		'마태오': '가'
	}

	return name + beDict[name]

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

def process_cover(rawList):
	mainTextList = ["**" + x + "**" for x in rawList if not x == ""]
	coverList = ["# 표지", ""]
	coverList.extend(mainTextList)
	coverList.extend(["", "", ""])

	return coverList

def process_pardon(rawList):
	mainTextList = cut_text(text=" ".join(rawList), maxLength=LINE_LENGTH)
	pardonList = [
		"# 입당송", 
		"", 
		"**입당송**", 
		""
	]
	pardonList.extend(mainTextList)
	pardonList.extend(["", "", ""])

	return pardonList

def process_collect(rawList):
	mainTextList = cut_text(text=" ".join(rawList), maxLength=LINE_LENGTH)
	collectList = [
		"# 본기도", 
		"",
		"**본기도**",
		"" 
	]
	collectList.extend(mainTextList)
	collectList.extend(["", "", ""])

	return collectList

def process_first_reading(rawList):
	title = rawList.pop(0)

	first_readingList = [
		"# 제1독서", 
		"",
		"**제1 독서**",
		"\'" + title + "\'"
	]
	first_readingList.extend(["", "", ""])

	return first_readingList

def process_second_reading(rawList):
	title = rawList.pop(0)

	second_readingList = [
		"# 제2독서", 
		"",
		"**제2 독서**",
		"\'" + title + "\'"
	]
	second_readingList.extend(["", "", ""])

	return second_readingList

def process_acclamation(rawList):
	mainTextList = []
	acclamationList = [
		"# 복음환호송",
		"",
		"**복음환호송**",
		""
	]

	for line in rawList:
		mainTextList.extend(cut_text(text=line.replace("(", "").replace(")", ""), maxLength=LINE_LENGTH))
		if not (line == rawList[-1]):
			mainTextList.append("")

	acclamationList.extend(mainTextList)
	acclamationList.extend(["", ""])

	return acclamationList

def process_sequence(rawList):
	mainTextList = []
	sequenceList = [
		"# 부속가",
		"",
		"**부속가**",
		""
	]

	for line in rawList:
		mainTextList.append(line)

	sequenceList.extend(mainTextList)
	sequenceList.extend(["", ""])

	return sequenceList

def process_gospel(rawList):
	title = rawList.pop(0)
	who, __, __ = title.partition(' ')
	mainTextList = cut_text(text=" ".join(rawList), maxLength=LINE_LENGTH)
	gospelList = [
		"# 복음",
		"",
		"**복음**",
		"\'" + title + "\'",
		"",
		"†주님께서 여러분과 함께",
		"**◎또한 사제의 영과 함께**",
		"",
		"†" + by(who) + " 전한",
		"거룩한 복음입니다.",
		"**◎주님 영광 받으소서.**",
		""
	]
	gospelListTrail = [
		"",
		"주님의 말씀입니다.",
		"**◎ 그리스도님 찬미합니다.**",
		""
	]
	gospelList.extend(mainTextList)
	gospelList.extend(gospelListTrail)
	gospelList.extend(["", "", ""])

	return gospelList

def process_antiphon(rawList):
	mainTextList = cut_text(text=" ".join(rawList), maxLength=LINE_LENGTH)
	antiphonList = [
		"# 영성체송", 
		"", 
		"**영성체송**", 
		""
	]
	antiphonList.extend(mainTextList)
	antiphonList.extend(["", "", ""])

	return antiphonList

def process_chants(rawList):
	chantsList = []

	entrance = ["# 입당성가", "", "**입당성가**"]
	offertory = ["# 봉헌성가", "", "**봉헌성가**"]
	eucharistic1 = ["# 성체성가1", "", "**성체성가**"]
	eucharistic2 = ["# 성체성가2", "", "**성체성가**"]
	dispatch = ["# 파견성가", "", "**파견성가**"]
	empty = ["", ""]

	for line in rawList:
		ent_match = re.match('입당성가:\s*(\d+)', line)
		off_match = re.match('봉헌성가:\s*(\d+)', line)
		euc1_match = re.match('성체성가1:\s*(\d+)', line)
		euc2_match = re.match('성체성가2:\s*(\d+)', line)
		dis_match = re.match('파견성가:\s*(\d+)', line)

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
	prayDict = {}
	mainTextList = []
	prayersList = [
		"# 보편지향기도",
		"",
		"**보편지향기도**",
		""
	]

	insertList = [
		"",
		"***",
		"♪ 주님 저희의 기도를",
		"들어주소서",
		"***",
		""
	]

	lineBreak = 0
	for line in rawList:
		titleMatch = re.match('(\d).+', line)

		if (line == ""): # Empty line
			lineBreak += 1

		else:
			if (lineBreak >= 1) and titleMatch:
				titleNum = titleMatch.group(1)
				prayDict[titleNum] = []
				prayDict[titleNum].append("")
				lineBreak = 0

			elif (lineBreak >= 1):
				prayDict[titleNum].append("")
                                lineBreak = 0

			if titleMatch:
				titleNum = titleMatch.group(1)
				prayDict[titleNum] = []

				prayDict[titleNum].append("***")
				prayDict[titleNum].extend(cut_text(text=line, maxLength=LINE_LENGTH))
				prayDict[titleNum].append("***")			

			else:		 # Main Text
				prayDict[titleNum].extend(cut_text(text=line, maxLength=LINE_LENGTH))

	for title in prayDict:
		mainTextList.extend(prayDict[title])
		mainTextList.extend(insertList)

	prayersList.extend(mainTextList)
	prayersList.extend(["", ""])

	return prayersList

def process_quiz(rawList):
	mainTextList = []
	quizList = [
		"# 강론",
		"",
		"**강론**",
		""
	]

	lineBreak = 0
	for line in rawList:
		titleMatch = re.match('[A-Z].+', line)
	
		if (line == ""): # Empty line
			lineBreak += 1

		else:
			if (lineBreak >= 1):
				mainTextList.append("")
				lineBreak = 0
			mainTextList.extend(cut_text(text=line, maxLength=LINE_LENGTH))

	quizList.extend(mainTextList)
	quizList.extend(["", "", ""])

	return quizList
