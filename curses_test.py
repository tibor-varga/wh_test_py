#!/usr/bin/env python
# Module:   curses_test.py
# Purpose:  test curses interface
# Date:     N/A
# Notes:
# 1) https://docs.python.org/2/library/curses.html
#    https://docs.python.org/2/howto/curses.html
#
import curses 
import time as t

#UL=curses.ACS_ULCORNER

# get window object representing whole screen
stdscr=curses.initscr()

# initialize the color facility, must be called before color fcn
# then setup the color pairs
curses.start_color()
curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)

# echo off and cbreak mode so we map F keys and special keys
curses.noecho()
curses.cbreak()

# process keys, return curses.KEYNAME
stdscr.keypad(1)

# clear screen and display a message
stdscr.clear()
stdscr.addstr("curses_test.py:  test curses")
stdscr.refresh()
t.sleep(1)

for y in range(1,4):
    stdscr.addstr(y, 0, "%03d test string" % y)
    stdscr.addstr(0, 40,"%03d" % y, curses.A_REVERSE)
    stdscr.refresh()
    t.sleep(1)

stdscr.addstr(13, 0, "R", curses.color_pair(1))
stdscr.addstr(13, 10, "G", curses.color_pair(2))
stdscr.addstr(13, 20, "B", curses.color_pair(3))
stdscr.refresh()

# create a text window and display data in it
y=15
x=10
win=curses.newwin(5, 25, 15, 10)
win.border()
win.addstr(1,1,"Test string", curses.color_pair(1))
win.addstr(3,1,"Press key to clear:", curses.color_pair(3))
win.refresh()
stdscr.getch()

# clear window, note it clears the border too!
win.clear()
win.addstr(3,1,"Press key:", curses.color_pair(3))
win.refresh()
stdscr.getch()

# done, prompt to exit, save user's char for display
stdscr.addstr(20,0, "Press any key to exit:  ")
stdscr.refresh()
c=stdscr.getch()



# cleanup
curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()

# normalize the char typed as it can be out of range
# for the chr() function, for example c=266; chr(c)
# where 266 is returned from pressing an F key....
cc=c
if c > 255:
    cc=0x20
print "You typed:  %c (%d)" % (cc, c)
print "Done!"

