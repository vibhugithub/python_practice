"""
Q6. Write a Python program to generate two strings from a given string. For
the first string, use the characters that occur only once, and for the
second, use the characters that occur multiple times in the said string.
Input: aabbcceffgh
Output
string1 = egh
string2 = abcf
Input: heello
Output
string1 = ho
string2 = el
"""


def generateStrings(input_string):

    char_freq = {}
    for ch in input_string:
        char_freq[ch] = char_freq.get(ch, 0) + 1
    # Part 1 contains single occurrence characters
    part1 = [key for (key, count) in char_freq.items() if count == 1]

    # Part 2 contains multiple occurrence characters
    part2 = [key for (key, count) in char_freq.items() if count > 1]

    return part1, part2


input = "heello"

s1, s2 = generateStrings(input)

print("".join(s1))
print("".join(s2))
