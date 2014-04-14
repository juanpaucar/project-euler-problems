#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import time

__author__ = 'Juan Paucar'

x = 2
number = 600851475143
start = time.clock()
while x **2 < number:
    while number % x == 0:
        number /= x
    x +=  1
stop = time.clock()
print number
print "Elapsed time: %s secs" % (str(stop-start))
