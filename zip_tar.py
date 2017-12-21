#!/usr/bin/env python
# Module:   zip_tar.py
# Purpose:  libzip and libtar 
# Date:     N/A
# Notes:
# 1) Based on perl examples
#
"""ZIP and TAR creation examples"""
import os
import sys
import zipfile
import tarfile

class pgm_opts:
    def __init__(self):
        self.verbose=1
        self.TEST_DIR="test"
        self.TEST_DIR2="test/moretests"


def make_dirs(P):
    """make test dirs"""
    try:
        os.mkdir(P.TEST_DIR)
        os.mkdir(P.TEST_DIR2)
    except Exception, e:
        print "Exception, e=", e
        sys.exit(1)
 

def test_main(P):
    make_dirs(P)


if __name__ == '__main__':
    P =  pgm_opts()
    if 0<P.verbose:  print "zip_tar.py:  making test ZIP/TAR files"
    test_main(P)
    if 0<P.verbose:  print "DONE"
