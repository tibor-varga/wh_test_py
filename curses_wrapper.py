#!/usr/bin/env python
# Module:   curses_wrapper.py
# Purpose:  test curses interface with wrapper for exceptions
# Date:     N/A
# Notes:
# 1) https://docs.python.org/2/library/curses.html
#    https://docs.python.org/2/howto/curses.html
#
# 2) Note curses coordinates are (y,x), top left is (0,0)
#
import curses 
from curses import wrapper
import time as t

# define a wrapped function so if we get an exception,
# things are cleaned up and we don't have a messed up screen
def curses_app(stdscr):

    # Clear screen
    stdscr.clear()
    stdscr.addstr("curses_wrapper.py:  curses test w/ wrapper and exception")
    stdscr.refresh()
    t.sleep(2)

    # This raises ZeroDivisionError when i == 10.
    for i in range(0, 11):
        v = i-10
        stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

    stdscr.refresh()
    stdscr.getkey()

# wrap curses so it cleans up on excptions....
wrapper(curses_app)
