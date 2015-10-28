#!/usr/bin/env python
# Module:   json_test.py
# Purpose:  json test, similar to the shelve test 
# Date:     N/A
# Notes:
# 1) Reference:
#      https://docs.python.org/2/library/json.html
# 2) This is meant to be similar to the dbm examples which
#    only support a key,value pair, and shelve test code.
# 3) This is faster than shelve/dbm, etc., more portable,
#    and results in a human-readable output.  However, it 
#    does not support all Python objects (for example complex)
#    unlike shelve.
# 4) Supported types are:
#      character strings
#      numbers
#      booleans (True/False)
#      None
#      lists
#      dictionaries with character string keys
#
import json as j
import random as r
import os

mydb="testdb.json"
rcnt=10
print "creating test db",mydb, "with ", rcnt, "records"

# create in-memory dictionary
dict={} 
for x in range(0,rcnt):
    key="%03d" % x
    val="%10f" % r.random()
    print "K[v]=", key, '[', val, ']'
    dict[key]=val

print "print using json.dumps with indent"
print(j.dumps(dict, indent=4))

print "using some dict methods"

keys=dict.keys()
print "Keys=", keys

ll=len(dict)
print "DB size=", ll

print "testing for key 000"
if ('000' in dict):
    print "Key 000 found"
else:
    print "key 000 not found"

print "deleting key"
del dict['000']
if ('000' in dict):
    print "Key 000 found"
else:
    print "key 000 not found"

ll=len(dict)
print "DB size=", ll

# -- Note unlike using dbm, etc., the object is not
#    persisted to disk until it is serialized by 
#    json.dump() or json.dumps().  
print "serialize the dictionary as JSON"
fp=open(mydb, 'w')
j.dump(dict, fp)
fp.close()

print "opening and reading the object, then looking through all keys"
fp=open(mydb, 'r')
idict=j.load(fp)
fp.close()

# use iteritems with dictionary and anydbm
for k,v in idict.iteritems():
    print k, ' ', v



