#!/usr/bin/env python
# Module:   gtk_hello1.py
# Purpose:  Enhanced Hello World in Python GTK with button and lots of docs
# Date:     N/A
# Notes:
# 1) This is largely based on the Pygtk tutorial:
#       http://www.pygtk.org/pygtk2tutorial/sec-UpgradedHelloWorld.html
# 2) This includes a box with two buttons.  It also includes data in
#    the callbacks.  A dictionary also contains the event data.
#
import pygtk
pygtk.require('2.0')
import gtk

class HelloWorld:
    # dictionary of connections
    conn = {}

    # callback for the "hello" button
    def hello(self, widget, data=None):
        print "Hello, this is a test %s" % data

    # callback for X events, these receive 4 values
    # "hello" button press, release, and focus_in
    def hello_press(self, widget, event, data=None):
        print "Hello pressed, data=%s" % data
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
        print "World is square! (%s)" % data

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
        self.conn['delete_event'] = \
            self.window.connect("delete_event", self.delete_event)
        self.conn['destroy'] = \
            self.window.connect("destroy", self.destroy)

        # define window attributes
        self.window.set_border_width(10)

        # define a box to pack widgets, this allows us to have 
        # multiple buttons.  Box is not visible but is a container.
        self.box1 = gtk.HBox(False, 0)
        self.window.add(self.box1)

        # define buttons and callback for "clicked" action
        self.hello_button = gtk.Button("Hello")

        # connect button's click event to handler, return handler ID
        self.conn['button_clicked'] = \
            self.hello_button.connect("clicked", self.hello, "HELLO!")
        # self.hello_button.connect_object("clicked", gtk.Widget.destroy, self.window)
        self.conn['button_press_event'] = \
            self.hello_button.connect("button_press_event", self.hello_press, "PUSH HARDER")
        self.conn['button_release_event'] = \
            self.hello_button.connect("button_release_event", self.hello_release, None)
        self.conn['button_focus_in_event'] = \
            self.hello_button.connect("focus_in_event", self.hello_focus_in, None)


        # second button
        self.world_button = gtk.Button("World")
        self.conn['world_clicked'] = \
            self.world_button.connect("clicked", self.world, "or is it?")
        self.world_button.connect_object("clicked", gtk.Widget.destroy, self.window)
        
        # -- no longer used as we use a box....
        # self.window.add(self.hello_button)
        # self.window.add(self.world_button)

        # pack the buttons into the box
        self.box1.pack_start(self.hello_button, True, True, 0)
        self.box1.pack_start(self.world_button, True, True, 0)

        self.hello_button.show()
        self.world_button.show()

        self.box1.show()
        self.window.show()

        # print the dictionary
        print "Connection dictionary:"
        for k, v in self.conn.iteritems():
            print "  %-25s %d" % (k, v)

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
