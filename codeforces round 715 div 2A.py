t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    odd = []
    even = []
    final = []
    for i in range(n):
        if arr[i] % 2 == 1:
            odd.append(arr[i])
        else:
            even.append(arr[i])

    odd.sort()
    even.sort()
    odd.reverse()
#even.reverse()
    final = odd + even
#print(odd)
#print(even)

    print(*final,sep=" ")
    t = t-1