# Test for Task 1: the hello function should print and return the greeting.
from src.task1 import hello


def test_hello(capsys):
    result = hello()
    captured = capsys.readouterr()

    assert result == "Hello World!"
    assert captured.out == "Hello World!\n"