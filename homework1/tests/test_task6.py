# Test for Task 6: verify the word count matches the read-me file contents.
from pathlib import Path

from src.task6 import count_words_in_file


def test_count_words_in_file():
    file_path = Path(__file__).resolve().parents[1] / "task6_read_me.txt"
    assert count_words_in_file(file_path) == 127