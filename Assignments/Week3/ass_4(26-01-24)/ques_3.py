"""
    Q3. Write a Python function that takes two lists and returns True if they
    have at least one common element.

    lst1 = [34, 11, 91, 59, 33, 221
    15t2 = [78, 14, 23]
    x = func(lst1, lst2)
    print (x)
    # Output
    False
    Lst1 = 134, 11, 91, 59, 33, 221
    Lst2 = 178, 14, 23, 341
    x = func (lst1, lst2)
    print (x)
    # Output
    True
"""


def func(l1, l2):
    for i in l1:
        if i in l2:
            return True


lst1 = [34, 11, 91, 59, 33, 22]
lst2 = [78, 14, 23, 11]
x = func(lst1, lst2)
print(x)
