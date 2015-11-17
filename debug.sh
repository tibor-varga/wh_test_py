#!/bin/bash
# Module:   debug.sh
# Purpose:  python and gdb debug of Python scripts
# Author:   Wade Hampton
# Date:     N/A
# Notes:
# 1) See:  https://wiki.python.org/moin/DebuggingWithGdb
#          https://fedoraproject.org/wiki/Features/EasierPythonDebugging
#          https://stripe.com/blog/exploring-python-using-gdb
# 2) GDB use with Python is fairly new and is rather difficult....
#
SCRIPT=py_loop.py
echo "Starting $SCRIPT in python debugger, type \"exit\" to exit"
python -m pdb $SCRIPT

echo "Starting $SCRIPT in gdb debugger, CTRL-D to exit"
gdb -ex r --args python $SCRIPT



