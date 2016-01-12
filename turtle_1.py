#!/usr/bin/env python
# Module:   turtle_1.py
# Purpose:  very simple example of turtle graphics
# Date:     N/A
# Notes:
# 1) Turtle graphics are a simple way of introducing programming,
#    especially to kids.  This has been around for MANY years (since 60's).
# 2) References:
#      https://docs.python.org/2/library/turtle.html
#      http://openbookproject.net/thinkcs/python/english3e/hello_little_turtles.html
#
# Import the turtle module
import turtle

# Create window and default turtle
wn = turtle.Screen()
t = turtle.Turtle()

# hide and move to (-200,0) 
wn.colormode(255)
t.penup()
# 
x0=-200
dx=100
mx=200
t.goto(x0,0)

# set color to red
t.pendown()
t.pencolor(255,0,0)
# 
# create some circles
for x in range(x0, mx+1, dx):
    t.goto(x,0)
    t.circle(20)

# home the cursor 
t.home()

#  wn.mainloop()


    
