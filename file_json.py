#!/usr/bin/env python
# Module:   file_json.py
# Purpose:  File json tests
# Date:     N/A
# Notes:
# 1) tbd
# Ref:  
#   https://docs.python.org/2/library/json.html
#
import json
import os
MYFILE="fj_test.json"

print "Create some strings:"
str1=[1, 2, 'Inner 1']
str2=['Inner 2']
str3=[3, str1, str2, 'Outer']
print "  1:    ", str1
print "  2:    ", str2
print "  3:    ", str3

print "Encode str3 as JSON"
js1 = json.dumps(str3)
print "  js1:  ", js1

str4=['foo', {'bar': ('baz', None, 1.0, 2)}]
js2 = json.dumps(str4)
print "  js2:  ", js2

print "Access some elements of str4:"
a = str4[0]
b = str4[1]
c = str4[1]['bar']
d = str4[1]['bar'][0]
print "  ", a, b, c, d

print "Persist to a file:"
fo = open(MYFILE, "w")
print "FO=", fo
json.dump(str4, fo)
fo.close()

print "Read back from the file:"
fi = open(MYFILE, "r")
print "FI=", fi
str5=json.load(fi)
fi.close()
print "  str5:  ", str5

print "Access some elements of str4:"
a = str5[0]
b = str5[1]
c = str5[1]['bar']
d = str5[1]['bar'][0]
print "  ", a, b, c, d




