#!/usr/bin/env python
# Module:   hash_test.py
# Purpose:  test hashes
# Date:     N/A
# Notes:
# 1) https://docs.python.org/2/library/hashlib.html
# 2) This requires python-hashlib be installed on CentOS 5
#    which is backported from Python 2.5....
#
import hashlib
import random as r
import os

TFILE="hash_test.dat"

HASHES=hashlib.algorithms
print "hash_test.py:  hash tests, supported libs=", HASHES

print "Creating a sha512 hash of random data"
m = hashlib.sha512()
for x in range(0,10):
    f=r.random()
    m.update(str(f))

print "Hash=", m.hexdigest()

print "Creating a test file and creating sha1 sum via cmd and code"
ofile=open(TFILE, "w")
m = hashlib.sha1()
for x in range(0,10):
    f=r.random()
    s="%03d %f\n" % (x, f)
    ofile.write(s)
    m.update(s)
ofile.close()
  
print "Hash=", m.hexdigest()
cmd="sha1sum %s" % TFILE
os.system(cmd)

    
