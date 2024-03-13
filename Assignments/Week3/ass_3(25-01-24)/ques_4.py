"""
    Q4. Create a function findSmallest that accepts an List of Integers and
    returns the smallest number from the list.
    my_list = 134, 11, 91, 59, 33, 221
    x = findSmallest(my_list)
    print (x)
    # Output
    11    
"""


def findSmallest(my_list):
    return min(my_list)


ll = [34, 11, 91, 59, 33, 22]
x = findSmallest(ll)
print(x)
