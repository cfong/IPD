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

if __name__ == '__main__':

	arduino = serial.Serial('/dev/ttyACM0', 9600)
	print('Initializing')
	time.sleep(2)
	blink(4)

	arduino.close()

