import os
import json
import requests
import urllib.request
from appscript import app, mactypes

URL = "https://api.nasa.gov/planetary/apod?api_key=<api_key>"
if URL.lower().startswith('http'):
	pass
else:
	raise ValueError from None

try:
	image_data = json.loads(requests.get(URL).text)
	image_url = image_data['url']
	image_hd_url = image_data['hdurl']
	image_name = image_data['title'].split()[0] + '.jpg'
	file_path = os.environ['HOME'] + '/Pictures/' + image_name
	if(os.path.exists(file_path)) is False:
		try:
			urllib.request.urlretrieve(image_hd_url, filename=file_path)
			image_desc = image_hd_url
		except urllib.error.HTTPError:
			urllib.request.urlretrieve(image_url, filename=file_path)
			image_desc = image_url
		app('Finder').desktop_picture.set(mactypes.File(file_path))
	else:
		print('image already present,setting up existing image as desktop wallpaper')
		app('Finder').desktop_picture.set(mactypes.File(file_path))
except Exception as inst:
	print('Exception occured: ',inst)
