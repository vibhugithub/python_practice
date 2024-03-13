"""
    Q5. Make a function named sumOfFirstAndLastDigit which accepts an
    integer n from the user. Calculate the sum of first and last digit of a
    number and return it.

    # Examples
    sumOfFirstAndLastDigit (1234)
    sumOfFirstAndLastDigit (8471)
    sumOfFirstAndLastDigit (5)
    sumOfFirstAndLastDigit (99)
    # Outputs
    5
    9
    5
    18

"""


def reverse(n: int):
    reverse_string = 0
    while n > 0:
        remainder = n % 10
        reverse_string = (reverse_string * 10) + remainder
        n = n // 10
    return reverse_string


def sumOfFirstAndLastDigit(n: int):
    num = n
    last_digit = num % 10
    reverse_num = reverse(num)
    first_digit = reverse_num % 10
    sum = last_digit + first_digit
    print(f"{first_digit} + {last_digit} = ", sum)


sumOfFirstAndLastDigit(8471)
