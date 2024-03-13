"""
Q1. Make a function which takes filename as a parameter. Return the
number of words present in that file.

"""

import os

file_path = "".join([os.getcwd(), "/Assignments/Week6/text.txt"])


def count_words(path):
    count = 0
    with open(path, "r") as f:
        lines = f.readlines()
        for i in lines:
            n = i.split()
            count += len(n)
    print(count)


count_words(file_path)
