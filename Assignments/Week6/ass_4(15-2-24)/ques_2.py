"""
    Q2. There is a file named numbers.txt and the content is given below.
Content (numbers.txt)
34
67
98
11
-87
100
Create another file named numbers_result.txt. It should have the following
content in it based on numbers.txt.
34 Even
67 Odd
98 Even
"""


def numbersOddEven(input_file: str, output_file: str):
    try:
        with open(input_file, "r") as file_in:
            with open(output_file, "w") as file_out:
                for line in file_in:
                    number = int(line.strip())
                    if number % 2 == 0:
                        file_out.write(f"{number} Even\n")
                    else:
                        file_out.write(f"{number} Odd\n")
        print(f"Content written to '{output_file}' successfully.")
    except FileNotFoundError:
        print("Error: One or both files not found.")
    except IOError:
        print("Error: An I/O error occurred.")


numbersOddEven("numbers.txt", "numbers_result.txt")
