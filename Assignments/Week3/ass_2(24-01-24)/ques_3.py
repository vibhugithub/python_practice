"""
        1 
      2 2 2 
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5
"""


def pattern_(n: int) -> None:
    for i in range(1, n + 1):
        for _ in range(n - i):
            print(" ", end=" ")
        for _ in range(2 * i - 1):
            print(i, end=" ")

        print()


pattern_(5)
