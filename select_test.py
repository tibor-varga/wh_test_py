#!/usr/bin/env python
# Module:   select_test.py
# Purpose:  example of using select
# Date:     N/A
# Notes:
# 1) https://docs.python.org/2/library/select.html
#
import select
import os
from time import time, sleep

print "select_test.py:  example of using select"
print "Note:  this uses select.epoll() with timeout"

pipe_r, pipe_w = os.pipe()

cpid=os.fork()
if (cpid == 0):
    print "%f Child" % time()
    for ii in range(0,5):
        sleep(2)
        os.write(pipe_w, "%f Child Msg %d\n" % (time(), ii))
    os.write(pipe_w, "%f Child:  DONE\n" % time())
    exit(1)

else:
    print "%f Parent" % time()

    ep=select.epoll()
    ep.register(pipe_r, select.EPOLLIN)
    
    done_flag = False
    while True:
        events = ep.poll(1)
        le=len(events)
        if (le == 0):
             print "%f Parent timeout" % time()
                    
        for fileno, event in events:
            if fileno == pipe_r:
                str=os.read(pipe_r, 100)
                print "%f Parent Read str=%s" % (time(), str)
                if 'DONE' in str:
                    done_flag=True
                    break
            elif event & select.EPOLLHUP:
                ep.unregister(pipe_r)
                print "%f Parent EPOLLHUP, exiting" % time()
                done_flag=True
                break

        if (done_flag == True):
            break

    print "%f Parent waiting on child" % time()
    os.waitpid(cpid, 0)

print "%f Done" % time()

