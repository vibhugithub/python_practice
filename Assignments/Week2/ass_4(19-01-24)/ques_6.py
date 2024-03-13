"""
    Q6. Write a function named pattern which accepts an integer n as an
    argument. Then print the following pattern.

    # Example 1
    pattern (4)
    # Output
    1 4 9 16

    # Example 2
    pattern (10)
    # Output
    1 4 9 16 25 36 49 64 81 100
"""


def pattern(n: int):
    i = 1
    while i <= n:
        print(i**2, end=" ")
        i += 1


pattern(10)
