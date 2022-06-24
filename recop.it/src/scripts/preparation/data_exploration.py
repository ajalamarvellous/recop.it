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
from tqdm import tqdm

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
def all_less_than_min_values(location, min_rows, return_counts=False):
    """
    This function returns a list of all fewer values than min_rows (given 
    the return_counts is set to False) in each of the files or a dictionary
    containing the count of each of the columns fewer than the min_rows
    
    Paramater(s)
    -------------
    location      : str
                    address to folder containing the files
    min_rows      : int
                    cut off value to find rows with values less than
    return_counts : bool
                    returns count of each of the values in a dict is True or
                    a list of all columns less than min_rows
    
    Return(s)
    ----------
    all_few_value : dict(File_name:list(columns_less_than_min_rows))
                    if return_counts = False
                    dict(File_name:dict(columns_less_than_min_rows:count))
                    if return_counts = True
    """
    files = all_files(location=location)
    all_few_values = dict()
    for file in files:
        # get dataframes
        df = get_df(location=location,
                    file_name=file)
        # get columns with less than min_rows
        values = less_than_min_values(df=df,
                                      min_rows=min_rows)
        # Check if whether count is True and min_rows is greater than 1
        # if min_rows in less than 1, then it is automatically 0
        if return_counts is True and min_rows >= 1:
            # Create dictionary for each file
            all_few_values[file] = dict()
            for index, value in zip(df[values].count().index,
                            df[values].count()):
                all_few_values[file][index] = value
        # if not return just the values
        else:
            # Add to all_few_values dict
            all_few_values[file] = values
        
    return all_few_values


def count_few_values(few_values_dict):
    """Returns number of time few values columns appear in all the preprocessed files"""
    x = Counter()
    for values in few_values_dict.values():
        # Checks if values of few_values_dict are lists
        if isinstance(values, list):
            # Update counter
            x.update(values)
        # Checks if values of few_values_dict are dicts
        if isinstance(values, dict):
            # Update counter
            x.update(list(values.keys()))
    return x


# +
# min_1_value
# -

def get_unique_values(all_values):
    """
    Returns unique values in the all_values given on the assumption that
    it is a dictionary or list
    """
    if isinstance(all_values, dict):
        final_list = list()
        for list_ in all_values.values():
            final_list.extend(list_)
        return list(set(final_list))
    elif isinstance(all_values, list):
        return list(set(all_values))
    else:
        return None


no_value = all_less_than_min_values(location=location,
                                    min_rows=1)
no_value_counts = count_few_values(no_value)
no_value_list = get_unique_values(no_value)

print(no_value_list)
no_value_counts


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


def get_values(df, column, n_iters=0):
    """
    Print n_iters rows of the specied column if n_iters is provided else 
    return all values in the specied column instead
    """
    if n_iters != 0:
        n = 0
        for x in df[column]:
            if n > n_iters:
                break
            else:
                print(x)
                n += 1
    else:
        return list(df[column].values)


get_values(diameter_df, "reviewText", 15)

sizename_df = view_file(df, columns_to_view, "Size Name:")
size = get_values(sizename_df, "Size Name:")

sizename_df["Size Name:"].value_counts()

modelnumb_df = view_file(df, columns_to_view, 'Model Number:')
print(modelnumb_df["Model Number:"].value_counts())
# view_n_column(modelnumb_df, "reviewText", 15)

def get_indices(df, column, values):
    """
    Return indices of all rows that the column value matches those in 
    values in the dataset
    """
    indices_list = list()
    for value in values:
        df1 = df[df[column] == value]
        indices_list.extend(list(df1.index))
    return indices_list


def drop_column(df, column):
    """This function drops a column from a dataset"""
    return df.drop(columns=column, inplace=True)


def delete_rows(df, indices):
    """This function deletes rows in matching the indices provided"""
    df.drop(indices, inplace=True)


def save_file(df, location, filename):
    """This function saves a new csv file"""
    df.to_csv(f"{location}processed/{filename}")
    print(f'{"."*20}Saving file {filename} now{"."*20}')


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
    files = all_files(location=location)
    # Obtaining each file in the list
    for file in tqdm(files, desc="Retrieving files"):
        # open file
        df = get_df(location=location,
                    file_name=file)
        # asin list to store all 'asin' values ('asin' values are unique 
        # identifiers of the product)
        asin_list = list()
        # get each column to remove their values
        for column in tqdm(columns_to_remove, desc="Removing columns"):
            # get all columns in the dataset
            all_columns = get_columns(df)
            # get not null rows of the column
            notnull_values = view_file(df=df,
                                       columns_to_view=all_columns[3:9],
                                       columns_to_search=column)
            # get 'asin' values of the notnull values
            notnull_asin_values = get_values(df=notnull_values,
                                             column="asin")
            # add to not null 'asin' values to asin_list
            asin_list.extend(notnull_asin_values)
            # drop column
            drop_column(df=df,
                        column=column)
        # get unique "asin" values
        unique_asin_values = get_unique_values(asin_list)
        # get indices of asin values
        indices = get_indices(df=df,
                              column="asin",
                              values=unique_asin_values)
        # delete rows matching the indices
        delete_rows(df=df,
                    indices=indices)
        # resave file
        save_file(df=df,
                  location=location,
                  filename=file)


columns_to_remove = ['Width:',
                     'Item Display Length:', 
                     'Total Diamond Weight:',
                     'Gem Type:',
                     'Style Name:',
                     'Diameter:',
                     'Size per Pearl:',
                     'Primary Stone Gem Type:',
                     'Capacity:',
                     'Item Package Quantity:',
                     'Metal Stamp:',
                     'Format:',
                     'Metal Type:',
                     'Length:',
                     'Model Number:',
                     'Number of Items:']
remove_values_from_all_file(location=location,
                            columns_to_remove=columns_to_remove)
