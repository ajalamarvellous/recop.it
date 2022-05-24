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

def main():
	files = get_files()
	for file in files:
		with open(file, "r") as doc:
			soup_doc = BeautifulSoup(doc,"html.parser")
			

if __name__ == "__main__":
	main()
