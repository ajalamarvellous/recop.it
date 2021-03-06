import os
import logging
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from pathlib import Path

# Setting log configuration to display time, logger.levelname, function name
# and log message
logging.basicConfig(
    format="%(asctime)s [%(levelname)s] \
		    %(funcName)s: %(message)s",
    level=logging.DEBUG,
)
logger = logging.getLogger()

def get_page(web_address):
    """Instantiate selenium browser and get web page

    This function instantiates the selenium browser and
    get the contents of the website

    Parameter(s)
    ------------
    web_address : string
                  address of the website to be scraped

    Return
    ----------
    browser : object
              instantiated selenium browser with the loaded web page content
    """

    browser = webdriver.Chrome()
    browser.get(web_address)
    logger.info("Page opened and returning safely")
    return browser


def parse(web_page):
    """Parse webpage and obtain needed information

    This function parse the file and extract the needed information
    from the websites

    Parameter(s)
    ----------------
    web_page : object
               instantiated and loaded selenium browser

    Returns
    ---------
    data : dictionary {Title: string,
                       price: string,
                       product_details: string,
                       recommendation: list(tuple(title, link))}
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

    recomm_sec = web_page.find_elements(By.CLASS_NAME, "Ha1Ya")

    recc= [a.get_attribute("aria-label") for a in web_page.find_elements(By.XPATH, "//*[@class = 'Usg4d']")]
    #recomm_products = recomm_sec.find_elements(By.TAG_NAME,"li")
    logger.info(f"{'*'*10} {len(recomm_sec)} found {'*'*10}")
    for products in recomm_sec:
        for page_div in products.find_elements(By.CLASS_NAME, "YV2UQ"):
            product_ = page_div.find_element_by_tag_name("a")
            label = product_.get_attribute("aria-label")
            link = product_.get_attribute("href")
            recommendations.append((label,link))
    logger.info(f"Title: {title} \n\
		          Price: {price} \n\
		          Product Details: {product_details} \n\
		          Number of recommendations: {len(recommendations)} \n\
                  first recommendation: {recommendations} \n\
                  recc: {recc}"
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
