Homework 1 - Introduction to Python & Unit Testing

SETUP

1. Activate the virtual environment (or create it if you haven't):
   python3 -m venv your_custom_env_name_here --system-site-packages
   source your_custom_env_name_here/bin/activate

2. Install dependencies:
   python3 -m pip install pytest numpy


PROJECT STRUCTURE

cs4300 /
2 | - - homework1 /
3 | | - - src /
4 | | | - - task1 . py
5 | | | - - task2 . py
6 | | | - - task3 . py
7 | | | - - task4 . py
8 | | | - - task5 . py
9 | | | - - task6 . py
10 | | \ - - task7 . py
11 | | - - tests /
12 | | | - - test_task1 . py
13 | | | - - test_task2 . py
14 | | | - - test_task3 . py
15 | | | - - test_task4 . py
16 | | | - - test_task5 . py
17 | | | - - test_task6 . py
18 | | \ - - test_task7 . py
19 | | - - task6_read_me . txt
21 | \ - - README . md # how to run my code and tests


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