alpha = 'abcdefghijklmnopqrstuvwxyz'


### 1	http://www.pythonchallenge.com/pc/def/map.html

### this is a pretty straightforward interpretation of a Caesar cipher, rotating each letter by 2 instead of the iconic 3. 
### however, I did not string.maketrans() as suggested in the hint. obviously. 

input_1 = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def find_shift(a,b): 

	return abs(alpha.index(b)-alpha.index(a))

def recursive_alpha(input, shift): 

	new_string = []

	for i in input: 
		try:
			index_i = alpha.index(i) 
			new_string.append(alpha[(index_i+shift)%26])
		except:
			new_string.append(i)

	print ''.join(new_string)


print find_shift('k', 'm')

recursive_alpha(input_1, find_shift('k','m'))

recursive_alpha('map', 2)

## new html: http://www.pythonchallenge.com/pc/def/ocr.html