"""
    Q4. Don’t create a function, just print the following pattern
1 11 111 1111 11111....n times
1 11 101 1001 10001 100001 1000001 ..n times
"""


def pattern2(n: int):
    i = 1
    num = 1
    while n >= i:
        print(num, end=" ")
        num = num + 10**i
        i += 1
    print()


pattern2(7)


def pattern(n: int):
    i = 1
    num = 1
    while n >= i:
        print(num, end=" ")
        num = 10**i + 1
        i += 1


pattern(7)
