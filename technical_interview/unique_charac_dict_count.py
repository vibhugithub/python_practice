'''
given a string, count the occurrence of each character in it and return a dictionary with characters as keys and their counts as values.
'''

def unique_char(string):
    unique={}
    for i in string.strip().lower():
        unique[i] = unique.get(i,0)+1
        
    print(unique)
        

s="geeksgeeks"
unique_char(s)