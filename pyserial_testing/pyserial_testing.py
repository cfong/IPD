# Christina Fong, 11/17/14
# IPD: testing with Arduino and pySerial

import serial
import time

def blink(duration):
	"""Blinks LED for specified duration"""
	
	arduino.write('H')
	print('LED on')
	time.sleep(duration)

	arduino.write('L')
	print('LED off')
	time.sleep(duration)

def vibrate(duration, intensity):
	"""Vibrates motor for specified duration"""

	arduino.write('M')

if __name__ == '__main__':

	arduino = serial.Serial('/dev/ttyACM0', 9600)
	print('Initializing')
	time.sleep(2)

	current_mode = 'Passive mode'

	while True:
		new_mode = arduino.readline()[:-2]
		if new_mode == 'Active mode':
			print 'Waiting for user input query'
			# temp2 = raw_input('Waiting for user input')
		elif new_mode == 'Passive mode':
			print 'Currently in passive mode'
			# fake_data = raw_input('Fake distance data (ft): ')


	arduino.close()

