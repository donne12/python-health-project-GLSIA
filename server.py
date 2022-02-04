import http.server
import socketserver

port = 80
address = ("", port)


server = http.server.HTTPServer

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/"]

httpd = server(address, handler)

'''
handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(address, handler)
'''

print(f"Server listening on port {port}...")
httpd.serve_forever()







