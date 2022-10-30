def binarySearch(arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2;
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1


arr = [2, 3, 4, 10, 40]
x = 10
l = 0
r = len(arr) - 1
result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")

print("second smallest number:")


def smallest(L):
    m = L[0]
    for i in range(len(L)):
        if L[i] < m:
            m = L[i]
    return m


L = []


def second_small(L):
    m = L[0]
    for i in range(len(L)):
        if (smallest(L)) < L[i] < m:
            m = L[i]

    return m


L = [12, 13, 1, 10, 34, 1, -100, -21]
print(second_small(L))

print("ceiling of an array")
L = [1, 2, 8, 10, 10, 12, 19]
while (1):
    x = int(input("x = "))
    a = max(L)
    if x > max(L):
        print("Not possible")
        break

    for i in L:
        if i >= x:
            break

    print(i)

print("Find common element in 3 sorted arrays")

L1 = [1, 5, 10, 20, 40, 80]
L2 = [6, 7, 20, 80, 100]
L3 = [3, 4, 15, 20, 30, 70, 80, 120]
L = []
for i in L1:
    for j in L2:
        for k in L3:
            if i == j == k:
                L.append(i)

print(L)

print("Find a pair with maximum product in array of Integers")
arr = [1, 4, 3, 6, 7, 0]
max_product = arr[0] * arr[1]
for i in range(0, len(arr), +1):
    for j in range(i + 1, len(arr), +1):
        if arr[i] * arr[j] > max_product:
            max_product = arr[i] * arr[j]

print(max_product)

print("Find the largest pair sum in an unsorted array")
arr = [12, 34, 10, 6, 40]
max_sum = arr[0] + arr[1]
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] > max_sum:
            max_sum = arr[i] + arr[j]

print(max_sum)

print("Find k closest elements to a given value")

arr = [12, 16, 22, 30, 35, 39, 42, 45, 48, 50, 53, 55, 56]

X = 35
closest = arr[0]
diff = X - arr[0]
for i in range(len(arr)):
    if abs(X - arr[i]) < diff and (X - arr[i]) != 0:
        diff = abs(X - arr[i])
        closest = (arr[i])

# print(diff)
print(closest)

print("Find the element that appears once in a sorted array")


def multiple_times(arr):
    L = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                L.append(arr[i])
    return L


arr = [1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8, 34, 34, 8]

# print(multiple_times(arr))

arr = [1, 1, 3, 3, 4, 5, 5, 7, 7, 8, 8, 34, 34]
L1 = multiple_times(arr)
li_dif = [i for i in arr + L1 if i not in arr or i not in L1]
print(li_dif)
