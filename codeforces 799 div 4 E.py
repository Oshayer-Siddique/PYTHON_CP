t = int(input())
while t > 0:
    n,s = map(int,input().split())
    arr = list(map(int,input().strip().split()))[:n]
    mx_len = 0
    for i in range(n):
        cur_sum = 0
        for j in range(i,n):
            cur_sum += arr[j]
            if cur_sum == s:
                mx_len = max(mx_len,j - i + 1)

    res = mx_len
    if sum(arr) < s:
        print(-1)
    else:
        print(n-res)
    t = t-1
            

    
    
    
    