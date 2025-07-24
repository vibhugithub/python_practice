'''
Given a string, reverse the order of the alphabetic characters while keeping the non-alphabetic characters in their original positions.
For example, given the input "a1b2cx34y", the output should be "y1x2cb34a".
'''

def reverse_string(string):
    char=[i for i in string if i.isalpha()]
    char.reverse()
    
    i=0
    new_l=[]
    for j in string:
        if j.isalpha():
            new_l.append(char[i])
            i+=1
        else:
            new_l.append(j)
    out = ''.join(new_l)
    print(out)
    
input="a1b2cx34y"
reverse_string(input)