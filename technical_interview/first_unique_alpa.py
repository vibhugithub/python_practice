'''
given a string consisting of lowercase letters, find the first non-repeating character in it.
If there is no such character, return -1.
'''

def first_unique_char(string):
    unique={}
    for i in string.strip().lower():
        unique[i] = unique.get(i,0)+1
        
    for i,char in enumerate(string,start=1):
        if unique[char]==1:
            print(f"index: {i} char: {char} ")
    return -1
        

s="geeksgeeks"
first_unique_char(s)