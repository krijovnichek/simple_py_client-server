# -*- coding: utf-8 -*-

import socket
import time

def tcping(host, port=80, timeout=2):
    s = socket.socket()
    s.settimeout(timeout)
    try:
        start = time.time()
        s.connect((host, port))
        s.close()
        end = time.time()
    except Exception as e:
        if e[0] == errno.ECONNREFUSED:
            end = time.time()
    ms = 1000*(end-start)
    print (str(ms) +" ms")

if __name__ == '__main__':
    times = 3 
    for i in range(times) : 
        tcping('46.17.43.79', 80)
