# author: kmindspark
# average distance
# largest distance'smallest distance
# how many twin primes
#sum of the distance between twin primes 17/19 to 41/43 => 41-19 


lastPrime = 2

total = 0
for n in range (2, 1001):
	
	tests = range (2, n-1)
	prime = True
	
	if prime == True:
		for t in tests:
			if n % t == 0:
				prime = False
	
	if prime == True:
		total = total + n
		print str (n) + " is prime."
		
print str (total) + " is their sum."

if prime == True:
	totdiff = totdiff + (n-lastPrime)
	lastPrime = n
	print "totdiff"