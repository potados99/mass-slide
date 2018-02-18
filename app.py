#-*- coding: utf-8 -*-
import sys 
sys.path.insert(0, 'src/') 
import re 
import templateModule

List = templateModule.makeChapterList(templateModule.readTemplate())

for i in List:
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

