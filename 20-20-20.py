"""A simple Script that sends a reminder every 20 minutes to take a 20-second
break. Avoid Computer Vision Syndrome.
~BY: ankitvad@gmail.com
V:0.01
To Do: Add a Screen-Lockout for 20 seconds in Python."""

import subprocess
from time import sleep

def sendAlert():
	#alert = "Take A Break","Please take a Break for 20-Seconds.\nLook Around a Bit.."
	subprocess.Popen(['notify-send', "Take A Break","Please take a Break for 20-Seconds.\nLook Around a Bit.."])

while(1):
	sendAlert()
	#Alert After 20-minutes. 20*60 = 1200. Adding 10 for notification.
	sleep(1240)
