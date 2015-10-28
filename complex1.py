#!/usr/bin/env python
# Module:   complex1.py
# Purpose:  Python test code
# Date:     N/A
# Notes:    
# 1)  Test python code to for complex numbers
#
import cmath

PI=cmath.pi
E=cmath.e
R=10

# define a function E^-jwt
def xe(w,t):
    return(E**(-1.0j*w*t))

# compute a series of complex points and print them
zz=0
cnt=100
for x in range(1,cnt+1):
    xx=2*PI/x
    y=xe(100,xx)
    print "X->Y", xx, y
    zz=zz+abs(y)

zz=zz/cnt
print "Sum ABS=", zz

