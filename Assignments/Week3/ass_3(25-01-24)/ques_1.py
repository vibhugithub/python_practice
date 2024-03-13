"""
    Q1. Create a function countOddEven that accepts an List of Integers and
    print how many even and odd numbers are there.
    my_list = 134, 11, 91, 59, 33, 221
    countOddEven (my_list)
    # Output
    Total even numbers = 2
    Total odd numbers = 4
"""


def countOddEven(my_list):
    even_count = 0
    odd_count = 0
    for i in my_list:
        if i % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    print(f"Total even numbers = {even_count}")
    print(f"Total odd numbers = {odd_count}")


my_list = [34, 11, 91, 59, 33, 22]
countOddEven(my_list)
