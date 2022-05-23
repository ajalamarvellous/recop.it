import os
import loging
import requests
import pyperclip

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
	FILE_NAME =
	with open(FILE_NAME, "w") as file:
		# Iteracting through the data downloaded
		for page in WEB_PAGE.iter_content(DATA_SIZE):
			file.write(page.decode())
	return None
