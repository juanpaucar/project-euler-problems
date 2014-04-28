"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""
import math
import time
__author__ = 'Juan'

a = 1
b = 0
c = 0
while 1<2:
    b = a+1
    c = math.trunc(math.sqrt(a**2 + b**2))
    while a+b+c <1000:
        b+=1
        c = math.trunc(math.sqrt(a**2 + b**2))
        print a+b+c
    a+=1
    if (a+b+c==1000):
        break

print (a-1)*b*c

