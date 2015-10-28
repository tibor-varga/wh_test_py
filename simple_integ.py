#!/usr/bin/env python
# Module:   simple_integ.py
# Purpose:  simple integration using numpy
# Date:     N/A
# Notes:
# 1) Requires scipy
# Ref:  http://docs.scipy.org/doc/scipy/reference/tutorial/integrate.html

# import special so we get bessel function (special.jv)
from scipy import special  

# import quad for typical integration
from scipy.integrate import quad

from math import exp

print "simple_integ.py:  sample integration using numpy"
print "result:  estimate, upper bound on error"

# from the reference, use a lambda in this sample
print "Test1 from reference:  jv(2.5,x) from 0..4.5"
result = quad(lambda x: special.jv(2.5,x), 0, 4.5)
print "Result=", result

print "Test2 simpler example:  x**2 from 0..2"
result = quad(lambda x: x**2, 0, 2)
print "Result=", result

print "Test using function:  e(-10x) from 1..10"
def testfunc(t,x):
    return exp(-x*t)

result = quad(testfunc, 1, 10, args=(10))
print "Result=", result

