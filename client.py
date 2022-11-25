from socket import *

s = socket(AF_INET,SOCK_DGRAM)
s.bind(('0.0.0.0',8812))
s.sendto(b'ok',('192.168.101.6',8889))
