'''
Reverse a number.
For example, given the input 4587, the output should be 7854.
'''

def reverse_num(number):
    n=number
    rev_num=0
    while n > 0:
        rem = n% 10
        rev_num = rev_num*10+rem
        n = n//10
        # print(n)
    print(rev_num)
    
    
input=4587
reverse_num(input)