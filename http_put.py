#!/usr/bin/env python
# Module:   http_put.py
# Purpose:  Make a HTTP PUT request
# Date:     N/A
# Notes:
# 1) Ref:  
#      http://stackoverflow.com/questions/111945/is-there-any-way-to-do-http-put-in-python
#      https://docs.python.org/2/library/httplib.html#httplib.HTTPResponse
#
# 2) This does a PUT, POST, and GET on port 1025 (by default).  It is a very
#    simple HTTP program using httplib to send the request and get the response.
#    This example can be the basis for a REST system/API.
#
# 3) Usage:
#      run http_multi_handler.py on port 1025 (or a similar program)
#      ./http_put.py
#
import datetime as dt
import httplib
import sys

port = 1025
today=dt.datetime.today()

print "http_put.py:  test making a HTTP PUT request"
URL="localhost:%d" % port
body_content = "Hello at %s, this is a test!" % today
print "Connecting to: %s\nMessage=%s" % (URL, body_content)
#connection =  httplib.HTTPConnection('localhost:1025')
connection =  httplib.HTTPConnection(URL)

# actually do the PUT
print "PUT:  "
try:
    connection.request('PUT', '/', body_content)
    result=connection.getresponse()
    print "status=%s, result=%s" % (result.status, result.read())
except Exception, e:
    print "Exception, e=", e
    sys.exit(1)

# do a POST
print "POST:  "
try:
    connection.request('POST', '/', body_content)
    result=connection.getresponse()
    print "status=%s, result=%s" % (result.status, result.read())
except Exception, e:
    print "Exception, e=", e

# do a GET
print "GET:  "
try:
    connection.request('GET', '/', "index.html")
    result=connection.getresponse()
    print "status=%s, result=%s" % (result.status, result.read())
except Exception, e:
    print "Exception, e=", e

print "DONE!"
