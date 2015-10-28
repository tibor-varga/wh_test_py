#!/usr/bin/env python
# Module:   py_gtk_test1.py
# Purpose:  Python + GTK, simple dialog
# Date:     N/A
# Notes:
# 1) 
# Ref:  any references
#
import pygtk
pygtk.require('2.0')
import gtk

class HelloWorld:
    def hello(self, widget, data=None):
        print "Hello World"

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        self.window=gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("destroy", self.destroy)
        self.window.set_border_width(10)
        self.button = gtk.Button("Hello World")
        self.button.connect("clicked", self.hello, None)
        self.button.connect_object("clicked", gtk.Widget.destroy, self.window)
        self.window.add(self.button)
        self.button.show()
        self.window.show()

    def main(self):
        gtk.main()

if __name__ == "__main__":
    hello = HelloWorld()
    hello.main()

