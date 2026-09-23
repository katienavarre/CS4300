# Tests for Task 5: favorite books and the student record dictionary.
from src.task5 import books, student_database


def test_books(capsys):
    result = books()
    captured = capsys.readouterr()

    assert result[:3] == [
        ("To Kill a Mockingbird", "Harper Lee"),
        ("Project Hail Mary", "Andy Weir"),
        ("Pride and Prejudice", "Jane Austen"),
    ]
    assert "First three books:" in captured.out
    assert "To Kill a Mockingbird by Harper Lee" in captured.out


def test_student_database(capsys):
    result = student_database()
    captured = capsys.readouterr()

    assert result["Alice Johnson"] == "12345"
    assert result["Brian Smith"] == "56789"
    assert "Student database:" in captured.out
    assert "Alice Johnson: 12345" in captured.out