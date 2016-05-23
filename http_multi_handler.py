#!/usr/bin/env python
# Module:   http_multi_handler.py
# Purpose:  handle HTTP GET, POST, PUT requests
# Date:     N/A
# Notes:
# 1) Ref: 
#      https://gist.github.com/codification/1393204
#      https://docs.python.org/2/library/basehttpserver.html
#      http://dummdida.tumblr.com/post/51492057725/simplehttpputserver-in-python
#      http://stackoverflow.com/questions/111945/is-there-any-way-to-do-http-put-in-python
#
# 2) Usage, specify port number, e.g., 1025:
#
#      ./http_put_handler.py 1025   
#
import sys
import signal
from threading import Thread
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

# subclass of BaseHTTPRequestHandler to handle HTTP PUT requests
class MULTIHandler(BaseHTTPRequestHandler):
    def do_PUT(self):
        print "----- SOMETHING WAS PUT!! ------"
        print self.headers
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length)
        self.send_response(200)
        print content
        # -- or do something with the content, e.g., if it was JSON

    def do_POST(self):
        print "----- SOMETHING WAS POSTED!! ------"
        print self.headers
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length)
        self.send_response(200)
        print content
        # -- or do something with the content, e.g., if it was JSON

    def do_GET(self):
        """Respond to a GET request."""
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write("<html><head><title>Title goes here.</title></head>")
        self.wfile.write("<body><p>This is a test.</p>")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        self.wfile.write("<p>You accessed path: %s</p>" % self.path)
        self.wfile.write("</body></html>")

# run the code in a thread
def run_on(port):
    print("Starting a server on port %i" % port)
    server_address = ('localhost', port)
    httpd = HTTPServer(server_address, MULTIHandler)
    httpd.serve_forever()

# module main -- first arg is the port we should listen on
if __name__ == "__main__":
    ports = [int(arg) for arg in sys.argv[1:]]
    for port_number in ports:
        server = Thread(target=run_on, args=[port_number])
        server.daemon = True # Do not make us wait for you to exit
        server.start()
    signal.pause() # Wait for interrupt signal, e.g. KeyboardInterrupt

