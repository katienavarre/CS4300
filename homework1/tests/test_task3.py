# Tests for Task 3: number classification, prime generation, and summation logic.
from src.task3 import classify_number, first_ten_primes, sum_to_hundred


def test_classify_number():
    assert classify_number(5) == "positive"
    assert classify_number(-3) == "negative"
    assert classify_number(0) == "zero"


def test_first_ten_primes():
    assert first_ten_primes() == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_sum_to_hundred():
    assert sum_to_hundred() == 5050