List = [['title1', '', '', 'trueV'],['title2', '', 'val'],['title3', 'val']]

print (List)

def deleteSpace(List):
        for chapter in List:
                j = 1
                while chapter[j] == '': # until not empty space
                        chapter.pop(j)
	return List
	
print (deleteSpace(List))
