import http.server
import socketserver

PORT = 80
class Handler(http.server.BaseHTTPRequestHandler):
	def do_HEAD(self):
		self.send_response(200)
		self.send_header("Content-type","text/html")
		self.end_headers()
		for i in self.headers:
			print(i+" : "+self.headers[i])


	def do_GET(self):
		self.send_response(200)
		self.send_header(b"Content-type","text/html")
		self.end_headers()
		self.wfile.write(b'<html><head><title>BEKA<title><head><html>')
		for i in self.headers:
			print(i+" : "+self.headers[i])

	def do_POST(self):
		self.send_response(200)
		self.send_header(b"Content-type","text/html")
		self.end_headers()
		self.wfile.write(b'<html><head><title>BEKA<title><head><html>')
		for i in self.headers:
			print(i+" : "+self.headers[i])
httpd = socketserver.TCPServer(('', PORT), Handler)

print("at port :",PORT)
httpd.serve_forever()