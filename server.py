import re
from http.server import BaseHTTPRequestHandler, HTTPServer
from os import curdir, sep
import json


# HTTPRequestHandler class
import model


class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):

    # GET
    def do_GET(self):
        if self.path == "/":
            self.path = "/page.html"

        try:
            # Check the file extension required and
            # set the right mime type

            sendReply = False
            if self.path.endswith(".html"):
                mimetype = 'text/html'
                sendReply = True
            if self.path.endswith(".jpg"):
                mimetype = 'image/jpg'
                sendReply = True
            if self.path.endswith(".gif"):
                mimetype = 'image/gif'
                sendReply = True
            if self.path.endswith(".js"):
                mimetype = 'application/javascript'
                sendReply = True
            if self.path.endswith(".css"):
                mimetype = 'text/css'
                sendReply = True

            if re.match("/\d+", self.path):
                num = int(self.path[1:])
                newTA = model.getTA(num)
                self.send_response(200)
                self.end_headers()
                jsonTA = bytes(json.dumps(newTA), "utf-8")
                self.wfile.write(jsonTA)
                sendReply=False

            if sendReply == True:
                # Open the static file requested and send it
                f = open(curdir + sep + self.path)
                self.send_response(200)
                self.send_header('Content-type', mimetype)
                self.end_headers()
                self.wfile.write(bytes(f.read(), "utf-8"))
                f.close()



            return



        except IOError:
            self.send_error(404, 'File Not Found: %s' % self.path)


def run():
    print('starting server...')

    # Server settings
    # Choose port 8080, for port 80, which is normally used for a http server, you need root access
    server_address = ('127.0.0.1', 8081)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
    httpd.serve_forever()


run()