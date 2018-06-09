import numpy as np
import bz2
import re
from bs4 import BeautifulSoup
import requests


# here the page source gives us a number of things to work with. we have  a username, and a password. these two things need decoded. we're clearly getting into ascii and hex style things now. 

un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'


print bz2.decompress(un)
print bz2.decompress(pw)	# I definitely had to look up what encoding this was. 


## next url: http://www.pythonchallenge.com/pc/return/good.html
