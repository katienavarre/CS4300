# Test for Task 4: the discount function should reduce the price correctly.
from src.task4 import calculate_discount


def test_calculate_discount():
    assert calculate_discount(100, 10) == 90.0
    assert calculate_discount(250, 20) == 200.0
    assert calculate_discount(80, 0) == 80.0