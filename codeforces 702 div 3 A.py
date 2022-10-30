import math
t = int(input())
while t > 0:
    n = int(input())
    arr = list(map(int,input().strip().split()))[:n]

    cnt = 0
    for i in range(n-1):
        mini = min(arr[i],arr[i+1])
        maxi = max(arr[i],arr[i+1])
        while 2* mini < maxi:
            mini = mini*2
            cnt += 1

    print(cnt)
    t = t-1
