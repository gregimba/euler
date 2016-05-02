list = []

def fib(n):
 a,b = 1,1
 for i in range(n-1):
  a,b = b,a+b
  list.append(a)
 return a

fib(33)

even_list = []
for item in list:
	if item % 2 == 0:
		even_list.append(item)

print sum(even_list)