n = int(input())
arr = list(map(int,input().strip().split()))[:n]

arr.sort()
if n % 2 == 0:
    stor1 = []
    stor2 = []
    for i in range(n):
        if i % 2 == 0:
            stor1.append(arr[i])
        else:
            stor2.append(arr[i])
    stor2.reverse()
    res = stor1 + stor2
elif n % 2 == 1:
    stor3 = []
    stor4 = []
    for j in range(n-1):
        if j % 2 == 0:
            stor3.append(arr[j])
        else:
            stor4.append(arr[j])
    stor4.reverse()
    res = stor3  + stor4
    res.insert((n//2),arr[n-1])

print(*res,sep=" ")