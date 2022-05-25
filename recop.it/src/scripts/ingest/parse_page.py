import os
import logging
from pathlib import Path
from bs4 import BeautifulSoup
from lxml import html

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

def parse(doc):
	"""
	This function parse the file and extract the needed information from the
	the file
	"""
	main_section = doc.xpath("//main[@class='-pvs']")[0]
	title = main_section.xpath(
								'//div[@class="-fs0 -pls -prl"]'
								)[0].text_content()
	rating = main_section.xpath(
								'//div[@class="stars _s _al"]'
								)[0].text_content()
	brand = main_section.xpath('//div[@class="-pvxs"]')[0].text_content()
	price = main_section.xpath(
								'//div[@class="-hr -mtxs -pvs"]'
								)[0].text_content()
	product_details = main_section.xpath(
							'//div[@class="markup -mhm -pvl -oxa -sc"]'
										)[0].text_content()
	spec = main_section.xpath('//div[@class="markup -pam"]')[0].text_content()
	print(f"Title: {title}\n\
			Price: {price}\n\
			Rating: {rating}\n\
			Brand: {brand}\n\
			Product Details: {product_details}\n\
			Specifications: {spec}")



def main():
	files = get_files()
	for file in files:
		doc = html.parse(file)
		parse(doc)
		print("*"*100)


if __name__ == "__main__":
	main()
