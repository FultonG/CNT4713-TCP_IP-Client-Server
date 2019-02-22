#!/usr/bin/env python

import socket
import re

#run it on localhost:5005
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
#this will close after recieving data once
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    #using a regular expression to remove anything that isnt alphanumeric
    data = re.sub("[^a-zA-Z0-9]", '' ,data)
    conn.send(data)
conn.close()