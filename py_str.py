#!/usr/bin/env python
# Module:   py_str.py
# Purpose:  structure and named tuples
# Date:     N/A
# Notes:    
# 1)  Test python code
#     http://stackoverflow.com/questions/35988/c-like-structures-in-python
#     https://docs.python.org/2/library/ctypes.html#structures-and-unions
#   
print "py_str.py:  Python structures and named tuples"

print "Using a simple class xx1 with 3 items, x, y, z:"
# create simple class and constructor
# - verbose but simple and clear, easy to understand
class xx1:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

x1 = xx1(1,2,3)
print "X1=", x1.x, x1.y, x1.z

# create a class with a dictionary
# - dynamic, not pre-defined
print "Another class xx2 using a dictionary:"
class xx2:
    def __init__(self, **kwds):
        self.__dict__.update(kwds)
        
x2 = xx2(a=1, b=2, c=3)
print "X2=", x2.a, x2.b, x2.c

# example using namedtuple, defined when you create the named tuple
from collections import namedtuple
print "Using a named tuple xx3 with three items, x, y, z):"
xx3=namedtuple("xx2", "a b c")
x3=xx3(1,2,3)
print "X3=", x3.a, x3.b, x3.c 

# example of simple class w/o constructor
print "Using a simple class w/o constructor:"
class xx4:
    a = 0
    b = 0
    c = 0

x4=xx4()
x4.a = 1
x4.b = 2
x4.c = 3
print "X4=", x4.a, x4.b, x4.c 

# example of a more complex structure using dictionaries
print "Using a more complex dictionary"
class xx5(dict):
    def __init__(self, **kwargs):
        super(xx5, self).__init__(**kwargs)
        self.__dict__ = self

x5=xx5(a=1, b=2, c=3)
# another example:  
#   x5=xx5(a=1, b='asdf', c=3.14)
print "X5=", x5.a, x5.b, x5.c 

# using C structures -- interesting -- not recommended....
print "Using ctypes and C data structures:"
from ctypes import *
class xx6(Structure):
    _fields_ = [("a", c_int),
                ("b", c_int),
                ("c", c_int)]

x6=xx6(1,2,3)
print "X6=", x6.a, x6.b, x6.c 
