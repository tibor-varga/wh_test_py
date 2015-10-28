#!/usr/bin/env python
# Module:   gtk_hello.py
# Purpose:  Simple Hello World in Python GTK with button and lots of docs
# Date:     N/A
# Notes:
# 1) This is largely based on the Pygtk tutorial:
#       http://www.pygtk.org/pygtk2tutorial/ch-GettingStarted.html#sec-HelloWorld
# 2) GTK+ uses "signals", much like QT's signals/slots.  These are events/message
#    unlike the UNIX "signal()" interface and should not be confused with such.
#    Signals are "connected" to callback functions.
#
import pygtk
pygtk.require('2.0')
import gtk

class HelloWorld:
    # callback for the "hello" button
    def hello(self, widget, data=None):
        print "Hello, this is a test"

    # callback for X events, these receive 4 values
    # "hello" button press, release, and focus_in
    def hello_press(self, widget, event, data=None):
        print "Hello pressed"
        # don't return True, let other processing handle the button
        # return True  # no further processing
    def hello_release(self, widget, event, data=None):
        print "Hello released"
        # don't return True, let other processing handle the button
        # return True  # no further processing
    def hello_focus_in(self, widget, event, data=None):
        print "Hello focus_in"
        return True  # no further processing

    # callback for the "world" button - see notes below
    def world(self, widget, data=None):
        print "World is square!"

    # If you return FALSE in the "delete_event" signal handler,
    # GTK will emit the "destroy" signal. Returning TRUE means
    # you don't want the window to be destroyed.
    # This is useful for popping up 'are you sure you want to quit?'
    # type dialogs.  If changed to True, window will not be destroyed.
    def delete_event(self, widget, event, data=None):
        print "delete event"
        return False

    # Destroy handler, tell GTK+ to cleanup and quit
    def destroy(self, widget, data=None):
        gtk.main_quit()

    # constructor, create the window, buttons, etc.
    def __init__(self):
        # define the GTK window and connect delete/destroy events
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.connect("delete_event", self.delete_event)
        self.window.connect("destroy", self.destroy)

        # define window attributes
        self.window.set_border_width(5)

        # define buttons and callback for "clicked" action
        self.hello_button = gtk.Button("Hello")
        # connect button's click event to handler, return handler ID
        self.hello_button.connect("clicked", self.hello, None)
        self.hello_button.connect_object("clicked", gtk.Widget.destroy, self.window)
        self.hello_button.connect("button_press_event", self.hello_press, None)
        self.hello_button.connect("button_release_event", self.hello_release, None)
        self.hello_button.connect("focus_in_event", self.hello_focus_in, None)
        self.hello_button.connect("clicked", self.hello, None)

        # -- won't work as window can only contain 1 button obj.
        # self.world_button = gtk.Button("World")
        # self.world_button.connect("clicked", self.world, None)
        # self.world_button.connect_object("clicked", gtk.Widget.destroy, self.window)
        
        self.window.add(self.hello_button)
        # self.window.add(self.world_button)
        
        self.hello_button.show()
        # self.world_button.show()

        self.window.show()

    def main(self):
        # From docs:  GTK+ is an event driven toolkit, it will sleep in 
        # gtk.main() until an event occurs and control is passed to the 
        # appropriate function.
        gtk.main()

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
    hello = HelloWorld()
    hello.main()
