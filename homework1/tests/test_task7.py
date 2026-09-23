# Test for Task 7: confirm the score summary statistics are calculated correctly.
from src.task7 import analyze_scores


def test_analyze_scores():
    scores = [85, 92, 78, 90, 88, 76, 95]
    result = analyze_scores(scores)

    assert result["min"] == 76
    assert result["max"] == 95
    assert result["mean"] == 86.28571428571429
    assert result["median"] == 88.0
    assert round(float(result["std_dev"]), 2) == 6.56