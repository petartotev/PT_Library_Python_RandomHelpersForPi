import http.client

domainFootballApi = "v3.football.api-sports.io"
keyFootballApi = "..."
headers = {
	'x-apisports-key': keyFootballApi
	}

def getRequest(queryLine):
	connection = http.client.HTTPSConnection(domainFootballApi)
	if (queryLine[0] != "/"):
		queryLine = "/" + queryLine
	connection.request("GET", queryLine, headers = headers)
	response = connection.getresponse()
	data = response.read()
	dataDecoded = data.decode("utf-8")
	return dataDecoded

def doesFootballClubPlayToday(footballClub):
	queryLine = "/fixtures?live=all"
	dataDecoded = getRequest(queryLine)
	indexFootballClub = dataDecoded.find(footballClub)
	if (indexFootballClub >= 0):
		return True
	else:
		return False
