"""
    Q7. Check if the number entered by User is divisible by 3 or not.
"""

user_input = int(input("Enter value to check is number is divisible or not: "))

if user_input % 3 == 0:
    print(f"{user_input} Values is divisible by 3")
else:
    print(f"{user_input} Values is NOT divisible by 3")
