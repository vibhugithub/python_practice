"""
* * * * 
  * * * * 
    * * * *
      * * * *
"""


def generate_diagonal_pattern(rows):
    for i in range(rows):
        # Print spaces before stars
        print("  " * i, end="")

        # Print stars
        for j in range(rows):
            print("* ", end="")

        # Move to the next line
        print()


# Example usage:
generate_diagonal_pattern(4)
