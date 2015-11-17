#!/usr/bin/env python
# Module:   py_daemon.py
# Purpose:  create a python daemon, low-level, based on inotify
# Date:     N/A
# Notes:
#
# includes
import time as t
import datetime as dt
import os
import sys
import signal
import atexit


# define constants

# LOG file -- use full path as we change dir to / to make a daemon
LF="py_daemon.log"
LDIR=os.getcwd()
LOG="%s/%s" % (LDIR, LF)

# PID file
PID_FILE="%s/%s" % (LDIR, "pid.log")

#-------------------------------------------------------------------
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

#-------------------------------------------------------------------
# signal handler for TERM, etc.
def sig_handler(signum, frame):
    msg="Signal %d" % signum
    log_event(msg, "None")
    sys.exit(0)

#-------------------------------------------------------------------
# custom exception class, simply pass value 
class PDError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

#-------------------------------------------------------------------
# daemonize the process, based on __daemonize from inotify
def daemonize(pid_file=None, stdin=os.devnull, stdout=os.devnull,
              stderr=os.devnull):
    """
    @param pid_file: file where the pid will be written. If pid_file=None
    the pid is written to
    /var/run/<sys.argv[0]|pyinotify>.pid, if pid_file=False
    no pid_file is written.
    @param stdin:
    @param stdout:
    @param stderr: files associated to common streams.
    """
    if pid_file is None:
        dirname = '/var/run/'
        basename = os.path.basename(sys.argv[0]) or 'py_daemon'
        pid_file = os.path.join(dirname, basename + '.pid')

    if pid_file != False and os.path.lexists(pid_file):
        err = 'Cannot daemonize: pid file %s already exists.' % pid_file
        raise PDError(err)

    def fork_daemon():
        # Adapted from Chad J. Schroeder's recipe
        # @see http://code.activestate.com/recipes/278731/
        pid = os.fork()
        if (pid == 0):
            # parent 2
            os.setsid()
            pid = os.fork()
            if (pid == 0):
                # child
                os.chdir('/')
                os.umask(022)
            else:
                # parent 2
                # print "Parent 2 (", pid, ") exiting"
                os._exit(0)
        else:
            # parent 1
            # print "Parent 1 (", pid, ") exiting"
            os._exit(0)

        # print "Child changing i/o"
        try:
            fd_inp = os.open(stdin, os.O_RDONLY)
            os.dup2(fd_inp, 0)
            fd_out = os.open(stdout, os.O_WRONLY|os.O_CREAT, 0600)
            os.dup2(fd_out, 1)
            fd_err = os.open(stderr, os.O_WRONLY|os.O_CREAT, 0600)
            os.dup2(fd_err, 2)
        except Exception, e:
            err = "Error with duping I/O, e=%s" % str(e)
            raise PDError(err)
            #log_event("Error with daemonize", str(e))

    # end fork_daemon()

    # Detach task
    fork_daemon()
    log_event("we be forked", "None")

    # Write pid
    if pid_file != False:
        try:
            flags = os.O_WRONLY|os.O_CREAT|os.O_NOFOLLOW|os.O_EXCL
            fd_pid = os.open(pid_file, flags, 0600)
            os.write(fd_pid, str(os.getpid()) + '\n')
            os.close(fd_pid)
        except Exception, e:
            err = "Error creating pid_file, e=%s" % str(e)
            raise PDError(err)

        # Register unlink function
        atexit.register(lambda : os.unlink(pid_file))

#-------------------------------------------------------------------
# main function 

print "py_daemon:  run as a python daemon (with debug test)"
log_event("starting", "None")

# trap signals so we can kill the daemon
signal.signal(signal.SIGHUP, sig_handler)
signal.signal(signal.SIGTERM, sig_handler)
signal.signal(signal.SIGINT, sig_handler)

log_event("starting as daemon", "None")
try:
    # daemonize(pid_file=False)
    daemonize(pid_file=PID_FILE)
except Exception, e:
    log_event("Error with daemonize", str(e))
    print "exiting...."
    sys.exit(1)

log_event("running as daemon", "None")
for i in range(0,1000):
    t.sleep(1)
    # log_event("msg", "None")

log_event("done", "None")
print "Done"
