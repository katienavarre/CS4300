# Task 6: read a text file (task6_read_me.txt) and count how many words it contains
from pathlib import Path


def count_words_in_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read()
    return len(text.split())


if __name__ == "__main__":
    readme_path = Path(__file__).resolve().parents[1] / "task6_read_me.txt"
    word_count = count_words_in_file(readme_path)
    print(f"Word count: {word_count}")
