#-*- coding: utf-8 -*-
import re

# read all texts and put it into rawText
def readTextFile():
    print('Reading text')
    f = open('../text/freshNewText.txt', 'r')
    paragraph = f.read()
    rawText = unicode(paragraph, 'utf-8')
    f.close
    return rawText

# make list of lines from raw texts
def makeLineList(rawText):
    lineList = []

    print('Removing patterns')

    # remove specific characters
    temp1 = re.sub('\d{1,2},\d{1,2}', '', rawText) 
    temp2 = re.sub('\d{1,2} ', '', temp1) 
    text = re.sub('\n', ' ', temp2)

    location = 0
    lineCount = 0
    while location < len(text): # until current character reaches the last character of texts
        length = 60 # recommanded length of each single line
	
	# when to add a new line, if it overs the length of total texts
        if location + length >= len(text): #last line
            print('Appending last line to list, ' + str(length) + 'characters')
            lineList.append(text[location:len(text)-1]) # make new line from current character to last character
            break # break while statement
   
        while text[location + length - 1] != ' ':
            length -= 1

        lineList.append(text[location:location+length])
        print('Appeding lines to list, ' + str(length) + 'characters')
        location += length
        lineCount += 1

    return lineList

def writeToTextFile(lineList):
    print('Writing lines')
    f = open('../text/readyToUse.txt', 'w+')
    f.write('\n'.join(lineList).encode('utf-8'))


writeToTextFile(makeLineList(readTextFile()))
