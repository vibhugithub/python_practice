def totaPlrime(s, e):
    r = []
    for i in range(s, e + 1):
        prime = 0
        for j in range(1, i + 1):
            print(f"{i} , {j}---> {i%j}")
            if i % j == 0:
                prime += 1
        if prime == 2:
            r.append(i)
    print(r)


totaPlrime(2, 10)


def search(arr, target):
    # Write your code here.
    n = len(arr)

    # Iterate through the array

    for i in range(n):

        # target is found at ith index

        if arr[i] == target:

            return i

    # target not found

    return -1


def read(n: int, book: list, target: int):
    # Write your code here.
    pages_set = set()

    for pages in book:
        remaining_pages = target - pages
        if remaining_pages in pages_set:
            return "YES"
        pages_set.add(pages)

    return "NO"


n = 5
target = 5
book = [4, 1, 2, 3, 1]
j = read(n, book, target)
print(j)


def missingNumber(arr, n):
    # Write your code here
    # Return a single integer
    low = 0
    high = len(arr) - 1
    diff = (arr[high] - arr[low]) // len(arr)

    while low < high:
        mid = low + (high - low) // 2
        expected_element = arr[0] + mid * diff

        if arr[mid] == expected_element:
            low = mid + 1
        else:
            high = mid

    missing_element = arr[low] - diff
    if arr[low] == expected_element:
        arr.insert(low, missing_element)
    else:
        arr.insert(low + 1, missing_element)
    print(arr)


a = [1, 4, 10]
k = missingNumber(a, 3)


def divide(X, Y, N):
    sign = "-" if X * Y < 0 else ""

    # Calculate the integer part
    integer_part = str(abs(X) // abs(Y))

    # Calculate the fractional part
    remainder = abs(X) % abs(Y)
    fractional_part = ""
    for _ in range(N):
        remainder *= 10
        fractional_part += str(remainder // abs(Y))
        remainder %= abs(Y)

    # Construct the final result
    result = sign + integer_part + "." + fractional_part
    return result


# Test cases
test_cases = [
    (1, -5, 6),
    (-1, 1000, 2),
    (1, -5, 6),
    (-1, 1000, 2),
]

for X, Y, N in test_cases:
    print(divide(X, Y, N))


def getFloorAndCeil(a, n, x):
    # Write your code here.
    floor = -1
    ceil = -1
    low = 0
    high = n
    while low <= high:
        mid = (low + high) // 2
        if a[mid] == x:
            return a[mid], a[mid]
        elif a[mid] > x:
            ceil = a[mid]
            high = mid - 1
        else:
            floor = a[mid]
            low = mid + 1
        print(low, high)
    return floor, ceil


getFloorAndCeil([23], 1, 2)


# -----------------------------------
def twoSum(arr, target, n):
    # Write your code here.
    two_sum = set()

    pairs = []
    i = 0
    j = i + 1
    for i in range(len(arr)):
        j = (i + 1) % n
        print("i", i)
        print("J", j)

    return pairs


n1 = [2, 7, 11, 13]
n2 = [1, -1, -1, 2, 2]
twoSum(n1, target, n)


from collections import deque
from collections import defaultdict

n = 4
edges = [[1, 0], [1, 2], [1, 3]]

# Build graph using adjacency list
graph = defaultdict(list)
print("graph", graph)
degrees = [0] * n
print("degrees", degrees)

for u, v in edges:
    graph[u].append(v)
    print("graph u", graph)
    graph[v].append(u)
    print("graph v", graph)
    degrees[u] += 1
    print("degrees u", degrees)
    degrees[v] += 1
    print("degrees v", degrees)

# Initialize queue with leaf nodes (degree == 1)
queue = deque()
for i in range(n):
    if degrees[i] == 1:
        queue.append(i)
        print(queue)
