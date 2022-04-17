import datetime
import time
from PyP100 import PyP100
import sys
import requests
import geocoder
import http.client
import json

# Tapo
ip = "192.168.0.000"
username = ""
password = ""

p100 = PyP100.P100(ip, username, password)


def set_p100():
	p100.handshake()
	p100.login()
	time.sleep(5)
	p100.turnOff()
	print("P100 initialized! Device information:")
	print(str(p100.getDeviceInfo()).replace(",", "\n"))


# Weather API
domain_ip_api = 'https://api.ipify.org'
domain_weather_api = 'api.openweathermap.org'
key_weather_api = 'f32fd645c455b498e9fd278e8ca0625e'


sunset_hour = 19
sunset_minute = 30


def get_offset_from_utc_to_local():
	now = time.time()
	offset = datetime.datetime.fromtimestamp(now) - datetime.datetime.utcfromtimestamp(now)
	return offset.seconds / 3600


def get_current_weather_data():
	ip_public = requests.get(domain_ip_api).text
	print("ip_public: " + str(ip_public))
	geo = geocoder.ip(ip_public)
	lat = geo.latlng[0]
	lon = geo.latlng[1]
	print("lat, lon: " + str(lat) + ", " + str(lon))
	url_weather_api = f'/data/2.5/weather?lat={lat}&lon={lon}&appid={key_weather_api}'
	conn = http.client.HTTPSConnection(domain_weather_api)
	conn.request("GET", url_weather_api)
	response = conn.getresponse()
	data = response.read()
	data_decoded = data.decode("utf-8")
	print("data_decoded: " + "\n" + str(data_decoded))
	return json.loads(data_decoded)


def update_sunset_data_from_response(response):
	global sunset_hour
	global sunset_minute
	owa_sys_sunset = response["sys"]["sunset"]
	owa_sys_sunset_datetime = datetime.datetime.utcfromtimestamp(int(owa_sys_sunset))
	offset = int(get_offset_from_utc_to_local())
	sunset_hour = int(owa_sys_sunset_datetime.hour) + offset
	sunset_minute = int(owa_sys_sunset_datetime.minute)


def update_sunset_data():
	response = get_current_weather_data()
	update_sunset_data_from_response(response)
	print("Sunset was updated: " + str(sunset_hour) + ":" + str(sunset_minute))


def main():
	set_p100()
	update_sunset_data()
	while(True):
		try:
			date_now = datetime.datetime.now()
			print(str(date_now))
			if (int(date_now.hour) == sunset_hour and int(date_now.minute) == sunset_minute):
				print("Sunset! Turning lights on...")
				p100.turnOn()
				time.sleep(60)
			elif (int(date_now.hour) == 0 and int(date_now.minute) == 1):
				print("Midnight! Turning lights off...")
				p100.turnOff()
				update_sunset_data()
			time.sleep(45)
		except KeyboardInterrupt:
			p100.turnOff()
			print("Goodbye...")
			sys.exit()
		except Exception as e:
			print("Something went wrong! But life goes on...")
			print(str(e))


main()
