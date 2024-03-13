"""
    Q8. Ask a number from user. Print if the number is ODD or EVEN.
"""

# user_input: int = int(input("Enter value to check odd or even: "))
user_input: int = 5

if user_input % 2 == 0:
    print("The number is even")
else:
    print("The provided number is odd")
