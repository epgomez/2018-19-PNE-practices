import http.server
import socketserver
import termcolor
import string

# Define the Server's port
PORT = 8000


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inheritates all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):

    # It's important to use the name do_GET, otherwise it won't work
    def do_GET(self):

        termcolor.cprint(self.requestline, 'green')

        if self.path == '/':
            f = open("form.html", 'r')
            content = f.read()

        elif self.path[:5] == '/echo':
            f = open('response.html', 'w')
            path = self.path
            msg = path.split('=')[1]
            info = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Response</title>
</head>
<body>
<h3>Echo of the message received</h3>
    <p></p>
    <p>"""+msg+"""</p>
    <p></p>
    <a href='/'>Main page</a>
</body>
</html>"""
            f.write(info)
            f.close()
            f = open('response.html', 'r')
            content = f.read()

        else:
            f = open('error.html', 'r')
            content = f.read()

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return


# - Server MAIN program

# Set the new handler
Handler = TestHandler

# Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT", PORT)

    # Main loop: Attend the client. Whenever there is a new
    # clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stoped by the user")
        httpd.server_close()

print("")
print("Server Stopped")