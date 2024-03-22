from math import *


def reverseArray(arr, m):
    # Write your code here.
    first_arr = arr[: m + 1]
    last_arr = arr[m + 1 :]
    reverse_array = last_arr[::-1]
    final = first_arr + reverse_array
    return final


arr = [1, 2, 3, 4, 6, 5]
h = reverseArray(arr, 3)
print(h)
