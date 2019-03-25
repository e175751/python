import http.server
import socketserver

with socketserver.TCPServer(('192.168.0.4', 8000),                           http.server.SimpleHTTPRequestHandler) as httpd:
    httpd.serve_forever()
