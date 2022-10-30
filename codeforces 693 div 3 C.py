t = int(input())
while t > 0:
    n = int(input())    
    arr = list(map(int,input().strip().split()))[:n]
    dp = [0 for i in range(n)]
#print(arr)
#print(dp)

    for i in range(n-1,-1,-1):
        dp[i] = arr[i]
        j = i + arr[i]
        if j  < n:
            dp[i] += dp[j]



#print(dp)
    ans = max(dp)
    print(ans)
    t = t-1