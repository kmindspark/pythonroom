# author: kmindspark
n = int (input ("What number would you like to check?"))
tests = range (2, n)
prime = True

if prime == True:
	for t in tests:
		if n % t == 0:
			prime = False

if prime == True:
	print str (n) + " is prime."
else:
	print str (n) + " is composite."