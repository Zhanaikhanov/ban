import http.client
h1 = http.client.HTTPConnection("intranet2.kbtu.kz")
h1.request("GET",'/home.aspx',b'',{'Cookie':"uname=AQAAANCMnd8BFdERjHoAwE%2fCl%2bsBAAAAAxycEyAyYk6BDZMTtukf3QQAAAACAAAAAAADZgAAqAAAABAAAAB%2bszCsjJagpzc5j8RUwLjsAAAAAASAAACgAAAAEAAAANcTohcrOmlTUQM1TUuwT18gAAAAyfEYsqbfP8Dxi3lD5aqiMVB6aVnR6it95eVSCK%2bqHiEUAAAAZezut2Z6U7in3PGBpF3dVRXyXWw%3d"})
data1 = h1.getresponse()

#data 1
#GET /home.aspx HTTP/1.1
#Host: intranet2.kbtu.kz
#Accept-Encoding: identity
#Content-Length: 0
#Cookie: uname=AQAAANCMnd8BFdERjHoAwE%2fCl%2bsBAAAAAxycEyAyYk6BDZMTtukf3QQAAAACAAAAAAADZgAAqAAAABAAAAB%2bszCsjJagpzc5j8RUwLjsAAAAAASAAACgAAAAEAAAANcTohcrOmlTUQM1TUuwT18gAAAAyfEYsqbfP8Dxi3lD5aqiMVB6aVnR6it95eVSCK%2bqHiEUAAAAZezut2Z6U7in3PGBpF3dVRXyXWw%3d



#h1.request("GET",'/OR3/OR.Schedule/Students/Schedule.aspx',b'',{'Cookie':"uname=AQAAANCMnd8BFdERjHoAwE%2fCl%2bsBAAAAAxycEyAyYk6BDZMTtukf3QQAAAACAAAAAAADZgAAqAAAABAAAAB%2bszCsjJagpzc5j8RUwLjsAAAAAASAAACgAAAAEAAAANcTohcrOmlTUQM1TUuwT18gAAAAyfEYsqbfP8Dxi3lD5aqiMVB6aVnR6it95eVSCK%2bqHiEUAAAAZezut2Z6U7in3PGBpF3dVRXyXWw%3d;ORAuth=FA0074839FB4BEB222FA969CE3461EE2145057BD3195A46F92EA7AB8FA901384B26192F5A82A4FACD44F9A5CEB134D91CF30B3C6D836F3F6DBA359F04FE74CA721CBA30A9DA28DB99C85EF83211323BFEF7475406129B391DC0014805A0DA5D13827F428C561637701975508934EB4517A9E618A"})
#data2 = h1.getresponse()

#data 2
#GET /OR3/OR.Schedule/Students/Schedule.aspx HTTP/1.1
#Host: intranet2.kbtu.kz
#Accept-Encoding: identity
#Content-Length: 0
#Cookie: uname=AQAAANCMnd8BFdERjHoAwE%2fCl%2bsBAAAAAxycEyAyYk6BDZMTtukf3QQAAAACAAAAAAADZgAAqAAAABAAAAB%2bszCsjJagpzc5j8RUwLjsAAAAAASAAACgAAAAEAAAANcTohcrOmlTUQM1TUuwT18gAAAAyfEYsqbfP8Dxi3lD5aqiMVB6aVnR6it95eVSCK%2bqHiEUAAAAZezut2Z6U7in3PGBpF3dVRXyXWw%3d;ORAuth=FA0074839FB4BEB222FA969CE3461EE2145057BD3195A46F92EA7AB8FA901384B26192F5A82A4FACD44F9A5CEB134D91CF30B3C6D836F3F6DBA359F04FE74CA721CBA30A9DA28DB99C85EF83211323BFEF7475406129B391DC0014805A0DA5D13827F428C561637701975508934EB4517A9E618A

#import requests