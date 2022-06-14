import sys
import pytest

# Adding preparation directiory to sys path
sys.path.insert(0,"/home/ajala/Documents/Programming/recop.it/recop.it/src/scripts/preparation")

from json_csv import *

LOCATION = "../../data/raw/Clothing_Shoes_and_Jewelry_5.json"
DESC = ["h", "i", "j"]
mock_content = {"a": 5.0, "b": "2", "c": "true", "d": "05 4, 2014",
                "e": "A2IC3NZN488KWK", "style": {"f:": " Paperback"},
                "g": "Ruby Tulip" }
def test_read_json():
    with open(LOCATION, "rb") as f:
        y = read_json(f.readline())
        assert isinstance(y, dict) is True

def test_get_columns():
    pass

def test_get_descriptions():
    pass

def test_get_values():
    pass
