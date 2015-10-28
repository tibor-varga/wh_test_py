#!/usr/bin/env python
# Module:   paramiko_test.py
# Purpose:  test paramiko for SSH connections 
# Date:     N/A
# Notes:
# 1) Paramiko home:
#      http://www.paramiko.org/
# 2) Multiple SSH discussions about Python
#      http://stackoverflow.com/questions/3586106/perform-commands-over-ssh-with-python
#     
# command is uptime
CMD="uptime"

# get the account/host info and password
ACCT_HOST="root@localhost"
PW="password"

verbose=0

def PrintHelp():
    print "paramiko_test.py:  test Paramiko SSH Python functions"
    print "Options:  -h   -- help,  -v  -- enable verbose"
    print "          -a user@host,  -p password"

import getopt, sys
optlist, args = getopt.getopt(sys.argv[1:], 'a:p:vh')
for o,a in optlist:
    if o == '-a':
        ACCT_HOST=a
    if o == '-p':
        PW=a
    if o == '-v':
        verbose=1
    if o == '-h':
        PrintHelp()
        exit(1)

acct, host = ACCT_HOST.split('@', 2)
if (verbose == 1):
    print "Paramiko test:  verbose enabled"
    print "SSH to ", host, "acct=", acct, "PW=", PW
    print "Command=", CMD

import paramiko
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
ssh.connect(host, username=acct, password=PW)
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(CMD)

print "Res: ", ssh_stdout.read()
print "Err: ", ssh_stderr.read()

# send a file
SF="myfile.dat"
fo=open(SF,"w")
import time as t
ts=t.time()
AT=t.asctime(t.localtime(ts))
print "Start=", AT
for x in range(0,100):
    fo.write("Time=%s\n" % AT)

fo.close()

# C w/ glib2
#   fname=g_strdup_printf("%010ld", ts);
# Perl
#   $fname=printf("%010ld", ts);
# Python
fname="%010ld" % ts
sftp=ssh.open_sftp()
sftp.put(SF, fname)
# or use sftp.get(...) or fh=sftp.file(...)
te=t.time()
ET=t.asctime(t.localtime(te))
dt=te-ts
print "Wrote ", fname, "from ", SF
print "End=", ET
print "DT=", dt

# close it and exit
ssh.close()
print "Done!"
