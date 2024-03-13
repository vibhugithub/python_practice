"""
    Q4. Ask x and n from user and then calculate the following answer.
    # Example 1
    pattern (x=6,n=4)
    # Output
    6^1 - 6^3 + 6^5 - 6^7
    -272370 (OUTPUT)

    # Example 2
    pattern (x=9, n=11)
    # Output
    9^1 - 9^3 + 9^5 - 9^7 + 9^9 .... upton times
    108084611215274403609  (OUTPUT)
"""


def calculate(x: int, n: int):
    total = 1
    sum = 0
    for i in range(1, n + 1):
        # just to print pattern 9/1 + 9/3
        if i % 2 != 0:
            print(f"{x}^{total }", end=" + ")
            sum = sum + x**total
        else:
            print(f"{x}^{total }", end=" - ")
            sum = sum - x**total
        total += 2
    print()
    print(f"Total sum {sum}")


calculate(9, 11)
calculate(6, 4)
