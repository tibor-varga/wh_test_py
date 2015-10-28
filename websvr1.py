#!/usr/bin/env python
# Module:   websvr1.py
# Purpose:  Simple web server test program, see notes
# Date:     N/A
# Notes:
# 1) Simple server that only runs for TMO seconds
# 2) Runs a thread with a timer to fetch a page from
#    the web server and print it, then kill the web server.
#    Also adds exceptions in multiple places to cleanup the 
#    error handling from the socket and web server.
#
import SimpleHTTPServer
import SocketServer
import threading
import time as t
import urllib as u
import sys

PORT = 8001
TMO  = 10    # seconds

print "websvr1.py:  web server and client in one test program"

# setup the handler
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

# or "0.0.0.0" for all, or "10.0.0.100" for an IP addr
try:
    httpd = SocketServer.TCPServer(("", PORT), Handler)
except Exception,e:
    print "Could not bind to port",PORT, " e=", e
    sys.exit(1)


# get time as string:  ssssssssss.uuuuuu
def Now():
    now=t.time()
    s_now = "%10.6f" % now
    return(s_now)

# timer thread, delay and close socket
def my_thread():
    print Now(), ":  thread starting, delaying 1 sec"
    t.sleep(1)
    # get data from the web server
    mydata=""
    try:
        myurl = "http://localhost:%s" % PORT
        print Now(), ":  fetching ", myurl
        myfd  = u.urlopen(myurl)
        mydata= myfd.read()
        myfd.close()

    except Exception, e:
        print "Exception, e=", e
    
    print Now(), ":  read:\n", mydata

    # sleep until timeout then close thread
    t.sleep(TMO-1)
    print Now(), ":  thread timeout"
    httpd.server_close()
    return


print Now(), ":  Running web server on port ", PORT
print Now(), ":  This will exit in ", TMO, "seconds, or type ctrl-C to exit...."

# start the timer thread
th=threading.Thread(target=my_thread)
th.start()

# run the server....
try:
    httpd.serve_forever()
except Exception, e:
    print "Exception, e=", e

# join thread and exit
print Now(), ":  joining thead"
th.join()

print Now(), ":  done"



