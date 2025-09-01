
'''
Write a function to find the first non-repeating character in a string. The function should take a string as input and return the first character that does not repeat anywhere in the string. If all characters repeat, the function should return None.'''

n='ssttrreff'
def unique_string(string):
    char={}
    for i in range(len(string)):
        char[string[i]]=char.get(string[i],0)+1

    for k,v in enumerate(string,start=1):
        if char[v]==1:
            print(v)
            
unique_string(n)