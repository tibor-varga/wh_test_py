#!/usr/bin/env python
# Module:   lists_fcn.py
# Purpose:  list tests
# Date:     N/A
# Notes:
# 1) ...
# Ref:  any references

import math as m

print "lists_misc.py:  misc list functions/operations"
print "Use lists for simple, mutable arrays of data."
print "Note lists can contain multiple types of data unlike numpy arrays."
l1 = ['a', 'b', 'c', 'z', 'y', 'x', 1, 2, 3, 4, 5]
print "Input list:  ", l1

print "changing entry 1 value to j:  l1[1]='j'"
l1[1]='j'

l1.sort()
print "sorted ", l1

l1.remove(3)
print "removed 3 ", l1

l1.insert(3, '3')
print "added 3 as a string ", l1

l2=l1[-3:]
print "last 3 of l1 ", l2

ll=len(l2)
print "len of l2 ", ll

print "Creating tuple t3 with some int and float values"
t3=(1, 2, 3, 4, 5, 6, 7, 8, m.pi)
ls=sum(t3)
print "t3=", t3
print "sum t3=", ls

# 3.4 supports statistics but we don't have 3.4 yet:
# import statistics
# print(statistics.mean(t3))

# use scipy or numpy to get mean
import numpy as np
lm=np.mean(t3)
print "mean numpy t3=", lm

# deprecated, use numpy???
import scipy as sp
lm=sp.mean(t3)
print "mean scipy t3=", lm

ld=np.std(t3)
print "stdev numpy=", ld

print "Converting t3 to a list l3 using list() method"
l3=list(t3)
print "List=", l3
lm=sp.mean(l3)
print "mean scipy l3=", lm

print "Adding string to l3 and trying mean again, throws error"
l3.append('x')
try:
    lm=sp.mean(l3)
    print "mean scipy l3=", lm
except Exception, e:
    print "Exception, e=", e

print "Done!"

    


