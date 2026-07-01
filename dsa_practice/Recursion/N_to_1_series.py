'''
TC - O(n)
SC - O(n)
'''
#without backtracking
print("without backtracking")
def func1(n):
    if n<1:
        return
    print(n)
    func1(n-1)

func1(3)

#with backtracking
print("with backtracking")
def func2(i,n):
    if i>n:
        return
    func2(i+1,n)
    print(i)

func2(1,3)