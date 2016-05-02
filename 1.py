#Find the sum of all multiples of 3 or 5 bellow 1000

total = 0
list = []

for x in xrange(1,1000):
	if x % 3 == 0:
		list.append(x)
	elif x % 5 == 0:
		list.append(x)


print sum(list)