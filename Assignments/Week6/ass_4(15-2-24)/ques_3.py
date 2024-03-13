"""
Q3. Create a function named multiplication which takes 2 parameter which
are filename and a number. Write the multiplication table of that number in that filename.
Content in filename after running the code, lets suppose number = 5.
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
...
5 x 10 = 50

"""


def multiplication(filename: str, number: int) -> None:
    try:
        with open(filename, "w") as file:
            for i in range(1, 11):
                result = number * i
                file.write(f"{number} x {i} = {result}\n")
        print(
            f"Multiplication table of {number} is written to '{filename}' successfully."
        )
    except IOError:
        print("Error: An I/O error occurred.")


multiplication("multiplication_table.txt", 5)
