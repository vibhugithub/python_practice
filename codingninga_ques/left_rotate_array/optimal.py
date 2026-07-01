from sys import *
from collections import *
from math import *

"""
Time Complexity = O(n), n is number of elements in array
Space Complexity = O(1)

This code is actually similar to Brute force one
"""


def rotateArray(arr: [], n: int) -> []:
    temp = arr[0]  # storing the first element of the array in a variable
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp  # assign the value of the variable at the last index
    return arr


"""
T.c - O(n)
sc - o(n)
"""


def rotateArray_(arr, n: int):
    # Write your code from here.
    l = []
    for i in range(len(arr)):
        if i == 0:
            temp = arr[0]

        else:
            l.append(arr[i])
    l.append(temp)
    print(l)


a = 5
arr = [1, 2, 3, 4, 5]
rotateArray_(arr, a)
