#!/usr/bin/env python
# Module:   py_inotify2.py
# Purpose:  use pyinotify to monitor a test dir and report
# Date:     N/A
# Notes:
# 1) https://github.com/seb-m/pyinotify/wiki
#
import pyinotify
import time as t
import datetime as dt
import os

# define the monitor dir
MONDIR="./test"

remove_mode = 1

# log event name
def log_event(name):
    try:
        tf = open(LOG, "a")
        now=t.time()
        ds = dt.datetime.fromtimestamp(now)
        str="%f %s %s\n" % (now, ds, name)
        tf.write(str)
        tf.close()
    except Exception, e:
        print "Exception, e=", e
        

# event handler for inotify events, inherit from processing base
# class ProcessEvent, handle notifications for specific actions
class EventHandler(pyinotify.ProcessEvent):
    def process_IN_MOVED_TO(self, event):
        print "Moved To:", event.pathname
        log_event(event.pathname)
        if (remove_mode > 0):
            os.remove(event.pathname)

    def process_IN_CLOSE_WRITE(self, event):
        print "Close Write:", event.pathname
        log_event(event.pathname)
        if (remove_mode > 0):
            os.remove(event.pathname)


print "py_inotify2.py:  pyinotify test -- loop and watch", MONDIR
print "After this starts, create some test files in ", MONDIR

# get dir and build log name
CWD=os.getcwd()
LOG="%s/logfile.log" % CWD

# Create WatchManager
wm = pyinotify.WatchManager()

# Associate this WatchManager with a Notifier (will be used to report and
# process events).
handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)

# Add a new watch on /tmp for ALL_EVENTS.
#wm.add_watch(MONDIR, pyinotify.ALL_EVENTS)
print "Watching for IN_MOVED_TO and IN_CLOSE_WRITE events"
wm.add_watch(MONDIR, pyinotify.IN_MOVED_TO|pyinotify.IN_CLOSE_WRITE)

# Loop and handle events.
try:
    notifier.loop()
except Exception, e:
    print "ERROR with loop, e=", e

print "Done"

