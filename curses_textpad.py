#!/usr/bin/env python
# Module:   curses_textpad.py
# Purpose:  test curses textpad based on Github posting
# Date:     N/A
# Notes:
# 1) https://docs.python.org/2/library/curses.html
#    https://docs.python.org/2/howto/curses.html
# 2) Textpad example:
#    https://gist.github.com/myano/1055442
#
import curses
import curses.textpad
import time as t

# get window object representing whole screen
stdscr=curses.initscr()

# initialize the color facility, must be called before color fcn
curses.start_color()

# echo off and cbreak mode so we map F keys and special keys
curses.noecho()
curses.cbreak()

# process keys, return curses.KEYNAME
stdscr.keypad(1)

# clear and add string w/ notes
stdscr.clear()
stdscr.addstr(0,0,"curses_textpad.py:  textpad example")
stdscr.addstr(1,0,"Type CTRL-G to exit")
stdscr.refresh()
# create a window and put a textpad in it
begin_x = 20
begin_y = 7
height = 5
width = 40

# put a box around the edit window, not sure why width must be +3
win1= curses.newwin(height+2, width+3, begin_y-1, begin_x-1)
curses.textpad.rectangle(win1, 0, 0, height+1, width+1)
win1.refresh()

# create the edit window and let user edit 
win = curses.newwin(height, width, begin_y, begin_x)
tb = curses.textpad.Textbox(win)
text = tb.edit()

# when done, display the text, note refresh and sleep
# -- without sleep, the endwin... remove the display
stdscr.addstr(3,0,"Text entered=%s" % text)
#stdscr.addstr(4,1,text.encode('utf_8'))
stdscr.refresh()
t.sleep(2)

# cleanup
curses.endwin()
curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()

