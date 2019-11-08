#!/bin/bash
# A program that scans for open hosts on a network and determines what operating system is running

sn=$1

for host in $(seq 1 255);
do
	# Catch for unreachable hosts
	ping -c 1 $sn.$host | grep "Unreachable" &>/dev/null
	if [ $? -eq 0 ]; then
		printf "%s\n" "$sn.$host is Offline"
	fi

	# Host found: Linux
	ping -c 1 $sn.$host | grep "ttl=64" &>/dev/null
	if [ $? -eq 0 ]; then
		printf "%s\n" "$sn.$host is Online: Linux System"
	fi

	# Host found: Windows
	ping -c 1 $sn.$host | grep "ttl=128" &>/dev/null
	if [ $? -eq 0 ]; then
		printf "%s\n" "$sn.$host is Online: Windows System"
	fi

	# Host found: iOS
	ping -c 1 $sn.$host | grep "ttl=255" &>/dev/null
	if [ $? -eq 0 ]; then
		printf "%s\n" "$sn.$host is Online: iOS System"
	fi
done