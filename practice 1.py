print("merge sort algoritm")
def mergesort(list):
    if len(list)>1:
        mid = len(list)//2
        left_list = list[:mid]
        right_list = list[mid:]
        mergesort(left_list)
        mergesort(right_list)
        i = 0
        j = 0
        k = 0

        while i<len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                list[k] = left_list[i]
                i = i+1
                k = k+1
            else:
                list[k] = right_list[j]
                j = j+1
                k = k+1


        while i<len(left_list):
            list[k] = left_list[i]
            i = i+1
            k = k+1
        while j < len(right_list):
            list[k] = right_list[j]
            j = j+1
            k = k+1

list = [int(input()) for x in range(6)]
mergesort(list)
print(list)



print("bubble sort algorithm")
List = [int(input()) for x in range (6)]
for i in range(len(List) - 1):
    for j in range(len(List) -1):
        if List[j] > List[j+1]:
            List[j] ,List[j+1] = List[j+1] ,List[j]

print(List)


print("selection sort assending")
list = [5,4,23,2,-8,444]
for i in range(len(list)):
    min_val = min(list[i:])
    min_index = list.index(min_val,i)
    list[i],list[min_index] = list[min_index],list[i]

print(list)

print("selection sort desending")
list = [6,5,78,6,4,3,-1,444]
for i in range(len(list)):
    max_val = max(list[i:])
    max_index = list.index(max_val,i)
    list[i] ,list[max_index] = list[max_index] ,list[i]

print(list)

print("selection sort another way")
def selection_sort(L):
    n = len(L)
    for i in range(0,n):
        index_min = i
        for j in range(i+1,n):
            if L[j] < L[index_min]:
                index_min = j
        if index_min != i:
            L[i] , L[index_min] = L[index_min],L[i]

L = [5,4,3,5,76,7]
selection_sort(L)
print(L)

print("binary search")
def binary_search(L,x):
    n = len(L)
    low = 0
    high = n-1
    while low<=high:
        mid = (low+high)//2

        if L[mid] == x:
            return mid
        if L[mid]<= x:
            low = mid+1
        else:
            high = mid-1

L = [1,2,3,4,5,7,8]
x = 5
print(binary_search(L,x))

print("interpolition search")
# pos = l +((x-L[0])*(h-l))//(L[h]-L[l])
def interpolition_search(L,x):
    n = len(L)
    l = 0
    h = n-1
    while l<h:
        pos = l +((x-L[0])*(h-l))//(L[h]-L[l])

        if L[pos] == x:
            return pos
        if L[pos]<=x:
            low = pos + 1
        else:
            high = pos - 1


L = [1,5,7,8,9,11,13,15]
x = 9
print(interpolition_search(L,x))


print("Quick Sort")


L = [1,2,3,4,5,55,666,5]
L.sort()
print(L)
L.reverse()
print(L)
L.append(100)
print(L)
L.remove(666)
print(L)

print("matrishoka dolls UVA live 6839")
def dolls(L):
    n = len(L)
    for i in range(n):
        for j in range(i+1,n):
            if L[i] == L[j]:
                return L[i]

L = [1,2,3,4,5,6,7,8,8,7]
print(dolls(L))
