#!/usr/bin/env python
# Module:   module_test.py
# Purpose:  test the test_module
# Date:     N/A
# Notes:
# 1)  https://docs.python.org/3/tutorial/modules.html
# 2)  This creates test_module.pyc before importing the test module
#     so you must use cleanup.py to remove it....
#
x=6
y=7
print "import module and running ", x, y, "times"
from test_module import f1, f2

f1(x)
f2(y)
print "done"
