"""
    Q1. Make a function named reverse which accepts an integer n from the
    user. Reverse the number passed as a parameter and return the reverse
    number. Do not use STRINGS.

    # Example 1
    reverse (91)
    # Output
    19
    # Example 2
    reverse (1000)
    # Output
    1
"""


def reverse(n: int):
    last_digit = 0
    while n > 0:
        remainder = n % 10
        last_digit = (last_digit * 10) + remainder
        n = n // 10
    return last_digit


x = reverse(159)
print(x)
