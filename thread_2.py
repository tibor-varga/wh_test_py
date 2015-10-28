#!/usr/bin/env python
# Module:   thread_2.py
# Purpose:  thread test with queue 
# Date:     N/A
# Notes:
# 1) Reference:
#     https://docs.python.org/3/library/threading.html
#     https://pymotw.com/2/threading/
#
import Queue
import threading
from threading import Timer
from threading import Event
import time as t
td=10.0

# define a queue
msgq = Queue.Queue()

# define a worker thread 
def my_thread():
    while True:
        msg=msgq.get()
        tt=t.asctime()
        print tt, ":  worker read:  ", msg
        
        if msg == 'quit':
            break
            
    tt=t.asctime()
    print tt, ":  worker done"
    t.sleep(1)
    return

# main below here....

print "creating thread"
th=threading.Thread(target=my_thread)

tt=t.asctime()
print tt, ":  thread starting"
th.start()

for x in range (1,5):
    msgq.put("x%d" % x)
    t.sleep(1)

msgq.put('quit')

tt=t.asctime()
print tt, ":  thread joining"
th.join()

tt=t.asctime()
print tt, ":  thread done"

