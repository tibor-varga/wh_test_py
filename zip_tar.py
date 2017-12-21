#!/usr/bin/env python
# Module:   zip_tar.py
# Purpose:  libzip and libtar 
# Date:     N/A
# Notes:
# 1) Based on perl examples
#    https://stackoverflow.com/questions/1855095/how-to-create-a-zip-archive-of-a-directory
#
"""ZIP and TAR creation examples"""
import os
import sys
import zipfile
import tarfile
import shutil

# program options/defaults -- use a class to store them!
class pgm_opts:
    def __init__(self):
        self.verbose=1
        self.TEST_DIR="test"
        self.TEST_DIR2="test/moretests"
        self.TAR_TYPE="w:gz"
        self.TAR_TYPE_R="r:gz"
        self.TGZ="test.tgz"
        self.ZIP="test.zip"
        self.ZIP1="test1.zip"
        

def make_dirs(P):
    """make test dirs as defined in P """
    try:
        os.mkdir(P.TEST_DIR)
    except Exception, e:
        print "Exception, e=", e

    try:
        os.mkdir(P.TEST_DIR2)
    except Exception, e:
        print "Exception, e=", e


def make_test_file(P,path,fname):
    """make a dummy test file"""

    try:
        tfn=path + "/" + fname
        tf=open(tfn, "w")
        tf.write("#!/bin/cat\n# test file %s" % tfn)
        for i in range(10):
            tf.write("# This is a test line %d\n" % i)
        tf.close()
    except Exception, e:
        print "Exception, e=", e

 
def make_test_files(P):
    """make test files in the P.TEST_DIR directory"""
    make_dirs(P)
    
    make_test_file(P, P.TEST_DIR, "top_test1.txt")
    make_test_file(P, P.TEST_DIR, "top_test2.txt")

    make_test_file(P, P.TEST_DIR2, "sub_test1.txt")
    make_test_file(P, P.TEST_DIR2, "sub_test2.txt")


def make_tgz(P):
    """make a compressed tar file as defined in P"""

    print "Creating tar file=%s from \"%s\"" % (P.TGZ, P.TEST_DIR)
    try:
        tf = tarfile.open(P.TGZ, P.TAR_TYPE)
        tf.add(P.TEST_DIR, recursive=True, exclude=None)
        tf.close

    except tarfile.TarError as err:
        print "TarError", str(err)

    except tarfile.ReadError as err:
        print "ReadError", str(err)

    except tarfile.CompressionError as err:
        print "CompressionError", str(err)

    print "Reading tar file"
    try:
        tf = tarfile.open(P.TGZ, P.TAR_TYPE_R)
        tf.list(verbose=True)
        tf.close

    except tarfile.TarError as err:
        print "TarError", str(err)

    except tarfile.ReadError as err:
        print "ReadError", str(err)

    except tarfile.CompressionError as err:
        print "CompressionError", str(err)


def zipdir(path, ziph):
    """add to ZIP file from a path, from stackexchange...."""

    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


def make_zip(P):
    """make a ZIP file as defined in P"""

    test_data="This is a test line\nand another\n"
    #test_bytes=bytearray(test_data)

    print "Creating ZIP file=%s from \"%s\"" % (P.ZIP, P.TEST_DIR)
    try:
        zf = zipfile.ZipFile(P.ZIP, "w")
        zf.writestr("writestr.txt", test_data)
        #zf.writestr("writestr.txt", test_bytes) <-- fails
        #zf.write(P.TEST_DIR)
        zipdir(P.TEST_DIR, zf)
        zf.close()
    except Exception, e:
        print "Exception, e=", e

    try:
        zf = zipfile.ZipFile(P.ZIP, "r")
        zf.printdir()
        zf.close()
    except Exception, e:
        print "Exception, e=", e


def make_zip_shutil(P):
    """make ZIP using shutil in one line"""
    
    try:
        shutil.make_archive(P.ZIP1, 'zip', P.TEST_DIR)
    except Exception, e:
        print "Exception, e=", e


def test_main(P):
    """test main function"""
    make_test_files(P)
    make_tgz(P)
    make_zip(P)


if __name__ == '__main__':
    """main if run standalone"""
    P =  pgm_opts()
    if 0<P.verbose:  print "zip_tar.py:  making test ZIP/TAR files"
    test_main(P)
    if 0<P.verbose:  print "DONE"
