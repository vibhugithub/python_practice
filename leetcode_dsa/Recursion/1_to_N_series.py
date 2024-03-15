'''
TC - O(n)
SC - O(n)
'''

#without backtracking 
print("without backtracking")
def func1(i,n):
    if i>n:
        return
    print(i)
    func1(i+1,n)

func1(1,3)



# with backtracking
print("with backtracking")
def func2(i,n):
    if i<1:
        return
    func2(i-1,n)
    print(i)

func2(3,3)