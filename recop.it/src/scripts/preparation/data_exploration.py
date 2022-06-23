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
    """
    Returns an executable str with eval() of rows in the columns which their
    values are notnull
    """
    if isinstance(columns, list):
        final_list = list()
        for x in columns:
            y = f"(df['{x}'].notnull())"
            final_list.append(y)
        str_list =  " & ".join(final_list)
        return f"df[{str_list}]"
    elif isinstance(columns, str):
        return f"df[df[{columns}].notnull()]"
    else:
        return None


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
        all_few_values[file] = less_than_min_values(df, min_rows)
    return all_few_values


# +
# min1_values = all_less_than_min_values(location=location, min_rows=1)
# -

def count_few_values(few_values_dict):
    """Returns number of time few values columns appear in all the preprocessed files"""
    x = Counter()
    for values in few_values_dict.values():
        x.update(values)  
    return x


min_1_value = count_few_values(min1_values)


# +
# min_1_value
# -

def get_unique_values(values_dict):
    final_list = list()
    for list_ in values_dict.values():
        final_list.extend(list_)
    return list(set(final_list))


min1_value_list = get_unique_values(min1_values)


# +
# min1_value_list
# -

def remove_columns(columns, col_2_remove):
    """Remove values in col_2_remove from columns"""
    for value in col_2_remove:
        columns.remove(value)
    return columns


columns = get_columns(df)
remove_list = less_than_min_values(df=df, min_rows=1)
new_columns = remove_columns(columns=columns, col_2_remove=remove_list)

div1, div2, div3 = split_columns(new_columns)


def div_df(div):
    df_div_notnull = eval(not_null(div))
    return df_div_notnull[div]


df_div1_notnull = div_df(div1)
df_div1_notnull.head()


@runtime
def view_file(df, columns_to_view, columns_to_search):
    if isinstance(columns_to_search, list):
        for x in columns_to_search:
            columns_to_view.append(x)
            print(df[df[x].notnull()][columns_to_view].head(15))
            print("_"*30)
            columns_to_view.remove(x)
    else:
        columns_to_view.append(columns_to_search)
        df  = df[df[columns_to_search].notnull()][columns_to_view]
        columns_to_view.remove(columns_to_search)
    return df


columns = get_columns(df)
columns_to_view = columns[3:9]
columns_to_search = columns[9:]
# view_file(df, columns_to_view, columns_to_search)

# +
# columns
# -

columns_to_view = columns[3:9]
diameter_df = view_file(df, columns_to_view, "Diameter:")


def view_n_column(df, column, n_iters):
    n = 0
    for x in df[column]:
        if n > n_iters:
            break
        else:
            print(x)
            n += 1


view_n_column(diameter_df, "reviewText", 15)

sizename_df = view_file(df, columns_to_view, "Size Name:")
view_n_column(sizename_df, "reviewText", 15)

sizename_df["Size Name:"].value_counts()

modelnumb_df = view_file(df, columns_to_view, 'Model Number:')
print(modelnumb_df["Model Number:"].value_counts())
# view_n_column(modelnumb_df, "reviewText", 15)

def get_indices(df):
    """Return indices of all rows in the dataset"""
    return list(df.index.values)


@runtime
def remove_values_from_all_file(location, columns_to_remove):
    """
    This function removes values we don't want from the entire dataset i.e
    all files in the processed folder and saves them back
    
    Parameter(s)
    --------------
    location : str
               location to the data folder
    columns_to_remove : list
                        list of columns to purge their values
                        
    Return(s)
    -----------
    None
    """
    
    # list of all the files
    files = all_files(location)
    # Obtaining each file in the list
    for file in files:
        # open file
        df = get_df(location, file_name)
        # asin list to store all 'asin' values ('asin' values are unique 
        # identifiers of the product)
        asin_list = list()
        # get each column to remove their values
        for column in columns_to_remove:
            # get all columns in the dataset
            all_columns = get_columns(df)
            # get not null rows of the column
            notnull_values = eval(not_null(column))
            # get 'asin' values of the notnull values
            notnull_asin_values = get_values(notnull_values)
            # add to not null 'asin' values to asin_list
            asin_list.extend(notnull_asin_values)
            # drop column
            drop_column(df, column)
        # get unique "asin" values
        unique_asin_values = get_unique(asin_list)
        # get indices of asin values
        indices = get_indices(df)
        # delete rows matching the indices
        delete_rows(df, indices)
        # resave file
        save_file(location, file)
