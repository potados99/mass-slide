#-*- coding: utf-8 -*-
import sys 
sys.path.insert(0, 'src/') 

import re 
import templateModule

List = templateModule.makeChapterList(templateModule.readTemplate(sys.argv[1]))

for chapter in List:
	linebreakCount = 0

	for line in chapter:
		m = re.match('\*\*.+\*\*', line)

		# Linebreak
		if (line == ""):
			linebreakCount += 1

		# Bold string
		elif (m):
			if (linebreakCount >= 1):
				print ("	new page")
				linebreakCount = 0
			print("[" + m.group().replace("*", "") + "]")

		# Title
		elif (chapter.index(line) == 0): # first line
			print ("		new chapter")
			print ("TITLE: " + line)

		else:
			if (linebreakCount >= 1):
				print ("	new page")
				linebreakCount = 0
			print (line)

'''
if __name__ == "__main__":
        if (len(sys.argv) > 1): # if arguments (except filename) exists, call function named sys.argv.[1]
                function = getattr(sys.modules[__name__], sys.argv[1])
'''
