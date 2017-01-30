#!/usr/bin/env python3

print("Content-type: text/html")
print()
  
form = cgi.FieldStorage()
text1 = form.getfirst("NAME")
text2 = form.getfirst("SURNAME")
            
print("""
<!DOCTYPE html>
<html>
<head>
</head>
<body>
    <form action="/cgi-bin/socketserver1.py" method="post">
        <input type="text" name="pass" value="beka">
        <input type="submit" name="submit" value="press!">        
    </form>
</body>
</html>
	""")