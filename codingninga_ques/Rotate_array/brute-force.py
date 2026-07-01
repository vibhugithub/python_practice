def rotateArray(arr, n: int):
    # Write your code from here.
    l = []
    for j in range(n):
        for i in range(len(arr)):
            if i == 0:
                temp = arr[0]

            else:
                l.append(arr[i])
        l.append(temp)
        arr = l
        print(arr)


a = 3
arr = [1, 2, 3, 4, 5, 6, 7]
rotateArray(arr, a)
