#!/usr/bin/env python
# Module:   sqlite2.py
# Purpose:  Sqlite test 2
# Date:     N/A
# Notes:
# 1) Test of Python SQLite interface
# 2) Define OLD=1 to use sqlite module, not sqlite3
#    (CentOS 5 still only includes the older sqlite module).
# 3) I like to give my SQLITE databases names with a 
#    sqlite suffix (makes it easier when listing dirs).
# 4) Verify on cmd line:
#      sqlite3 test2_db.sqlite "select * from test_tbl"
# 5) When done, manually delete the test database, or
#    run the cleanup.py cleanup script....
#
# Ref:  http://zetcode.com/db/sqlitepythontutorial/

# define our test DB 
# -- can use special name ":memory:" for in-memory RAM database
TEST_DB="test2_db.sqlite"

print "SQLITE2.PY:  creating and using test db:", TEST_DB

# define timeout in seconds
TMO=15

# support older sqlite module for CentOS 5, etc.
OLD=0

if (OLD):
    import sqlite as sl
    TMO=TMO*1000
else:
    import sqlite3 as sl

import sys
from subprocess import call

# handle exceptions for connection and creation of DBS
try:
    # connect/create the test DB then create a cursor
    # specify timeout, seconds (for older this is in ms)
    con = sl.connect(TEST_DB, timeout=TMO)
    cur = con.cursor()

    # create a test table called "test_tbl" then populate it
    cur.execute('drop table if exists test_tbl')
    sql = \
"""create table test_tbl  (
     sec   int,
     usec  int,
     key   text

   )
"""

    #print "SQL=",  sql
    cur.execute(sql)

    # commit the changes, i.e., write to the DBS
    con.commit()

except sl.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)

    
print "DB created..."

# do some work here....

# handle exceptions for data insertion
try:

    for i in range (1,11):
        str = "Hello %d" % i
        sql = "insert into test_tbl values(%d, %d, '%s')" % (i, i*i, str)
        print "SQL=", sql
        cur.execute(sql)

    # commit the changes, i.e., write to the DBS
    con.commit()
except sl.Error, e:
    
    print "Error %s:" % e.args[0]
    con.close()
    sys.exit(1)

# handle exceptions for querying the database
try:
    # from example, get the SQLITE version
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    
    print "SQLite version: %s" % data     

    sql = "select * from test_tbl where sec between 3 and 5"
    print "SQL=\"%s\"" % sql
    cur.execute(sql)
    
    data = cur.fetchall()
    print "Data: %s" % data    
    
except sl.Error, e:
    
    print "Error %s:" % e.args[0]
    sys.exit(1)
    
# Use "finally:" in Python 2.5 and later (CentOS 5 uses 2.4):
# finally:

# handle exceptions for dumping the DBS
try:
    # dump the DBS to xxx.sql using the iterdump() method
    # to restore:  cat xxx.sql | sqlite3 newdb.sqlite
    dumpfile="xxx.sql"
    with open(dumpfile, 'w') as f:
        for line in con.iterdump():
            f.write('%s\n' % line)
  
except Exception, e:
    print "Exception, e=", e
    sys.exit(1)


if con:
    con.close()

