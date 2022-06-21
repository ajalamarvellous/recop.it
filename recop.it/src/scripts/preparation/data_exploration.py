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

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

#Location t
location = "../../data/"


# +
# list of overview of all the data files
# -

# Go through all the folders and get the contents (leaf nodes)
def first_5(location):
    # getting the directory name, directories and files in the location
    # directory from the top to the bottom
    for dir_name, dirs, files in os.walk(location):
        # obtain only end /leaf nodes (final directory)
        if dir_name.endswith("/") is False:
            for file in files:
                # concatenate file name with dir_name
                file_name = os.path.join(dir_name, file)
                print(f"{'-'*30}The filename is {file_name}{'-'*30}")
                if file_name != "Clothing_Shoes_and_Jewelry_5.json":
                    # Open file
                    f = open(file_name)
                    # Read top 5 lines
                    for i in range(5):
                        print(f.readline())
                print("_"*100)
            print("_"*100)
            print(f"{'-'*30} Opening another folder {'-'*30}")


df = pd.read_csv(location+"processed/FILE_1.csv")

df.head()

df.describe(include="all")

df.info()


def get_columns(df):
    return list(df.columns)


columns

import math


def split_columns(columns):
    divs = math.ceil(len(columns)/3)
    div1, div2, div3 = columns[:divs], columns[divs:divs*2], columns[divs*2:]
    return div1, div2, div3
