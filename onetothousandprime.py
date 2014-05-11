# author: kmindspark
total = 0
pdiff = 0
diff = 0
n = 0
pn = 0
for n in range (2, 1001):
	
	tests = range (2, n-1)
	prime = True
	
	if prime == True:
		for t in tests:
			if n % t == 0:
				prime = False
			else:
				pdiff = n-pn
				totdiff = pdiff + diff
				diff=pdiff
				n=pn
				
	
	if prime == True:
		total = total + n
		print str (n) + " is prime."
		
print str (total) + " is their sum."
print totdiff