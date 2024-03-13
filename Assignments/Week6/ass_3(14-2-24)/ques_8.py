"""
Aditi has used a text editing software to type some text. After saving
the article as WORDS.TXT, she realized that she has wrongly typed
alphabet J in place of alphabet I everywhere in the article.
Write a function definition for JTOI() in Python that would display the
corrected version of entire content of the file WORDS.TXT with all the
alphabets "J" to be displayed as an alphabet "I" on screen.
Note: Assuming that WORD.TXT does not contain any J alphabet otherwise.

"""
import os


def JTOI(path):
    try:
        file = open(path, "r")
        data = file.read()
        corrected_data = data.replace("J", "I")
        print(corrected_data)
        file.close()
        print()
    except FileNotFoundError:
        print("File not found!")


filename = "".join([os.getcwd(), "/Assignments/Week6/text.txt"])
word_count = JTOI(filename)
