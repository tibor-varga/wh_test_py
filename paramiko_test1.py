#!/usr/bin/env python
# Module:   paramiko_test1.py
# Purpose:  test paramiko for SSH connections w/ keyless SSH and exceptions
# Date:     N/A
# Notes:
# 1) Paramiko home:
#      http://www.paramiko.org/
# 2) Multiple SSH discussions about Python
#      http://stackoverflow.com/questions/3586106/perform-commands-over-ssh-with-python
# 3) Made DSA keys on Ubuntu, copied pub key to C7 and installed
#    in ~/.ssh/authorized_keys (not authorized_keys2).
#     
import getopt,sys
import time as t
import paramiko
import socket

# command is uptime
CMD="uptime"

# get the account/host info and password
ACCT_HOST="root@localhost"
PW="password"

verbose=0

def PrintHelp():
    print "paramiko_test1.py:  test Paramiko SSH Python functions"
    print "Options:  -h   -- help,  -v  -- enable verbose"
    print "          -a user@host"

optlist, args = getopt.getopt(sys.argv[1:], 'a:vh')
for o,a in optlist:
    if o == '-a':
        ACCT_HOST=a
    if o == '-v':
        verbose=1
    if o == '-h':
        PrintHelp()
        exit(1)

# at this point, we have all info we need
acct, host = ACCT_HOST.split('@', 2)
if (verbose == 1):
    print "Paramiko test:  verbose enabled"
    print "SSH to ", host, "acct=", acct
    print "Command=", CMD

try:
    ssh=paramiko.SSHClient()
    ssh.load_system_host_keys()
    # use the following missing_host_key for Ubuntu as Ubuntu uses
    # the newer ecdsa keys.  Note they can be disabled system-wide:
    #    /etc/ssh/sshd_config:
    #       # HostKey /etc/ssh/ssh_host_ecdsa_key
    #
    # see:  http://stackoverflow.com/questions/10670217/paramiko-unknown-server
    #
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=acct, timeout=5.0)

    for x in range(0, 1000):
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(CMD)
        
        print "Res: ", ssh_stdout.read()
        print "Err: ", ssh_stderr.read()
        t.sleep(1)

# trap IO error, e.g., errors in many places inside the
# sftp object and other objects.
except IOError as err:
    print "IOError", str(err)
    sys.exit(2)

# trap SSH errors including closed channel
except paramiko.SSHException as err:
    print "SSHException:  ", str(err)
    sys.exit(2)

# trap socket errors, for example on timeout or closure
except socket.error as err:
    print "socket.error", str(err)
    sys.exit(2)

except socket.timeout as err:
    print "socket.timeout", str(err)
    sys.exit(2)

ssh.close()
print "Done!"
