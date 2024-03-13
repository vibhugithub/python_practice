"""
    Q2. Make a function which takes filename as a parameter. Return the
number of lines present in that file.

"""
import os

file_path = "".join([os.getcwd(), "/Assignments/Week6/text.txt"])


def count_lines(path):
    count = 0
    with open(path, "r") as f:
        lines = f.readlines()
        count += len(lines)
    print(count)


count_lines(file_path)
