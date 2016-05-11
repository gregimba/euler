total = 0

for x in xrange(0,100):
	total = x + total


squared_total = total**2

print squared_total

total_squared = 0
for x in xrange(0,100):

	total_squared += x**2

print total_squared

print squared_total - total_squared


