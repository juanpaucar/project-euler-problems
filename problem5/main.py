#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time
import math
__author__ = 'Juan'

#20 = 4* 5 = 2* 2* 5
#19 = 19
#18 = 9 * 2 = 6 * 3 = 2 * 3 *3
#17 = 17
#16 = 8 * 2 = 4 * 4 = 2* 2 * 2*2
#15 = 5 * 3
#14 = 7 * 2
#13 = 13
#12 = 6 *2 = 4* 3 = 2 *2* 3
#11 = 11
#the other numbers are already included inside bigger ones
#if we start to count from 11's factorial we already know al these numbers can be divided by numbers from 1 to 11
#so we start the test starting from 12
#i decided to use 11's factorial and not a bigger or smaller one because
# 12 it's already a number composed by smaller numbers and 11 isn't
#this problem is the first which really causes me a problem with performance, with O(n^2) it took one a a half minute
#now it takes around 629 ms

number = 0
current = math.factorial(11)
print current
start = time.clock()
while number==0:
    i=12
    while current%i==0:
        if i==20:
            number=current
            break
        i+=1
    current+=1
stop = time.clock()

print number
print "Elapsed time: %s ms" %(str((stop-start)*1000))
