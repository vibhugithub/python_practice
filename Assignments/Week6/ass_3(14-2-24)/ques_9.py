"""
There is a file having numbers in each line of that file. 
Calculate the total of all numbers.
Example (File Content)
100
250
100
50
98

OUTPUT
598
"""
import os


def calculateTotal(filename: str) -> int:
    try:
        # Shortcut
        f = open(filename, "r")
        calculate = sum(list(map(int, f.read().split())))
        return calculate
        # file = open(filename, "r")
        # total = 0
        # for line in file:
        #     total += int(line.strip())
        # file.close()
        # return total
    except FileNotFoundError:
        print("File not found!")
        return -1  # Return -1 to indicate an error


filename = "".join([os.getcwd(), "/Assignments/Week6/text.txt"])
total = calculateTotal(filename)
if total != -1:
    print(f"Total = {total}")
