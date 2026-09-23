Homework 1 - Introduction to Python & Unit Testing

SETUP

1. Activate the virtual environment (or create it if you haven't):
   python3 -m venv your_custom_env_name_here --system-site-packages
   source your_custom_env_name_here/bin/activate

2. Install dependencies:
   python3 -m pip install pytest numpy


PROJECT STRUCTURE

cs4300 /
| - - homework1 /
| | - - src /
| | | - - task1 . py
| | | - - task2 . py
| | | - - task3 . py
| | | - - task4 . py
| | | - - task5 . py
| | | - - task6 . py
| | \ - - task7 . py
| | - - tests /
| | | - - test_task1 . py
| | | - - test_task2 . py
| | | - - test_task3 . py
| | | - - test_task4 . py
| | | - - test_task5 . py
| | | - - test_task6 . py
| | \ - - test_task7 . py
| | - - task6_read_me . txt
| \ - - README . md # how to run my code and tests


RUNNING THE CODE

From inside the homework1 directory, run any task script directly, for example:
  python3 -m src.task1
  python3 -m src.task7


RUNNING THE TESTS

From inside the homework1 directory, run:
  python3 -m pytest

To run a single task's tests:
  python3 -m pytest tests/test_task1.py

For verbose output:
  python3 -m pytest -v