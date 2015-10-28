#!/usr/bin/env python
# Module:   py_url1.py
# Purpose:  test some URL encode/decode functions
# Date:     N/A
# Notes:
# 1) See library notes for urllib, etc.
#
import urllib

print "py_url1.py:  Python URL processing test"


istr="https://github.com/joebob?tab=contributions&from=2015-10-21"
ostr=urllib.unquote(istr)
print "Test istr=", istr
print "     ostr=", ostr

istr="http://http://www.example.con/test%2BABC%20Test%3BValue"
ostr=urllib.unquote(istr)
print "Test istr=", istr
print "     ostr=", ostr

istr="https://mail.google.com/mail/u/0/?tab=om&zx=xxabckvjl#inbox"
ostr=urllib.unquote(istr)
print "Test istr=", istr
print "     ostr=", ostr

istr="abc=%2BABCDE jkl=%2BFGHIJ%3BKLMN"
ostr=urllib.unquote(istr)
print "Test istr=", istr
print "     ostr=", ostr
