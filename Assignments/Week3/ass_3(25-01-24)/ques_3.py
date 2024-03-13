"""
    Q3. Create a function findLargest that accepts an List of Integers and
    returns the largest number from the list.
    my_list = [34, 11, 91, 59, 33, 221
    x = findLargest (my_list)
    # Output
    91
"""


def findLargest(my_list):
    return max(my_list)


ll = [34, 11, 91, 59, 33, 22]
x = findLargest(ll)
print(x)
