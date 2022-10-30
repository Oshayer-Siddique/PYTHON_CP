n,m = map(int,input().split())

dp = [0 for i in range (n+2)]

if n < m:
    print(1)
else:
    for i in range(0,m,+1):
        dp[i] = 1
    for i in range(m,n+1,+1):
        dp[i] = dp[i-1] + dp[n-m]
        
        

print(dp[n])