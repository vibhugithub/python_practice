"""
* * * * * 
 * * * * 
  * * *
   * *
    *
   * *
  * * *
 * * * *
* * * * *
"""


def generate_pattern(rows):
    for i in range(rows):
        # Print spaces before stars
        print(" " * i, end="")

        # Print stars
        for j in range(rows - i):
            print("* ", end="")

        # Move to the next line
        print()

    # Generate the bottom part of the pattern
    for i in range(rows - 2, -1, -1):
        # Print spaces before stars
        print(" " * i, end="")

        # Print stars
        for j in range(rows - i):
            print("* ", end="")

        # Move to the next line
        print()


# Example usage:
generate_pattern(5)
