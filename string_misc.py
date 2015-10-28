#!/usr/bin/env python
# Module:   string_misc.py
# Purpose:  string functions
# Date:     N/A
# Notes:
# 1) Reference:
#     https://docs.python.org/3.1/library/stdtypes.html#string-methods
#     http://stackoverflow.com/questions/1228299/change-one-character-in-a-string-in-python

s = "Create test string \"s\" with misc data!"
print "Input=", s

print "test using conversion to list to make changeable"
print "strings are read-only, immutable, so can't change, assign to list"
sl = list(s)

n = 0
for c in s:
    if (c == ' '):
        sl[n]='_'    # convert space to _
    n+=1             # unlike C, can't do n++

print "new list:  \n  ", sl

snew="".join(sl)
print "join back to string at end:\n  ", snew

print "test using bytearray"
bs = bytearray(s)
n=0
for c in s:
    if (c == ' '):
        bs[n]='_'    # convert space to _
    n+=1             # unlike C, can't do n++
snew2=str(bs)
print "convert back to string at end\n  ", snew2

print "split into words and print 2nd word"
sw=s.split()
sw2=s.split()[1]
print "  split=", sw
print "  2d=", sw2

print "string escaping, use \" or ' and \\ to escape"
cmd="date -d '2000-01-01 00:00:00 UTC' +'%s'"
print "CMD=\"%s\"" % cmd

print "raw strings start with r\""
rstr=r"C:\somepath\i\am\a\virus.exe"
print "raw string=\"%s\"" % rstr

print "multi-line string"
mlstr="""This is a very long
and multi-line string and is a test of using
the special \"\"\" operator on it.

This is the end...."""
print "long string=\"%s\"" % mlstr
