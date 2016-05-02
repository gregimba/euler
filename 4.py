def palindrome(str):
	if str == str[::-1]:
		return True
	else:
		return False


for x in xrange(100,999):
	for y in xrange(100,999):
		if palindrome(str(x * y)):
			print x * y