from weather_app import app
from flask import render_template, request as fl_req
from requests import request as r_req
from pprint import pprint


login = True # Login flag for debugging, True or False

# possible weather_stations:
# openweathermap (owm), accuweather (aw)
weather_station = 'owm'


@app.route("/")
@app.route("/home")
def home():
	"""Handles request for the Homepage of the application. Trigered by
	the `/home` via the localhost, i.e: `localhost:port/home`.

	Returns:

	`render_template()` - Renders the HTML template through Jinja, with
	additional parameters.
	"""
	# if weather_station == 'owm':
	# 	r_method = "GET"
	# 	url = f""
	# 	response = r_req(r_method, url)
	# 	response_in_dict = dict(response)

	# elif weather_station == 'aw':
	# 	r_method = "GET"
	# 	url = "http://dataservice.accuweather.com/locations/v1/adminareas/PK?apikey=7wyLbCopjj0TMByxVc0jpGEOs9T2H6NZ&language=en-us&offset=100"
	# 	response = r_req(r_method, url)
	# 	response_in_dict = dict(response)
	# 	pprint(response_in_dict)

	return render_template("index.html", title="Homepage", login=login, ws=weather_station)


@app.route("/settings", methods=["POST", "GET"])
def settings():
	"""Handles request for the Settings page of the application. Trigered by
	the `/settings` via the localhost, i.e: `localhost:port/settings`. Also 
	accepts data from the settings form, via an HTTP `POST` method.

	Returns:

	`render_template()` - Renders the HTML template through Jinja, with
	additional parameters.
	"""
	if fl_req.method == "POST":
		req = fl_req.form

		weath_stat = req("weather_station")
		print(f"{weath_stat = }")

		return render_template("settings.html", title="Settings", login=login, ws=weather_station)

	# if weather_station == 'owm':
	# 	...
	# elif weather_station == 'aw':
	# 	...
	return render_template("settings.html", title="Settings", login=login, ws=weather_station)