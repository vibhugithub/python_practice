"""
Q1. Write a Python function that takes two numbers as input and returns
the result of their division. Handle the ZeroDivisionError exception if the
second number is zero. If there is ZeroDivisionError, the function should
return -1
"""


def division(n1, n2):
    try:
        return n1 / n2
    except ZeroDivisionError:
        return -1


num1 = float(input("Enter the first number = "))
num2 = float(input("Enter the second number = "))

result = division(num1, num2)

if result != -1:
    print(f"Result = {result}")
else:
    print("Cannot carry out the division.")


import traceback

try:
    v = "s" + 5
# except:
#     raise RuntimeError("unable to handle error")
except TypeError:
    print("An exception flew by!")
    raise
