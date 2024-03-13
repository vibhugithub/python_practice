"""
    Q5. Make a function which takes filename as a parameter. Print the words
in that file which has length greater than 4.
"""
import os

file_path = "".join([os.getcwd(), "/Assignments/Week6/text.txt"])


def count_lines(path):
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            h = line.split()
            for i in h:
                if len(i) > 4:
                    print(i, end=" ")
            print()


count_lines(file_path)
