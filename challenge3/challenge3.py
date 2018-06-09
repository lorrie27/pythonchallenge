### 3 http://www.pythonchallenge.com/pc/def/equality.html

import numpy as np
import csv 

textfile = open('python_challenge_input_3.txt', 'r')
lines = textfile.read().replace('\n', '')
thislist = list(lines)
thislist = np.array(thislist)
print thislist

def KnuthMorrisPratt(text, pattern):

	pattern = list(pattern)
	length = len(pattern)

	shifts = [1]*(length+1)
	shift = 1
	for pos, pat in enumerate(pattern):
		while shift <= pos and pat != pattern[pos-shift]:
			shift += shifts[pos-shift]
		shifts[pos+1] = shift
	startPos = 0
	matchLen = 0
	for c in text:
		while matchLen == length or matchLen>=0 and pattern[matchLen]!=c:
			startPos += shifts[matchLen]
			matchLen -= shifts[matchLen]
		matchLen += 1
		if matchLen == length: 
			yield startPos

upper_array = np.zeros(len(thislist))

upper_array[np.core.defchararray.isupper(thislist)]=1

upper_array.tolist()
print upper_array

#for s in KnuthMorrisPratt([1,2,3,4,5], [4,5]): print s
for s in KnuthMorrisPratt(upper_array, [0,1,1,1,0,1,1,1,0]): print thislist[s+4]

## new url: http://www.pythonchallenge.com/pc/def/linkedlist.html, http://www.pythonchallenge.com/pc/def/linkedlist.php
