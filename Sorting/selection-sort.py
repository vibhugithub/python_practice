"""
Selection sort
Time complexity - O(n^2)
Space complexity - O(1)
"""


def selection_sort(arr):
    n = len(arr)
    k = 1
    # Traverse through all array elements
    for i in range(0, n):
        print(f"case {k}")
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        print("min", min_idx)
        for j in range(i + 1, n):
            print(f"{arr[j]} < {arr[min_idx]}")
            if arr[j] < arr[min_idx]:
                min_idx = j
                print("min_new", min_idx)

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(f"{arr[i]} = {arr[min_idx]}, {arr[min_idx]} = {{arr[i]}} ")
        print(arr)
        k += 1


# arr = [64, 25, 12, 22, 11]
arr = [5, 2, 4, 9, 1, 3, 10]
selection_sort(arr)
print(arr)
