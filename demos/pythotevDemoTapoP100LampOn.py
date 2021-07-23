import datetime
from time import sleep
from PyP100 import PyP100

ip = "..."
username = "..."
password = "..."

p100 = PyP100.P100(ip, username, password)

p100.handshake()
p100.login()
sleep(5)
p100.turnOff()

print(str(p100.getDeviceInfo()).replace(",", "\n"))

while True:
	dateNow = datetime.datetime.now()
	if (dateNow.minute %5 == 0 and dateNow.second == 0):
		try:
			sleep(1)
			p100.turnOn()
			print(f'{str(dateNow)} | ON')
		except:
			print("Could not turn on P100.")
	elif (dateNow.minute %5 != 0 and dateNow.second == 0):
		try:
			sleep(1)
			p100.turnOff()
			print(f'{str(dateNow)} | OFF')
		except:
			print("Could not turn off P100.")
