#!/usr/bin/env python
# Module:   clean_with_cfg.py
# Purpose:  pylint clean module with config obj
# Date:     N/A
# Notes:
# 1) ...
# Ref:  any references
#
"""Clean module that passes pylint and includes a Cfg object"""

MY_CFG = None
#------------------------------------------------------------------
class Cfg(object):
    """configuration object"""
    # pylint: disable=too-few-public-methods
    # pylint: disable=too-many-instance-attributes
    verbose = True
    opt1 = True
    opt2 = False
    opt3 = False
    opt4 = False
    opt5 = False
    opt6 = False
    opt7 = False

#------------------------------------------------------------------
def some_func(my_cfg):
    """some_func docstring goes here"""
    print "some_func opt7=", my_cfg.opt7

#------------------------------------------------------------------
def mname_func(my_cfg):
    """mname_func docstring goes here"""
    print __doc__
    print "OPT1=", my_cfg.opt1

    # implement the main function here
    some_func(my_cfg)

#------------------------------------------------------------------
if __name__ == "__main__":
    MY_CFG = Cfg()
    mname_func(MY_CFG)
