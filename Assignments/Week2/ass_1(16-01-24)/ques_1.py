"""
    Q1. Write a Python function to find the Maximum and minimum of three
    numbers. Use 3 parameters. Make 2 different functions named as maxi and
    mini.
"""


def maxi(a, b, c):
    if a > b and a > c:
        print(f"{a} is maximum")
    elif b > a and b > c:
        print(f"{b} is maximum")
    elif c > a and c > b:
        print(f"{c} is maximum")


def mini(a, b, c):
    if a < b and a < c:
        print(f"{a} is minimum")
    elif b < a and b < c:
        print(f"{b} is minimum")
    elif c < a and c < b:
        print(f"{c} is minimum")


maxi(15, 45, 96)
mini(45, 52, 12)
