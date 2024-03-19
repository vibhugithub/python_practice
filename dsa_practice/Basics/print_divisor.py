from typing import List

#bruteforce
def printDivisor(n:int)->List[int]:
    result=[]
    for i in range(1,n+1):
        if n%i==0:
            result.append(i)
    return result

#optimalway
def printdivisor(n:int)->List[int]:
    result=[]  #---- SC:  O(sq root of n)
    for i in range(1,int((n**0.5))+1):
        if n%i==0:
            result.append(i)
            if i!=n//i:
                result.append(n//i)
    result.sort()   #---- TC:  O(nlogn)
    return result
l=printdivisor(36)
print(l)

'''
TC: o(sq root of n)
SC: o(sq root of n log (sq root of n)))'''