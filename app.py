#-*- coding: utf-8 -*-

import re 
import sys 
sys.path.insert(0, 'src/') 

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE
import templateModule
import fontModule

def newPresentation():
	global prs
	prs = Presentation()

def newSlide(slideLayout):
	newSlide = prs.slides.add_slide(prs.slide_layouts[slideLayout])
	
	left = top = Inches(0.1)
	width = Inches(9.8)
	height = Inches(7.3)

	textBox = newSlide.shapes.add_textbox(left, top, width, height)

	global text_frame
	text_frame = textBox.text_frame
	text_frame.word_wrap = True
	text_frame.auto_size = MSO_AUTO_SIZE.SHAPE_TO_FIT_TEXT
	text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

def blankSlide():
	return 0

def newLine(text, size, bold):
	p = text_frame.add_paragraph()
	p.alignment = PP_ALIGN.CENTER

	run = p.add_run()
	run.text = text
	run.font.bold = bold
	run.font.size = Pt(size)
	run.font.name = u"1훈하얀고양이 R"

def savePresentation():
	prs.save('/home/pi/WebDAV/test.pptx')	

List = templateModule.makeChapterList(templateModule.readTemplate(sys.argv[1]))

newPresentation()

for chapter in List:

	linebreakCount = 0
	SIZE = 0
	BOLD = False

	for line in chapter:
		boldMatch = re.match('\*\*.+\*\*', line)

		# Linebreak
		if (line == ""):
			linebreakCount += 1

		# Bold mark
		elif (line == "***"):
			if (BOLD):
				BOLD = False
			else:
				BOLD = True

		# Empty
		elif (line == "//"):
			# create a blank page with black background
			blankSlide()

		# Title
		elif (chapter.index(line) == 0): # first line
#			if (List.index(chapter) != 0):
			print ("\n//new chapter//\n")
			print ("<" + line + ">")

			newSlide(6)

		# Text
		else:
			SIZE = fontModule.setFontSize(chapter[0])
			
			if (linebreakCount >= 1):
				print ("//new page//")
				linebreakCount = 0

				newSlide(6)

			# Bold
			if (boldMatch):
				print("[" + boldMatch.group().replace("*", "") + "]")
#				SIZE = fontSize('medium')

				if (chapter.index(line) == 1): # first bold line
					SIZE = fontModule.fontSize('big')

				newLine(text=boldMatch.group().replace("*", ""), size=SIZE, bold=True)

			# Plane
			else:
				print (line)
#				SIZE = fontSize('medium')

				newLine(text=line, size=SIZE, bold=BOLD)

savePresentation()

'''
if __name__ == "__main__":
if (len(sys.argv) > 1): # if arguments (except filename) exists, call function named sys.argv.[1]
function = getattr(sys.modules[__name__], sys.argv[1])
'''
