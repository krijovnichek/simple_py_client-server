# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('localhost', 8080))
sock.send('some data'.encode())

data = sock.recv(1024)
sock.close()

print (data)