#!/usr/bin/python
# import a library  which allows us to use connect function
# on our selected host
import socket
# AF_INET => IPV4 Addresses / Sock_STREAM => TCP Packets
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "your_ip_or_host"
port = #port to be scanned

def portScanner(port):
#checks if connection method throws any errors
	if sock.connect_ex((host,port)):
		print "port %d is closed" % (port)
#if no error is thrown, the port is open
	else:
		print "Port%d is opened" % (port)
portScanner(port)
