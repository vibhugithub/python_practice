"""
    1
    2 3
    4 5 6
    7 8 9 10
    11 12 13 14 15
"""
oi = 1
for i in range(1, 6):
    for j in range(0, i):
        print(oi, end=" ")
        oi += 1
    print()


def pattern(n: int) -> None:
    count = 1
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(count, end=" ")
            count += 1
        print()


pattern(5)
