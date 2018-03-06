#-*- coding: utf-8 -*-

import sys
import templateModule
import textModule


rawDict = templateModule.get_raw_dict()

'''
processedCol = textModule.process_gospel(rawDict["복음"])
for i in processedCol:
	print i

processedCht = textModule.process_chants(rawDict["성가"])
for i in processedCht:
	print i
'''

#def process(title, list):
	

processedList = []

for title in rawDict:
	function = getattr(textModule, "process_" + templateModule.convert_title(title=title, eng=True))
	processedList.extend(function(rawDict[title]))

for i in processedList:
	print i
