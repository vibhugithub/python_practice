"""
Q6. Make a function which takes filename as a parameter. Return the count
of words which end with e.
"""
import os

file_path = "".join([os.getcwd(), "/Assignments/Week6/text.txt"])


def count_lines(path):
    count = 0
    with open(path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line.strip().lower().endswith("e") or line.strip().lower().endswith("E"):
                count += 1
    print(count)


count_lines(file_path)


def countWords(filename: str) -> int:
    try:
        file = open(filename, "r")
        data = file.read()
        file.close()
        words = data.split()
        count = 0
        for word in words:
            if word.endswith("e") or word.endswith("E"):
                count += 1
        return count
    except FileNotFoundError:
        print("File not found!")
        return -1  # Return -1 to indicate an error


filename = "test.txt"  # Replace with the name of your file
word_count = countWords(filename)
if word_count != -1:
    print(f"Count of words ending with 'e' = {word_count}")
