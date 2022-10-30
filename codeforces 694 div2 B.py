t = int(input())
while t>0:
    n,x = map(int,input().split())
    arr = list(map(int,input().strip().split()))[:n]
    i = 0
    while(arr[i] % x == 0):
        for j in range(x):
            arr.append(arr[i]//x)
        i = i+1
    ans = sum(arr)
    print(ans)
    t = t-1


    