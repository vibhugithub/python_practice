"""
    Q1. Make a function named sumPattern that takes an integer n as an
    argument from the user. And then calculate the sum of the following
    pattern.
    ! means factorial of that number
    # Example
    sumPattern (5)
    Means
    1/1! + 1/2! + 1/3! + 1/41 + 1/5!
    # Output
    1.7166666666666668
"""


def factorial(n: int) -> int:
    i = 1
    answer = 1
    while i <= n:
        answer = answer * i
        i += 1
    return answer


def sumPattern(n: int) -> float:
    i = 1
    total = 0
    while i <= n:
        total = total + (1 / factorial(i))
        i += 1
    return total


print(sumPattern(5))
