import numpy as np
from PIL import Image
from itertools import chain


#### 6 http://www.pythonchallenge.com/pc/def/channel.html

im = Image.open('channel.jpg')
imarray = np.array(im)
print len(imarray)
#imlist = imarray.tolist()
#newlist = list(chain(*imlist[0]))

