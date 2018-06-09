from PIL import Image
import numpy as np


# my thoughts: there is clearly a barcode-esque sequence in the middle of this image. It looks to be exactly halfway in the rows, so I measured the shape of the image array. it has 95 rows, so halfway would be row 48. The last column in each pixel is the transparency: always 255, so we can ignore it. The other three values are RGB values which determine the color. For instance, 115 115 115 is a medium grey color. 

im = Image.open('oxygen.png')
imarray = np.array(im)
print imarray.shape	# check the array shape. it has 95 rows.  
new_list =  imarray[48][:-21].tolist()	# there are some non-greyscale pixels at the end of this row. I just manually counted them out since there weren't many, but it would be straightforward to write a line that made a list of r=g=b color values. 

# remove duplicates:

new_list = new_list[::7]	# except for the first batch which seems to only be five pixels wide, all other colors are 7 pixels wide. so we remove duplicates in this fashion. 

flat_list = [item for sublist in new_list for item in sublist]	# get rid of the nested lists
flat_list = flat_list[::4]	# get rid of the duplicate GBA and only keep the first of four values from each pixel
print flat_list	# sanity check. looks good. 


print "".join(map(chr, flat_list))	# treat numbers as ascii codes, map them and join them. 


second_level = [105, 110, 116, 101, 103, 114, 105, 116, 121]	# the above gives you a second list of numbers to map. 

print "".join(map(chr, second_level))	# map the second list and get the final answer. 

## new url: http://www.pythonchallenge.com/pc/def/integrity.html