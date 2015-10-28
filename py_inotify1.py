#!/usr/bin/env python
# Module:   py_inotify1.py
# Purpose:  use pyinotify to monitor a test dir
# Date:     N/A
# Notes:
# 1) https://github.com/seb-m/pyinotify/wiki
#

import pyinotify
import time as t

# define the monitor dir
MONDIR="./test"

print "py_inotify1.py:  pyinotify test -- basic dir watch of ", MONDIR
print "After this starts, create some test files in ", MONDIR

# Create WatchManager
wm = pyinotify.WatchManager()

# Associate this WatchManager with a Notifier (will be used to report and
# process events).
notifier = pyinotify.Notifier(wm)

# Add a new watch on /tmp for ALL_EVENTS.
#wm.add_watch(MONDIR, pyinotify.ALL_EVENTS)
print "Watching for IN_MOVED_TO and IN_CLOSE_WRITE events"
wm.add_watch(MONDIR, pyinotify.IN_MOVED_TO|pyinotify.IN_CLOSE_WRITE)

# Loop forever and handle events.
notifier.loop()
