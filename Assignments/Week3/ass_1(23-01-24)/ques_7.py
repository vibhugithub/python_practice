"""
    5 4 3 2 1
    4 3 2 1
    3 2 1
    2 1
    1
"""
oi = 0
for i in range(1, 6):
    for j in range(5 - oi, 0, -1):
        print(j, end=" ")
    oi += 1
    print()


def pattern(n: int) -> None:
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


pattern(5)
