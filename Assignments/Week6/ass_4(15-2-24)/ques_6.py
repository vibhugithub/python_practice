"""Q6. There is a file having sentences in it. Create a new file result.txt having
the same sentence as it is but also number of vowels written beside each
line.
Original file (Content)
python is great
we are doing dsa
HELLLLLOOO
Output (result.txt)
python is great 4
we are doing dsa 6
HELLLLLOOO 4



"""


def countVowels(sentence: str) -> int:
    vowels = "aeiouAEIOU"
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count


def addVowelCount(input_file: str, output_file: str) -> None:
    try:
        with open(input_file, "r") as file_in:
            lines = file_in.readlines()

        with open(output_file, "w") as file_out:
            for line in lines:
                line = line.strip()
                vowel_count = countVowels(line)
                file_out.write(f"{line} {vowel_count}\n")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except IOError:
        print("Error: An I/O error occurred.")


addVowelCount("input.txt", "result.txt")
