from gtts import gTTS
import os

def readStringInMp3File(string, directory, fileName):
	if (directory[-1] != "/"):
		directory = directory + "/"
	if (".mp3" not in fileName):
		fileName = fileName + ".mp3"
	filePath = f'{directory}{fileName}'
	defLang = 'en'
	myObj = gTTS(text = string, lang = defLang, slow = False)
	myObj.save(filePath)
	return filePath

def playMp3File(filePath):
	os.system(f'omxplayer -o alsa {filePath}')
