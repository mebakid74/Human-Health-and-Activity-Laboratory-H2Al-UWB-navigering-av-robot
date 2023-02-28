from http.server import HTTPServer, BaseHTTPRequestHandler

HOST = "130.240.114.19"
PORT = 9559

class GuiHTTP(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_header()

        self.wfile.write(bytes("<html><body><h1> GUI Handler </h1></body></html>", "utf-8"))

server = HTTPServer((HOST, PORT), GuiHTTP)
print("Server now running on...")

server.serve_forever()
server.server_close()
print("Server has stoped")