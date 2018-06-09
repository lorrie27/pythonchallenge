### 4 http://www.pythonchallenge.com/pc/def/linkedlist.html, http://www.pythonchallenge.com/pc/def/linkedlist.php

import csv
import requests
from bs4 import BeautifulSoup
import re


nothing_1 = 12345	# this is the first nothing given by clicking the image. you could also find it by using beautiful soup to pull the href in the webpage html, but as this is a one-off... 


### use the following to test individual cases if necessary: 


# nothing_test = 49574

# first_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % str(nothing_test)

# pages = requests.get(first_url)
# soup = BeautifulSoup(pages.content, 'html.parser')
# print [int(s) for s in re.findall(r'\d+', soup.get_text()) if s.isdigit()]

#######################

nothing_next = 16044/2	# at some point you run into a page that says you're on the right track, but now you need to divide the previous nothing by 2 to proceed. this is also a one-off, so I just hardcoded it.

for i in range(400):

	first_url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s" % str(nothing_next)

	pages = requests.get(first_url)	# pull the url 

	soup = BeautifulSoup(pages.content, 'html.parser')	# use beautiful soup to pull the page content	

	print soup.get_text()	# print the text of the webpage for a sanity check

	new_search = re.findall(r'and\sthe\snext\snothing\sis\s\d+', soup.get_text())	# use regex to search for "and the next nothing is " with digits following, put that exact phrase into a list

	new_list = [i.split() for i in new_search]	# split the above list phrase into its components

	nothing_next = [int(s) for s in new_list[0] if s.isdigit()][0]	# search the split list for digits and convert to int, set that integer to nothing_next and feed it into the next url

## new url: http://www.pythonchallenge.com/pc/def/peak.html