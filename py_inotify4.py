#!/usr/bin/env python
# Module:   py_inotify4.py
# Purpose:  use pyinotify in a thread w/ old file processing
# Date:     N/A
# Notes:
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
    notifier.stop()
    sys.exit(0)


# Loop and do other stuff while inotify is running in background
def do_loop():
    while (1==1):
        t.sleep(1)


# event handler for inotify events, inherit from processing base
# class ProcessEvent, handle notifications for specific actions
class EventHandler(pyinotify.ProcessEvent):
    def process_IN_MOVED_TO(self, event):
        log_event("Moved To", event.pathname)

    def process_IN_CLOSE_WRITE(self, event):
        log_event("Close Write", event.pathname)


print "py_inotify4.py:  pyinotify test -- thread to watch", MONDIR
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
notifier = pyinotify.ThreadedNotifier(wm, handler)

# Log startup message and start the notifier
log_event("Startup", "None")
notifier.start()

# Add a new watch on /tmp for ALL_EVENTS.
# - example with ALL events:
#     wm.add_watch(MONDIR, pyinotify.ALL_EVENTS) 
print "Watching for IN_MOVED_TO and IN_CLOSE_WRITE events"
wm.add_watch(MONDIR, pyinotify.IN_MOVED_TO|pyinotify.IN_CLOSE_WRITE)


# Touch all existing files so they get picked up
old_files = os.listdir(MONDIR)
#print "Old files", old_files
for old_file in old_files:
    try:
        ofile = "%s/%s" % (MONDIR, old_file)
        of = open(ofile, "a")
        of.close()
    except Exception, e:
        log_event("Could not open", old_file)


# Run a loop waiting for exit.... 
do_loop()


print "Done"
log_event("Done", "None") 
