# -*- coding: utf-8 -*-

import socket

sock = socket.socket()
sock.bind(('', 8080))
sock.listen(1)
conn, addr = sock.accept()

print ('connected:'+str(addr))

try:

	while True:
		data = conn.recv(1024)
		if not data:
			break
		conn.send(data.upper())

except Exception:
	print ("Error:" + str(Exception))
	
print("Connect closed")
conn.close()