"""
    Q5. Print the following pattern.
    * * * * * 
     * * * * 
      * * *
       * *
        *
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


# Example usage:
generate_pattern(5)
