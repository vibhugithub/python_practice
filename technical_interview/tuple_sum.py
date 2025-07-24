'''
Given a list of integers, find two numbers that add up to a specific target sum.
For example, given the input list [2, 3, 4, 5]
and target sum 8, the output should be (3, 5).
'''


def tuple_sum(lst,target_sum):
    seen=set()
    for n in lst:
        num = target_sum - n
        if num in seen:
            return (num,n)
        seen.add(n)
k = tuple_sum([2,3,4,5],8)
print(k)