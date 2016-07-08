#!/usr/bin/env python
# Module:   entropy.py
# Purpose:  compute entropy of a group of bytes
# Date:     N/A
# Notes:
# 1) ...
# Ref:
#  http://stackoverflow.com/questions/990477/how-to-calculate-the-entropy-of-a-file
#
"""Compute Shannon Entropy of blocks of bytes"""

import math
import random

# compute the Shannon entropy of a buffer
def compute_entropy(in_buf):
    """Compute and display entropy of a buffer"""

    byte_buff = bytearray(in_buf)

    # create byte count array, initialized to 0
    byte_count = [0 for x in range(256)]

    print "Compute counts for each byte value"
    total = len(byte_buff)
    for this_byte in range(256):
        #print "this_byte=", this_byte
        cnt = 0
        for byte in byte_buff:
            if byte == this_byte:
                cnt += 1
        byte_count[this_byte] = cnt

    #print "len byte_count = ", len(byte_count)
    print "Compute probability and Shannon entropy"
    ent = 0.0
    #i = 0
    #print len(byte_count)
    for cnt in byte_count:
        #print "I=", i
        if cnt == 0:
            #i += 1
            continue
        prob = (1.0 * cnt) / total
        #print "P[{0}] = {1}".format(i, p)
        ent -= prob * math.log(prob, 256)
        #i += 1
    print "Entropy is ", ent


# run the entropy test
def run_entropy():
    """Run the entropy tests"""

    print "entropy.py:  Computing entropy of a byte buffers"

    tot = 1024
    print "Creating buffer with random data, len={0}".format(tot)
    byte_buff = bytearray(tot)
    #print "buff len=", len(byte_buff)
    random.seed(1234)
    for i in range(tot):
        byte_buff[i] = int(random.random()*256)

    compute_entropy(byte_buff)

    byte_buff = b'0123456789'
    tot = len(byte_buff)
    print "Creating buffer with ASCII 0..9, len={0}".format(tot)
    compute_entropy(byte_buff)

    byte_buff = bytearray([int(random.triangular(0, 100, 50))
                           for x in range(1024)])
    tot = len(byte_buff)
    print "Creating buffer with triangular distribution, len={0}".format(tot)
    compute_entropy(byte_buff)

# module main
if __name__ == "__main__":
    run_entropy()
