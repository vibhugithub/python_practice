"""
Q7. There is a file (any random file) having sentences in it. Create a new file
result.txt having each sentence in a reverse order.
Original file (Content)
python is great
we are doing dsa
HELLLLLOOO
Output (result.txt)
HELLLLLOOO
we are doing dsa
python is great
"""


def reverseLines(input_file: str, output_file: str) -> None:
    try:
        with open(input_file, "r") as file_in:
            lines = file_in.readlines()

        with open(output_file, "w") as file_out:
            for line in lines:
                line = line.strip()
                reversed_line = line[::-1]
                file_out.write(reversed_line + "\n")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except IOError:
        print("Error: An I/O error occurred.")


reverseLines("input.txt", "result.txt")
