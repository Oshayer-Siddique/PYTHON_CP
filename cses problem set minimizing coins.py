n,x = map(int,input().split())
coins = list(map(int,input().strip().split()))[:n]
dp = [10**9]*(x+1)
dp[0] = 0

for i in range(x+1):
    for j in range(n):
        if i - coins[j] >= 0:
            dp[i] = min(dp[i],dp[i-coins[j]]+1)

if dp[x] == 10**9:
    dp[x] = -1
ans = dp[x]

print(ans)
