"""
    Q1. There are two variables.
    a=5
    b=10
    What will be the output of following:
    Q2. Python program to convert kilometers to miles. Ask kilometer from
    User.

"""

a = 5
b = 10

# 1 kilometer equals 0.62137 miles.

user_input = float(input("Enter Kilometer to convert into miles: "))
conversion = user_input * 0.6
print(f"{user_input} kilometer conversion value into miles {conversion}")
