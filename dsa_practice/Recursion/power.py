# power -- 5**3--> 5*5*5=125

'''
    TC - O(n)
    SC - O(n)
'''

def power(b,p):
    if type(p) != int or p<0:
        raise Exception("Invalid Value") 
    if p==0:
        return 1
    if  p==1:
        return b
    return b*power(b,p-1)
p=power(5,3)
print(p)