"""
    Q1. Create a function named factorial which takes a integer as an input and
returns the factorial of that number.
Factorial of 5 means 5 x 4 x 3 x 2 x 1 = 120
"""


def factorial(num: int):
    i = num
    total = 1
    if num != 0:
        while i >= 1:
            total = total * i
            i -= 1
        return total


x = factorial(5)
print(x)
