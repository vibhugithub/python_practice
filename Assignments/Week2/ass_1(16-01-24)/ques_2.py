"""
    Q2. Attempt the same leap year question (Week 1 - Assignment 2 - Q8) but
    using function. Try calling function with different years as a parameter and
    check the output.

"""


def leap_year(year):
    if year % 4 == 0 and year % 400 == 0 and year % 100 != 0:
        print(f"{year} is Leap year.")
    else:
        print(f"{year} is not Leap year.")


year = int(input("Enter a year: "))

leap_year(year)
