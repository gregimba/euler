def is_prime(n):
    i = 2
    while i < n:
        if n%i == 0:
            return False
        i += 1
    return True


counter = 0
number = 1
while counter != 10002:
	if is_prime(number):
		print str(counter) + '->' + str(number)
		counter += 1
		number += 1
	else:
		number += 1