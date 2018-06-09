import numpy as np
import csv
import re
import glob
import zipfile


#### 6 http://www.pythonchallenge.com/pc/def/channel.html

## this one totally threw me off. it was completely unintuitive to me to change html to zip in the url. the first line of the page source (<html> <!-- <-- zip -->) is supposed to give it away, I suppose, but even though I found the line it didn't indicate to me that that's what I should do. I had to look up this hint, and now we move forward from there. 

## except for lines 16 and 25 the solution is my own. 

all_files = glob.glob('./channel/*.txt') # collect the files. not strictly necessary, but I wanted to...
print len(all_files) # ... check the number of files. that's the max number of iterations.
f = zipfile.ZipFile("channel.zip") # I pulled this from a solutions manual. Except for a related line below (25), the rest is my own. 

next_file = 90052	# from the readme.txt, this is the first file number. 

file_list = [90052] # append the file numbers in order... also not necessary, I think. 
comments = [] # append the comment corresponding to the file number. 

for i in range(len(all_files)-1):
	file = open('./channel/%s.txt' % str(next_file), 'r')	# open file
	comments.append(f.getinfo(str(next_file) + ".txt").comment.decode("utf-8")) # I also pulled this from a solutions manual, because I have never used this sort of thing before. I didn't even know zip files had comments, potentially. 
	text = file.read()	# pull text from file
	print text	# sanity check on the contained text
	new_search = re.findall(r'Next\snothing\sis\s\d+', text)	# make sure the text matches the pattern
	new_list = [i.split() for i in new_search]	# split the above list phrase into its components
	try:
		next_file = [int(s) for s in new_list[0] if s.isdigit()][0]	# search the split list for digits and convert to int, set that integer to nothing_next and feed it into the next url
	except:
		pass	# if we hit a file with no number, exit. 
	file_list.append(next_file)	# append the file number to the file list. 

#print file_list
#print comments

print "".join([k for k in comments])	# now we have a list of comments, join them together to get the solution. 

## next url: http://www.pythonchallenge.com/pc/def/hockey.html

# you get: it's in the air. look at the letters.

# the answer to which is: oxygen. the output of the above script is an ascii image of the word "hockey," but each letter of "hockey" is depicted by a different letter. H is made of O's, O is make of X's, etc. they make the word "oxygen." Nice. 

## final url: http://www.pythonchallenge.com/pc/def/oxygen.html



