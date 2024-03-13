"""
        5 
      5 4 
    5 4 3
  5 4 3 2
5 4 3 2 1
"""


def pattern_(n: int) -> None:
    for i in range(1, n + 1):
        for _ in range(n - i):
            print(" ", end=" ")
        for k in range(5, 5 - i, -1):
            print(k, end=" ")
        print()


pattern_(5)


def pattern(n: int) -> None:
    for i in range(n, 0, -1):
        for j in range(i - 1):
            print(" ", end=" ")
        for k in range(n, i - 1, -1):
            print(k, end=" ")
        print()


pattern(9)
