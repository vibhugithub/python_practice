"""
    Q1. 2 22 222 2222 22222 ... upto n
"""


def pattern2(n: int):
    i = 1
    num = 2
    while i <= n:
        print(num, end=" ")
        num = num * 10 + 2
        i += 1
    print()


pattern2(7)
