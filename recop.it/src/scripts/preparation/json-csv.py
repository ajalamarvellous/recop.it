# ---
# jupyter:
#   jupytext:
#     formats: notebooks//ipynb,scripts/preparation//py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
# Loading necessary libraries
# -

import os
import orjson

#Location to the json
location = "../../data/raw/Clothing_Shoes_and_Jewelry_5.json"

#loading file
json_file = open(location, "rb")

first_line = json_file.readline()
json_reader = orjson.loads(first_line)


i = list(json_reader.keys())
print(i)


# This function gets the keys in the original json file
def get_columns(json_reader):
    # Gets all the keys
    file_keys = list(json_reader.keys())
    # Add the keys found in the style value which is contains another dictionary
    file_keys.extend(["Size:", "Color:", "Packaging:", "Number of Items:"])
    # Remove the style key since we'll be adding it's contents to the main body
    file_keys.remove("style")
    return file_keys


def get_descriptions(prod_dict):
    """
    This function gets all the description keys in the entire data set
    that are in the "style" of the main product dictionary

    Depends on the product, the description in the "style" key is different
    e.g books in the dataset have description format, where as clothing has
    size, colorand some other descriptions. So this function will obtain all
    keys that are describing the different properties.

    Argument(s)
    -----------
    prod_dict : dict()
                a dictionary for each person interation containing basic
                info about them, their rankings and the product they are
                interacting with

    Return(s)
    ---------------
    desc_list : list()
                a list of all the description keys in the "style" value
    """
    desc_list = list()
    KEY = "style"
    desc_dict = prod_dict.get(KEY)
    if desc_dict != None:
        desc_list.extend(list(desc_dict.keys()))
    return desc_list
            
