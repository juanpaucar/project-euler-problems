#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
#The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000."""

import time
__author__ = 'Juan Paucar'

sum= 0

start = time.clock()

for i in range(3,1000):
    if (i%3==0 or i%5==0):
        sum+=i
else:
    print sum

stop = time.clock()
print "Elapsed time: %s ms" %(str((stop-start)*1000))
