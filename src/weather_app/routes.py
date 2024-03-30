from weather_app import app
from flask import render_template
from requests import request
from pprint import pprint
from os import getcwd


login = True # Login flag for debugging, True or False


@app.route("/home")
def home():
	"""Handles request for the Homepage of the application. Trigered by
	the `/home` via the localhost, i.e: `localhost:port/home`.

	Returns:

	`render_template()` - Renders the HTML template through Jinja, with
	additional parameters.
	"""
	method = "GET"
	url = "http://dataservice.accuweather.com/locations/v1/adminareas/PK?apikey=7wyLbCopjj0TMByxVc0jpGEOs9T2H6NZ&language=en-us&offset=100"
	response = request(method, url)
	response_in_json = response.json()
	pprint(response_in_json)
	
	pwd = getcwd()
	with open(f"{pwd}\\src\\weather_app\\recieveddata.txt", "r") as data_file:
		areas = data_file.readline()
		areas = list(areas)
		for area in areas:
			pprint(area)

	with open("recieved_data.txt", "a") as data_file:
		for area in response_in_json:
			data_file.writelines(area)

	return render_template("index.html", title="Homepage", login=login)


@app.route("/settings")
def settings():
	"""Handles request for the Settings page of the application. Trigered by
	the `/home` via the localhost, i.e: `localhost:port/settings`.

	Returns:

	`render_template()` - Renders the HTML template through Jinja, with
	additional parameters.
	"""
	return render_template("index.html", title="Settings", login=login)