#-*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from modules import IOModule
from modules import processModule
from modules import pptxModule

#rawDict = IOModule.get_raw_chapter_dict()

#rawChapterList = []
#for title in rawDict:
#	processFunction = getattr(processModule, "process_" + IOModule.convert_title(title=title, eng=True))
#	rawChapterList.append(processFunction(rawDict[title]))

#IOModule.write_processed(fileName='recent', chapterList=rawChapterList)

processedChapterList = IOModule.get_processed_chapter_list(fileName='recent')

IOModule.write_done(fileName='recent', chapterList=processedChapterList, template='lent')

doneChapterList = IOModule.get_done_chapter_list(fileName='recent')

myPrs = pptxModule.new_presentation()

pptxModule.write_presentation(Presentation=myPrs, List=doneChapterList)

pptxModule.save_presentation(prs=myPrs, path='/home/pi/WebDAV/new.pptx')
