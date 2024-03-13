"""
    Q2. Create a function sumCountOddEven that accepts an List of Integers
    and calculate sum of even and odd numbers.
    my_list = [34, 11, 91, 59, 33, 22]
    sumCountOddEven (my_list)
    # Output
    Even numbers sum = 56
    Odd numbers sum = 194
"""


def sumCountOddEven(my_list):
    even_count = 0
    odd_count = 0
    for i in my_list:
        if i % 2 == 0:
            even_count = even_count + i
        else:
            odd_count = odd_count + i

    print(f"Total even numbers = {even_count}")
    print(f"Total odd numbers = {odd_count}")


my_list = [34, 11, 91, 59, 33, 22]
sumCountOddEven(my_list)
