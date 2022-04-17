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

sunrise_hour = 8
sunrise_minute = 0
sunset_hour = 20
sunset_minute = 0


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


def update_sunrise_and_sunset_data_from_response(response):
	global sunrise_hour
	global sunrise_minute
	global sunset_hour
	global sunset_minute

	offset = int(get_offset_from_utc_to_local())

	owa_sys_sunrise = response["sys"]["sunrise"]
	owa_sys_sunrise_datetime = datetime.datetime.utcfromtimestamp(int(owa_sys_sunrise))
	sunrise_hour = int(owa_sys_sunrise_datetime.hour) + offset
	sunrise_minute = int(owa_sys_sunrise_datetime.minute)

	owa_sys_sunset = response["sys"]["sunset"]
	owa_sys_sunset_datetime = datetime.datetime.utcfromtimestamp(int(owa_sys_sunset))
	sunset_hour = int(owa_sys_sunset_datetime.hour) + offset
	sunset_minute = int(owa_sys_sunset_datetime.minute)


def update_sun_data():
	response = get_current_weather_data()
	update_sunrise_and_sunset_data_from_response(response)
	print("Sunrise was updated: " + str(sunrise_hour) + ":" + str(sunrise_minute))
	print("Sunset was updated: " + str(sunset_hour) + ":" + str(sunset_minute))

def it_is_sunrise(date_now):
	return (int(date_now.hour) == sunrise_hour and int(date_now.minute) == sunrise_minute)

def it_is_sunset(date_now):
	return (int(date_now.hour) == sunset_hour and int(date_now.minute) == sunset_minute)

def it_is_bright_part_of_day(date_now):
	return (int(date_now.hour) > sunrise_hour and int(date_now.hour) < sunset_hour) or (int(date_now.hour) == sunrise_hour and int(date_now.minute) >= sunrise_minute) or (int(date_now.hour) == sunset_hour and int(date_now.minute) <= sunset_minute)

def main():
	set_p100()
	update_sun_data()
	date_init = datetime.datetime.now()
	if not it_is_bright_part_of_day(date_init):
		print(str(date_init) + " Program was started during the dark part of the day. Turning light on!")
		p100.turnOn()
	while(True):
		try:
			date_now = datetime.datetime.now()
			print(str(date_now))
			if (it_is_sunrise(date_now)):
				print(str(date_now) + " It's Sunrise! Time to turn light off...")
				p100.turnOff()
				time.sleep(60)
			elif (it_is_sunset(date_now)):
				print(str(date_now) + " It's Sunset! Time to turn light on...")
				p100.turnOn()
				time.sleep(60)
			elif (int(date_now.hour) == 0 and int(date_now.minute) == 5):
				print(str(date_now) + " It's Midnight! Time to update Sun information from API...")
				update_sun_data()
				time.sleep(60)
			time.sleep(45)
		except KeyboardInterrupt:
			p100.turnOff()
			print("KeyboardInterrupt occurred! Goodbye...")
			sys.exit()
		except Exception as e:
			print("Something went wrong! But life goes on...")
			print(str(e))


main()
