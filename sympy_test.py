#!/usr/bin/env python
# Module:   sympy_test.py
# Purpose:  examples of sympy 
# Date:     N/A
# Notes:
#   http://docs.sympy.org/latest/tutorial/intro.html#what-is-symbolic-computation
#
from sympy import *

print "syypy_test.py:  Test of SYMPY"

x,y,z = symbols('x y z')
res=diff(sin(x),x)
print "diff(sin(x) dx is:  ", res
res=diff(cos(x),x)
print "diff(cos(x) dx is:  ", res

res=integrate(sin(x**2), (x, -oo, oo))
print "integrate(sin(x**2) is:  ", res

res=diff(sin(3*x),x)
print "diff(sin(3*x) dx is:  ", res
res1=diff(res,x)
print "diff(%s) dx is:  %s" % (res, res1)
res2=diff(res1,x)
print "diff(%s) dx is:  %s" % (res1, res2)
