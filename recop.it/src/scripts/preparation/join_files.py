import logging
import os
from pathlib import Path
from typing import List, Tuple

import pandas as pd

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] \
            %(funcName)s: %(message)s",
    level=logging.DEBUG,
)
logger = logging.getLogger()


def get_files(LOCATION: str) -> Tuple[str]:
    """Returns a iterator for the address of all the files in it"""
    assert os.path.exists(LOCATION)
    files = os.listdir(LOCATION)
    return files


def get_address(filename: str):
    """Returns a iterator for the address of all the files in it"""
    address = os.path.join(LOCATION, filename)
    return address


def read_csv(address: str):
    """Returns a dataframe from the CSV file read"""
    return pd.read_csv(address)


def pop_list(array: List[str]):
    """
    Returns two values from list, removes those values from the list and
    returns them as a tuple
    """
    list_ = list()
    for num in range(2):
        if array != []:
            x = array.pop()
            list_.append(x)
        else:
            list_.append(None)
    return tuple(list_)


def drop_cols(df: object, columns: List[str]):
    """Drops columns from the dataframe"""
    return df.drop(columns, axis=1, inplace=True)


def save_file(df: object, LOCATION: str, iteration: int):
    """Saves the file with the given name"""
    name = f"COMBINED_FILE-{iteration}.parquet"
    address = get_address(filename=name)
    df.to_csv(address, index=False)


def stack_df(file1: object, file2: object, iteration: int):
    """Stacks two dataframes on top of each other, vertically"""
    if file2 is not None:
        df1, df2 = read_csv(file1), read_csv(file2)
        df = pd.concat([df1, df2])
        drop_cols(df, ["Unnamed: 0", "Unnamed: 0.1"])
        df.fillna(-1)
        logger.info("columns dropped successfully.....")
        save_file(df, LOCATION, iteration)
        logger.info(f"file saved to {LOCATION} sucessfully....")
    else:
        df = read_csv(file1)
        drop_cols(df, ["Unnamed: 0", "Unnamed: 0.1"])
        logger.info("columns dropped successfully.....")
        save_file(df, LOCATION, iteration)
        logger.info(f"file saved to {LOCATION} sucessfully....")


def main():
    iteration = 0
    files = get_files(LOCATION)
    logger.info("....starting task now......")
    while files != []:
        iteration += 1
        file1, file2 = pop_list(files)
        if file2 is not None:
            file1_address = get_address(file1)
            file2_address = get_address(file2)
        else:
            file1_address, file2_address = get_address(file1), None
        stack_df(file1=file1_address, file2=file2_address, iteration=iteration)
    logger.info("Tasks sucessfully completed....")


if __name__ == "__main__":
    LOCATION = Path(__file__).resolve().parents[3].joinpath("data", "processed")  # noqa
    main()
