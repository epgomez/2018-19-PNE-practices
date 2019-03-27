import http.server
import socketserver
import termcolor
from Seq import Seq

PORT = 8002

class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):

        global base_op, length
        termcolor.cprint(self.requestline, 'green')
        path = self.path

        if path == '/':
            f = open("index.html", 'r')
            content = f.read()
            resp=200

        elif (path[:4] == '/seq' and '=' in path):
            resp=200
            msg = path.split('&')
            seq = msg[0].split('=')[1]
            if seq.upper().strip('ACTG') == '':
                seq = Seq(seq)
                count = {'base=A': ('Count of A: ' + seq.count('A')),
                         'base=C': ('Count of C: ' + seq.count('C')),
                         'base=T': ('Count of T: ' + seq.count('T')),
                         'base=G': ('Count of G: ' + seq.count('G'))}
                perc = {'base=A': ('Percentage of A: ' + seq.perc('A') + '%'),
                        'base=C': ('Percentage of C: ' + seq.perc('C') + '%'),
                        'base=T': ('Percentage of T: ' + seq.perc('T') + '%'),
                        'base=G': ('Percentage of G: ' + seq.perc('G') + '%')}
                ops = {'count': count, 'perc': perc}
                if len(msg) == 3:
                    length = ''
                    op = msg[1].split('=')[1]
                    base = msg[2]
                    if base in ops[op].keys():
                        base_op = ops[op][base]

                elif len(msg) == 4:
                    length = 'The lenght is: ' + str(seq.len())
                    op = msg[2].split('=')[1]
                    base = msg[3]
                    if base in ops[op].keys():
                        base_op = ops[op][base]

                d = open('response.html', 'w')
                info = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sequence</title>
</head>
<body>
<h3>Analysis of the sequence</h3>
    <p></p>
    <p>Sequence: {}</p>
    <p></p>
    <p>{}</p>
    <p></p>
    <p>{}</p>
    <p></p>
    <a href='/'>Main page</a>
</body>
</html>""".format(seq.strbases.upper(), length, base_op)
                d.write(info)
                d.close()
                d = open('response.html', 'r')
                content = d.read()

            else:
                f = open('errorseq.html', 'r')
                content = f.read()

        else:
            resp=404
            f = open('error.html', 'r')
            content = f.read()

        self.send_response(resp)
        self.send_header('Content-Type', 'text/html')
        self.send_header('Content-Length', len(str.encode(content)))
        self.end_headers()

        self.wfile.write(str.encode(content))

        return

Handler = TestHandler

# Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Serving at PORT: ", PORT)

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
