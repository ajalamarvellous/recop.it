import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(
    0, Path(__file__).resolve().parents[1].joinpath("preparation").__str__()
)
import join_files  # noqaa


@pytest.fixture
def location():
    return Path(__file__).resolve().parents[3].joinpath("data", "processed")


def test_get_files(location):
    files = join_files.get_files(location)
    assert Path(next(files)).exists()


@pytest.fixture
def address(location):
    address = next(join_files.get_files(location)).__str__()
    return address


def test_read_csv(address):
    df = join_files.read_csv(address)
    assert isinstance(df, pd.core.frame.DataFrame)
    assert df.shape[0] > 1
    assert df.shape[1] > 1
    assert df.size == df.shape[0] * df.shape[1]


@pytest.fixture
def df():
    df_dict = {
        "a": [1, 2, 3, 4, 5],
        "b": [11, 12, 13, 14, 15],
        "c": [21, 22, 23, 24, 25],
    }
    return pd.DataFrame(df_dict)


def test_stack_df(df):
    stacked_df = join_files.stack_df(df, df)
    assert isinstance(stacked_df, pd.core.frame.DataFrame)
    assert stacked_df.shape[0] == df.shape[0] * 2
    assert stacked_df.shape[1] == df.shape[1]


def test_drop_cols(df):
    x, y = df.shape
    join_files.drop_cols(df, "b")
    assert "b" not in df.columns.values
    assert df.shape[1] == y - 1
    assert df.shape[0] == x


def test_save_file():
    pass
