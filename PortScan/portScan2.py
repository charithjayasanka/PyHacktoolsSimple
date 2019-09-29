#!/usr/bin/python
# import a library  which allows us to use connect function
# on our selected host
import socket
from termcolor import colored

# AF_INET => IPV4 Addresses / Sock_STREAM => TCP Packets
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#socket.setdefaulttimeout(2)

host = input("[*] Enter the host to be scanned : ")
portStart =int(input("[*] Enter the port starting range: "))
portEnd=int(input("[*] Enter the port ending range : "))

def portScanner(port):
#checks if connection method throws any errors
	if sock.connect_ex((host,port)):
		print (colored("[!!] Port %d is closed" % (port),'red'))
#if no error is thrown, the port is open
	else:
		print (colored("[+] Port %d is open" % (port), 'green'))

for port in range(portStart,portEnd):
	portScanner(port)
