#The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
#The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 552 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 - 385 = 2640.
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import time
__author__ = 'Juan Paucar'

therange = xrange(1, 101)

start = time.clock()

sum_of_squares = sum(i**2 for i in therange)
square_of_the_sum = sum(therange)**2
diff = square_of_the_sum - sum_of_squares

stop = time.clock()

print diff
print "Elapsed time: %s ms" %(str((stop-start)*1000))