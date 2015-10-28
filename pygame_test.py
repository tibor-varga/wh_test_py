#!/usr/bin/env python
# Module:   pygame_test.py
# Purpose:  test/demo animated fractal using pygame
# Date:     N/A
# Notes: 
# 1) This is an example from the on-line book:
#      How to Think Like a Computer Scientist: Learning with Python 3
#    Link:  
#      http://openbookproject.net/thinkcs/python/english3e/recursion.html
# 2) This uses PyGame:  https://www.pygame.org/docs/
# 3) Tested on Ubuntu 14 installed via:
#      apt-get install python-pygame
# 4) The only changes to the book example are several prints, 
#    comments, and this header.
#
print "pygame_test.py:  fractals with pygame"
print "From: How to Think Like a Computer Scientist: Learning with Python 3"
#
import pygame, math
pygame.init()           # prepare the pygame module for use

# Create a new surface and window (surface is 1024x1024 square).
surface_size = 1024
main_surface = pygame.display.set_mode((surface_size,surface_size))

# create Clock object to keep track of time
# https://www.pygame.org/docs/ref/time.html
my_clock = pygame.time.Clock()


# draw the tree and if order>0 make recursive calls to this fcn
def draw_tree(order, theta, sz, posn, heading, color=(0,0,0), depth=0):

   trunk_ratio = 0.29       # How big is the trunk relative to whole tree?
   trunk = sz * trunk_ratio # length of trunk
   delta_x = trunk * math.cos(heading)
   delta_y = trunk * math.sin(heading)
   (u, v) = posn
   newpos = (u + delta_x, v + delta_y)
   pygame.draw.line(main_surface, color, posn, newpos)

   if order > 0:   # Draw another layer of subtrees

      # These next six lines are a simple hack to make the two major halves
      # of the recursion different colors. Fiddle here to change colors
      # at other depths, or when depth is even, or odd, etc.
      if depth == 0:
          color1 = (255, 0, 0)
          color2 = (0, 0, 255)
      else:
          color1 = color
          color2 = color

      # make the recursive calls to draw the two subtrees
      newsz = sz*(1 - trunk_ratio)
      draw_tree(order-1, theta, newsz, newpos, heading-theta, color1, depth+1)
      draw_tree(order-1, theta, newsz, newpos, heading+theta, color2, depth+1)


# main program with loop
def gameloop():

    theta = 0
    while True:

        # Handle events from keyboard, mouse, etc.
        ev = pygame.event.poll()
        if ev.type == pygame.QUIT:
            break;

        # Updates - change the angle
        theta += 0.01

        # Draw everything
        main_surface.fill((255, 255, 0))

        # draw the top-level, make 9 recursive calls (order=9)
        draw_tree(9, theta, surface_size*0.9, 
                  (surface_size//2, surface_size-50), -math.pi/2)

        # update display, swap video pages/update contents of surface
        pygame.display.flip()

        # update the clock, delay frame to 120 frames/sec max
        my_clock.tick(120)


# main code -- call the game loop and when done cleanup pygame
gameloop()
pygame.quit()
