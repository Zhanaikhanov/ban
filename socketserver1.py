#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
IP_ADD = str(input('type your ip: '))
sock = socket.socket()
sock.bind((IP_ADD,9090))
sock.listen(1)
conn, addr = sock.accept()

while True:
	data = conn.recv(1024)
	print('He	:'+data.decode('ascii'))
	if not data:
		break
	sent = input("You	:")
	conn.send(sent.encode('ascii'))
