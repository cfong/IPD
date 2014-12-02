# Christina Fong, 12/1/14
# Super-sketchy subprocess testing

import subprocess
import time
import matplotlib.pyplot as plt 

phone_MAC = '40:78:6A:E2:9D:53'

def connect2device(MAC_address):
	"""Opens RFCOMM connection to designated bluetooth device"""
	p = subprocess.Popen(['sudo', 'rfcomm', 'connect', '0', '40:78:6A:E2:9D:53', '10', '>/dev/null/', '&'], stdin=subprocess.PIPE)
	p.wait()

def rssi_update(MAC_address):
	"""Queries and returns the RSSI value from designated device."""
	command = ["hcitool", "rssi", "40:78:6A:E2:9D:53"]
	p = subprocess.Popen(command, stdout=subprocess.PIPE)
	res = p.stdout.readline()
	rssi_val = res.split()[-1]
	return rssi_val

if __name__=='__main__':
	
	while True:	
		rssi_val = rssi_update(phone_MAC)
		print rssi_val
		time.sleep(0.1)


