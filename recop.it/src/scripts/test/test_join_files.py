import sys
from pathlib import Path

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
    assert isinstance(df.shape, tuple)
    assert df.shape[0] > 1
    assert df.shape[1] > 1
    assert df.size == df.shape[0] * df.shape[1]


def test_stack_df():
    pass


def test_drop_cols():
    pass


def test_save_file():
    pass
