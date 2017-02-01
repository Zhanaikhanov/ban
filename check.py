#check student for studying in KBTU
from http import client
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
	print(cook)
	r = client.HTTPConnection('intranet2.kbtu.kz',80)
	r.putrequest('POST','/login.aspx',True,True)#POST
	r.putheader('Host', 'intranet2.kbtu.kz')#host
	r.putheader('User-Agent', 'Mozilla/5.0')#user-agent
	r.putheader('Cookie',cook)#cookie
	login = str(input('type login:'))
	password = str(input('type pass:'))
	post = 'uname={0}&pwd={1}'.format(login,password)
	r.putheader('Content-Length',str(len(post)))#c-len
	r.putheader('Content-Type','application/x-www-form-urlencoded')#c-type
	r.endheaders(post.encode('ascii'))
	print(post)
	r.send('')
	data = r.getresponse()
	data1 = str(data.headers)
	if 	"Set-Cookie:" in data1:
		print('valid')
	else:
		print('invalid')
else:
	print("bad request")
