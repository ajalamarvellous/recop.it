import sys
from pathlib import Path

import pytest

sys.insert(0, Path(__file__).parents[1].joinpath("preparation"))
import join_files  # noqa


@pytest.fixture
def location():
    return Path.cwd().parents[2].joinpath("data", "processed")


def test_get_files(location):
    pass


def test_read_csv():
    pass


def test_stack_df():
    pass


def test_drop_cols():
    pass


def test_save_file():
    pass
