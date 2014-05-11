# author: kmindspark
tests = range (2, 1001)
prime = True

if prime == True:
	for t in tests:
		if n % t == 0:
			prime = False

if prime == True:
	print str (n) + " is prime."
