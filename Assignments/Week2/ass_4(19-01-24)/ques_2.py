"""
    Q2. Create a function named pattern which takes an integer as an input
    and print the following pattern.

    # Example 1
    pattern (11)
    # Output
    10 20 30 40 50 60 70 80 90 100 110
"""


def pattern(n: int):
    i = 1
    total = 0
    if n != 0:
        while n >= i:
            total = total + 10
            print(total, end=" ")
            i += 1


pattern(11)
