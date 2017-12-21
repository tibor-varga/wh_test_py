#!/usr/bin/env python
# Module:   zip_simple.py
# Purpose:  simple zip of a dir
# Date:     N/A
# Notes:
# 1) Based on:
#    https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory
#
import os
import zipfile

print "zip_simple.py:  simple zip example w/ dir walking"

# make some test files
try:
    os.mkdir("test")
except Exception, e:
    pass
try:
    os.mkdir("test/moretests")
except Exception, e:
    pass

fp=open("test/filea.txt", "w")
for i in range(10):  fp.write("test line\n")
fp.close()
fp=open("test/moretests/fileb.txt", "w")
fp.close()

# create the ZIP and walk the dir tree to add files
print "Creating myzipfile1.zip"
zf = zipfile.ZipFile("myzipfile1.zip", "w")
for dirname, subdirs, files in os.walk("test"):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))

zf.close()
print "Done!"
