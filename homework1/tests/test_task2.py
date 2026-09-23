# Test for Task 2: the data types dictionary should contain the expected values.
from src.task2 import datatypes


def test_datatypes():
    data = datatypes()

    assert data["string"] == "Hello World"
    assert data["integer"] == 100
    assert data["float"] == 0.5
    assert data["boolean"] is True