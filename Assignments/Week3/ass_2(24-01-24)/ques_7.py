"""
        1 
      1 2 3 
    1 2 3 4 5
  1 2 3 4 5 6 7
1 2 3 4 5 6 7 8 9
  1 2 3 4 5 6 7
    1 2 3 4 5
      1 2 3
        1
"""

for i in range(1, 6):
    for j in range(5 - i):
        print(" ", end=" ")
    for k in range(1, 2 * i):
        print(k, end=" ")
    print()
for n in range(4, 0, -1):
    for h in range(5 - n):
        print(" ", end=" ")
    for l in range(1, 2 * n):
        print(l, end=" ")
    print()


def pattern(n: int) -> None:
    for i in range(1, n // 2 + 2):
        for j in range(n // 2 - i + 1):
            print(" ", end=" ")
        for k in range(1, 2 * i):
            print(k, end=" ")
        print()
    for i in range(n // 2, -1, -1):
        for j in range(n // 2 - i + 1):
            print(" ", end=" ")
        for k in range(1, 2 * i):
            print(k, end=" ")
        print()


pattern(7)
