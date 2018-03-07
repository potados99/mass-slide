#-*- coding: utf-8 -*-

import sys
from python-modules import templateModule
from python-modules import textModule


rawDict = templateModule.get_raw_dict()

processedList = []

for title in rawDict:
	function = getattr(textModule, "process_" + templateModule.convert_title(title=title, eng=True))
	processedList.extend(function(rawDict[title]))

for i in processedList:
	print i
