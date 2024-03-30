from weather_app import app

def main():
	debug = True # Debug Flag, True or False

	if debug == True:
		app.run(
			debug=True,
			host="0.0.0.0",
			port=5000
		)
	elif debug == False:
		app.run()

if __name__ == "__main__":
	main()