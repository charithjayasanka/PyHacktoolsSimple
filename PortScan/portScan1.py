#!/usr/bin/python
# import a library  which allows us to use connect function
# on our selected host
import socket
# AF_INET => IPV4 Addresses / Sock_STREAM => TCP Packets
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = raw_input("[*] Enter the host to be scanned : ")
port = int(raw_input("[*] Enter the Port to be Scanned: "))

def portScanner(port):
#checks if connection method throws any errors
	if sock.connect_ex((host,port)):
		print "Port %d is closed" % (port)
#if no error is thrown, the port is open
	else:
		print "Port%d is opened" % (port)
portScanner(port)

#you can also check the open ports using 
# nmap <your_host_or_ip_to_check>
