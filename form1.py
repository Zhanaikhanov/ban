#!/usr/bin/env python3
import cgi, html
import os
import http.cookies

form = cgi.FieldStorage()
form1 = html.escape(form.getfirst('like'))

cookie = http.cookies.SimpleCookie(os.environ.get("HTTP_COOKIE"))
cook = cookie.get('name')
print("Content-type: text/html")
print()

print("""<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Start page!</title>
</head>
<body>""")
if form1 == 'yes':
	print("<h1>Thanks</h1>")
else:
	print("<h1>Close it!</h1>")
print("Your cookie is: {}".format(cook))
print("""<p>This is my first start page!</p>
</body>
</html>""")
