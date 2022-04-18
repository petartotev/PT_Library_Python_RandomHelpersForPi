import datetime
import time
import requests
import http.client
import json
import urllib.request

api_domain = 'api.nasa.gov'
api_key = 'value'


def get_apod_data_from_nasa_api():
	url = f'/planetary/apod?api_key={api_key}'
	conn = http.client.HTTPSConnection(api_domain)
	conn.request("GET", url)
	response = conn.getresponse()
	data = response.read()
	data_decoded = data.decode("utf-8")
	return json.loads(data_decoded)


def get_image_url_from_apod_data(data, is_hd):
	# date = data["date"]
	# explanation = data["explanation"]
	# media_type = data["media_type"]
	# service_version = data["service_version"]
	# title = data["title"]
	hdurl = data["hdurl"]
	url = data["url"]

	if is_hd:
		print(datetime.datetime.now() + " HD URL: " + hdurl)
		return hdurl
	else:
		print(datetime.datetime.now() + " URL: " + url)
		return url


def get_format_from_url_image(url_image):
	if url_image and ('.' in url_image):
		format = url_image.split('.')[-1]
		print(datetime.datetime.now() + " Format image: " + format)
		return format


def save_image_from_url_on_drive(url_image, filename, format):
	path = "/dir/"
	file = filename + ".jpg" # or format
	urllib.request.urlretrieve(url_image, path + file)
	print(datetime.datetime.now() + " Success! Image saved as: " + path + file)
	return file


def main():
	try:
		data = get_apod_data_from_nasa_api()
		url_img = get_image_url_from_apod_data(data, False)
		format_img = get_format_from_url_image(url_img)
		file = save_image_from_url_on_drive(url_img, data["date"], format_img)
	except Exception as ex:
		print(datetime.datetime.now() + " ERROR: An error occurred while retrieving data from NASA api! " + str(ex))


main()
