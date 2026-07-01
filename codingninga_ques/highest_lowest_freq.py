"""
    https://www.codingninjas.com/studio/problems/k-most-occurrent-numbers_625382?leftPanelTabValue=PROBLEM
"""

from typing import List


def getFrequencies(v: List[int]) -> List[int]:
    # initialize dict to get count
    fre_dict = {}
    for i in v:
        fre_dict[i] = fre_dict.get(i, 0) + 1

    # initialize list to get min max value of key value of dict
    max_ele_list, min_ele_list = [], []
    result = []

    for k, v in fre_dict.items():
        if v == max(fre_dict.values()):
            max_ele_list.append(k)
        if v == min(fre_dict.values()):
            min_ele_list.append(k)

    result = [min(max_ele_list), min(min_ele_list)]
    return result


k = [1, 2, 3, 1, 1, 4]
p = [10, 10, 10, 3, 3, 3]

h = getFrequencies(k)
f = getFrequencies(p)
