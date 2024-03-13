"""
    Q4. Write a Python Program to find sum and average of List in Python.
"""


def sum_avg(l):
    list_len = len(l)
    sum = 0
    for i in l:
        sum = sum + i
    avg = sum / list_len
    print(f"Sum = {sum}")
    print(f"Average = {avg}")


lst2 = [78, 14, 23, 11]
sum_avg(lst2)
