#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10 001st prime number?

import time
import math
__author__ = 'Juan Paucar'

def isPrime(number):
    maxDiv = math.trunc(math.floor(math.sqrt(number)))
    for i in xrange(2, maxDiv+1):
        if number%i==0:
            return False
    return True

count = 1 #starting from 3
number = 1

start = time.clock()

while count < 10001:
    number+=2           #obviously just odd numbers are checked
    if isPrime(number):
        count+=1

stop = time.clock()

print number
print "Elapsed time: %s ms" %(str((stop-start)*1000))