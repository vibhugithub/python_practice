"""
    Q1. Create a function that takes three numbers as parameters and returns the largest among them. Also if no arguments are passed, 
    make sure the parameters take default value as None and return answer as -1.
"""


# int | None --- It means it can be an int or None
def largest_number(
    num1: int | None = None, num2: int | None = None, num3: int | None = None
) -> int:
    if num1 != None and num2 != None and num3 != None:
        if num1 > num2 and num1 > num3:
            return num1
        elif num2 > num1 and num2 > num3:
            return num2
        else:
            return num3
    else:
        return -1


largest_number(4, 5, 6)
