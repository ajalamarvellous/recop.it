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
for dir_name, dirs, files in os.walk(location):
    if dir_name_.endswith("/") is False:
        for file in files:
            file_name = os.path.join(dir_name, file)
            print(f"{'-'*30}The filename is {file_name}{'-'*30}")
            if file_name != "Clothing_Shoes_and_Jewelry_5.json":
                f = open(file_name)
                for i in range(5):
                    print(f.readline())
            print("_"*100)
        print("_"*100)
        print(f"{'-'*30} Opening another folder {'-'*30}")





















 
