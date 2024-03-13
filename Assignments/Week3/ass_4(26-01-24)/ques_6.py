"""
    Q6. Write a program to remove the nth index element from a list using a
    function.

    lst = [34, 11, 91, 59, 33, 22]
    removeNth (Lst, 3)
    # Output
    [34, 11, 91, 33, 22]
    lst = 134, 11, 91, 59, 33, 223
    removeNth(lst, 67)
    # Output
    # (Do not throw error instead
    # display this if index does not exists
    Index does not exists
"""


def removeNth(l: list, n: int):
    l.pop(n)
    print(l)


lst = [34, 11, 91, 59, 33, 22]
removeNth(lst, 3)
