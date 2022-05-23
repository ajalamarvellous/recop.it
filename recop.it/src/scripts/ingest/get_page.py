import os
import loging
import requests
import pyperclip
from pathlib import Path

logging.basicConfig(format = "%(asctime)s [%(levelname)] \
							  %(funcName): %(message)s",
					level =  logging.DEBUG)
logger = logging.getLogger()

def get_webpage():
	"""Function to download the page from the internet"""

	# This function copies the webpage from my clipboard
	WEB_PAGE = pyperclip.paste()
	try:
		page = requests.get(WEB_PAGE)
		logger.info("%(WEB_PAGE)s successfully retrieved")
	except HTTPError:
		logger.exception(" The webpae does not exist")
	return WEB_PAGE

def save_page(WEB_PAGE):
	"""This function creates a document for the downloaded webpage"""

	DATA_SIZE = 5024
	FILE_NAME = get_filename()
	with open(FILE_NAME, "w") as file:
		# Iterating through the data downloaded
		for page in WEB_PAGE.iter_content(DATA_SIZE):
			file.write(page.decode())
	return None

def get_filename():
	"""This function gets the location in which the file will be stored"""
	present_location = os.getcwd()
	DATA_FOLDER = "Documents/Programming/recop.it/recop.it/data/raw"
	final_location = None
	if present_location = Path(Path.home, DATA_FOLDER):
		final_location = present_location
	else:
		final_location = Path(Path.home, DATA_FOLDER)

	FILE_NAME = f"{str(final_location)}/webpage.txt"
	FILE_NAME = verify_filename(FILE_NAME)
	return FILE_NAME

def verify_filename(FILE_NAME):
	"""This function verifies if there is an existing filename
		and returns another name if the name exists"""
	COUNT = 0
	FILE_NAME = FILE_NAME
	file_exists = os.path.exists(FILE_NAME)

	while file_exists:
		basename = os.path.basename().split(".")
		dir_name = os.path.dirname()
		FILE_NAME = f"{str(dir_name)}/{basename[0]}{COUNT}.{basename[1]}"
		COUNT += 1
		file_exists = os.path.exists(FILE_NAME)

	return FILE_NAME
