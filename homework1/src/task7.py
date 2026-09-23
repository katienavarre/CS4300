# Task 7: analyze a list of numeric scores using NumPy
import numpy as np


def analyze_scores(scores):
    arr = np.array(scores)
    return {
        "scores": arr,
        "mean": np.mean(arr),
        "median": np.median(arr),
        "std_dev": np.std(arr),
        "min": np.min(arr),
        "max": np.max(arr),
    }


if __name__ == "__main__":
    test_scores = [85, 92, 78, 90, 88, 76, 95]

    results = analyze_scores(test_scores)

    print("Scores:", results["scores"])
    print(f"Mean: {results['mean']:.2f}")
    print(f"Median: {results['median']:.2f}")
    print(f"Standard Deviation: {results['std_dev']:.2f}")
    print(f"Min: {results['min']}")
    print(f"Max: {results['max']}")