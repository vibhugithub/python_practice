"""
1 
1 2 
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""


def pattern_(tt: int) -> None:
    for i in range(1, tt + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    for n in range(tt - 1, 0, -1):
        for h in range(1, n + 1):
            print(h, end=" ")
        print()


pattern_(5)


def pattern(n: int) -> None:
    for i in range(1, n // 2 + 2):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()
    for k in range(n // 2, -1, -1):
        for l in range(1, k + 1):
            print(l, end=" ")
        print()


pattern(13)
