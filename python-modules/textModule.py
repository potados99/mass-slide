#-*- coding: utf-8 -*-

import re

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










def process_gospel(rawList):
	title = rawList.pop(0)
	mainText = cut_text(text=" ".join(rawList), maxLength=60)

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

	gospelList.extend(mainText)

	return gospelList
