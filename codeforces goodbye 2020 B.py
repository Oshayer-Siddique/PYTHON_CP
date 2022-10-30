t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]
    prev = -1
    ans = 0
    for i in range(n):
        if arr[i] <= prev:
            arr[i] = arr[i]+1
        if arr[i] > prev:
            prev = arr[i]
            ans+= 1
        

    print(ans)
    t = t-1
