### 2  http://www.pythonchallenge.com/pc/def/ocr.html

import csv
from collections import Counter


textfile = open('python_challenge_input_2.txt', 'r')

lines = textfile.read().replace('\n', '')

thislist = list(lines)

print Counter(thislist)

#	rarest are: a e i l q u t y ---> this translates to "equality"

## new url: http://www.pythonchallenge.com/pc/def/equality.html