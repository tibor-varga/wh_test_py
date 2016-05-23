#!/usr/bin/env python
# Module:   siphash_test.py
# Purpose:  to test siphash module
# Date:     N/A
# Notes:
# 1) References:
#      https://131002.net/siphash/
#      https://github.com/bozhu/siphash-python
#      -- this details how to install siphash....
# 2) This uses the siphash and md5 hash functions to hash a
#    blob of data.  The blob is created first. 
# 3) Siphash is a new (2012) hash which is better for collisions.
#    and is much faster.  The siphash included with this example
#    is in Python so it will be slower than the optomized md5 included
#    with the standard hashlib.
# 4) Python 3.4 includes Siphash as the default hash() (as does Perl
#    and Ruby).
#
import siphash
import hashlib

# get listing of functions in the siphash module
D=dir(siphash)
print "Methods in SIPHASH:", D

TEST_FCN_LOOPS=100
TEST_LOOPS=1000

mymsg = "This is a very long message that will be hashed.\
It includes multiple lines of text and all that stuff.\
The siphash function is in pure Python. \
End!"

# siphash test function
def siphash_test_fcn():
    key = '0123456789ABCDEF' 
    sip = siphash.SipHash_2_4(key)
    sip.update(mymsg)
    myhash=sip.hash()
    print "Key=%s Hash=%s" % (key, myhash)

# md5hash test function
def md5hash_test_fcn():
    key = '0123456789ABCDEF' 
    m = hashlib.md5()
    m.update(key)  # to be fair, include the key in the hash
    m.update(mymsg)
    myhash=m.hexdigest()
    print "Key=%s Hash=%s" % (key, myhash)


# module main, call both test functions
if __name__ == '__main__':

    import timeit
    print "siphash.py:  test siphash and time it"
    print "Test using siphash and timeit"
    print(timeit.timeit("siphash_test_fcn()",
                        setup="from __main__ import siphash_test_fcn",
                        number=TEST_LOOPS))

    print(timeit.timeit("md5hash_test_fcn()", 
                        setup="from __main__ import md5hash_test_fcn", 
                        number=TEST_LOOPS))

