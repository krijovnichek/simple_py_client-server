# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.connect(('192.168.1.35', 8080))
sock.send('some data'.encode())

data = sock.recv(1024)
sock.close()

print (data)