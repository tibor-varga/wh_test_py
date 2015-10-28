#!/usr/bin/env python
# Module:   py_inotify3.py
# Purpose:  use pyinotify to monitor a test dir
# Date:     N/A
# Notes:
# 1) https://github.com/seb-m/pyinotify/wiki
#    -- examples/daemon.py
#
import pyinotify
import time as t
import datetime as dt
import os
import sys
import signal

# define the monitor dir
MONDIR="./test"


# log event and name of event
def log_event(ltype, name):
    try:
        tf = open(LOG, "a")
        now=t.time()
        ds = dt.datetime.fromtimestamp(now)
        str="%10.6f %s %s %s\n" % (now, ds, name, ltype)
        tf.write(str)
        tf.close()
        print "%10.6f: %s %s\n" % (now, name, ltype)
    except Exception, e:
        print "Exception, e=", e


# signal handler for TERM, etc.
def sig_handler(signum, frame):
    msg="Signal %d" % signum
    log_event(msg, "None")
    sys.exit(0)


# callback function for inotify
# - extra as we can do all with the EventHandler below....
def loop_func(notifier):
    msg="loop_func() called"
    log_event(msg, "None")
    return False  # required to keep from exiting main inotify loop


# event handler for inotify events, inherit from processing base
# class ProcessEvent, handle notifications for specific actions
class EventHandler(pyinotify.ProcessEvent):
    def process_IN_MOVED_TO(self, event):
        log_event("Moved To", event.pathname)

    def process_IN_CLOSE_WRITE(self, event):
        log_event("Close Write", event.pathname)


print "py_inotify3.py:  pyinotify test -- daemon to watch", MONDIR
print "After this starts, create some test files in ", MONDIR


# Create log file name with current directory
CWD=os.getcwd()
LOG="%s/logfile.log" % CWD


# trap signals so we can kill the daemon
signal.signal(signal.SIGHUP, sig_handler)
signal.signal(signal.SIGTERM, sig_handler)
signal.signal(signal.SIGINT, sig_handler)


# Create WatchManager object for inotify
wm = pyinotify.WatchManager()

# Associate this WatchManager with a Notifier 
# - will be used to report and process events
# - calls the "handler" for each event received
handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)

# Add a new watch on /tmp for ALL_EVENTS.
# - example with ALL events:
#     wm.add_watch(MONDIR, pyinotify.ALL_EVENTS) 
print "Watching for IN_MOVED_TO and IN_CLOSE_WRITE events"
wm.add_watch(MONDIR, pyinotify.IN_MOVED_TO|pyinotify.IN_CLOSE_WRITE)

# Log startup message
log_event("Startup", "None")

# Loop and handle events via a daemon in the notifier object
try:
    notifier.loop(daemonize=True, callback=loop_func,
                  pid_file='/tmp/py_inotify3.pid',
                  stdout=LOG)
except Exception, e:
    msg = "ERROR with loop, e=", e
    print "msg"
    log_event(msg, "None") 

print "Done"

