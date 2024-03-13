"""
    Q6. Ask 4 numbers from user. Make sure all the numbers entered by user
    are different. Print which number is the smallest.
"""
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
num4 = int(input("Enter fourth number: "))

list_num = [num1, num2, num3, num4]
list_num.sort()

print(list_num[0])

# Another way

# Initialize the smallest_number variable with the first number
smallest_number = num1
# Check and update if the second number is smaller
if num2 < smallest_number:
    smallest_number = num2
# Check and update if the third number is smaller
if num3 < smallest_number:
    smallest_number = num3
# Check and update if the fourth number is smaller
if num4 < smallest_number:
    smallest_number = num4
print(f"The smallest number is: {smallest_number}")
