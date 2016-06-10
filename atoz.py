#!/usr/bin/env python
# Module:   atoz.py
# Purpose:  example of range a..z using multiple means
# Date:     N/A
# Notes:
# 1) Reference:
# http://stackoverflow.com/questions/3190122/python-how-to-print-range-a-z
# http://stackoverflow.com/questions/1247486/python-list-comprehension-vs-map/
# 2) This was tested with pylint....
#
"""Print the letters from A to Z -- simple chr() and ord() test"""

print "atoz.py:  a..z as a result of range"

print "Simple examples of range of a..z using ord() and chr()"
# simple version using ord and chr
for i in range(ord('a'), ord('z')+1):
    c = chr(i)
    print "Char=%c" % c

# more complex version using map
print "Simple examples of range of a..z using map"
# According to pylint, don't use map, use list comprehension
#ATOZ = map(chr, range(ord('a'), ord('z')+1))
ATOZ = [chr(x) for x in range(ord('a'), ord('z')+1)]
for c in ATOZ:
    print "Char=%c" % c

# version using a generator xrange()
print "Version using xrange generator"
XR = xrange(0, 26)
for x in XR:
    c = (chr(ord('a')+x))
    print "Char=%c" % c

# all in one print
for x in XR:
    print "Char={0}".format(chr(ord('a')+x))

