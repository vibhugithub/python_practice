"""
    Q8. Take 10 integer inputs from user and store them in a list. Now, copy all
    the elements in another list but in reverse order.
"""

# Take 10 integer inputs from the user
user_inputs = []
for _ in range(10):
    try:
        num = int(input("Enter an integer: "))
        user_inputs.append(num)
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Create a reversed copy of the list
reversed_list = user_inputs[::-1]

# Print the original and reversed lists
print("Original list:", user_inputs)
print("Reversed list:", reversed_list)
