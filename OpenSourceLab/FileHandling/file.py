
def testForPunctuations(line):
	line = line.replace("?", "")
	line = line.replace(".", "")
	line = line.replace(",", "")
	line = line.replace("!", "")
	return line


def processLine(line, wordcounts):
	line = testForPunctuations(line)
	words = line.split()#Default is space


	for aWord in words:

		
		if aWord in wordcounts:
		#If a word is part of dictonary increment its counter
			wordcounts[aWord]+=1


		else:
		#Else assign its counter 1
			wordcounts[aWord]=1


filename = "test.txt"
file = open(filename, "r")
wordcounts = {}


#Spliting the file into multiple lines
for line in file:
	processLine(line, wordcounts)


#Sorting the line
for w in sorted(wordcounts, key=wordcounts.get,reverse=True):
	print (w,":",wordcounts[w])


#Finding the word repeated the most
maxwords=0
for w in wordcounts:
	if wordcounts[w] > maxwords:
		maxwords = wordcounts[w]
		key = w


print("MAX  ",key,wordcounts[key])
file.close()
