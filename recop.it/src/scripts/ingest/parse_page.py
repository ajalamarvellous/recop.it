import os
import logging
import pyperclip
from pathlib import Path
from lxml import html
from get_page import get_webpage, save_page

logging.basicConfig(
    format="%(asctime)s [%(levelname)] \
							%(funcName)s: %(message)s",
    level=logging.DEBUG,
)
logger = logging.getLogger()

# Location to the saved txt files
LOCATION = Path(Path.home(), "Documents/Programming/recop.it/recop.it/data/raw")

# def get_files():
# 	"""Function to get the .txt data files"""
# 	files = list(LOCATION.glob("*.txt"))
# 	return files


def parse(doc):
    """
    This function parse the file and extract the needed information from the
    the file
    """
    recommendations = []
    main_section = doc.xpath("//main[@class='-pvs']")[0]
    title = main_section.xpath('//div[@class="-fs0 -pls -prl"]')[0].text_content()
    rating = main_section.xpath('//div[@class="stars _s _al"]')[0].text_content()
    price = main_section.xpath('//div[@class="-hr -mtxs -pvs"]')[0].text_content()
    brand = main_section.xpath('//div[@class="-pvxs"]')[0].text_content()
    product_details = main_section.xpath('//div[@class="markup -mhm -pvl -oxa -sc"]')[
        0
    ].text_content()
    spec = main_section.xpath('//div[@class="markup -pam"]')[0].text_content()
    recomm_div = main_section.xpath('.//div[@class="reco _res -mtm"]')
    for divs in recomm_div:
        for article in divs.xpath('.//div[@class="itm col"]'):
            try:
                a_tag = article.xpath('.//a[contains(@data-category, "Clothing")]')[0]
                recommendations.append(html.tostring(a_tag))
            except IndexError:
                logger.exception("no a <> with that data-category tag")
    logger.info(
        f"Title: {title}\n\
				Price: {price}\n\
				Rating: {rating}\n\
				Brand: {brand}\n\
				Product Details: {product_details}\n\
				Specifications: {spec}\n\
                Number of recommendations: {len(recommendations)}\n\
                first recommendation: {recommendations[:6]}"
    )


def main():
    web_address = input("Please enter the web address here: ")
    web_page = get_webpage(web_address)
    file = save_page(web_page)
    file_content = file.read()
    doc = html.fromstring(file_content)
    parse(doc)
    print("*" * 100)
    file.close()


if __name__ == "__main__":
    main()
