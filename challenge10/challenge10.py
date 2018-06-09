# len(a[30])=?

#a = [1, 11, 21, 1211, 111221]	# example given in page source

a = [1]

# it's clear what we have to do. expand the sequence to find out what the 30th position contains. this is a classic "look and say" sequence, or the Morris Number Sequence.  


from itertools import groupby
def lookandsay(n):
    return ''.join( str(len(list(g))) + k for k, g in groupby(n))

for i in range(30):
	x = lookandsay(str(a[i]))
	a.append(x)

print len(a[30])

## new url: http://www.pythonchallenge.com/pc/return/5808.html
