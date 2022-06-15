import sys
import pytest

# Adding preparation directiory to sys path
sys.path.insert(0,"/home/ajala/Documents/Programming/recop.it/recop.it/src/scripts/preparation")

from json_csv import *

LOCATION = "../../data/raw/Clothing_Shoes_and_Jewelry_5.json"
DESC = ["h", "i", "j"]
mock_content = {"a": 5.0, "b": "2", "c": "true", "d": "05 4, 2014",
                "e": "A2IC3NZN488KWK", "style": {"f:": "Paperback"},
                "g": "Ruby Tulip" }
def test_read_json():
    with open(LOCATION, "rb") as f:
        y = read_json(f.readline())
        assert isinstance(y, dict) is True

def test_get_columns():
    columns = get_columns(mock_content, DESC)
    assert len(columns) == 9
    assert "style" not in columns
    assert isinstance(columns, list)

def test_get_desc_keys():
    x = get_desc_keys(mock_content)
    assert isinstance(x, list)
    assert len(x) == 1
    assert x[0] == "f:"
    y = mock_content
    del y["style"]
    assert get_desc_keys(y) is None


def test_get_values():
    pass

def test_get_all_desc():
    pass

def test_get_file_destination():
    pass

def test_create_file():
    pass

def test_product_desc_present():
    pass

def test_new_file_break():
    pass

def test_write_line():
    pass

def test_main():
    pass
