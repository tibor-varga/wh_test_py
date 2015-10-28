#!/usr/bin/env python
# Module:   file_io.py
# Purpose:  misc file io tests
# Date:     N/A
# Notes:
# 1) tbd
# Ref:  
#   https://docs.python.org/2/tutorial/inputoutput.html
#   http://stackoverflow.com/questions/275018/how-can-i-remove-chomp-a-newline-in-python
#
import os
import subprocess

MYFILE="my_out.dat"

print "FILE_IO:  read/write/seek, etc. file IO"

print "Creating test file:  ", MYFILE
fo = open(MYFILE, "w")
print "FO=", fo

fo.write("(5**2)\n") 
fo.write("(5**2)\n") 
fo.write("99\n")
fo.write("99\n")
fo.close()

# read the file, open again for read
# Note:  If expecting \r\n or other newlines, use the
#        universal newline mode for reading so open as
#        "rU" or "U".  
print "Reading in test file"
fi = open(MYFILE, "r")
print "FI=", fi
fi_all=fi.read()
print "All contents:  "
print  fi_all
print 

# seek to start of file and re-read
print "Reading line at a time w/ strip "
fi.seek(0)
ii=1
for fi_line in fi:
    # equivalent to Perl's chomp(), remove newline
    # -- for UNIX, can just use rstrip('\n')
    fi_line=fi_line.rstrip('\r\n')
    # formatted print
    print "%3d:  %s" % (ii, fi_line)
    ii=ii+1

print "Read using file as iterator with exception handling"
fi.seek(0, os.SEEK_END)
fsize=fi.tell()
fi.seek(0)
for x in range(0, fsize+2):
    try:
        fi_line = fi.next()
        fi_line=fi_line.rstrip('\r\n')
        print "%05d " % x, fi_line
    except StopIteration:
        print "Iteration done"
        break

print "Done"
fi.close()

