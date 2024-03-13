"""
5 
4 5 
3 4 5
2 3 4 5
1 2 3 4 5
2 3 4 5
3 4 5
4 5
5
"""

for i in range(1, 6):
    for j in range(6 - i, 6):
        print(j, end=" ")
    print()
for n in range(4, 0, -1):
    for h in range(6 - n, 6):
        print(h, end=" ")
    print()


def pattern(n: int) -> None:
    for i in range(n // 2 + 1, 0, -1):
        for j in range(i, n // 2 + 2):
            print(j, end=" ")
        print()
    for i in range(2, n // 2 + 2):
        for j in range(i, n // 2 + 2):
            print(j, end=" ")
        print()


pattern(13)
