#!/usr/bin/env python
# Module:   web_read_get.py
# Purpose:  Get file from web site
# Date:     N/A
# Notes:
# 1) See this page for data types for normal downloads:
#       http://www.srh.noaa.gov/jetstream/doppler/ridge_download.html
#
import urllib
import sys

# Import one of the string io modules so we can read response
# a line at a time, see my test program py_stringio.py.
try:
    print "Trying to use cStringIO first"
    import cStringIO
    StringIO = cStringIO
except ImportError:
    print "cStringIO not found, use StringIO instead"
    import StringIO

WX_URL='http://radar.weather.gov/ridge/Conus/RadarImg/'
print("web_read_get.py:  get NWS RADAR national mosaic (latest)")

print("Should throw exception:")
try:
    test_url="http://xaxlkjaasdfl" + "/" + "badfile.gif"
    print("Reading from URL=%s" % test_url)
    conn=urllib.urlopen(test_url)
    code=conn.getcode()
    if (code == 200):
        print("GET URL, GOOD, code=%d, Read:" % code)
    else:
        print("GET URL, GOOD, code=%d, Read:" % code)
except Exception, e:
    print "GET URL Exception, e=", e

print("Should not throw exception but should have 404 code:")
try:
    test_url=WX_URL + "/" + "badfile.gif"
    print("Reading from URL=%s" % test_url)
    conn=urllib.urlopen(test_url)
    code=conn.getcode()
    if (code == 200):
        print("GET URL, GOOD, code=%d, Read:" % code)
    else:
        print("GET URL, GOOD, code=%d, Read:" % code)
except Exception, e:
    print "GET URL Exception, e=", e


rd = "NO DATA"
print("Should read a file:")
try:
    test_url=WX_URL + "/" + "latest_radaronly.gfw"
    print("Reading from URL=%s" % test_url)
    conn=urllib.urlopen(test_url)
    code=conn.getcode()
    rd=conn.read()
    if (code == 200):
        print("GET URL, GOOD, code=%d, Read:" % code)
    else:
        rd=conn.read()
        print("GET URL, GOOD, code=%d, Read:" % code)
except Exception, e:
    print "GET URL Exception, e=", e

if (rd != "NO DATA"):
    print("Read %d characters:" % len(rd))
    for line in StringIO.StringIO(rd):
        line = line.strip()
        print("  %s" % line)

print("Should read a file and write it to disk:")
try:
    fname="latest_Small.gif"
    test_url=WX_URL + "/" + fname
    print("Reading from URL=%s" % test_url)
    res = urllib.urlretrieve(test_url, fname)
    print("Result:", res)
except Exception, e:
    print "GET URL Exception, e=", e
