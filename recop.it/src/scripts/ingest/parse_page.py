import os
import logging
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
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

def get_page(web_address):
    """Function to get the .txt data files"""
    browser = webdriver.Chrome()
    browser.get(web_address)
    logger.info("Page opened and returning safely")
    return browser


def parse(web_page):
    """
    This function parse the file and extract the needed information from the
    the file
    """
    recommendations = []
    main_section = web_page.find_elements(By.XPATH, "//main[@id='chrome-app-container']")[0]
    title_block = web_page.find_elements(By.XPATH, '//div[@class="product-hero"]')[0]
    title = title_block.find_element_by_tag_name("h1").text
    logger.info(f"{'*'*10} {title} obtained {'*'*10}")
    price = title_block.find_element(By.XPATH, '//span[@data-id="current-price"]').text
    logger.info(f"{'*'*10} {price} obtained {'*'*10}")
    product_details = web_page.find_element(By.XPATH, '//div[@class="product-description"]').text
    logger.info(f"{'*'*10} {product_details} obtained {'*'*10}")
    #recomm_sec = web_page.find_elements(By.XPATH, '//div[@class="YV2UQ"]')
    #loggers.info(f"{len(recomm_sec)} found with the tag")

    recomm_sec = web_page.find_elements(By.XPATH, '//*[@class="YV2UQ"]')
    #recomm_products = recomm_sec.find_elements(By.TAG_NAME,"li")
    logger.info(f"{'*'*10} {len(recomm_sec)} found {'*'*10}")
    for product in recomm_sec:
        product_ = product.find_element_by_tag_name("a")
        label = product_.get_attribute("aria-label")
        link = product_.get_attribute("href")
        recommendations.append((label,link))
    logger.info(
        f"Title: {title}\n\
		Price: {price}\n\
		Product Details: {product_details}\n\
		Number of recommendations: {len(recommendations)}\n\
        first recommendation: {recommendations}"
    )


def main():
    web_address = input("Please enter the web address here: ")
    web_page = get_page(web_address)
    #file = save_page(web_page)
    #file_content = file.read()
    #doc = html.fromstring(file_content)
    parse(web_page)
    print("*" * 100)


if __name__ == "__main__":
    main()
