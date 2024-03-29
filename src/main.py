from weather_app import app

def main():
	debug = True # Debug Flag, True or False

	if debug == True:
		app.run(
			debug=True
		)
	elif debug == False:
		app.run()

if __name__ == "__main__":
	main()