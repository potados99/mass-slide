#-*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from modules import templateModule
from modules import textModule


rawDict = templateModule.get_raw_chapter_dict()

processedChapterList = []
for title in rawDict:
	processFunction = getattr(textModule, "process_" + templateModule.convert_title(title=title, eng=True))
	processedChapterList.append(processFunction(rawDict[title]))

templateModule.write_processed(fileName='recent', chapterList=processedChapterList)

processedChapterListRead = templateModule.get_processed_chapter_list(fileName='recent')

templateModule.write_done(fileName='recent', chapterList=processedChapterListRead, template='lent')
