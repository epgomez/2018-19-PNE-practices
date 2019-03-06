import http.server
import socketserver

PORT = 8003

class TestHandler (http.server.BaseHTTPRequestHandler):

    #function called whenever we have a request
    def do_GET(self):
        print('GET received')

        print('Request line:' + self.requestline)
        print(' Cmd: '+ self.command)
        print(' Path: ' + self.path)

        content=''

        if self.path == '/':
            with open('index.html', 'r') as f:
                for line in f:
                    content += line

        else:
            with open('error.html', 'r') as f:
                for line in f:
                    content += line

        self.send_response(200)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Length-Type', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return

# function that's called whenever there's a request
Handler = TestHandler

# if you don't write any IP, you use yours
with socketserver.TCPServer(("",PORT), Handler) as httpd:
    print('Serving at PORT',PORT)

    httpd.serve_forever()