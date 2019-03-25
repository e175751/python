import socket
from contextlib import closing
import sys

s = socket.socket()
#b="hoge"

host = sys.argv[1]
port = 5000

#with closing(s):
s.connect((host, port))
s.send(b'hello')
while True:
    print (host, s.recv(4096))
