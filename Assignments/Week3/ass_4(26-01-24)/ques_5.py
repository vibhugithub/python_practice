"""
    Q5. Write a program to put all the common elements (in 2 lists) in another
    list and print it using function.
    lst1 = [34, 11, 91, 59, 33, 22]
    lst2 = [78, 14, 23]
    x = common (lst1, lst2)
    print (x)
    # Output
    []
    1st1 = 134, 11, 91, 59, 33, 22.
    Ist2 = [11, 78, 14, 23, 34]
    x = func(lst1, lst2)
    print (x)
    # Output
    [34, 11] # Order doesnt matter
"""


def func(l1, l2):
    duplicate = []
    for i in l1:
        if i in l2:
            duplicate.append(i)
    return duplicate


# lst1 = [34, 11, 91, 59, 33, 22]
# lst2 = [11, 78, 14, 23, 34]
lst1 = [34, 11, 91, 59, 33, 22]
lst2 = [78, 14, 23]
x = func(lst1, lst2)
print(x)
