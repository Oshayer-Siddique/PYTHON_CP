##All distinct subset of a given set
subarrays = []


def distinct_subsets(array, n, out):
    global subarrays
    if n < 0:
        subarrays.append(out[:])
        return
    out.append(array[n])
    distinct_subsets(array, n - 1, out)
    out.pop()
    distinct_subsets(array, n - 1, out)


array = [1, 2, 3]
distinct_subsets(array, len(array) - 1, [])
print(subarrays)

from collections import deque


# Recursive function to print all distinct subsets of S
# S   --> input set
# out --> list to store subset
# i   --> index of next element in set S to be processed
def findPowerSet(S, out, i):
    # if all elements are processed, print the current subset
    if i < 0:
        print(list(out))
        return

    # include current element in the current subset and recur
    out.append(S[i])
    findPowerSet(S, out, i - 1)

    # exclude current element in the current subset
    out.pop()  # backtrack

    # remove adjacent duplicate elements
    while i > 0 and S[i] == S[i - 1]:
        i = i - 1

    # exclude current element in the current subset and recur
    findPowerSet(S, out, i - 1)


# Program to generate all distinct subsets of given set
if __name__ == '__main__':
    S = [1, 3, 1]

    # sort the set
    S.sort()

    # create an empty list to store elements of a subset
    out = deque()
    findPowerSet(S, out, len(S) - 1)

print("subset generate")


def subset_generate(S, temp, i):
    if i < 0:
        print(list(temp))
        return
    temp.append(S[i])
    subset_generate(S, temp, i - 1)

    temp.pop()
    subset_generate(S, temp, i - 1)


S = [1, 2, 3]
temp = []
print(subset_generate(S, temp, len(S) - 1))

print("subset generate another way")


def subset_generate(S, temp, i):
    if i > len(S) - 1:
        print(list(temp))
        return
    temp.append(S[i])
    subset_generate(S, temp, i + 1)

    temp.pop()
    subset_generate(S, temp, i + 1)


S = [1, 2, 3]
temp = []
i = 0
print(subset_generate(S, temp, i))

print("subset generate with duplicates")


def subset_generate(S, temp, i):
    if i < 0:
        print(list(temp))
        return
    temp.append(S[i])
    subset_generate(S, temp, i - 1)

    while i > 0 and S[i] == S[i - 1]:
        i = i - 1

    temp.pop()
    subset_generate(S, temp, i - 1)


S = [1, 2, 3, 4, 6, 7, 2]
S.sort()
temp = []
print(subset_generate(S, temp, len(S) - 1))

print("subset generate another way with duplicates")


def subset_generate(S, temp, i):
    if i > len(S) - 1:
        print(list(temp))
        return
    temp.append(S[i])
    subset_generate(S, temp, i + 1)

    while i < len(S) - 1 and S[i] == S[i + 1]:
        i = i + 1

    temp.pop()
    subset_generate(S, temp, i + 1)


S = [1, 2, 1]
S.sort()
temp = []
i = 0
print(subset_generate(S, temp, i))




print(" definite Combination of list element")


def combi(L, temp, i):
    if i > len(L) - 1:
        if len(temp) > 3:
            return None
        elif len(temp) == 1 or len(temp) == 0 or len(temp) == 2:
            return None
        print(list(temp))
        return
    else:
        temp.append(L[i])
        combi(L, temp, i + 1)

        temp.pop()
        combi(L, temp, i + 1)


L = [1, 2, 3, 4]
L.sort()
i = 0
temp = []
print(combi(L, temp, i))

print(" definite Combination of list element")


def combi(arr, temp, i, k):
    if i > len(arr) - 1:
        if len(temp) == k:
            print(list(temp))

        return

    else:
        temp.append(arr[i])
        combi(arr, temp, i + 1, k)

        temp.pop()
        combi(arr, temp, i + 1, k)


if __name__ == '__main__':
    arr = [1, 2, 3, 4]
    k = int(input("k = "))
    temp = []
    i = 0
    print(combi(arr, temp, i, k))

