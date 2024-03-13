import math

"""
not nice approch
    a=str(1234)
    a[::-1]
    a=int(a)
"""
"""
Time complexity=O(n)
space=O(1)
"""


def reverse_number_(n: int):
    reverse = ""
    while n > 0:
        remainder = n % 10
        reverse += str(remainder)
        n = n // 10
    print(reverse)


reverse_number_(123456)
"""
Time complexity=O(log10(n))
space=O(1)
"""


def reverse_number(n):
    # Handle negative numbers
    sign = -1 if n < 0 else 1
    n = abs(n)

    reversed_n = 0
    while n > 0:
        # Extract the last digit
        digit = n % 10
        # Build the reversed number
        reversed_n = reversed_n * 10 + digit
        # Remove the last digit
        n //= 10

    # Restore the sign
    reversed_n *= sign

    return reversed_n


# Example usage
number = 12345
reversed_number = reverse_number(number)
print("Original number:", number)
print("Reversed number:", reversed_number)
