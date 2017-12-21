#!/usr/bin/env python
# Module:   tar_test.py
# Purpose:  test/demonstrate TAR API
# Date:     N/A
# Notes:
# 1) https://docs.python.org/2/library/tarfile.html
#    https://docs.python.org/3/library/tarfile.html
#
# 2) Python 3 supports lzma (xz) tar files, but Python 2
#    only supports zip, gzip, and bz2.
#
# -- for compressed TAR
#TF="myfile.tgz"
#TYPE="w:gz"   # or w:bz2 or w:xz (
TF="myfile.tar"
TYPE="w"

import tarfile
import time as t
import sys, os
import StringIO

#-------------------------------------------------------------------
def make_test_file(fname="myfile.dat", cnt=10):
    # Create test file
    SF=fname
    if (cnt < 0):
        cnt = 10
    fo=open(SF,"w")
    ts=t.time()
    AT=t.asctime(t.localtime(ts))
    print "Start=", AT
    for x in range(0,cnt):
        fo.write("Time=%s\n" % AT)
    
    fo.close()



#-------------------------------------------------------------------
# main code below here
try:
    tf=tarfile.open(TF, mode=TYPE)

except tarfile.TarError as err:
    print "TarError", str(err)
    sys.exit(2)

except tarfile.ReadError as err:
    print "ReadError", str(err)
    sys.exit(2)

except tarfile.CompressionError as err:
    print "CompressionError", str(err)
    sys.exit(2)

except tarfile.StreamError as err:
    print "StreamError", str(err)
    sys.exit(2)

except tarfile.ExtractError as err:
    print "ExtractError", str(err)
    sys.exit(2)

except tarfile.HeaderError as err:
    print "HeaderError", str(err)
    sys.exit(2)


# make test files
for x in range(0,10):
    fname="test_data_%03d.dat" % x
    make_test_file(fname, x)
    tf.add(fname)

# open a test file, then make a tarinfo point to it, then add it
# -- there is a bug in this code somewhere.....
#x=1000
#fname="long_file.dat"
#make_test_file(fname, x)
#ti=tarfile.TarInfo(fname)
#ti.size=os.stat(fname).st_size
#ti.mode=0666
#ti.mtime=t.time()
#ti.type=tarfile.REGTYPE
#ti.uid=1000
#ti.gid=1000
#tf.addfile(ti)
#print "added ", fname


# use StringIO to make a file object and add it 
so=StringIO.StringIO()
for x in range(0,100):
    so.write("Test string %06d\n" % x)

sol=so.tell()
so.seek(0)
print "so size is ", sol

#tf.close()
#sys.exit(0)

fname="StringIO_File.dat"
ti=tarfile.TarInfo(fname)
ti.size=sol # so.tell() # so.len()
ti.mode=0600
ti.mtime=t.time()
ti.type=tarfile.REGTYPE
ti.uid=1001
ti.gid=1001
tf.addfile(ti,so)
so.close()
print "added ", fname

# add this file
fname = 'tar_test.py'
tf.add(fname)
print "added ", fname

tf.close()




  

