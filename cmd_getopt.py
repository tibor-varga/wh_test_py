#!/usr/bin/env python
# Module:   cmd_getopt.py
# Purpose:  Python getopt test 
# Date:     N/A
# Notes:    
# 1)  Test python code to test using getopt
#     https://docs.python.org/2/library/getopt.html
# 2)  Note, there is optparse for Python 2.6, but it has been
#     deprecated with 2.7 in favor of argparse.  The new 
#     recommended Python method is now "argparse".  However,
#     CentOS 5 uses Python 2.4 and CentOS 6 uses Python 2.6
#     so no argparse.  For simple scripts, stay with getopt???
# 3)  Ref:  
#       http://www.tutorialspoint.com/python/python_command_line_arguments.htm
#       https://docs.python.org/2/library/argparse.html#module-argparse
#
import getopt, sys

test_args1 = '-i file.txt -o ofile.txt -h -v 0 XXX YYY'.split()
test_args2 = '-? XXX YYY ZZZ'.split()

# test 1, support:  -i x, -o x, -v x, -t -u -v -h
print "Testing test args string "
optlist, args = getopt.getopt(test_args1, 'i:o:tuv:h')
print "Optlist = ", optlist, " Args=", args

for o,a in optlist:
    if o == '-i':
        print "Input=", a
    if o == '-o':
        print "Output=", a
    if o == '-v':
        print "Verbose=", a

# parse command line args using try, etc.
print "Testing command line args"
try:
    optlist, args = getopt.getopt(sys.argv[1:], 'i:o:tuv:h')
except getopt.GetoptError as err:
    print str(err)
    sys.exit(2)

for o,a in optlist:
    if o == '-i':
        print "Input=", a
    if o == '-o':
        print "Output=", a
    if o == '-v':
        print "Verbose=", a

