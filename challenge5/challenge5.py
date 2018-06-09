### 5 http://www.pythonchallenge.com/pc/def/peak.html

import requests
from bs4 import BeautifulSoup
import re
import pickle


pages = requests.get('http://www.pythonchallenge.com/pc/def/peak.html')
soup = BeautifulSoup(pages.content, 'html.parser')
#print soup.find('peakhell')['src']

new_page = requests.get('http://www.pythonchallenge.com/pc/def/%s' % soup.find('peakhell')['src']) 
new_soup = BeautifulSoup(new_page.content, 'html.parser')

reader = pickle.load(open('banner.p', 'rb'))
for line in reader: 
	print "".join([k * v for k, v in line])


## new url: http://www.pythonchallenge.com/pc/def/channel.html