"""
        1 
      2 2 2 
    3 3 3 3 3
  4 4 4 4 4 4 4
5 5 5 5 5 5 5 5 5
  4 4 4 4 4 4 4
    3 3 3 3 3
      2 2 2
        1
"""


def pattern_(input: int) -> None:
    for i in range(1, input + 1):
        for j in range(input - i):
            print(" ", end=" ")
        for k in range(2 * i - 1):
            print(i, end=" ")

        print()
    for n in range(input - 1, 0, -1):
        for h in range(input, n, -1):
            print(" ", end=" ")
        for t in range(2 * n - 1):
            print(n, end=" ")
        print()


pattern_(5)


def pattern(n: int) -> None:
    for i in range(1, n // 2 + 2):
        for j in range(n // 2 - i + 1):
            print(" ", end=" ")
        for k in range(2 * i - 1):
            print(i, end=" ")
        print()
    for i in range(n // 2, -1, -1):
        for j in range(n // 2 - i + 1):
            print(" ", end=" ")
        for k in range(2 * i - 1):
            print(i, end=" ")
        print()


pattern(13)
