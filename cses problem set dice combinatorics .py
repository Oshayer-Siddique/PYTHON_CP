mod=10**9+7
dp=[0]*(10**7+5)
n = int(input())
dp[0] = 1
dp[1] = 1
 
for i in range(2,n+1,+1):
    dp[i] += (dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4] + dp[i-5] + dp[i-6]) % mod
    
    
ans = dp[n]
print(ans)