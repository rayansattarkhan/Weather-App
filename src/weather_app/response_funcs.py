from os import getcwd


def write_response_to_file(response: dict, weath_stat: str) -> None | bool:
	"""Writes the response from API to file.

	Parameters:

	`response` - Response from the API.
	`weath_stat` - The weather station used for API.

	Returns:

	`None` - Currently.
	`success` - Boolean flag to show status.
	"""
	#TODO: Implement the bool return logic.

	pwd = getcwd()
	with open(f"{pwd}\\src\\weather_app\\recieved_data\\{weath_stat}.txt", "r") as data_file:
		for area in response:
			data_file.writelines(area)