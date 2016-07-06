#!/usr/bin/env python
# Module:   bytearray.py
# Purpose:  bytearray examples
# Date:     N/A
# Notes:
# 1) See http://www.dotnetperls.com/bytes-python
# Ref:  any references
#
"""bytearray.py:  examples of Python bytearray"""

import hashlib
OF = "ba_test.bin"

def bytearray_test():
    """bytearray.py:  run the examples"""
    
    print "Creating a byte array with data:"
    bv = [1, 2, 3, 4, 5, 255, 254, 253, 252]
    ba = bytearray(bv)

    print "ArrayA= ",
    for i in range(len(ba)):
        print "%02x" % ba[i],
    print ""

    print "Creating a binary file \"{0}\", use wb for open type:".format(OF)
    bf = open(OF, "wb")
    bf.write(ba)
    bf.close()

    print "Reading back in to buffer B"
    bf = open(OF, "rb")
    rd = bf.read()
    bb = bytearray(rd)
    bf.close()

    m=hashlib.sha1()
    m.update(ba)
    print "DigestA= ", m.hexdigest()
    
    m=hashlib.sha1()
    m.update(bb)
    print "DigestB= ", m.hexdigest()

    print "Making a copy -> C"
    bc = bytearray(ba)
    if (ba == bc):
        print "SAME BUFFER"
    else:
        print "DIFFERENT BUFFER"

    print "Changing the data"
    bc[1] = 0
    bc[2] = 0

    print "ArrayA= ",
    for i in range(len(ba)):
        print "%02x" % ba[i],
    print ""
    print "ArrayC= ",
    for i in range(len(bc)):
        print "%02x" % bc[i],
    print ""

    m=hashlib.sha1()
    m.update(bc)
    print "DigestC= ", m.hexdigest()

    if (ba == bc):
        print "SAME BUFFER"
    else:
        print "DIFFERENT BUFFER"

    print "Directly create a bytearray and convert back to list"
    bf = bytearray([3,4,5])
    lf = list(bf)

    print "Finding substring using .find()"
    idx = ba.find(bf)
    print "Found {0} at {1}".format(lf, idx)


if __name__ == "__main__":
    bytearray_test()



