"""
    Q2. Make a function named checkPalindrome which accepts an integer n
    from the user. Return True or False if the number is palindrome or not.
    Palindrome means which is same as forward and backwards. Do not use
    STRINGS.

    # Examples
    checkPalindrome (91)
    checkPalindrome (1221)
    checkPalindrome (9854)
    checkPalindrome (123454321)
    # Output
    False
    True
    False
    True
"""


def reverse(n: int):
    last_digit = 0
    while n > 0:
        remainder = n % 10
        last_digit = (last_digit * 10) + remainder
        n = n // 10
    return last_digit


def checkPalindrome(num: int):
    reverse_string = reverse(num)
    if num == reverse_string:
        return True
    else:
        return False


x = checkPalindrome(91)
y = checkPalindrome(1221)
z = checkPalindrome(9854)
y_ = checkPalindrome(123454321)
print(x)
print(y)
print(z)
print(y_)
