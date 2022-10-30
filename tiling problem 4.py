n = int(input())

dp = [0 for i in range(n+3)]

dp[2],dp[3] = 1,1

for i in range(4,n+2,+1):
    dp[i] = dp[i-2] + dp[i-3]
    
print(dp[n+1])