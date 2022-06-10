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

#Location to the json file
LOCATION = "../../data/raw/Clothing_Shoes_and_Jewelry_5.json"


def read_json(line):
    """This function reads a line of the json file as a dictionary"""
    return orjson.loads(line)


def get_columns(json_line, descriptions):
    """
    This function gets the keys (to be used as columns) and the description
    keys and combines all of them together as the columns to be used
    
    Parameter(s)
    --------------
    json_line : dict()
                a complete data point already parsed as a dictionary by
                orjson.loads()
                
    descriptions : list()
                   a list of all keys in the dataset found in the "style" key 
                   of each data point
                   
    Return(s)
    -----------
    column_keys : list()
                  a list of all the keys in the dataset and the keys originally
                  in the 'style' key minus the "style key"
    """
    
    column_keys = list(json_line.keys())
    file_keys.extend(descriptions)
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


def get_values(file_keys, prod_dict):
    """
    This function gets the values from the keys of the json file present

    The existing json contains the description of the products
    ["Size:", "Color:", "Packaging:", "Number of Items:"] all inside the style
    key, this function obtain all these values and make them available all
    together accesible via .get() method od the product's dictionary

    Argument(s)
    ---------------
    file_keys : list
                contains list of all the keys in the product to be obtained

    prod_dict : dictionary
                key-value pairs for each dinstint product

    Returns
    ------------
    new_prod_dict : dictionary
                    new key-value pairs of the product including descriptions
                    which were previously key-value pairs inside style

    """
    new_prod_dict = dict()
    STYLE = "style"
    mini_column = ["Size:", "Color:", "Packaging:", "Number of Items:"]
    for key in file_keys:
        if key not in mini_column:
            new_prod_dict[key] = prod_dict.get(key)
        elif key in mini_column:
            value = prod_dict[STYLE].get(key)
            if value == None:
                new_prod_dict[key] = "null"
            else:
                new_prod_dict[key] = value
    return new_prod_dict


["Size:", "Color:", "Packaging:", "Number of Items:"]

# +

#loading file
json_file = open(location, "rb")first_line = json_file.readline()
json_reader = orjson.loads(first_line)
