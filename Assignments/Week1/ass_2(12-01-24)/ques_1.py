"""
    Q1. Write a program that takes two numbers as input and checks if the first
    number is divisible by the second.
    
"""
print("To Check first number is divisible by the second")
print()
num1: int = int(input("Enter First Number: "))
num2: int = int(input("Enter Second Number: "))

if num1 % num2 == 0:
    print(f"First Number {num1} divisible by {num2}")
else:
    print(f"First Number {num1} not divisible by {num2}")
