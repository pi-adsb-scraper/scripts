import configparser
import sys

# All important changes can be done through the config file, this code doesn't need to be modified
CONFIG_FILEPATH = "config.ini"

API_BASEURL = ""
API_SECONDS_BETWEEN_REQUESTS = 0
API_AIRCRAFT_TYPES = ""
PATH_OUTPUT_FOLDER = ""

def readConfig():

	"""
	Load configuration from .ini file to global vars	
	Handles errors gracefully
	"""
	
	# Python makes new variables, even when global var exists with same name?
	# Anyway, tell Python we want to change the *global* vars, not create local ones
	global API_BASEURL, API_SECONDS_BETWEEN_REQUESTS, PATH_OUTPUT_FOLDER 
	
	config = configparser.ConfigParser()
	if not config.read(CONFIG_FILEPATH):
		print(f"Unable to open config file at {CONFIG_FILEPATH}")
		sys.exit(1)

	try:

		API_BASEURL = config.get("API", "baseurl")
		API_SECONDS_BETWEEN_REQUESTS = config.get("API", "s_between_reqs")
		PATH_OUTPUT_FOLDER = config.get("PATH", "scan_output_folder")
		
		tempString = config.get("API", "aircraft_types")	
		API_AIRCRAFT_TYPES = [item.strip() for item in tempString.split(',') if item.strip()]
	

	except configparser.NoSectionError as e:
		print(f"Missing section in config file: {e}")
		sys.exit(1)

	except configparser.NoOptionError as e:
		print(f"Missing key in config file: {e}")
		sys.exit(1)

	print(f"Read values from config. API_BASEURL: {API_BASEURL}, API_SECONDS_BETWEEN_REQUESTS: {API_SECONDS_BETWEEN_REQUESTS}, API_AIRCRAFT_TYPES: {API_AIRCRAFT_TYPES} PATH_OUTPUT_FOLDER: {PATH_OUTPUT_FOLDER}")



# Am I going to put this in a package? Most likely not.
# Am I going to question Python standards? Also no.
if __name__ == "__main__":
	
	readConfig()