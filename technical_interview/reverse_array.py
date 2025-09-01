'''
Write a function to reverse an array in place. The function should take an array as input and modify the array to reverse its elements without using any additional arrays or lists.
'''
def reverse_arr(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1
    return arr

l = [85, 65, 75, 25, 42, 78]
k = reverse_arr(l)
print(k)   # [78, 42, 25, 75, 65, 85]
