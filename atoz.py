#!/usr/bin/env python
# Module:   atoz.py
# Purpose:  example of range a..z using multiple means
# Date:     N/A
# Notes:
# 1) ...
# Ref:  http://stackoverflow.com/questions/3190122/python-how-to-print-range-a-z
#
print "atoz.py:  a..z as a result of range"

print "Simple examples of range of a..z using ord() and chr()"
# simple version using ord and chr
for i in range(ord('a'), ord('z')+1):
    c=chr(i)
    print "Char=%c" % c

# more complex version using map
print "Simple examples of range of a..z using map"
atoz = map(chr, range(ord('a'), ord('z')+1))
for c in atoz:
    print "Char=%c" % c
  
# version using a generator xrange() 
print "Version using xrange generator"
xr=xrange(0,26)
for x in xr:
    c = (chr(ord('a')+x))
    print "Char=%c" % c

# all in one print
for x in xr:
    print "Char={0}".format(chr(ord('a')+x))

