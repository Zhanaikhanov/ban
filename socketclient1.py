#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket

sock = socket.socket()
sock.connect(('localhost', 80))

while True:
	name = input("You	:")
	sock.send(name.encode('ascii'))
	data = sock.recv(1024)
	print("He	:"+data.decode('ascii'))

sock.close()