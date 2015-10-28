#!/usr/bin/env python
# Module:   anydbm_test.py
# Purpose:  anydbm test 
# Date:     N/A
# Notes:
# 1) Reference:
#      https://docs.python.org/2/library/anydbm.html
# 2) This has been renamed to "dbm" in Python 3.
#
import anydbm
import random as r

mydb="testdb.db"
rcnt=10
print "creating test db",mydb, "with ", rcnt, "records"

try:
    db=anydbm.open(mydb, 'c')
except anydbm.error as err:
    print str(err)
    sys.exit(2)
    
for x in range(0,rcnt):
    key="%03d" % x
    val="%10f km" % (10*r.random())
    print "K[v]=", key, '[', val, ']'
    db[key]=val

print "using some dict methods"

keys=db.keys()
print "Keys=", keys

ll=len(db)
print "DB size=", ll

print "testing for key 000"
if ('000' in db):
    print "Key 000 found"
else:
    print "key 000 not found"

print "deleting key"
del db['000']
if ('000' in db):
    print "Key 000 found"
else:
    print "key 000 not found"

ll=len(db)
print "DB size=", ll

# shrink the DB
# -- not supported by anydbm
#db.reorganize()

db.close()

print "opening and looking through all keys"
db=anydbm.open(mydb, 'r')
# use iteritems with anydbm
for k,v in db.iteritems():
    print k, ' ', v

print "get keys ans sort then loop on sorted keys"
keys=db.keys()
keys.sort()
print "Keys=", keys
for k in keys:
    v=db[k]
    print k, ' ', v

db.close()


