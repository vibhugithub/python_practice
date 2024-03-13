"""
    1 2 3 4 5
    2 3 4 5
    3 4 5
    4 5
    5
"""
oi = 1
for i in range(6, 0, -1):
    for j in range(oi, 6):
        print(j, end=" ")
    oi += 1
    print()


def pattern(n: int) -> None:
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            print(j, end=" ")
        print()


pattern(5)
