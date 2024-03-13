"""
    Q3. Make a function named printWords which accepts an integer n from
    the user. Print the number as words

    # Examples
    printWords (91)
    printWords (1221)
    printWords (9854)
    printWords (1001)
    # Output
    Nine One
    One Two Two One
    Nine Eight Five Four
    One Zero Zero One
"""


def integerword(remainder):
    if remainder == 1:
        print("One", end=" ")
    elif remainder == 2:
        print("Two", end=" ")
    elif remainder == 3:
        print("Three", end=" ")
    elif remainder == 4:
        print("Four", end=" ")
    elif remainder == 5:
        print("Five", end=" ")
    elif remainder == 6:
        print("Six", end=" ")
    elif remainder == 7:
        print("Seven", end=" ")
    elif remainder == 8:
        print("Eight", end=" ")
    elif remainder == 9:
        print("Nine", end=" ")


def printWords(n: int):
    while n > 0:
        remainder = n % 10
        n = n // 10
        integerword(remainder)


printWords(1221)
