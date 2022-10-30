t = int(input())
while t > 0:
    n,k = map(int,input().split())
 
    arr = list(map(int,input().strip().split()))[:n]
    mx = max(arr)
    left = 0
    for i in range(n):
        left = left + (mx - arr[i])
 
    if k > left:
        print(-1)
    else:
        for i in range(k):
            flag = 0
            for j in range(n-1):
                if arr[j] < arr[j+1]:
                    flag = 1
                    arr[j] = arr[j]+1
                    ans = j+1
                    break
        if flag == 0:
            print(-1)
        else:
            print(ans)
    t = t-1




