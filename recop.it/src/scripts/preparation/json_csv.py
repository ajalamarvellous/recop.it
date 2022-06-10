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
from tqdm import tqdm
import csv

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
    This function gets the description keys in each data entry i.e each line
    representing the data for interaction of a user with a product that are
    in the "style" of that data enty dictionary

    Depends on the product, the description in the "style" key is different
    e.g books in the dataset have description format, where as clothing has
    size, color and some other descriptions. So this function will obtain all
    keys that are describing the different properties of that data entry.

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


def get_all_desc(LOCATION):
    """
    This function combines all the descriptions of each data entry to obtain
    all unique desciptions in the 'style' key
    """
    file = open(LOCATION, "rb")
    desc = list()
    for line in tqdm(file, desc="Reading each line of json file"):
        json_dict = read_json(line)
        line_desc = get_descriptions(json_dict)
        desc.extend(line_desc)
    return list(set(desc))


# +
#all_desc = get_all_desc(LOCATION)
# -

all_desc


def get_file_destination(LOCATION):
    """
    This function sets the destination to save the files to as 'data/processed'
    """
    destination_list = LOCATION.split("/")
    return "/".join(destination_list[:-2]) + str("/processed/")


# +
def main():
    n_rows = 1
    n_files = 1
    columns = list()
    with open(LOCATION, "rb") as file:
        file_destination = get_file_destination(LOCATION)
        processed_file, n_files = create_file(file_destination, n_files)
        csv_writer = None
        for line in file:
            line_dict = read_json(line)
            if n_rows == 1:
                columns = get_columns(line_dict, all_desc)
                csv_writer = csv.DictWriter(processed_file,
                                            fieldnames=columns)
            else:
                pass
            if PRODUCT_DESC_PRESENT(line_dict):
                n_rows += 1
                values = get_values(columns, line_dict)
                if NEW_FILE_BREAK(n_rows):
                    processed_file.close()
                    processed_file, n_files = create_file(
                                                file_destination, n_files)
                    csv_writer = csv.DictWriter(processed_file,
                                                fieldnames=columns)
                else:
                    pass
                write_line(processed_file, values)
            else:
                pass
        processed_file.close()


# -
