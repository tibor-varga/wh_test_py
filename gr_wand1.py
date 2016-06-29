#!/usr/bin/env python
# Module:   gr_wand1.py
# Purpose:  Graphics:  wand example 1
# Date:     N/A
# Notes:
# 1) Wand is a C-types ImageMagick binding for Python:
# Ref:  http://docs.wand-py.org/en/0.4.3/
# 2) This is based on examples and some scripts I made.
#
"""Graphics:  wand example 1"""

import os
import subprocess
from wand.image import Image
from wand.display import display
from wand.drawing import Drawing
from wand.color import Color
import time as t

print "gr_wand1.py:  Graphics example 1 using Wand for ImageMagick"

IFILE = "latest_Small.gif"
print "Getting a sample file into ", IFILE
if not os.path.isfile(IFILE):
    subprocess.call('./web_read_get.py', shell=True)

def wand1():
    """This is Python Wand example 1"""
    the_time = t.asctime()

    print "Importing image ", IFILE
    img_1 = Image(filename=IFILE)

    print "Cropping and resizing the image"
    img_1.crop(300, 0, width=300, height=282)
    img_1.resize(width=600, height=564)

    print "Creating a drawing and overlaying on it"
    draw = Drawing()

    draw.circle((100, 100), (120, 120))

    draw.rectangle(left=img_1.width-300, top=img_1.height-45, width=230,
               height=40, radius=5)

    draw.font_size = 17
    draw.fill_color = Color('white')
    draw.text_color = Color('white')
    draw.text(img_1.width-290, img_1.height-20, the_time)
    draw(img_1)

    print "Displaying, close the XTERM when done"
    display(img_1)

if __name__ == "__main__":
    wand1()
