# Christina Fong, 12/1/14
# Super-sketchy subprocess testing

import subprocess
import time
import matplotlib.pyplot as plt
import numpy as np 

def connect2device(MAC_address):
	"""Opens RFCOMM connection to designated bluetooth device"""
	p = subprocess.Popen(['sudo', 'rfcomm', 'connect', '0', '40:78:6A:E2:9D:53', '10', '>/dev/null/', '&'], stdin=subprocess.PIPE)
	p.wait()

def rssi_update(MAC_address):
	"""Queries and returns the RSSI value from designated device."""
	command = ["hcitool", "rssi", "40:78:6A:E2:9D:53"]
	p = subprocess.Popen(command, stdout=subprocess.PIPE)
	res = p.stdout.readline()
	rssi_val = int(res.split()[-1])
	return rssi_val

if __name__=='__main__':

	for i in range(1,7):
		print 'Pass #: ', i
		plt.clf()

		delay = 0.1
		phone_MAC = '40:78:6A:E2:9D:53'

		t = 0
		max_time = 20
		rssi_val =[]

		while t<=max_time:
			new_val = rssi_update(phone_MAC)
			rssi_val.append(new_val)
			t = t+delay
			# print new_val
			time.sleep(delay)

		timespan = np.linspace(0,max_time, len(rssi_val))

		mean_RSSI = np.mean(rssi_val)
		median_RSSI = np.median(rssi_val)

		plt.plot(timespan, rssi_val, marker='o')
		plt.plot((0, timespan[-1]), (mean_RSSI, mean_RSSI), linestyle='--')
		plt.plot((0, timespan[-1]), (median_RSSI, median_RSSI), linestyle='--')
		plt.ylim([min(rssi_val)-0.5, max(rssi_val)+0.5])
		plt.title('Phone 244" to side of laptop')
		plt.xlabel('Time (m)')
		plt.ylabel('RSSI')
		plt.legend(['RSSI data', 'Mean RSSI = {}'.format(mean_RSSI), 'Median RSSI = {}'.format(median_RSSI)], loc='best')
		# plt.show()
		plt.savefig('244in_away_test_hall_{}'.format(i))



	# plt.axis([0,100,-20,5])
	# plt.ion()
	# plt.show()
	
	# while x<=10:	
	# 	rssi_val = rssi_update(phone_MAC)
	# 	print rssi_val, 'at', x
	# 	plt.scatter(x,rssi_val)
	# 	plt.draw()
	# 	x = x+delay
	# 	time.sleep(delay)


