######################################
# PROGRAMMED BY: CENSORED            #
# DUE DATE: 12/12/19                 #
# CLASS: COMP-5970                   #
######################################

# imports
import socket
import struct

# global variables
URGFlag = 0
ACKFlag = 0
PSHFlag = 0 
RSTFlag = 0 
SYNFlag = 0 
FINFlag = 0
firstStealthAccess = True
firstACKAccess = True
firstXMASAccess = True 
server = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

# sets TCP flags
def setFlags(packet):
	global URGFlag
	URGFlag = packet & 0x020
	URGFlag >>= 5            # URGFlag is now a bool value (0 or 1)
	global ACKFlag
	ACKFlag = packet & 0x010
	ACKFlag >>= 4            # ACKFlag is now a bool value (0 or 1)
	global PSHFlag
	PSHFlag = packet & 0x008
	PSHFlag >>= 3            # PSHFlag is now a bool value (0 or 1)
	global RSTFlag
	RSTFlag = packet & 0x004
	RSTFlag >>= 2            # RSTFlag is now a bool value (0 or 1)
	global SYNFlag
	SYNFlag = packet & 0x002
	SYNFlag >>= 1            # SYNFlag is now a bool value (0 or 1)
	global FINFlag
	FINFlag = packet & 0x001
	FINFlag >>= 0            # FINFlag is now a bool value (0 or 1)

# prints TCP packet details
def printPacketDetails(packet):
	print "[#] The captured packet has the following details..."
	print "[#]     Source Port: ", packet[0]
	print "[#]     Destination Port: ", packet[1]
	print "[#]     Sequence Number: ", packet[2]
	print "[#]     ACK Number: ", packet[3]
	print "[#]     Data Offset: ", packet[4]
	print "[#]     TCP Header Length: ", packet[4] >> 4
	print "[#]     Flags:"
	print "[#]         URG Flag: ", URGFlag
	print "[#]         ACK Flag: ", ACKFlag
	print "[#]         PSH Flag: ", PSHFlag
	print "[#]         RST Flag: ", RSTFlag
	print "[#]         SYN Flag: ", SYNFlag
	print "[#]         FIN Flag: ", FINFlag
	print ""

# main function
def main():
	print "[#] The IDS is running! Now scanning for intrusive packets... (Press CTRL+C to quit at any time)"
	print ""
	while True: # infinite loop
		packet = server.recvfrom(65565) # server receives a packet
		packet = packet[0]
		IPHeader = packet[0:20]
		unpackedIP = struct.unpack('!BBHHHBBH4s4s' , IPHeader) # unpack the IP portion of the packet into a usable format
		version = unpackedIP[0]
		IPHeaderLength = (version & 0xF) * 4 # Marks the end of the IP Header Length segment (i.e., the start of the TCP segment)

		TCPHeader = packet[IPHeaderLength:IPHeaderLength+20]
		unpackedTCP = struct.unpack("!HHLLBBHHH", TCPHeader) # unpack the TCP portion of the packet into a usable format
		setFlags(unpackedTCP[5]) # Determines what flags are set in the TCP segment of the packet

		# Now we determine whether a scan has been attempted and what kind it was based on the flags that were set with setFlags
		if(not(URGFlag) and not(ACKFlag) and not(PSHFlag) and not(RSTFlag) and SYNFlag and not(FINFlag)):
			scan = "stealth"
		elif(not(URGFlag) and ACKFlag and not(PSHFlag) and not(RSTFlag) and not(SYNFlag) and not(FINFlag)):
			scan = "ACK"
		elif(URGFlag and not(ACKFlag) and PSHFlag and not(RSTFlag) and not(SYNFlag) and FINFlag):
			scan = "XMAS"
		else:
			scan = "none"

		# define the global variables to use in the upcoming if statements
		global firstStealthAccess
		global firstACKAccess
		global firstXMASAccess

		# print what type of scan has performed (only one time each to help prevent clutter)
		if(scan == "stealth" and (unpackedTCP[4] == 96) and firstStealthAccess): # DEFAULT NMAP SCAN (STEALTH SCAN)
			print "[!] An NMAP Stealth Scan has been performed on the network!"
			printPacketDetails(unpackedTCP) # print the captured packet details
			firstStealthAccess = False
		elif(scan == "ACK" and (unpackedTCP[2] == 0) and firstACKAccess): # NMAP ACK SCAN
			print "[!] An NMAP ACK Scan has been performed on the network!"
			printPacketDetails(unpackedTCP) # print the captured packet details
			firstACKAccess = False
		elif(scan == "XMAS" and (unpackedTCP[3] == 0) and firstXMASAccess): # NMAP XMAS SCAN
			print "[!] An NMAP XMAS Scan has been performed on the network!"
			printPacketDetails(unpackedTCP) # print the captured packet details
			firstXMASAccess = False

main()
