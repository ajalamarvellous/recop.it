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
import time
import math
from collections import Counter

#Location t
location = "../../data/"


def runtime(func):
    """Decorator function to return function runtime"""
    def wrapper(*args, **kwargs):
        """Decorator wrapper"""
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        print(f"Runtime for {func.__name__} is: {time.perf_counter()-start_time:.6f}s")
        return result
    return wrapper


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


def get_df(location, file_name):
    """This function returns a dataframe"""
    return pd.read_csv(location+"processed/"+file_name)


df = get_df(location=location, file_name="FILE_1.csv")

df.head()

df.describe(include="all")

df.info()


def get_columns(df):
    return list(df.columns)


columns = get_columns(df)


def split_columns(columns):
    divs = math.ceil(len(columns)/3)
    div1, div2, div3 = columns[:divs], columns[divs:divs*2], columns[divs*2:]
    return div1, div2, div3


def less_than_min_values(df, min_rows):
    """Returns function with less than the specified rows"""
    values = list()
    for x,y in zip(df.count(), df.count().index):
        if x < min_rows: values.append(y)
    return values


def not_null(columns):
    final_list = list()
    for x in columns:
        y = f"(df['{x}'].notnull())"
        final_list.append(y)
    str_list =  " & ".join(final_list)
    return f"df[{str_list}]"


div1, div2, div3 = split_columns(columns)

few_values = get_few_values(df, 1)


def all_files(location):
    """This function returns list of all processed csv"""
    return os.listdir(os.path.join(location, "processed"))


@runtime
def all_less_than_min_values(location, min_rows):
    """This function returns a list of all fewer values than min_rows in each of the files"""
    files = all_files(location=location)
    all_few_values = dict()
    for file in files:
        df = get_df(location=location, file_name=file)
        all_few_values[file] = get_few_values(df, min_rows)
    return all_few_values


all_few_values = get_all_few_values(location=location, min_rows=1)





def count_few_values(few_values_dict):
    """Returns number of time few values columns appear in all the preprocessed files"""
    x = Counter()
    for values in few_values_dict.values():
        x.update(values)  
    return x


min_1_value = count_few_values(all_few_values)




