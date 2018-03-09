#-*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from modules import templateModule
from modules import textModule
from modules import pptxModule

rawDict = templateModule.get_raw_chapter_dict()

rawChapterList = []
for title in rawDict:
	processFunction = getattr(textModule, "process_" + templateModule.convert_title(title=title, eng=True))
	rawChapterList.append(processFunction(rawDict[title]))

templateModule.write_processed(fileName='recent', chapterList=rawChapterList)

processedChapterList = templateModule.get_processed_chapter_list(fileName='recent')

templateModule.write_done(fileName='recent', chapterList=processedChapterList, template='lent')

doneChapterList = templateModule.get_done_chapter_list(fileName='recent')

myPrs = pptxModule.new_presentation()

pptxModule.write_presentation(Presentation=myPrs, List=doneChapterList)

pptxModule.save_presentation(prs=myPrs, path='/home/pi/WebDAV/new.pptx')
