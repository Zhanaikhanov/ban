#!/usr/bin/env python3
import cgi

form1 = cgi.FieldStorage.getfirst('NAME')
form2 = cgi.FieldStorage.getfirst('SURNAME')

print("""<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Start page!</title>
</head>
<body>
	<h1>Hello ! {0}, {1}</h1> 
	<p>This is my first start page!</p>
	<form action='/cgi-bin/forma.py'>
		<input type='radio' name='like' value='yes'>Do you like it?<br/><input type='radio' name='dislike' value='yes'>
		<input type='submit'>
	</form>
</body>
</html>""".format(str(form1), str(form2))