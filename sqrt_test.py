#!/usr/bin/env python
# Module:   sqrt_test.py
# Purpose:  Newton's method for SQRT
# Date:     N/A
# Notes:
# 1) TBD
# Ref:  http://en.wikipedia.org/wiki/Newton%27s_method

import math 

inval=33.0
guess=inval/2.0

sqrt_val = math.sqrt(inval)
print "IN=", inval, " SQRT(IN)=", sqrt_val

print "GUESS=", guess 


ival=[]
for i in range (1,10):
    guess = (inval/guess + guess)/2
    ival.append(guess)

print "RES=", guess
print "ival=", ival
