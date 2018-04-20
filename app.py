#-*- coding: utf-8 -*-

import pkg_resources
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from datetime import datetime
from modules import IOModule
from modules import processModule
from modules import pptxModule

PR = pkg_resources.resource_filename('__main__','')
now = datetime.now()
CREATED = PR + '/created'
FILENAME = ( '%s%s%s.pptx' % ( now.year, now.month, now.day ) )
TEMPLATE = sys.argv[1]


rawDict = IOModule.get_raw_chapter_dict(TEMPLATE)

processedChapterList = processModule.raw_to_processed(rawDict)

IOModule.write_processed(fileName='recent', chapterList=processedChapterList)


readProcessedChapterList = IOModule.get_processed_chapter_list(fileName='recent')

doneChapterList = processModule.processed_to_done(readProcessedChapterList, TEMPLATE)

IOModule.write_done(fileName='recent', chapterList=doneChapterList)


readDoneChapterList = IOModule.get_done_chapter_list(fileName='recent')

myPrs = pptxModule.new_presentation()

pptxModule.write_presentation(Presentation=myPrs, List=readDoneChapterList)

pptxModule.save_presentation(prs=myPrs, path=CREATED + '/' + FILENAME)
