'''
Reverse a string.
For example, given the input "nahan", the output should be "nahan".
'''


def reverse_str(string):
    reverse_str=""
    for char in string:
        reverse_str= char+reverse_str
        
    print(reverse_str)
    
    
input="nahan"
reverse_str(input)