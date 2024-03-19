#Factorial series 5*4*3*2*1=120
'''
TC - O(n)
SC - O(n)
'''
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
v=fact(5)
print(v)