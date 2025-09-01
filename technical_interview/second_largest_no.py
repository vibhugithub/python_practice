
'''
Find the second largest and second smallest numbers in a list.
For example, given the input list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], the output should be (2, 9).'''

def second_largest_no(lst):
    s_smallest = float('inf')
    s_largest = float('-inf')   
    small = float('inf')
    largest = float('-inf')

    for i in range(0,len(lst)):
        if lst[i]< small:
            s_smallest = small
            small = lst[i]
        elif lst[i] < s_smallest and lst[i] != small:
            s_smallest = lst[i]

        if lst[i] > largest:
            s_largest = largest
            largest = lst[i]        
        elif lst[i] > s_largest and lst[i] != largest:
            s_largest = lst[i]
    print(f"smallest: {small}, second smallest: {s_smallest}")
    print(f"largest: {largest}, second largest: {s_largest}")

    return s_smallest, s_largest
second_largest_no([1,2,3,4,5,6,7,8,9,10])