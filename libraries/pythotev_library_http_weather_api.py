import datetime
import time
import requests
import geocoder
import http.client
import json
import random
from rpi_lcd import LCD
import RPi.GPIO as GPIO

domainIpApi = 'https://api.ipify.org'
domainWeatherApi = 'api.openweathermap.org'
keyWeatherApi = '...'

helloPhrases = [ "Good morning!", "Morning, folk!", "Hey, there!", "WOW! You look amazing today!", "What a day!" ]
goodbyePhrases = [ "Have a great day!", "Take it easy!", "Yo later dude!", "Catch you later!", "See you later, aligator!" ]
weatherPhrases = [ "Let me tell you about", "Lets start the day with", "Here is some info on", "You gotta hear about", "How beautiful" ]

def getOffsetFromUtcToLocal():
	now = time.time()
	offset = datetime.datetime.fromtimestamp(now) - datetime.datetime.utcfromtimestamp(now)
	return offset.seconds / 3600

def getCardinalDirectionByDegree(degree):
	if ((degree >= 338) or (degree >= 0 and degree < 23)):
		return "North"
	elif (degree >= 23 and degree < 68):
		return "North-East"
	elif (degree >= 68 and degree < 113):
		return "East"
	elif (degree >= 113 and degree < 158):
		return "South-East"
	elif (degree >= 158 and degree < 203):
		return "South"
	elif (degree >= 203 and degree < 248):
		return "South-West"
	elif (degree >= 248 and degree < 293):
		return "West"
	elif (degree >= 293 and degree < 338):
		return "North-West"
	else:
		return "Default"

def getCurrentWeatherData():
	ipPublic = requests.get(domainIpApi).text
	geo = geocoder.ip(ipPublic)
	lat = geo.latlng[0]
	lon = geo.latlng[1]
	urlWeatherApi = f'/data/2.5/weather?lat={lat}&lon={lon}&appid={keyWeatherApi}'
	conn = http.client.HTTPSConnection(domainWeatherApi)
	conn.request("GET", urlWeatherApi)
	response = conn.getresponse()
	data = response.read()
	dataDecoded = data.decode("utf-8")
	return json.loads(dataDecoded)

def generateStringFromWeatherData(dataDic, myDate):
	owaWeatherMain = dataDic["weather"][0]["main"].capitalize()
	owaWeatherDescription = dataDic["weather"][0]["description"].capitalize()
	owaMainTemp = "%.1f" % (float(dataDic["main"]["temp"]) - 273.15)
	owaMainTempFeelsLike = "%.1f" % (float(dataDic["main"]["feels_like"]) - 273.15)
	owaMainHumidity = dataDic["main"]["humidity"]
	owaWindSpeed = "%.1f" % float(dataDic["wind"]["speed"])
	owaWindDeg = dataDic["wind"]["deg"]
	owaCloudsAll = dataDic["clouds"]["all"]
	owaSysSunrise = dataDic["sys"]["sunrise"]
	owaSysSunriseDatetime = datetime.datetime.utcfromtimestamp(int(owaSysSunrise))
	owaSysSunset = dataDic["sys"]["sunset"]
	owaSysSunsetDatetime = datetime.datetime.utcfromtimestamp(int(owaSysSunset))
	owaName = dataDic["name"]
	owaWindDir = getCardinalDirectionByDegree(int(owaWindDeg))

	offset = int(getOffsetFromUtcToLocal())

	return f'{helloPhrases[random.randint(0,4)]} Time is {myDate.hour}:{myDate.minute}... {weatherPhrases[random.randint(0,4)]} the weather in {owaName}... {owaWeatherMain}... {owaWeatherDescription}... Temperature is {owaMainTemp} degrees, but it feels like {owaMainTempFeelsLike} degrees... Humidity is {owaMainHumidity} percent... Clouds coverage is {owaCloudsAll} percent... Wind speed is {owaWindSpeed} meters per second, coming from {owaWindDir}... The Sun rises at {int(owaSysSunriseDatetime.hour) + offset}:{int(owaSysSunriseDatetime.minute)} and falls at {int(owaSysSunsetDatetime.hour) + offset}:{int(owaSysSunsetDatetime.minute)}... {goodbyePhrases[random.randint(0,4)]}'

def getCurrentWeatherText(myDate):
	try:
		dataDic = getCurrentWeatherData()
		return generateStringFromWeatherData(dataDic, myDate)
	except KeyboardInterrupt:
		return "Error"
