#!/usr/bin/env python
# Module:   test_module.py
# Purpose:  a test module with a couple of functions
# Date:     N/A
# Notes:
# 1) https://docs.python.org/3/tutorial/modules.html

# f1 function, print f1 N times
def f1(n):
    for x in range(0, n):
        print "F1"

# f2 function, print cos(pi*n)
def f2(n):
    from math import cos, pi
    for x in range(0, n):
        print "cos(x)=", cos(pi*x)

# module test 
if __name__ == "__main__":
    f1(5)
    f2(6)


