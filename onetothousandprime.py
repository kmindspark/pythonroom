# author: kmindspark
total = 0
for n in range (2, 1001):
	
	tests = range (2, n-1)
	prime = True
	
	if prime == True:
		for t in tests:
			if n % t == 0:
				prime = False
			else:
				diff=pdiff
				n=pn
				pdiff = n-pn
				totdiff = pdiff + diff
	
	if prime == True:
		total = total + n
		print str (n) + " is prime."
		
print str (total) + " is their sum."
print totdiff