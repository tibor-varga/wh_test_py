#!/usr/bin/env python
# Module:   websvr.py
# Purpose:  Simple web server test program, see notes
# Date:     N/A
# Notes:
# 1) Default page is index.html.  
# 2) Very useful to display pictures from a Raspberry Pi camera.
# 3) Browsers will also ask for favicon.ico and this will of course
#    complain if missing.  Create 16x16 icon and name favicon.ico.
# 2) Start from the cmd line:  python -m SimpleHTTPServer 8000
# 3) Ref:
#      https://docs.python.org/2/library/simplehttpserver.html
#
import SimpleHTTPServer
import SocketServer

PORT = 8001

print "websvr1.py:  web server on port", PORT
print "Access using URL:  http://localhost:%d" % PORT

# setup the handler
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

# or "0.0.0.0" for all, or "10.0.0.100" for an IP addr
httpd = SocketServer.TCPServer(("", PORT), Handler)

print "serving at port", PORT
print "type ctrl-C to exit...."

# run the server....
httpd.serve_forever()

