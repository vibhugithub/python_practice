# 0 1 1 2 3 5 8 13
"""
    0+1=1
    1+1=2
    2+1=3
    3+2=5
    5+3=8
    8+5=13
    
TC - O(n)
SC - O(n)
"""


def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fib(n - 1) + fib(n - 2)


f = fib(5)
print(f)
