#!/usr/bin/env python
# Module:   bessel_test.py
# Purpose:  Numpy example
# Date:     ? (from references)
# Notes:
# 1) This uses pylab (scipy, numpy, matplotlib)
# 2) See: 
#     http://stackoverflow.com/questions/9622163/  
#        save-plot-to-image-file-instead-of-displaying-it-using-matplotlib-so-it-can-be
#
from pylab import *
from optparse import OptionParser
OFILE="plot_pie.png"

print "plot_pie:  generate a pie-chart, save to PNG"

# Make a square figure and axes
figure(1, figsize=(6,6))
ax = axes([0.1, 0.1, 0.8, 0.8])

labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
fracs = [15,30,45, 10]

explode=(0, 0.05, 0, 0)
pie(fracs, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True)
title('Raining Hogs and Dogs', bbox={'facecolor':'0.8', 'pad':5})

print "  saving to ", OFILE
print "  display using browser or \"display ", OFILE, "\""
#show()
#savefig(OFILE)
savefig(OFILE, bbox_inches='tight')
