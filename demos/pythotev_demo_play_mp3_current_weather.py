import datetime
import sys
sys.path.append("../libraries")
import libHttpWeatherApi
import libTextToMp3

soundsDir = "/home/pi/Desktop/MyDocuments/MySounds"

try:
	dateNow = datetime.datetime.now()
	mp3FileName = str(dateNow).replace(" ", "T") + ".mp3"
	weatherText = libHttpWeatherApi.getCurrentWeatherText(dateNow)
	weatherMp3FilePath = libTextToMp3.readStringInMp3File(weatherText, soundsDir, mp3FileName)
	libTextToMp3.playMp3File(weatherMp3FilePath)
except KeyboardInterrupt:
	print("exception!")
finally:
	print("end")
