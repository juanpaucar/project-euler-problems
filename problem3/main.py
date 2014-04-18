#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

import time

__author__ = 'Juan Paucar'

x = 3
number = 600851475143
start = time.clock()
while x **2 < number: #we know it must be less or equal to square root of 600851475143
    while number % x == 0: #just reducing the number
        number /= x
    x +=  2 #just odds
stop = time.clock()
print number
print "Elapsed time: %s ms" %(str((stop-start)*1000))
