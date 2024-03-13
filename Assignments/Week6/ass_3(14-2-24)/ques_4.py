"""
Q4. Make a function which takes filename as a parameter. Return the
number of time the word the has appeared in that file.
"""
import os

file_path = "".join([os.getcwd(), "/Assignments/Week6/text.txt"])


def count_lines(path):
    count = 0
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            h = line.split()
            for i in h:
                if i.lower() == "the":
                    count += 1
    print(count)


count_lines(file_path)
