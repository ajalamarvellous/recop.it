import os
import logging
import requests
import pyperclip
from pathlib import Path
import tempfile

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] \
							%(funcName)s: %(message)s",
    level=logging.DEBUG,
)
logger = logging.getLogger()


def get_webpage(page_address):
    """Function to download the page from the internet"""

    # This function copies the webpage from my clipboard

    try:
        page = requests.get(page_address)
        logger.info(f"{page_address} successfully retrieved")
    except HTTPError:
        logger.exception(" The webpage does not exist")
    return page


def save_page(WEB_PAGE):
    """This function creates a temporary file for the downloaded webpage"""

    DATA_SIZE = 5024
    file = temp.TemporaryFile("w+")
    # Iterating through the data downloaded
    for page in WEB_PAGE.iter_content(DATA_SIZE):
    	file.write(page.decode())
    logger.info(f"{file.name} saved successfully")
    return file


#def get_filename():
#    This function gets the location in which the file will be stored
#    present_location = os.getcwd()
#    DATA_FOLDER = "Documents/Programming/recop.it/recop.it/data/raw"
#    final_location = None
#    if present_location == Path(Path.home(), DATA_FOLDER):
#        final_location = present_location
#    else:
#        final_location = Path(Path.home(), DATA_FOLDER)
#        logger.info(f"Changed file destination to {final_location}")

#    FILE_NAME = f"{str(final_location)}/webpage.txt"
#    FILE_NAME = verify_filename(FILE_NAME)
#    return FILE_NAME


#def verify_filename(FILE_NAME):
#    This function verifies if there is an existing filename
#    and returns another name if the name exists
#    COUNT = 0
#    FILE_NAME = FILE_NAME
#    file_exists = os.path.exists(FILE_NAME)

#    while file_exists:
#        logger.info(f"{FILE_NAME} exist if folder, renaming.......")
#        basename = os.path.basename(FILE_NAME).split(".")
#        dir_name = os.path.dirname(FILE_NAME)
#        FILE_NAME = f"{str(dir_name)}/{basename[0]}{COUNT}.{basename[1]}"
#        COUNT += 1
#        file_exists = os.path.exists(FILE_NAME)

##    return FILE_NAME


def main():
    WEB_PAGE = get_webpage()
    file = save_page(WEB_PAGE)
	return file


if __name__ == "__main__":
    main()
