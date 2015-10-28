#!/usr/bin/env python
# Module:   socket_example.py
# Purpose:  sample using sockets and epoll
# Date:     N/A
# Notes:
# 1) Ref:
#    http://stackoverflow.com/questions/12738590/python-epoll-and-nonblocking
#    http://scotdoyle.com/python-epoll-howto.html
#
import os
import socket,select,time

# define host and port
host = socket.gethostname()
port = 1234

print "socket_example.py:  example of client/server w/ socket"
print "Note:    this is also an example of epoll() in python"
print "         host=", host
print "         port=", port

# create the child which will run as a server on port
cpid=os.fork()
if (cpid==0):
    print "Child:   starting server on port", port
    s = socket.socket()
    s.bind((host,port))
    s.listen(50)
    s.setblocking(0)

    fdmap = {s.fileno():s}

    # setup for polling using select.epoll()
    p = select.epoll()
    p.register(s)
    done_flag = False
    print "Child:   waiting for events"

    # -- this should be using exception handling
    while done_flag == False:
        events = p.poll()
        for fd,event in events:
            if fd is s.fileno():
                c,addr = s.accept()
                c.setblocking(0)
                print "Child:   Got connection from: ",addr
                p.register(c)
                fdmap[c.fileno()] = c 
            elif event & select.EPOLLIN:
                data = fdmap[fd].recv(1024)
                if not data:
                    print "Child:   socket disconnected"
                    p.unregister(fd)
                    del fdmap[fd]
                    done_flag = True
                else:
                    print "Child:   read=", data

# the parent is the client, connect, send msg, close, wait
else:
    
    print "Parent:  client starting"
    time.sleep(1)
    s = socket.socket()
    
    s.connect((host,port))
    res = s.send(b'hello server')
    print "Parent:  sent=%d" % res
    s.close()

    os.waitpid(cpid, 0)

print "Done"
    
