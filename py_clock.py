#!/usr/bin/env python
# Module:   py_clock.py
# Purpose:  gtk-based clock
# Date:     N/A
# Notes:
# 1) This uses Python + GTK to display a window with a box
#    container in it.  The box contains a time label on the L
#    and a single quit button on the right.  The time (the label)
#    is updated every second from a GObject timeout (1000ms).
# 2) Tested on CentOS 7 and Ubuntu 18.04.
#    On Ubuntu:
#      apt-get install python-gobject python-dbus
#
"""Python gtk-based clock, similar to xclock"""

import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gi.repository import GObject
import time
import datetime

class MyClock(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="GTK Clock")
        
        self.start_time=time.time()
        
        hbox=Gtk.Box()
        hbox.set_homogeneous(False)
        
        self.label=Gtk.Label("clock goes here")
        hbox.pack_start(self.label, True, True, 0)
        
        self.button=Gtk.Button(label="Exit")
        self.button.connect("clicked", self.on_button_clicked)
        hbox.pack_start(self.button, True, True, 0)
        
        self.add(hbox)
        self.timer=GObject.timeout_add(1000, self.clk_timeout)
        
    def on_button_clicked(self, widget):
        print "Exiting"
        Gtk.main_quit()

    def clk_timeout(self):
        t=time.time()
        snow=datetime.datetime.fromtimestamp(t).strftime("%Y/%m/%d %H:%M:%S")
        tstr="%s\nTIME_T=%f\nELAPSED=%f" % (snow, t, t-self.start_time)
        self.label.set_text(tstr)
        return True

def PyClock():
    win=MyClock()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    PyClock()
