import logging
from pathlib import Path

import pandas as pd

LOCATION = Path(__file__).resolve().parents[3].joinpath("data", "processed")

logging.basicConfig(
    format="%(asctime)s [%(levelname)s]\
            %(funcName): %(message)s",
    level=logging.DEBUG,
)
logger = logging.getLogger(__name__)


def get_files(LOCATION):
    """Returns a iterator for the address of all the files in it"""
    assert LOCATION.exists()
    files = LOCATION.iterdir()
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
    address = LOCATION.joinpath(name)
    df.to_csv(address)
