#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

from itertools import product
import time
__author__ = 'Juan Paucar'

def isPalindrome(number):
    strNumber=str(number)
    if strNumber==strNumber[::-1]:
        return True
    return False

maxPalindrome=1

start = time.clock()
for i,j in  product(range(1,1000), repeat=2):
    palindrome=i*j
    #print "i= %s  j= %s" % (str(i), str(j))
    if isPalindrome(palindrome) and palindrome>maxPalindrome:
        maxPalindrome=palindrome
stop =time.clock()


print maxPalindrome
print "Elapsed time: %s ms" % (str((stop-start)*1000))
