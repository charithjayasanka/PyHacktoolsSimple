#!/usr/bin/python

import socket

def retBanner(ip,port):
	try:
	#	socket.defaulttimeout(2)
		s = socket.socket()
		s.connect((ip,port))
		banner = s.recv(1024)
		return banner
	except:
		return "dfdfdf"

def main():
	port = 22 # port to be used
	ip = "192.168.136.129" #use the ip of your need to scan host
	banner = retBanner(ip,port)
	if banner:
		print "[+]" + ip + ": " + banner
main()
