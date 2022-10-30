print("permutaion by backtracking")


def perm(list):
    if len(list) == 0:
        return []
    elif len(list) == 1:
        return [list]
    else:
        l = []
        for i in range(len(list)):
            x = list[i]
            xs = list[:i] + list[i + 1:]
            for p in perm(xs):
                l.append([x] + p)
        return l


list = [1, 2, 3]
for p in perm(list):
    print(p)
print("Permutation")


def tostring(List):
    return ''.join(List)


def permute(a, first, last):
    if first == last:
        print(tostring(a))
    else:
        for i in range(first, last + 1):
            a[first], a[i] = a[i], a[first]
            permute(a, first + 1, last)
            a[first], a[i] = a[i], a[first]


string = '321'
a = list(string)
first = 0
last = len(string) - 1
permute(a, first, last)

print("permutations")


def permutations(L, l, h):
    if l == h:
        print(L)
    else:
        for i in range(l, h, +1):
            L[l], L[i] = L[i], L[l]
            permutations(L, l + 1, h)
            L[l], L[i] = L[i], L[l]


L = [1, 2, 3]
l = 0
h = len(L)
print(permutations(L, l, h))


print("permutatons")
def permute(arr,l,h):
    if l == h:
        print(arr)
    else:
        for i in range(l,h+1):
            arr[l],arr[i] = arr[i],arr[l]
            permute(arr,l+1,h)
            arr[l],arr[i] = arr[i],arr[l]
arr = [1,2,3]
l = 0
h = len(arr)-1
permute(arr,l,h)
