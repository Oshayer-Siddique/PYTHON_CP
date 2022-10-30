t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    arr.sort()
    stor = []
    unique = []
    for i in range(n-1):
        if arr[i] == arr[i+1]:
            stor.append(arr[i+1])

#print(stor)
    stor.sort()

    for x in arr:
        if x not in unique:
            unique.append(x)

#print(unique)
    ans = unique+stor
    print(*ans,sep=" ")
    t = t-1