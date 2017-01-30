#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
IP_ADD = str(input('type your ip from <ipconfig>'))
sock = socket.socket()
sock.connect((IP_ADD, 9090))

while True:
	name = input("You	:")
	sock.send(name.encode('ascii'))
	data = sock.recv(1024)
	print("He	:"+data.decode('ascii'))

sock.close()
