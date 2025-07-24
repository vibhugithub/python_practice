'''
A pangram is a sentence that contains every letter of the alphabet at least once.
For example, "The quick brown fox jumps over the lazy dog" is a pangram.
'''

def alphabets(string):
    alpha=set('abcdefghijklmnopqrstuvwxyz')
    return set(string.lower()) >= alpha

def check_pangram(string_list):
    for s in string_list:
        if alphabets(s):
            print(f"This statement `{s}` is pangram")
        else:
            print(f"This statement `{s}` is not pangram")


s=["pack my box with five dozen liquor jugs","this is not a pangram"]
check_pangram(s)