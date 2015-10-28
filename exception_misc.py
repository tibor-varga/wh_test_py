#!/usr/bin/env python
# Module:   exception_misc.py
# Purpose:  misc exception handlers
# Date:     N/A
# Notes:
# 1) https://docs.python.org/2/tutorial/errors.html
#    http://stackoverflow.com/questions/129144/generic-exception-handling-in-python-the-right-way
# 

import math

print "exception_misc.py:  misc exception examples"

print "divide by 0 with ZeroDivisonError trapped"
try:
    10 * (1/0)
except ZeroDivisionError as e:
    print "Exception, e=", e

print "Generic exception"
try:
    10 * (1/0)
except Exception, e:
    print "Exception, e=", e

print "Exception with finally -- newer Python only"
try:
    print "Test exception of KeyboardInterrupt"
    raise KeyboardInterrupt
finally:
    print "Done"

print "Should not get here"



