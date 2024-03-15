# Count Frequency in a range
"""
    https://www.codingninjas.com/studio/problems/count-frequency-in-a-range_8365446?leftPanelTabValue=PROBLEM
"""
from typing import *


def countFrequency(n: int, m: int, edges: List[List[int]]):
    # create list with value 0 upto n
    freq_arr = [0] * n
    # iterate with list of element to get count of less than equal to n
    for i in edges:
        if i <= n:
            freq_arr[i - 1] += 1

    return freq_arr


n = 10
x = 14
arr = [11, 14, 8, 3, 12, 14, 1, 7, 4, 3]
f = countFrequency(n, x, arr)
print(f)
