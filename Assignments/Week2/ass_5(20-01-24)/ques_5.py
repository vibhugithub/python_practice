"""
    Q5. Create a function addDigits() that takes an integer as an argument.
    Calculate the sum of digits of that number.

    # Example 1
    addDigits (123)
    # Output
    6
    # Example 2
    addDigits (58714)
    # Output
    25
"""


def addDigits(num: int) -> int:
    # Dont change the num so storing number in n
    n: int = num
    total = 0
    i = 1
    while n > 0:
        print(f"CASE {i}: ")
        print(f"total  {total} +  {n%10}")
        total = total + (n % 10)  # n%10 gives us last digit
        n = n // 10
        print(f" value of n {n//10}")
        print()
        i += 1
    return total


print(addDigits(123))
print(addDigits(58714))
