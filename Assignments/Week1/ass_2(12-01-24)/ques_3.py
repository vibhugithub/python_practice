"""
    Q3. Write a program to check if number is divisible by 2 and 3 but not 8.
"""
num = int(input("Enter number: "))


if (num % 2 == 0) and (num % 3 == 0) and (num % 8 != 0):
    print(f"Yayy!!! {num:} divisible by 2 and 3 but not 8")
else:
    print(f"{num} not divisible by 2 and 3 but not 8")
