#!/usr/bin/env python
# Module:   format_test.py
# Purpose:  demonstrate string.format and old string formatting
# Date:     N/A
# Notes:
# 1) https://docs.python.org/2/tutorial/inputoutput.html
#
from math import pi, cos

print "format_test.py:  output formatting examples"
print "simple case old and new format:"
for x in range(0,5):
    y=cos(pi/5 * x)
    # note for simple case, old format is easier
    print "old format %03d %10.5f" % (x, y)
    print "new format {0:03d} {1:10.5f}".format(x, y)

x=3
y=cos(pi/5 * x)
print "complex case re-use same var multiple times"
print "new format {0} {1:.5f} {0:03d} {1}".format(x, y)



 
