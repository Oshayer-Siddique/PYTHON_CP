t = int(input())
while t > 0:
    n ,d = map(int,input().split())
    arr = list(map(int,input().strip().split()))[:n]
    arr.sort()
    flag = 1
    for i in range(len(arr)):
        if arr[i] > d:
            flag = 0
            break
    if flag == 1 or arr[0] + arr[1] <= d:
        print("YES")
    else:
        print("NO")
    t = t-1