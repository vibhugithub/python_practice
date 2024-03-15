'''
    2 type of method
    Parameterized  --> NO return statement
    Functional     --> YES return statement

    1+2+3+4+5=15
'''
'''
    TC - O(n)
    SC - O(n)
'''
#Parameterized
print("Parameterized")
def func1(i,sum):
    if i<1:
        print(sum)
        return
    func1(i-1,sum+i)
func1(5,0)

#Functional
print("Functional")
def add(n):
    if n==1:
        return 1
    return n+add(n-1)

n=add(5)
print(n)
