import os
import sys
sys.path.append("../libraries")
import libHttpFootballApi
import libLogger

logsDir = "../logs"
logFile = logsDir + f'/logs_{str(os.path.realpath(__file__)).split("/")[-1].replace(".py", ".txt")}'

try:
	footballClub = "Bayern Munich"
	result = libHttpFootballApi.doesFootballClubPlayToday(footballClub)
	message = f'Does {footballClub} play today? {result}.'
	libLogger.logToTxtFile(message, logFile)
except:
	print("Exception!")
finally:
	print("Finally!")
