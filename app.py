#-*- coding: utf-8 -*-

import re 
import sys 
sys.path.insert(0, 'src/') 

from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.enum.text import PP_ALIGN
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE
from pptx.enum.shapes import MSO_SHAPE
from pptx.dml.color import RGBColor

import templateModule
import fontModule

ref = Presentation('reference/sample.pptx')
#xml_slides = ref.slides._sldIdLst
#slides = list(xml_slides)
#whiteSlide = ref.slides[0]

def newPresentation():
	global prs
	prs = Presentation()

def newSlide(slideLayout):
	newSlide = prs.slides.add_slide(prs.slide_layouts[6]) 
#	prs.slides.append(whiteSlide)

	left = top = Inches(0)
	width = Inches(10)
	height = Inches(7.5)

	backgroundShape = newSlide.shapes.add_shape(
		MSO_SHAPE.RECTANGLE, left, top, width, height
	)

	line = backgroundShape.line
	line.color.rgb = RGBColor(255, 252, 197)

	fill = backgroundShape.fill
	fill.solid()
	fill.fore_color.rgb = RGBColor(255, 252, 197)	

	textBox = newSlide.shapes.add_textbox(left, top, width, height)

	global text_frame
	text_frame = textBox.text_frame
	text_frame.word_wrap = True
	text_frame.auto_size = MSO_AUTO_SIZE.SHAPE_TO_FIT_TEXT
	text_frame.vertical_anchor = MSO_ANCHOR.MIDDLE

def blankSlide():
	newSlide = prs.slides.add_slide(prs.slide_layouts[6]) # blank

	left = top = Inches(0)
	width = Inches(10)
	height = Inches(7.5)

	backgroundShape = newSlide.shapes.add_shape(
		MSO_SHAPE.RECTANGLE, left, top, width, height
	)

	line = backgroundShape.line
	line.color.rgb = RGBColor(0, 0, 0)

	fill = backgroundShape.fill
	fill.solid()
	fill.fore_color.rgb = RGBColor(0, 0, 0)	

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

List = templateModule.deleteSpace(templateModule.makeChapterList(templateModule.readTemplate(sys.argv[1])))

newPresentation()

for chapter in List:

	linebreakCount = 0
	SIZE = 0
	BOLD = False

	for line in chapter:
		boldMatch = re.match('\*\*.+\*\*', line)
		tinyMatch = re.match('\'.+\'', line)

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
			print ("//black page//")
			linebreakCount = 0
	
			blankSlide()

		# Title
		elif (chapter.index(line) == 0): # first line
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
				print ("[" + boldMatch.group().replace("*", "") + "]")

				if (chapter.index(line) == 1): # first bold line
					SIZE = fontModule.fontSize('big')

				newLine(text=boldMatch.group().replace("*", ""), size=SIZE, bold=True)

			# Small
			elif (tinyMatch):
				print ("(" + tinyMatch.group().replace("\'", "") + ")")
				SIZE = fontModule.fontSize('tiny')

				newLine(text=tinyMatch.group().replace("\'", ""), size=SIZE, bold=False)

			# Plane
			else:
				print (line)

				newLine(text=line, size=SIZE, bold=BOLD)

savePresentation()
