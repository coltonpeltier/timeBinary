import os
import time
import ntplib
from time import ctime

hour = 0
min = 0
sec = 0
c = ntplib.NTPClient()

while True:
	while hour < 24:
		response = c.request('pool.ntp.org')
		myTime = ctime(response.tx_time).split()
		myTimeDone = myTime[3].split(':')
		hour = int(myTimeDone[0])
		min = int(myTimeDone[1])
		sec = int(myTimeDone[2])
		date = myTime[0] + " " + myTime[1] + " " + myTime[2]
		while min < 60:
			while sec < 60:
				os.system('cls')
				print "Date: "
				print "-----"
				print date
				print " "
				print "Time:"
				print "-----"
				print "Hours" + '\t' + "Minutes" + '\t' + "Seconds"
				hourBin = bin(hour)
				minBin = bin(min)
				secBin = bin(sec)
				print hourBin[2:] + '\t' + minBin[2:] + '\t' + secBin[2:]
				sec = sec + 1
				time.sleep(1)
			sec = 0
			min = min + 1
		min = 0
		hour = hour + 1
	hour = 0
	
