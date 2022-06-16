import sys
import os
import pytest
from unittest.mock import *

# Adding preparation directiory to sys path
sys.path.insert(0,"/home/ajala/Documents/Programming/recop.it/recop.it/src/scripts/preparation")

from json_csv import *

@pytest.fixture
def LOCATION():
    return "../../data/raw/Clothing_Shoes_and_Jewelry_5.json"


@pytest.fixture
def create_mock_dict():
    """This function create a mock dictionary"""
    return {"a": 5.0, "b": "2", "c": "true", "d": "05 4, 2014",
            "e": "A2IC3NZN488KWK", "style": {"f:": "Paperback"},
            "g": "Ruby Tulip" }


@pytest.mark.parametrize("input, expected", [
                        (500000, True),
                        (500001, False),
                        (2519235, False),
                        (11000000, True),
                        (1500000, True)
                        ])

                        
def test_read_json(LOCATION):
    with open(LOCATION, "rb") as f:
        y = read_json(f.readline())
        assert isinstance(y, dict) is True

def test_get_columns(create_mock_dict):
    DESC = ["h", "i", "j"]
    columns = get_columns(create_mock_dict, DESC)
    assert len(columns) == 9
    assert "style" not in columns
    assert isinstance(columns, list)


def test_get_desc_keys(create_mock_dict):
    x = get_desc_keys(create_mock_dict)
    assert isinstance(x, list)
    assert len(x) == 1
    assert x[0] == "f:"
    y = create_mock_dict
    del y["style"]
    assert get_desc_keys(y) is None


def test_get_values(create_mock_dict):
    columns, all_prod_desc = ["a", "b", "c", "d", "e", "g", "f:", "z"], ["f:", "z"]
    expected_values = [5.0, "2", "true",  "05 4, 2014", "A2IC3NZN488KWK",
                       "Ruby Tulip", "Paperback", "null"]
    values = get_values(create_mock_dict, columns, all_prod_desc)
    assert isinstance(values, dict)
    assert values["f:"] == "Paperback"
    assert values["z"] == "null"
    assert list(values.values()) == expected_values


@pytest.mark.skip(reason="Tested already and takes too long to load")
def test_get_all_desc(LOCATION):
    desc_keys = get_all_desc_keys(LOCATION)
    assert isinstance(desc_keys, list)
    assert len(desc_keys) != 0


def test_get_file_destination(LOCATION):
    loc = get_file_destination(LOCATION)
    assert os.path.exists(loc)
    assert loc.endswith(r"/processed/")
    assert "data" in loc.split(r"/")
    assert "raw" not in loc.split(r"/")


def test_create_file(LOCATION):
    file, n_files = create_file(LOCATION, 0)
    assert n_files == 1
    assert file.mode == "w"
    assert file.name.endswith("FILE_0.csv")
    assert file.closed is False
    os.remove(file.name)


def test_product_desc_present(create_mock_dict):
    assert PRODUCT_DESC_PRESENT(create_mock_dict) is True
    del create_mock_dict["style"]
    assert PRODUCT_DESC_PRESENT(create_mock_dict) is False


def test_new_file_break(input, expected):
    assert NEW_FILE_BREAK(input) is expected

def test_write_line():
    pass

def test_main():
    pass
