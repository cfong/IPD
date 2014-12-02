#!/usr/bin/env python

#rssitracker.py by Peter Lavelle (peter@solderintheveins.co.uk)
#This script can be used to track the proximity of a PAIRED bluetooth enabled device 
#using both a visual indicator, provided by an Arduino and 3 LED's, as well as
#via messages printed to the terminal screen.
#
#You can also use this program to anounce when you are very close to your PC via Twitter 
#if this option is enabled.


import pyrssi, time, serial, bluetooth, sys#, twitter


#******************************
#[CONFIGURATION OPTIONS]
#******************************


#Set the serial port device your Arduino is connected to here

ArduinoPort = '/dev/ttyUSB0'


#Setup the PAIRED Bluetooth device's MAC address you which to track below:

DEV_MAC	= '40:78:6A:E2:9D:53'

#Set this to true if you want your proximity to the PC 'twittered' and to False if you don't.
UseTwitter = False 


#Set your twitter account details here
TwitterUser = "    "
TwitterPass = "   "



#Set the message you want to 'Twitter' when you're close to the PC
TwitterThis = "I am at the PC now!"




#Proximity Value. Use these to set the trigger points for the different proximity messages:
# Anything 0 or above indicates very close proximity, while everything -1 and below indicates 
#the device is not in close proximity to the PC. Only Integer Values are valid here.
VeryClose	= 0
AwayFromPC = -4
VeryFarAway = -12


#*****************END OF CONFIGURATION OPTIONS************************************



def GetRSSI(DEV_MAC):
	distance = pyrssi.read_rssi(DEV_MAC)	#Retrieve RSSI value
	print distance
	return distance
	

	

def UpdateStatus(distance):
	
	
	#Check if device is Very Close to us.
	
	if distance >= VeryClose:
		
		# ser.write('A')			#Send  signal to Arduino.
		time.sleep(1)			#Wait 1 second
		print 'User is very close to their PC now\n'	#Print debug message
	
		
		#Check if user wants to use Twitter. If so, send the right anouncement.
		#We only want to send it once here so we're not bombarding Twitter with messages.
		
		#Send message to Twitter if that's what the user wants to do.
		if (UseTwitter == True):
			client = twitter.Api(username= TwitterUser, password= TwitterPass)
			update = client.PostUpdate(TwitterThis) 
			
			
	
	
	#Check if device is a small distance away from us.
	
	elif distance == AwayFromPC:
		
		# ser.write('B')			#Send signal to Arduino.
		time.sleep(1)			#Wait 1 second
		print 'User is away from their PC Now.\n' #Print debug message
		
		
	#Check if device is very far away from us.

	elif distance == VeryFarAway:
		# ser.write('C')	
		time.sleep(1)			#Wait 1 second
		print 'User is very far away from their PC now.\n' #Print debug message
	
	
	


#Main Code Block


try:		

	
	#Setup and open serial connection.
	# ser = serial.Serial(port= ArduinoPort,  baudrate=9600, timeout=2, bytesize=8,   xonxoff=0, rtscts = 0 )
	# ser.open( )

	# if (ser.isOpen( )):
	# 	print 'Establishing serial connection. Please wait 3 seconds....\n'
	# 	time.sleep(3)	#Give the Arduino 3 seconds to respond	
	# 	print 'Connected! Press CTRL-C to terminate program.\n'
	
	
	
	while True:
		distance = GetRSSI(DEV_MAC)		#Get RSSI value
		UpdateStatus(distance)			#Pass RSSI value to UpdateStatus( ). 
		time.sleep(0.25)
		
		

#Error handling routine for incorrect serial port value
	# print 'Unable to establish serial connection on %s. Exiting...\n' %(ArduinoPort)
	sys.exit(1)
	

except KeyboardInterrupt:
	
	print 'Exiting Cleanly... Please wait.\n'
	# ser.close( )	#Close serial port
	print 'Thank you for using this program: Goodbye.\n'
	sys.exit(0)	#Exit Normally
	
	
	
#Error handing routines for both invalid user and serial device I/0
except ValueError:
	print 'Invalid input recieved from terminal or serial port... Exiting...\n'
	sys.exit(1)	#Exit on error
	

except TypeError:
	print 'Invalid Configuration or input values supplied, cannot continue... Exiting...\n'
	# ser.close( )
	sys.exit(1)	#Exit on error


#Error Handling routine for all other invalid input
 				
except AttributeError:
	print ' Invalid input recieved! Cannot continue, Exiting...\n'
	# ser.close
	sys.exit(1)
