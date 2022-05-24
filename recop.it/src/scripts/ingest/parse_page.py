import os
import logging
from pathlib import Path
from bs4 import BeautifulSoup

logging.basicConfig(format="%(asctime)s [%(levelname)] \
							%(funcName)s: %(message)s",
					level = logging.DEBUG)
logger = logging.getLogger()

# Location to the saved txt files
LOCATION = Path(Path.home(),
				"Documents/Programming/recop.it/recop.it/data/raw")

def get_files():
	"""Function to get the .txt data files"""
	files = list(LOCATION.glob("*.txt"))
	return files
