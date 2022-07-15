import types
from pathlib import Path

import pandas as pd

home = Path.cwd().parents[2]


def get_files(home: str) -> types.GeneratorType[str]:
    """Returns a iterator for the address of all the files in it"""
    assert home.exists()
    files = home.joinpath("data", "processed").iterdir()
    return files


def read_csv(address):
    """Returns a dataframe from the CSV file read"""
    return pd.read_csv(address)


def stack_df(df1, df2):
    """Stacks two dataframes on top of each other, vertically"""
    return pd.concat([df1, df2])


def drop_cols(df, columns):
    """Drops columns from the dataframe"""
    return df.drop(columns, axis=1, inplace=True)


def save_file(df, name):
    """Saves the file with the given name"""
    address = home.joinpath("data", "processed", name)
    df.to_csv(address)
