#!/usr/bin/env python
# Module:   http_put_handler.py
# Purpose:  handle HTTP put requests
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
# 3) Test using curl or another program to generate a PUT request
#
#      curl -T date.out http://localhost:1025/
#
# 4) PUT versus POST:  http://stackoverflow.com/questions/630453/put-vs-post-in-rest
#
#    According to the HTTP/1.1 Spec:
#    
#    The POST method is used to request that the origin server accept the entity 
#    enclosed in the request as a new subordinate of the resource identified by 
#    the Request-URI in the Request-Line...
#
#    -- In other words, POST is used to create.
#
#    The PUT method requests that the enclosed entity be stored under the supplied 
#    Request-URI. If the Request-URI refers to an already existing resource, the 
#    enclosed entity SHOULD be considered as a modified version of the one residing 
#    on the origin server. If the Request-URI does not point to an existing resource, 
#    and that URI is capable of being defined as a new resource by the requesting 
#    user agent, the origin server can create the resource with that URI."
#
#    --  That is, PUT is used to create or update.
#    --  The core BaseHTTPServer only handles do_HEAD and do_GET requests.
#
import sys
import signal
from threading import Thread
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler

# subclass of BaseHTTPRequestHandler to handle HTTP PUT requests
class PUTHandler(BaseHTTPRequestHandler):
    def do_PUT(self):
        print "----- SOMETHING WAS PUT!! ------"
        print self.headers
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length)
        self.send_response(200)
        print content
        # -- or do something with the content, e.g., if it was JSON

# run the code in a thread
def run_on(port):
    print("Starting a server on port %i" % port)
    server_address = ('localhost', port)
    httpd = HTTPServer(server_address, PUTHandler)
    httpd.serve_forever()

# module main -- first arg is the port we should listen on
if __name__ == "__main__":
    ports = [int(arg) for arg in sys.argv[1:]]
    for port_number in ports:
        server = Thread(target=run_on, args=[port_number])
        server.daemon = True # Do not make us wait for you to exit
        server.start()
    signal.pause() # Wait for interrupt signal, e.g. KeyboardInterrupt

