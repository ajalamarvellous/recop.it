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


def test_read_csv():
    pass


def test_stack_df():
    pass


def test_drop_cols():
    pass


def test_save_file():
    pass
