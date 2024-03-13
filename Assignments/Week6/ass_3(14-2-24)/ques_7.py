"""
Q7. Make a function which takes filename as a parameter. Return the count
of uppercase characters in that file.
"""
import os


def count_char(filename: str) -> int:
    try:
        file = open(filename, "r")
        data = file.read()
        file.close()
        count = sum(1 for char in data if char.isupper())
        return count
    except FileNotFoundError:
        print("File not found!")
        return -1  # Return -1 to indicate an error


filename = "".join([os.getcwd(), "/Assignments/Week6/text.txt"])
word_count = count_char(filename)
if word_count != -1:
    print(f"Count of uppercase characters = {word_count}")
