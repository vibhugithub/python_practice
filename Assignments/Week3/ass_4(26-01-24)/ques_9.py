"""
    Q9. Make a list. Write a simple program for addition of the 2nd element
    from start and 2nd element from the end.

"""

# Create a list
my_list = [10, 20, 30, 40, 50]

# Check if the list has at least 2 elements
if len(my_list) >= 2:
    # print(my_list[1], my_list[-2])
    result = my_list[1] + my_list[-2]

    # Print the result
    print(f"Sum of the 2nd element from start and 2nd element from end: {result}")
else:
    print("List should have at least 2 elements for this operation.")
