#!/usr/bin/env python
# Module:   nums.py
# Purpose:  numeric and string conversions
# Date:     N/A
# Notes:
# 1) 
# Ref:  any references

print "nums.py:  Python numbers"

aa='127-3'
ae=eval(aa)
print "start with an expression \'", aa, "\' and evaluate it=", ae

ab=bin(ae)
print "convert to binary string=", ab

ai=int(ab,2)
print "convert back to int=", ai

ai=int(ab,0)
print "convert back to int (auto conversion using 0)=", ai

am=int(ab,2)&int('0xf',0)
print "mask off all but lower 4 bits=", am

ah=hex(int(ab,2))
print "convert to hex=", ah

db="deadbeef"
di=int(db, 16)
print "convert \"", db, "\" to int=", di

dbh="0xdeadbeef"
di=int(dbh, 0)
print "convert \"", db, "\" to int (auto conv)=", di

hdb="%x" % di
print "convert back to hex=", hdb

import math as m
pi=m.pi

fhdb=float(int(hdb,16))
print "converted to float=", fhdb

fp=fhdb/pi * m.cos(pi/2.0)
print "math test=", fp

fh=fp.hex()
print "converted to hex=", fh





